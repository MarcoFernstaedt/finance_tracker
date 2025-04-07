from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TransactionCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, min_length=2, required=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    type = models.CharField(
        max_length=10, choice=(("income", "Income"), ("expense", "Expense"))
    )

    def __str__(self):
        return f"{self.type.capitalize()} - ${self.amount}"


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_palces=2)
    month = models.DateField(())

    def __str__(self):
        return (
            f"{self.category.name} - ${self.amount} for {self.month.strftime('%B %Y')}"
        )
