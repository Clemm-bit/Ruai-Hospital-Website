from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import (
    CustomTokenObtainPairSerializer,
    PatientRegistrationSerializer,
)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class PatientRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PatientRegistrationSerializer
    permission_classes = [AllowAny]


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import PatientProfileSerializer


class PatientProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = PatientProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user

        if user.role != "patient":
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only patients can access this profile.")

        return user
