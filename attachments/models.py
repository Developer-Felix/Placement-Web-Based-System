from tags.models import Tag
from django.db import models


class Attachment(models.Model):
    title = models.CharField(max_length=20,null=True,blank=True)
    description =  models.CharField(max_length=255,null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

