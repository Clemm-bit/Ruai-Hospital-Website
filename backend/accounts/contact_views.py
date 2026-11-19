from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .contact_models import ContactMessage
from .contact_serializers import ContactMessageSerializer


class ContactMessageListCreateView(generics.ListCreateAPIView):

    serializer_class = ContactMessageSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.role not in ["super_admin", "receptionist"]:
            raise PermissionDenied(
                "You are not allowed to view contact messages."
            )

        return ContactMessage.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(status="unread")


class ContactMessageDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ContactMessageSerializer
    lookup_field = "message_id"
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role not in ["super_admin", "receptionist"]:
            raise PermissionDenied(
                "You are not allowed to manage contact messages."
            )

        return ContactMessage.objects.all()
