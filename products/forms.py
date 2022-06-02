from django import forms
from django.core.exceptions import ValidationError
from .widgets import CustomClearableFileInput
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
        # If the model instance is a new instance, self.instance.id will be
        # None and all existing model instances will be taken into account when
        # checking the uniqueness of that new model instance.
        if self.instance.id is None:
            instances = model.objects.all()
        # If the model instance is being edited, self.instance.id will be
        # the edited instance's id and that model instance will be excluded
        # when checking uniqueness.
        else:
            instances = model.objects.all().exclude(id=self.instance.id)
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
        ValidationError is raised, else the form entry data is returned in
        the application clean method.
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
    """
    Provides the default form and additional form validation for adding
    and editing bags used in the admin panel and by the WebsiteBagForm
    subclass.
    """

    class Meta:
        model = Bag
        fields = '__all__'

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


class WebsiteBagForm(BagForm):
    """
    Subclasses the BagForm class to provide the default form for adding
    and editing bags used on the site including a custom image field widget.
    """

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)


class CategoryForm(forms.ModelForm, UniqueMixin):
    """
    Provides the form and additional form validation for adding
    and editing categories used in the admin panel.
    """

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
    """
    Provides the form and additional form validation for adding
    and editing sizes used in the admin panel.
    """

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


class ColourForm(forms.ModelForm, UniqueMixin):
    """
    Provides the form and additional form validation for adding
    and editing colours used in the admin panel.
    """

    class Meta:
        model = Size
        fields = '__all__'

    def clean_name(self):
        """
        Method to clean the colour name field to ensure it is truly unique,
        ignoring case sensitivity and whitespace.
        """
        name = self.cleaned_data.get('name')
        error_message = 'Colour names must be unique'
        self.check_form_entry_unique('name', Colour, error_message, name)
        return name


class DiscountForm(forms.ModelForm, UniqueMixin):
    """
    Provides the form and additional form validation for adding
    and editing discounts used in the admin panel.
    """

    class Meta:
        model = Discount
        fields = '__all__'

    def clean_name(self):
        """
        Method to clean the discount name field to ensure it is truly unique,
        ignoring case sensitivity and whitespace.
        """
        name = self.cleaned_data.get('name')
        error_message = 'Discount names must be unique'
        self.check_form_entry_unique('name', Discount, error_message, name)
        return name


class CharmForm(forms.ModelForm, UniqueMixin):
    """
    Provides the form and additional form validation for adding
    and editing charms used in the admin panel.
    """

    class Meta:
        model = Charm
        fields = '__all__'

    def clean_name(self):
        """
        Method to clean the charm name field to ensure it is truly unique,
        ignoring case sensitivity and whitespace.
        """
        name = self.cleaned_data.get('name')
        error_message = 'Charm names must be unique'
        self.check_form_entry_unique('name', Charm, error_message, name)
        return name
