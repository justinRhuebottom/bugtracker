from django.db import models
from django.utils import timezone
from CustomUserApp.models import MyUser

class Ticket(models.Model):
    # NEW = 0
    # DONE = 1
    # IN_PROGRESS = 2
    # INVALID = 3
    # STATUS = [
    #     (NEW, 'New'),
    #     (DONE, 'Done'),
    #     (IN_PROGRESS, 'In Progress'),
    #     (INVALID, 'Invalid')
    # ]

    # status = models.CharField(
    #     max_length=32,
    #     choices=STATUS,
    #     default=NEW
    # )

    class ticketStatus(models.TextChoices):
        NEW = 'New',
        DONE = 'Done',
        IN_PROGRESS = 'In Progress',
        INVALID = 'Invalid'

    title       = models.CharField(max_length=70)
    time        = models.DateTimeField(default=timezone.now, editable=False)
    description = models.TextField(max_length=300)
    status      = models.CharField(choices=ticketStatus.choices, default=ticketStatus.NEW, max_length=15)
    author      = models.ForeignKey(MyUser, null=True, on_delete=models.CASCADE, related_name='ticketAuthor')
    assigned    = models.ForeignKey(MyUser, blank=True, null=True, on_delete=models.CASCADE, related_name='ticketAssigned')
    completer   = models.ForeignKey(MyUser, blank=True, null=True, on_delete=models.CASCADE, related_name='ticketCompleter')

    def __str__(self):
        return self.title

class Meta:
    constraints = [
        models.UniqueConstraint(fields=['title', 'description'], name='unique_ticket')
    ]