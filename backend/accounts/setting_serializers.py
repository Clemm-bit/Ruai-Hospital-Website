from rest_framework import serializers
from .setting_models import HospitalSetting


class HospitalSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = HospitalSetting
        fields = [
            "setting_id",
            "hospital_name",
            "tagline",
            "description",
            "physical_address",
            "phone_number",
            "alternative_phone",
            "email",
            "website_url",
            "logo_url",
            "google_maps_url",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "setting_id",
            "created_at",
            "updated_at",
        ]
