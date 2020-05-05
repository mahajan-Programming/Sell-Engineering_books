from django.shortcuts import render,redirect
from .models import UserPersonalInfo,NewBook
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html",{})

from .forms import RegisterForm,UserInfoForm,UserNewBook


# Create your views here.
def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/home")
    else:
	    form = RegisterForm()

    return render(response, "register.html", {"form":form})


@login_required
def userInfoFrom(request):
    userinfo=UserInfoForm(request.POST)
    if request.method == 'POST':
        user = userinfo.save(commit=False)
        user.username=request.user
        userinfo.save()
        return redirect('index')
    return render(request,"UserInfoForm.html",{'userinfo':userinfo})

@login_required
def NewBookForm(request):
    new = UserNewBook(request.POST)
    if request.method == 'POST':
        n=  new.save(commit=False)
        current_user= UserPersonalInfo.objects.get(username=request.user)
        n.BookOwner=current_user
        new.save()
        return redirect('index')

    return render(request,"NewBook.html",{'new':new})