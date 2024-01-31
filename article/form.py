from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'image', 'message']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'subject',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'message',
        })

