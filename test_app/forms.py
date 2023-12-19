from django import forms

class CreateNewUser(forms.Form):
    key = forms.CharField(label="KEY", max_length=200)
    url = forms.CharField(label="URL", max_length=200)
    active = forms.BooleanField(required=False)