from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["rating", "comments"]
        widgets = {
            "rating": forms.RadioSelect(choices=[(i, f"{i}★") for i in range(1, 6)]),
            "comments": forms.Textarea(
                attrs={"rows": 4, "placeholder": "리뷰를 남겨주세요…"}
            ),
        }
