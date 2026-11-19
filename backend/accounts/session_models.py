from django.db import models


class AppointmentSession(models.Model):

    session_id = models.AutoField(primary_key=True)

    session_name = models.CharField(max_length=100)

    start_time = models.TimeField()

    end_time = models.TimeField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField()

    class Meta:
        db_table = "appointment_sessions"
        managed = False

    def __str__(self):
        return self.session_name
