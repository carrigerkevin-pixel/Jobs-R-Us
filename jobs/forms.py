from django import forms

class FiltersForm(forms.Form):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter items separated by commas..."
        })
    )
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter items separated by commas..."
        })
    )
    skills = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter items separated by commas..."
        })
    )
    onSite = forms.BooleanField(
        required=False,
        initial=True
    )
    remote = forms.BooleanField(
        required=False,
        initial=True
    )
    minSalary = forms.IntegerField(
        min_value=0,
        required=False
    )
    maxSalary = forms.IntegerField(
        min_value=0,
        required=False
    )
    visaSponsorship = forms.BooleanField(
        required=False,
        initial=False
    )

class QuickApplyForm(forms.Form):
    note = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter a note..."
    }))