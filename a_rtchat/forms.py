from django import forms
from .models import GroupMessage


class ChatMessageCreateForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Add message...',
                'class': 'p-4 text-black',
                'maxlength': '300',
                'autofocus': True
            })
        }
