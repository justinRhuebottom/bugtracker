from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from CustomUserApp.models import MyUser
from BugTrackerApp.models import Ticket
from BugTrackerApp.forms import AddTicketForm, LoginForm

def index_view(request):
    if request.method == "POST":
        sort = request.POST.get('sort')

        if 'New' in sort:
            return render(request, "index.html", {"tickets": Ticket.objects.filter(status='New')})
        if 'Done' in sort:
            return render(request, "index.html", {"tickets": Ticket.objects.filter(status='Done')})
        if 'In Progress' in sort:
            return render(request, "index.html", {"tickets": Ticket.objects.filter(status='In Progress')})
        if 'Invalid' in sort:
            return render(request, "index.html", {"tickets": Ticket.objects.filter(status='Invalid')})

    return render(request, "index.html", {"tickets": Ticket.objects.all()})

@login_required
def ticket_view(request, ticket_id):
    if request.POST:
        options = request.POST.get('options')
        t = Ticket.objects.get(id=ticket_id)
        edit_title = request.POST.get('New Title')
        edit_description = request.POST.get('New Description')
        if 'Assign' in options:
            t.assigned = request.user
            t.save()
        if 'Invalid' in options:
            t.status = 'Invalid'
            t.save()
        if 'Complete' in options:
            t.status = 'Complete'
            t.save()
        if 'Edit' in options:
            t.title = edit_title
            t.description = edit_description
            t.save()

    return render(request, "ticket.html", {"ticket": Ticket.objects.filter(id=ticket_id).first()})

@login_required
def author_view(request, author_id):
    author_name = MyUser.objects.filter(id=author_id).first()
    tickets = Ticket.objects.filter(author=author_name)
    assigned_tickets = Ticket.objects.filter(assigned=author_name)
    completed_tickets = Ticket.objects.filter(completer=author_name)
    return render(request, 'author.html', {"author": author_name, "tickets": tickets, "assigned_tickets": assigned_tickets, "completed_tickets": completed_tickets})

@login_required
def add_ticket(request):
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        form = form.save(commit=False)
        form.author = request.user
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddTicketForm()
    return render(request, "generic_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
