from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .service_models import Service
from .service_serializers import ServiceSerializer


class ServiceListCreateView(generics.ListCreateAPIView):

    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        return Service.objects.select_related(
            "department"
        ).filter(
            is_active=True
        ).order_by("service_name")

    def perform_create(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied(
                "Only the super administrator can add services."
            )

        serializer.save()


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ServiceSerializer
    lookup_field = "service_id"

    def get_permissions(self):
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = Service.objects.select_related("department")

        if (
            self.request.user.is_authenticated
            and self.request.user.role == "super_admin"
        ):
            return queryset

        return queryset.filter(is_active=True)

    def check_permissions(self, request):
        super().check_permissions(request)

        if request.method in ["PUT", "PATCH", "DELETE"]:
            if request.user.role != "super_admin":
                raise PermissionDenied(
                    "Only the super administrator can manage services."
                )
