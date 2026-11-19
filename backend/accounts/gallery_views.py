from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .gallery_models import HospitalGallery
from .gallery_serializers import HospitalGallerySerializer


class HospitalGalleryListCreateView(generics.ListCreateAPIView):

    serializer_class = HospitalGallerySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queryset = HospitalGallery.objects.select_related("uploaded_by")

        if (
            self.request.user.is_authenticated
            and self.request.user.role == "super_admin"
        ):
            return queryset.order_by("-created_at")

        return queryset.filter(
            is_active=True
        ).order_by("-created_at")

    def perform_create(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied(
                "Only the super administrator can upload gallery images."
            )

        serializer.save(uploaded_by=self.request.user)


class HospitalGalleryDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = HospitalGallerySerializer
    lookup_field = "image_id"

    def get_permissions(self):
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = HospitalGallery.objects.select_related("uploaded_by")

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
                    "Only the super administrator can manage gallery images."
                )
