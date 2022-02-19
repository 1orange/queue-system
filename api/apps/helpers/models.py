from django.db import models


class GenericResponseModel(models.Model):
    reason = models.TextField()
