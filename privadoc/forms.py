from django import forms


class TransferMoney(forms.Form):
    amount=forms.CharField()