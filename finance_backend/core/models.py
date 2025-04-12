from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} - {self.email}"


class TimeStampedModel(models.Model):
    """
    Abstract model to add created_at and updated_at timestamps.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TransactionCategory(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="transactions"
    )
    category = models.ForeignKey(
        TransactionCategory, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)
    type = models.CharField(
        max_length=10, choices=(("income", "Income"), ("expense", "Expense"))
    )

    def __str__(self):
        return f"{self.type.capitalize()} - ${self.amount}"


class Budget(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="budgets"
    )
    category = models.ForeignKey(
        TransactionCategory, on_delete=models.CASCADE, related_name="budgets"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

    def __str__(self):
        return (
            f"{self.category.name} - ${self.amount} for {self.month.strftime('%B %Y')}"
        )


class LimitAlert(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="limit_alerts"
    )
    category = models.ForeignKey(
        TransactionCategory, on_delete=models.CASCADE, related_name="limit_alerts"
    )
    threshold = models.DecimalField(max_digits=10, decimal_places=2)
    alert_type = models.CharField(
        max_length=14,
        choices=(
            ("email", "Email"),
            ("sms", "SMS"),
        ),
    )

    def __str__(self):
        return f"{self.category.name} - {self.alert_type.capitalize()} Alert at ${self.threshold}"
