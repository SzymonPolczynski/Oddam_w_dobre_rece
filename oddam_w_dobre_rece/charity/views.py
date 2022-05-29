from django.shortcuts import render, redirect
from django.views import View

from .forms import SignUpForm
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


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


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
