"""
Views for user management.
"""
from django.views.generic import (TemplateView, 
                                  CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from django import forms

from alert.utils import (send_sms,
                         make_call)
from alert.models import UserModel

from geopy.geocoders import Nominatim


class SignUpForm(UserCreationForm):
    """SignUpForm Creation"""
    # guardian_no = forms.CharField(max_length=15)

    class Meta:
        model = UserModel
        fields = ["guardian_no", "username", "password1", "password2"]


class SignUpView(CreateView):
    """Sign up view."""
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("alert:login")


class HomeView(LoginRequiredMixin, TemplateView):
    """Home page view."""
    template_name = "index.html"


class AlertView(View):
    """Make call and send SMS."""

    def post(self, request):
        user = request.user
        guardian_no = user.guardian_no

        message = "Alert! I am in danger, help me. I have sent my location."
        
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        try:
            geolocator = Nominatim(user_agent="my_emergency_alert_app", timeout=10)
            location = geolocator.reverse(f"{latitude}, {longitude}")
            location_address = location.address if location else "Unknown location"
            # location_message = f"Alert! I am in danger, help me. My location is {location_address}."
            location_message = f"Alert! I am in danger, help me. My location is {location_address}."
            location_message = "Alert! I am in danger, help me. My location is  https://maps.app.goo.gl/iZmjBLTFo9BX34vd7 ."
        except Exception as e:
            location_address = f"Error: {str(e)}"
            location_message = "Alert! I am in danger, help me."

        # location_message = f"Alert! I am in danger, help me. My location is {location_address}."

        print("location message is ", location_message)
        print("location address is ", location_address)

        sms_response  = send_sms(guardian_no, location_message)
        call_response  = make_call(guardian_no, location_message)

        context = {}

        if not sms_response["success"]:
            context["error_sms"] = "SMS not sent."

        if not call_response["success"]:
            context["error_call"] = "Call not placed."

        return render(request, "alert.html", context)