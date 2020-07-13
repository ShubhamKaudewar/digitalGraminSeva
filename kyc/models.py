from django.db import models

def aadhaar_path(instance, filename):
    return 'img/{0}_{1}/{2}'.format(instance.kycFirstName,instance.kycLastName,filename)
    
def pancard_path(instance, filename):
    return 'img/{0}_{1}/{2}'.format(instance.kycFirstName,instance.kycLastName,filename)
    
class kycModel(models.Model):
    kycFirstName = models.CharField(max_length=200,blank=False,null=False)
    kycMiddleName = models.CharField(max_length=200,blank=False,null=False)
    kycLastName = models.CharField(max_length=200,blank=False,null=False)
    kycCompanyName = models.TextField(blank=False,null=False)
    kycRegisteredNumber = models.CharField(max_length=200,blank=False,null=False)
    kycRegisteredEmail = models.EmailField(blank=False,null=False)
    kycDateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    kycPanCardNumber = models.CharField(max_length=200,blank=False,null=False)
    kycPinCode = models.IntegerField(blank=False,null=False)
    kycDistrict = models.CharField(max_length=200,blank=False,null=False)
    kycState = models.CharField(max_length=200,blank=False,null=False)
    kycCity = models.CharField(max_length=200,blank=False,null=False)
    kycAddress = models.TextField(blank=False,null=False)
    kycAadhar = models.FileField(upload_to=aadhaar_path,blank=False,null=False)
    kycPanCard = models.FileField(upload_to=pancard_path,blank=False,null=False)