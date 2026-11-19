from rest_framework import serializers
from .contact_models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactMessage
        fields = [
            "message_id",
            "full_name",
            "email",
            "phone",
            "subject",
            "message",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "message_id",
            "created_at",
        ]
