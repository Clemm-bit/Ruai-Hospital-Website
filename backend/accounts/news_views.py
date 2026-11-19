from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .news_models import HospitalNews
from .news_serializers import HospitalNewsSerializer


class HospitalNewsListCreateView(generics.ListCreateAPIView):

    serializer_class = HospitalNewsSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queryset = HospitalNews.objects.select_related("author")

        if (
            self.request.user.is_authenticated
            and self.request.user.role == "super_admin"
        ):
            return queryset.order_by("-created_at")

        return queryset.filter(
            status="published"
        ).order_by("-published_at")

    def perform_create(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied(
                "Only the super administrator can publish hospital news."
            )

        status_value = serializer.validated_data.get("status", "draft")

        extra_fields = {"author": self.request.user}

        if status_value == "published":
            extra_fields["published_at"] = timezone.now()

        serializer.save(**extra_fields)


class HospitalNewsDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = HospitalNewsSerializer
    lookup_field = "news_id"

    def get_permissions(self):
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = HospitalNews.objects.select_related("author")

        if (
            self.request.user.is_authenticated
            and self.request.user.role == "super_admin"
        ):
            return queryset

        return queryset.filter(status="published")

    def check_permissions(self, request):
        super().check_permissions(request)

        if request.method in ["PUT", "PATCH", "DELETE"]:
            if request.user.role != "super_admin":
                raise PermissionDenied(
                    "Only the super administrator can manage hospital news."
                )

    def perform_update(self, serializer):
        status_value = serializer.validated_data.get(
            "status",
            serializer.instance.status
        )

        extra_fields = {}

        if (
            status_value == "published"
            and serializer.instance.published_at is None
        ):
            extra_fields["published_at"] = timezone.now()

        serializer.save(**extra_fields)
