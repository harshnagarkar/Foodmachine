from django.shortcuts import render
import pyrebase 

config = {
'apiKey': "AIzaSyASDoN9Ej8whnuYKvcqhoIYsVASg0lATAQ",
'authDomain': "food-machine.firebaseapp.com",
'databaseURL': "https://food-machine.firebaseio.com",
'projectId': "food-machine",
'storageBucket': "food-machine.appspot.com",
'messagingSenderId': "800501179983"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def signIn(request):
    return render(request, "registration/login.html")
    
def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
    return render(request,"registration/login.html",{"msg":message})
    print(user)
    return render(request, "home.html",{"e":email})
