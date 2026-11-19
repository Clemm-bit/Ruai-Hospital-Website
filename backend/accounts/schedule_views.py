from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .schedule_models import DoctorSchedule
from .schedule_serializers import DoctorScheduleSerializer


class DoctorScheduleListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorScheduleSerializer

    def get_queryset(self):
        queryset = DoctorSchedule.objects.filter(
            is_active=True,
            doctor__is_active=True
        ).select_related(
            "doctor__user"
        )

        doctor_id = self.request.query_params.get("doctor_id")

        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)

        return queryset.order_by("day_of_week", "start_time")

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied(
                "Only the superuser can create doctor schedules."
            )

        if not serializer.validated_data["doctor"].is_active:
            from rest_framework.exceptions import ValidationError
            raise ValidationError(
                {"doctor": "Cannot schedule an inactive doctor."}
            )

        serializer.save()


class DoctorScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorScheduleSerializer
    queryset = DoctorSchedule.objects.select_related(
        "doctor__user"
    )
    lookup_field = "schedule_id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_update(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied(
                "Only the superuser can edit doctor schedules."
            )
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.role != "super_admin":
            raise PermissionDenied(
                "Only the superuser can delete doctor schedules."
            )
        instance.delete()
