from Library.models import Login
from django.http.response import HttpResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import LoginDetailsSerializer 
 

@csrf_exempt
class LoginDetailsList(APIView):

    @csrf_exempt
    def postSave(request):
        prod=Login()
        prod.userName=request.POST.get('userName')
        prod.name=request.POST.get('name')
        prod.position=request.POST.get('position')
        sha_salt = os.urandom(32)
        prod.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        prod.password = new_key
        prod.save()
        return HttpResponse("Success")

    
    #Function for Login
    @csrf_exempt
    def login(request):
        userName=request.POST.get('userName')
        password=request.POST.get('password')
        print(userName)
        print(password)
        UserLoginDetails1=Login.objects.all().filter(userName=userName) 
        serializer = LoginDetailsSerializer(UserLoginDetails1, many = True)
        total_LoginDetails1 = json.dumps(serializer.data)
        total_LoginDetails = json.loads(total_LoginDetails1)
        for item in total_LoginDetails:
            sha_salt = item['salt']
            Encrypted_Password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), bytes(sha_salt, 'utf-8'), 100000)
            if item['password'] == str(Encrypted_Password):
                print("Success Password")
                if item['position'] == 'Admin':
                    return HttpResponse("Admin")

                elif item['position'] == 'User':
                        return HttpResponse("User")
        return HttpResponse("Failure")


        
        