from django import forms

class PredictionForm(forms.Form):
    headline = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(widget=forms.SelectDateWidget)
    open_price = forms.DecimalField(required=False, max_digits=9, decimal_places=2)
    high_price = forms.DecimalField(required=False, max_digits=9, decimal_places=2)
    low_price = forms.DecimalField(required=False, max_digits=9, decimal_places=2)
    volume = forms.IntegerField(required=False, min_value=0)
