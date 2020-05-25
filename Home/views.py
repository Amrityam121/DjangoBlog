from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contact
from blog.models import Post
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def Home(request):
    post = Post.objects.filter(slug='Thewikireport').first()
    context = {'post': post}
    return render(request,'Home/index.html',context)

def contacts(request):
   if request.method == 'POST':
       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']
       print(name,email,phone,message)
       con= contact(Name=name,email=email,phone=phone,message=message)
       con.save()
       messages.success(request, 'your response has been recorded')
   return render(request,'Home/contact.html')



def about(request):
    return render(request,'Home/about.html')


def search(request):
        if request.method == 'GET':
            query = request.GET.get('query')
            if query:
                lookups = Q(title__icontains=query) | Q(content__icontains=query)
                print(lookups)
                allpost = Post.objects.filter(lookups).distinct()
                print(allpost)
                context = {'allpost':  allpost,'query':query }

                return render(request, 'Home/search.html', context)

            else:
                context = {'query':query}
                return render(request, 'Home/search.html',context)

        else:
            return render(request, 'Home/index.html')

def Signup(request):
    if request.method == 'POST':
        user = request.POST['Username']
        Fname = request.POST['First']
        Lname = request.POST['Last']
        email = request.POST['Email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(user) > 11:
            messages.error(request, 'error lenght of username exceeds given range')
            return redirect('Home')

        if not user.isalnum():
            messages.error(request, 'username not alphanumeric')
            return redirect('Home')

        if pass1 != pass2:
            messages.error(request, 'password do not match')
            return redirect('Home')


        myuser = User.objects.create_user(user,email,pass1)
        myuser.First_name = Fname
        myuser.Last_name = Lname
        myuser.save()
        messages.success(request,'Acount has been sucessfully created')
        return redirect('Home')

    else:
        return HttpResponse('error 404')

def handlelogin(request):
    if request.method == 'POST':
       loginusername = request.POST['Loginuser']
       loginpassword = request.POST['Loginpass']
       user = authenticate(username=loginusername,password=loginpassword)
       if user is not None:
           login(request,user)
           messages.success(request,'sucessfully logged in')
           return redirect('Home')
       else:
           messages.error(request, 'invalid credentials!!')
           return redirect('Home')

    return HttpResponse('404-no found')


def handlelogout(request):
       logout(request)
       messages.success(request, 'sucessfully logged off')
       return redirect('Home')







