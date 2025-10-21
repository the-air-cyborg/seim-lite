from django.db import models

class Alert(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    source_ip = models.GenericIPAddressField()
    event_type = models.CharField(max_length=100)
    severity = models.CharField(max_length=20, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ])
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.timestamp} - {self.event_type} ({self.severity})"