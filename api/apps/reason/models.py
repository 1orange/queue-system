from django.db import models


class MedicalReason(models.Model):
    reason = models.TextField()
    execution_time = models.PositiveIntegerField(default=0)
    parallelizable = models.BooleanField(default=False)