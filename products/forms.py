from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    subtitle = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Subtitle"}),
                               required=False)    # overriding or adding fileds that are not in the database model object nor in Meta.fields

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
        widgets = {
            'description': forms.Textarea(attrs={"placeholder": "Add description here"})        # overriding default widgets
        }                                                                                       #initials are initiated in views

    # ______ ROBUST here in this template 'clean_*' declare addictional field check logic
    def clean_title(self, *args, **kwargs):                                                 # clean functions being invoked on 'is_valid()' method in views
        title = self.cleaned_data.get('title')
        if 'DUDA' in title:
            raise forms.ValidationError('There is DUDA in the title')
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if 'DUPA' in description:
            raise forms.ValidationError('Bad words has been used. Correct that PLEASE')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Price must be greater than \'0\'')
        return price


# Raw form class using django mechanics, instead of being pure HTML, but does not compare to ModelForms, so we need to
# fix all the fields below.  conclusion -> use ModelForm if you have a Model
class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "new-class-name two",
                                          'rows': 20,
                                          'id': "my-personal-id",
                                          "placeholder": "Your Description"}))
    price = forms.DecimalField(initial=999.99)
