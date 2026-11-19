from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_id"] = user.user_id
        token["full_name"] = user.full_name
        token["email"] = user.email
        token["role"] = user.role
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = {
            "user_id": self.user.user_id,
            "full_name": self.user.full_name,
            "email": self.user.email,
            "role": self.user.role,
        }
        return data


class PatientRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = [
            "user_id",
            "full_name",
            "email",
            "phone",
            "password",
        ]
        read_only_fields = ["user_id"]

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            password=validated_data["password"],
            phone=validated_data.get("phone"),
            role="patient",
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id",
            "full_name",
            "email",
            "phone",
            "created_at",
        ]
        read_only_fields = [
            "user_id",
            "email",
            "created_at",
        ]
