# graphics/models.py
from django.db import models

class Graphic(models.Model):
    api_key = models.CharField(max_length=255)
    graphic_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.api_key

