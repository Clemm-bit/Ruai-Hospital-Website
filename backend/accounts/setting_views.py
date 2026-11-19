from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .setting_models import HospitalSetting
from .setting_serializers import HospitalSettingSerializer


class HospitalSettingListCreateView(generics.ListCreateAPIView):

    serializer_class = HospitalSettingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return HospitalSetting.objects.all().order_by("setting_id")

    def perform_create(self, serializer):
        if (
            not self.request.user.is_authenticated
            or self.request.user.role != "super_admin"
        ):
            raise PermissionDenied(
                "Only the super administrator can create hospital settings."
            )

        serializer.save()


class HospitalSettingDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = HospitalSettingSerializer
    lookup_field = "setting_id"
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return HospitalSetting.objects.all()

    def check_permissions(self, request):
        super().check_permissions(request)

        if request.method in ["PUT", "PATCH", "DELETE"]:
            if (
                not request.user.is_authenticated
                or request.user.role != "super_admin"
            ):
                raise PermissionDenied(
                    "Only the super administrator can manage hospital settings."
                )
