from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['author','signed_up'] # author will be determined by request.user
        labels = {
            'event_date': 'Date and time of event (format: MM/DD/YYYY 24H:MM)'
        }
        widgets = {
            'event_date': forms.Textarea(attrs={'cols': 80, 'rows': 3}), # TODO: replace with datetime widget
        }

class SearchForm(forms.Form):
    search = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'search for events'}),max_length=100, required=False)
    show_old = forms.BooleanField(label='show old events', required=False)
