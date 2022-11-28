from django import forms
from django.forms import ModelForm
from .models import Message


class MessageForm(ModelForm):
    #function to validate the length of the message before allowing submission
    def clean_userMessage(self):
        message = self.cleaned_data["userMessage"]
        message = message.split(" ")
        if len(message) < 10:
            raise forms.ValidationError("Too short, You need at least 10 words")
        else:
            return message


    class Meta:
        model = Message
        fields = ["userMessage"]