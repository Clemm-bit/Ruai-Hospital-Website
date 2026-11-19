from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .department_models import Department
from .department_serializers import DepartmentSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.filter(is_active=True).order_by("department_name")

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied("Only the superuser can add departments.")
        serializer.save()


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    lookup_field = "department_id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_update(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied("Only the superuser can edit departments.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.role != "super_admin":
            raise PermissionDenied("Only the superuser can delete departments.")
        instance.delete()
