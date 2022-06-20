from django.db import models
from attachments.models import Attachment
from users.models import Account

STATUS = ((1, "Pending"), (0, "Success"), (0, "Failed"))

# Create your models here.
class Application(models.Model):
    applicant = models.ForeignKey(Account, blank=True,null=True, on_delete=models.CASCADE,related_name="applicant")
    organization = models.ForeignKey(Account, blank=True,null=True, on_delete=models.CASCADE,related_name="organization")
    attachment = models.ForeignKey(Attachment, blank=True,null=True, on_delete=models.CASCADE,related_name="attachment")
    status = models.CharField(choices=STATUS,default=1,max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)