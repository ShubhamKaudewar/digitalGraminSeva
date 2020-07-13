from django.urls import path
from kyc.views import *

app_name = 'kyc'
urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('kyc/',kycForm,name="kycForm")
]