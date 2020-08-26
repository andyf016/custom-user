from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from userapp.models import CustomUser
from customuser import settings
from .forms import CustomUserCreationForm, LoginForm




def index(request):
    return render(request, 'index.html')

@login_required
def homepage_view(request):
    current_settings = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'the_settings': current_settings})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
                # return HttpResponseRedirect(request.GET.get('next', reverse("home")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def signup_view(request):
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=data.get("username"), 
                password=data.get("password"), 
                display_name=data.get("display_name"), 
                age=data.get("age"), 
                homepage=data.get("homepage"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    form = CustomUserCreationForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginview"))


"""
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'genericform.html'
"""
