from django import forms
from .models import Main


class Subscribe(forms.Form):
    pass

class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        # fields that should be visible on the form template:
        fields = ('senderTitle', 'senderName', 'senderAddress', 'senderCity', 'senderProvince', 'senderCountry', 'senderZip', 'receiverTitle', 'receiverName', 'receiverAddress', 'receiverCity', 'receiverProvince', 'receiverCountry', 'receiverZip', )

        def __str__(self):
            return self.fields
