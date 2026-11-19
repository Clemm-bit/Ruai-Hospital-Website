from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from .views import (
    CustomTokenObtainPairView,
    PatientRegistrationView,
    PatientProfileView,
)

urlpatterns = [
    path("register/", PatientRegistrationView.as_view(), name="patient-register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("profile/", PatientProfileView.as_view(), name="patient-profile"),
]

from .department_views import (
    DepartmentListCreateView,
    DepartmentDetailView,
)

urlpatterns += [
    path("departments/", DepartmentListCreateView.as_view(), name="department-list-create"),
    path("departments/<int:department_id>/", DepartmentDetailView.as_view(), name="department-detail"),
]

from .doctor_views import (
    DoctorListCreateView,
    DoctorDetailView,
)

urlpatterns += [
    path("doctors/", DoctorListCreateView.as_view(), name="doctor-list-create"),
    path("doctors/<int:doctor_id>/", DoctorDetailView.as_view(), name="doctor-detail"),
]

from .schedule_views import (
    DoctorScheduleListCreateView,
    DoctorScheduleDetailView,
)

urlpatterns += [
    path("schedules/", DoctorScheduleListCreateView.as_view(), name="schedule-list-create"),
    path("schedules/<int:schedule_id>/", DoctorScheduleDetailView.as_view(), name="schedule-detail"),
]

from .appointment_views import AppointmentListCreateView

urlpatterns += [
    path(
        "appointments/",
        AppointmentListCreateView.as_view(),
        name="appointment-list-create"
    ),
]

from .session_views import (
    AppointmentSessionListCreateView,
    AppointmentSessionDetailView,
)

urlpatterns += [
    path(
        "sessions/",
        AppointmentSessionListCreateView.as_view(),
        name="session-list-create"
    ),
    path(
        "sessions/<int:session_id>/",
        AppointmentSessionDetailView.as_view(),
        name="session-detail"
    ),
]

from .payment_views import (
    PaymentListView,
    PaymentDetailView,
)

urlpatterns += [
    path(
        "payments/",
        PaymentListView.as_view(),
        name="payment-list"
    ),
    path(
        "payments/<int:payment_id>/",
        PaymentDetailView.as_view(),
        name="payment-detail"
    ),
]

from .payment_submission_views import PaymentSubmissionView

urlpatterns += [
    path(
        "payments/submit/",
        PaymentSubmissionView.as_view(),
        name="payment-submit"
    ),
]

from .payment_verification_views import PaymentVerificationView

urlpatterns += [
    path(
        "payments/<int:payment_id>/verify/",
        PaymentVerificationView.as_view(),
        name="payment-verify"
    ),
]

from .pending_payment_views import PendingPaymentListView

urlpatterns += [
    path(
        "payments/pending/",
        PendingPaymentListView.as_view(),
        name="pending-payment-list"
    ),
]

from .service_views import (
    ServiceListCreateView,
    ServiceDetailView,
)

urlpatterns += [
    path(
        "services/",
        ServiceListCreateView.as_view(),
        name="service-list-create"
    ),
    path(
        "services/<int:service_id>/",
        ServiceDetailView.as_view(),
        name="service-detail"
    ),
]

from .news_views import (
    HospitalNewsListCreateView,
    HospitalNewsDetailView,
)

urlpatterns += [
    path(
        "news/",
        HospitalNewsListCreateView.as_view(),
        name="news-list-create"
    ),
    path(
        "news/<int:news_id>/",
        HospitalNewsDetailView.as_view(),
        name="news-detail"
    ),
]

from .gallery_views import (
    HospitalGalleryListCreateView,
    HospitalGalleryDetailView,
)

urlpatterns += [
    path(
        "gallery/",
        HospitalGalleryListCreateView.as_view(),
        name="gallery-list-create"
    ),
    path(
        "gallery/<int:image_id>/",
        HospitalGalleryDetailView.as_view(),
        name="gallery-detail"
    ),
]

from .contact_views import (
    ContactMessageListCreateView,
    ContactMessageDetailView,
)

urlpatterns += [
    path(
        "contact/",
        ContactMessageListCreateView.as_view(),
        name="contact-list-create"
    ),
    path(
        "contact/<int:message_id>/",
        ContactMessageDetailView.as_view(),
        name="contact-detail"
    ),
]

from .setting_views import (
    HospitalSettingListCreateView,
    HospitalSettingDetailView,
)

urlpatterns += [
    path(
        "settings/",
        HospitalSettingListCreateView.as_view(),
        name="hospital-settings-list-create"
    ),
    path(
        "settings/<int:setting_id>/",
        HospitalSettingDetailView.as_view(),
        name="hospital-settings-detail"
    ),
]
