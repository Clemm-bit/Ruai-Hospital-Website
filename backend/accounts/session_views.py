from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .session_models import AppointmentSession
from .session_serializers import AppointmentSessionSerializer


class AppointmentSessionListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSessionSerializer

    def get_queryset(self):
        return AppointmentSession.objects.filter(
            is_active=True
        ).order_by("start_time")

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied(
                "Only the superuser can create appointment sessions."
            )
        serializer.save()


class AppointmentSessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSessionSerializer
    queryset = AppointmentSession.objects.all()
    lookup_field = "session_id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_update(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied(
                "Only the superuser can edit appointment sessions."
            )
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.role != "super_admin":
            raise PermissionDenied(
                "Only the superuser can delete appointment sessions."
            )
        instance.delete()
