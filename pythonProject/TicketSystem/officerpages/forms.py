from django import forms
from .models import Tickets

# AddTicket form (uses 'Ticket' model from model.py)
class AddTicket(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['Title','Description','TicketTypeId']

