from django import forms
from django.core.exceptions import ValidationError

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'author',
            'title',
            'text',
            'rating',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        # if text is not None and len(Post.text) < 20:
        #     raise ValidationError({
        #         "Text": "Описание не может быть менее 20 символов."
        #     })

        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data
