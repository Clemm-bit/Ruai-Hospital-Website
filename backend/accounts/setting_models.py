from django.db import models


class HospitalSetting(models.Model):

    setting_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=200)
    tagline = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    description = models.TextField(null=True, blank=True)
    physical_address = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    alternative_phone = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    email = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    website_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    logo_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    google_maps_url = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "hospital_settings"
        managed = False

    def __str__(self):
        return self.hospital_name
