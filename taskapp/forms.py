from django import forms
class add_form(forms.Form):
    """add_form definition."""
    title  = forms.CharField(max_length = 50)
    desc = forms.CharField(max_length = 500)
    done = forms.CharField(max_length=20)
    # TODO: Define form fields here
