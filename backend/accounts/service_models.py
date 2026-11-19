from django.db import models
from .department_models import Department


class Service(models.Model):

    service_id = models.AutoField(primary_key=True)

    service_name = models.CharField(max_length=150, unique=True)

    description = models.TextField(
        null=True,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        db_column="department_id",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="services"
    )

    image_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "services"
        managed = False

    def __str__(self):
        return self.service_name
