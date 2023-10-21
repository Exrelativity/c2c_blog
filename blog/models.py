import datetime
from django.db import models
import uuid

class BaseAbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def soft_delete(self):
        """Soft delete a model instance"""
        self.deleted_at = datetime.datetime.now()
        self.save()

    class Meta:
        abstract = True
        ordering = ['created_at']
