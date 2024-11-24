from django.contrib import admin
from .models import Tickets
from .models import TicketType

# Allows Admin users to edit and delete 'Tickets' and 'TicketType' records from '/admin'.
admin.site.register(Tickets)
admin.site.register(TicketType)