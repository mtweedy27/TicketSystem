from django.db import models

class TicketType(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.Name

class Tickets(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    TicketTypeId = models.ForeignKey(TicketType, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
