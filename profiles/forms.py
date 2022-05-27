from django import forms
from django.core.validators import RegexValidator

from allauth.account.forms import SignupForm

from .models import UserProfile


class CustomSignUpForm(SignupForm):
    """
    CustomSignUpForm class added so that the django-allauth
    standard SignUpForm class can be extended to add first name and
    last name fields.
    """

    # Code for this CustomSignUpForm class is based upon code
    # included in an article entitled 'The complete django-allauth guide'
    # by Gajesh at -
    # https://dev.to/gajesh/the-complete-django-allauth-guide-la3
    #
    # Code for validating the first_name and last_name fields so that
    # only letters are allowed was adapted from an answer given by
    # Martijn Pieters and edited by Lord Elrond on this Stack Overflow
    # post - https://stackoverflow.com/questions/17165147/how-can-i-make-
    # a-django-form-field-contain-only-alphanumeric-characters
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')
    first_name = forms.CharField(max_length=30, label='First Name',
                                 widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'First Name',
                                        'required': 'true'
                                    }),
                                 validators=[alpha])
    last_name = forms.CharField(max_length=30, label='Last Name',
                                widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Last Name',
                                        'required': 'true'
                                    }),
                                validators=[alpha])

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_postcode': 'Postal Code',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
