from django.db import models

class Ticket(models.Model):
    from_place          = models.CharField(max_length=58, blank=False, null=False)
    to_place            = models.CharField(max_length=58, blank=False, null=False)
    start               = models.DateTimeField(null=False, blank=False)
    end                 = models.DateTimeField(null=False, blank=False)
    description         = models.TextField(blank=True, null=True, max_length=1200)
    ticket_ulgowy        = models.PositiveIntegerField(default=0)
    ticket_szybki        = models.PositiveIntegerField(default=0)
    ticket_dzieci        = models.PositiveIntegerField(default=0)
    ticket_ulgowy_price  = models.DecimalField(max_digits=10000, decimal_places=2, blank=False, null=False)
    ticket_szybki_price  = models.DecimalField(max_digits=10000, decimal_places=2, blank=False, null=False)
    ticket_dzieci_price  = models.DecimalField(max_digits=10000, decimal_places=2, blank=False, null=False)