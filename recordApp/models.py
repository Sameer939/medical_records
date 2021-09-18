from django.db import models

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=30)


class Students(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=30)
    waiting_status = models.BooleanField()

    @property
    def is_waiting(self):
        return bool(self.waiting_status)

