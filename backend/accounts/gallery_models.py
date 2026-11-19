from django.db import models
from .models import User


class HospitalGallery(models.Model):

    image_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=255)

    category = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    uploaded_by = models.ForeignKey(
        User,
        db_column="uploaded_by",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="gallery_images"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "hospital_gallery"
        managed = False

    def __str__(self):
        return self.title
