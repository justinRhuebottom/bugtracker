from django import forms
from BugTrackerApp.models import Ticket

class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)