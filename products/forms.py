from django import forms
from django.core.exceptions import ValidationError
from .models import Bag, Category, Size, Colour, Charm, Discount


class UniqueMixin:
    """
    Mixin to check that fields required to be unique are truly unique by
    ignoring case sensitivity and whitespace.
    """

    def _get_all_model_instances(self, model):
        """
        Gets all instances of a model.
        """
        instances = model.objects.all()
        return instances

    def _get_lowercase_names_no_whitespace_array(self, model):
        """
        Gets an array of the names of all model instances, in lowercase
        and removing all whitespace.
        """
        instances = self._get_all_model_instances(model)
        lowercase_names_no_whitespace_array = [
            instance.name.lower().replace(' ', '') for instance in instances
        ]
        return lowercase_names_no_whitespace_array

    def _get_lowercase_friendly_names_no_whitespace_array(self, model):
        """
        Gets an array of the friendly_names of all model instances, in
        lowercase and removing all whitespace.
        """
        instances = self._get_all_model_instances(model)
        lowercase_friendly_names_no_whitespace_array = [
            instance.friendly_name.lower().replace(' ', '')
            for instance in instances
        ]
        return lowercase_friendly_names_no_whitespace_array

    def _get_lowercase_skus_no_whitespace_array(self, model):
        """
        Gets an array of the skus of all model instances, in lowercase
        and removing all whitespace.
        """
        instances = self._get_all_model_instances(model)
        # Use of the replace function to remove all whitespace taken from
        # an answer given by Mark Byers and edited by Randall Cook on this
        # Stack Overflow post - https://stackoverflow.com/questions/8270092/
        # remove-all-whitespace-in-a-string
        lowercase_skus_no_whitespace_array = [
            instance.sku.lower().replace(' ', '') for instance in instances
        ]
        return lowercase_skus_no_whitespace_array

    def check_form_entry_unique(self, field, model, error_message, form_entry):
        """
        Checks whether the form entry in lowercase and with all whitespace
        removed can be found in the array of model instance names/skus that
        are also in lowercase with whitespace removed. If so, an appropriate
        ValidationError is raised, else the form entry data is returned.
        """
        if field == 'sku':
            array = self._get_lowercase_skus_no_whitespace_array(model)
        elif field == 'friendly_name':
            array = self._get_lowercase_friendly_names_no_whitespace_array(
                model
            )
        else:
            array = self._get_lowercase_names_no_whitespace_array(model)

        if form_entry.lower().replace(' ', '') in array:
            raise ValidationError(error_message)


class BagForm(forms.ModelForm, UniqueMixin):

    class Meta:
        model = Bag
        exclude = ['overall_rating']

    def clean_name(self):
        """
        Method to clean the bag name field to ensure it is truly unique,
        ignoring case sensitivity and whitespace.
        """
        name = self.cleaned_data.get('name')
        error_message = 'Bag names must be unique'
        self.check_form_entry_unique('name', Bag, error_message, name)
        return name

    def clean_sku(self):
        """
        Method to clean the bag sku field to ensure it is truly unique,
        ignoring case sensitivity and whitespace.
        """
        sku = self.cleaned_data.get('sku')
        error_message = 'Bag skus must be unique'
        self.check_form_entry_unique('sku', Bag, error_message, sku)
        return sku


class CategoryForm(forms.ModelForm, UniqueMixin):

    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        """
        Method to clean the category name field to ensure it is truly unique,
        ignoring case sensitivity and whitespace.
        """
        name = self.cleaned_data.get('name')
        error_message = 'Category names must be unique'
        self.check_form_entry_unique('name', Category, error_message, name)
        return name

    def clean_friendly_name(self):
        """
        Method to clean the category friendly_name field to ensure it is truly
        unique, ignoring case sensitivity and whitespace.
        """
        friendly_name = self.cleaned_data.get('friendly_name')
        error_message = 'Category friendly names must be unique'
        self.check_form_entry_unique('friendly_name', Category, error_message,
                                     friendly_name)
        return friendly_name


class SizeForm(forms.ModelForm, UniqueMixin):

    class Meta:
        model = Size
        fields = '__all__'

    def clean_name(self):
        """
        Method to clean the size name field to ensure it is truly unique,
        ignoring case sensitivity and whitespace.
        """
        name = self.cleaned_data.get('name')
        error_message = 'Size names must be unique'
        self.check_form_entry_unique('name', Size, error_message, name)
        return name
