from django.db import models
from django.contrib.auth.models import User

SUBSCRIPTION_PLANS = (
    ('Free', 'Free'),
    ('Basic', 'Basic'),
    ('Premium', 'Premium'),
)

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=10, choices=SUBSCRIPTION_PLANS, default='Free')
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan}"
