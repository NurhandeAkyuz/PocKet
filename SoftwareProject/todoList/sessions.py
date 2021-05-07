from django.shortcuts import render,redirect
from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"passwords"}))

class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            error = "Please check all fields!"
            form = RegistrationForm()
            return render(request, "signup.html", {"reg_error": error, "form": form})
        email = form.cleaned_data["email"]
        if email in [user.email for user in User.objects.all()]:
            error = "Email already exists!"
            form = RegistrationForm()
            return render(request, "signup.html", {"reg_error": error, "form": form})
        password1 = form.cleaned_data["password1"]
        password2 = form.cleaned_data["password2"]
        if password1 != password2:
            error = "Passwords do not match!"
            form = RegistrationForm()
            return render(request, "signup.html", {"reg_error": error, "form": form})

        user = User.objects.create(email=email, password=password1)
        user.save()
        return redirect("/login")
    else:
        form = RegistrationForm()
        return render(request, "signup.html", {"form": form})

def session(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.get(email=email)
            if password == user.password:
                request.session["email"] = email
                return redirect("/home")
            else:
                form = LoginForm()
                login_error = "Please check your email / password"
                return render(request, "login.html", {"form": form, "login_error": login_error})
        else: pass
    else:
        if "action" in request.GET:
            if "logout" == request.GET.get("action"):
                request.session.flush()
                return redirect("/login")
        form = LoginForm()
        return render(request, "login.html", {"form": form})

