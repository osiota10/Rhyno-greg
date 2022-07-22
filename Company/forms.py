from .models import *
from django.forms import ModelForm


class EmailSubscriptionForm(ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ['email']


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'


class QuotationForm(ModelForm):
    class Meta:
        model = RequestForQuotation
        fields = '__all__'
