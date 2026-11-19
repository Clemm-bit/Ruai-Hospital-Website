from rest_framework import serializers
from .news_models import HospitalNews


class HospitalNewsSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(
        source="author.full_name",
        read_only=True
    )

    class Meta:
        model = HospitalNews
        fields = [
            "news_id",
            "title",
            "content",
            "image_url",
            "author",
            "author_name",
            "status",
            "published_at",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "news_id",
            "author",
            "author_name",
            "published_at",
            "created_at",
            "updated_at",
        ]
