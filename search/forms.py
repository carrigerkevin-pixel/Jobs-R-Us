from django import forms


#class MessageForm(forms.Form):
    #add later

class EmailForm(forms.Form):
    candidate_id = forms.IntegerField(widget=forms.HiddenInput())
    email = forms.CharField(
        max_length = 200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your email address...'}),
        label = "email"
    )
    subject = forms.CharField(
        max_length = 200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your subject...'}),
        label = "subject"
    )
    body = forms.CharField(
        widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Write your email...'}),
        label = "body"
    )
