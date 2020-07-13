from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from kyc.models import kycModel
from django.core.mail import send_mail
from datetime import datetime

def dashboard(request):
    return render(request,'index.html')

def kycForm(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        cname = request.POST['cname']
        number = request.POST['number']
        email = request.POST['email']
        dob = request.POST['dob']
        pancardnumber = request.POST['pancardnumber']
        pincode = request.POST['pincode']
        dist = request.POST['dist']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        aadharImage = request.FILES['aadharImage']
        pancardImage = request.FILES['pancardImage']
        
        # Form Conditions
        error = 0
        if len(number) != 10:
            messages.info(request,'Incorrect Phone Number !')
            error=1
        if len(pancardnumber) != 10 or any(char.isdigit() for char in pancardnumber[:5]) == True or pancardnumber[-1].isdigit() == True:
            messages.info(request,'Invalid PAN Card Number')
            error=1
        if len(pincode) != 6:
            messages.info(request,'Invalid Pincode Number')
            error=1
        if int(dob[:4]) < 1900 or int(dob[:4]) >= int(datetime.today().strftime('%Y')):
            messages.info(request,'Invalid Date of Birth')
            error=1
        if error == 0:
            kycModel.objects.create(
                kycFirstName = fname,
                kycMiddleName = mname,
                kycLastName = lname,
                kycCompanyName = cname,
                kycRegisteredNumber = number,
                kycRegisteredEmail = email,
                kycDateOfBirth = dob,     
                kycPanCardNumber = pancardnumber,
                kycPinCode = pincode,
                kycDistrict = dist,
                kycState = state,
                kycCity = city,
                kycAddress = address,
                kycAadhar = aadharImage,
                kycPanCard = pancardImage
            )
            messages.info(request,'Submitted ! Under Review !!')
    return render(request,'kyc/index.html')