from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import SignUpForm, LoginForm
from .models import Institution, Donation, Category


class LandingPageView(View):
    def get(self, request):
        institutions = Institution.objects.all()
        institutions_count = institutions.count()
        donations = Donation.objects.all()
        categories = Category.objects.all()
        # quantity = []
        # for donation in donations:
        #     quantity.append(donation.quantity)
        sum_of_bags = sum([donation.quantity for donation in donations])
        ctx = {
            "institutions": institutions,
            "institutions_count": institutions_count,
            "sum_of_bags": sum_of_bags,
            "categories": categories,
        }
        return render(request, "index.html", context=ctx)


class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html")


class RegisterView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/#login-section')
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            user = User.objects.filter(username=username)
            if user:
                error = 'Nieprawidłowe hasło'
                form = LoginForm()
                ctx = {'form': form, 'error': error}
                return render(request, 'login.html', ctx)
            return redirect('/register/#register-section')

        else:
            ctx = {'form': form}
            return render(request, 'login.html', ctx)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("index")
