from django.db import models
import uuid
from datetime import datetime


class BaseAbstractModel(models.Model):

    """
     This model defines base models that implements common fields like:
     created_at
     updated_at
     is_deleted
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    deletedAt = models.DateTimeField(null=True)

    def soft_delete(self):
        """soft  delete a model instance"""
        self.deletedAt = datetime.now() 
        self.save()

    class Meta:
        abstract = True
        ordering = ['-createdAt']