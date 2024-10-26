from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Ticket
from .services.ticket_operations import add_ticket as add_ticket_service, get_current_ticket, attend_ticket as attend_ticket_service, get_sorted_tickets
from .utils.searching import binary_search

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

def add_ticket(request):
    if request.method == 'POST':
        name = request.POST['customer_name']
        description = request.POST['issue_description']
        priority = request.POST['priority']
        new_ticket = Ticket(customer_name=name, issue_description=description, priority=priority)
        add_ticket_service(new_ticket)
        return redirect('ticket_list')
    return render(request, 'tickets/add_ticket.html')

def current_ticket(request):
    ticket = get_current_ticket()
    return render(request, 'tickets/current_ticket.html', {'ticket': ticket})

def attend_ticket(request):
    ticket = attend_ticket_service()
    return redirect('ticket_list')

def sorted_tickets_view(request):
    tickets = Ticket.objects.all()
    sorted_tickets = get_sorted_tickets(tickets)
    return render(request, 'tickets/ticket_list.html', {'tickets': sorted_tickets})

def search_ticket_view(request, ticket_id):
    tickets = list(Ticket.objects.all())
    result = binary_search(tickets, ticket_id)
    return render(request, 'tickets/search_result.html', {'ticket': result})

