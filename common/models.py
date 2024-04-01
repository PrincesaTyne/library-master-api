import shortuuid
from django.db import models


class AuditableModel(models.Model):
    ''' Auditable base model '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=256, null=True, blank=True)
    updated_by = models.CharField(max_length=256, null=True, blank=True)
    deleted_by = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        abstract = True


class BaseModel(AuditableModel):
    '''Base model'''
    id = models.CharField(max_length=22, primary_key=True, default=shortuuid.uuid)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
