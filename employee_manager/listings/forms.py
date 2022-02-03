from django import forms
class Add(forms.Form):
   name = forms.CharField()
   surname = forms.CharField()
   departement = forms.CharField()