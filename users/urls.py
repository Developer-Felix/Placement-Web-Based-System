
from django.contrib import admin
from django.urls import path, include
from applications.views import apply
from attachments.views import  attachment_application_detail, attachments_create, list_attachments

from users.views import customer_home, index, org_home, register


app_name = 'users'

urlpatterns = [
    path('',index, name='index'),
    path('customer/home/',customer_home, name='customer_home'),
    path('organization/home/',org_home, name='org_home'),
    path("create/attachment/", attachments_create, name="create_attachment"),
    path('list/attachment/',list_attachments, name='list_attachment'),
    path('list/attachment/applications/<int:attachment_id>',attachment_application_detail,name="attachment_application_detail"),
    # path('customer/chat',chat, name='chat'),
    path('register/',register, name='register'),
    path('attachment/apply/<attachment_id>',apply,name="apply")
    # path('otp/',otp, name='otp'),
]
