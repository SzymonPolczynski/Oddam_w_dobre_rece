from django.shortcuts import render
from django.views import View

from charity.models import Institution, Donation


class LandingPageView(View):
    def get(self, request):
        institutions = Institution.objects.all().count()
        donations = Donation.objects.all()
        # quantity = []
        # for donation in donations:
        #     quantity.append(donation.quantity)
        sum_of_bags = sum([donation.quantity for donation in donations])
        ctx = {
            "institutions": institutions,
            "sum_of_bags": sum_of_bags,
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
        return render(request, "register.html")
