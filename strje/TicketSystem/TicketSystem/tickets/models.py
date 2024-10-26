from django.db import models

# Create your models here.
from django.db import models

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    issue_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.customer_name} - Priority: {self.priority}"
