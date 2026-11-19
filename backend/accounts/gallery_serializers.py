from rest_framework import serializers
from .gallery_models import HospitalGallery


class HospitalGallerySerializer(serializers.ModelSerializer):

    uploader_name = serializers.CharField(
        source="uploaded_by.full_name",
        read_only=True
    )

    class Meta:
        model = HospitalGallery
        fields = [
            "image_id",
            "title",
            "description",
            "image_url",
            "category",
            "uploaded_by",
            "uploader_name",
            "is_active",
            "created_at",
        ]

        read_only_fields = [
            "image_id",
            "uploaded_by",
            "uploader_name",
            "created_at",
        ]
