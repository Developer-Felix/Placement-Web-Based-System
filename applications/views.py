
from django.shortcuts import render

from applications.models import Application
from attachments.models import Attachment
from users.models import Account

# Create your views here.
def apply(request,attachment_id):
    if request.method == "POST":
        print(request.user.id)
        app = Account.objects.get(id=request.user.id)

        org = request.POST.get('org')
        attachment_id = Attachment.objects.get(id=attachment_id)
        attachment = attachment_id
        cv = request.POST.get('cv')
        print(cv)
        status = "Pending"
        print(status)

        applic = Application(
        organization = org,
        attachment = attachment,
        status = status,
        applicant = app,
        cv = cv
        )
        print("Saved")
        applic.save()

    return render(request,'apply.html')