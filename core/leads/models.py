from django.db import models

class Lead(models.Model):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50)
    budget = models.PositiveIntegerField()
    formatted_budget = models.CharField(max_length=50, blank=True)
    raw_query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property_type} in {self.location} under {self.formatted_budget}"
