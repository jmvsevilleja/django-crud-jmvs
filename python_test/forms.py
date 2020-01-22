from django import forms
from .models import Client

from django.forms import EmailField
from django.core.exceptions import ValidationError


class ClientForm(forms.ModelForm):

    # Required fields for a client include: client name, email address, phone number
    name = forms.CharField(label='Client Name',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    street = forms.CharField(label='Street Name',
                             required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    suburb = forms.CharField(label='Suburb',
                             required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    postcode = forms.CharField(label='Postal Code',
                               required=False,
                               max_length=10,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    state = forms.CharField(label='State',
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    contact = forms.CharField(label='Contact Name',
                              required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label='Email Address',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone = forms.CharField(label='Phone Number',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Client

        fields = {'name', 'street', 'suburb', 'postcode',
                  'state', 'contact', 'email', 'phone'}

    def clean_name(self):
        name = self.cleaned_data['name']

        # There should be no duplicate client names
        if Client.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This client name already exist.")
        return name
