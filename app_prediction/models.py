from django.db import models

class Prediction(models.Model):
    headline = models.TextField()
    date = models.DateField()
    stock_ticker = models.CharField(max_length=10, null=True, blank=True)  # Make it optional
    predicted_close = models.FloatField()
    actual_close = models.FloatField(null=True, blank=True)  # Optional, for storing the actual close prices
    
    def __str__(self):
        return f"Prediction for {self.stock_ticker} on {self.date}"
