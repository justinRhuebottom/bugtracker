from django.contrib import admin
from BugTrackerApp.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')

admin.site.register(Ticket, TicketAdmin)