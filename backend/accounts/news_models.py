from django.db import models
from .models import User


class HospitalNews(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]

    news_id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200)

    content = models.TextField()

    image_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        User,
        db_column="author_id",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="hospital_news"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
        null=True,
        blank=True
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        null=True,
        blank=True
    )

    updated_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "hospital_news"
        managed = False

    def __str__(self):
        return self.title
