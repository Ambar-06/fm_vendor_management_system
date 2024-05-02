from django.db import models
import uuid

class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super(BaseModelManager, self).get_queryset().filter(is_deleted=False)

class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    objects = BaseModelManager()

    class Meta:
        get_latest_by = "updated_at"
        abstract = True