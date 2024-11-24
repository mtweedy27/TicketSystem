from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Tickets
from .forms import AddTicket

# Officer dashboard -- Used to navigate to functionality.
def dashboard(response):
    return render(response, "officerpages/dashboard.html")


# Create -- Used to add tickets
def create(request):
    # Defining request method as 'POST' and using 'AddTickets' from 'form.py'
    if request.method == "POST":
        form = AddTicket(request.POST)

    # Handling validation and redirect
        if form.is_valid():
                Tickets = form.save()
                messages.success(request, "Ticket successfully added.")
        return redirect("/dashboard")

    else:
        form = AddTicket()
    return render(request, "officerpages/create.html", {"form":form})


# View -- Used to view all tickets
def view(request):
    # Gets all tickets under variable 'Tickets_data', used in html file to add to a table
    Tickets_data = Tickets.objects.all()
    return render(request, 'officerpages/view.html', {'Tickets_data':Tickets_data})


# Update -- Separate form to update existing tickets.
def update(request, Tickets_data):
    # Get ticket data, apply to 'ticket' variable
    ticket = Tickets.objects.get(pk=Tickets_data)
    # Populate form with data from 'ticket'
    form = AddTicket(request.POST or None, instance=ticket)
    # Handling validation and redirect
    if form.is_valid():
        form.save()
        messages.success(request, "Ticket successfully updated.")
        return redirect('/view')

    else:
        form = AddTicket(request.POST or None, instance=ticket)

    return render(request, "officerpages/update.html",
                  {'ticket': ticket,
                  'form' :form})
