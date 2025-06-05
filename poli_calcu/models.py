from django.db import models
from django.contrib.auth.models import User

class CalculationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    function = models.CharField(max_length=255)
    method = models.CharField(max_length=50)
    root = models.FloatField()
    iterations = models.IntegerField()
    error = models.FloatField()
    calculation_date = models.DateTimeField(auto_now_add=True)
    plot_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.function} - {self.method} - {self.root:.6f}"