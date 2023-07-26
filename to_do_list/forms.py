from django import forms

from to_do_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "is_done",
            "tags",
        ]
        widgets = {
            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date"
                }),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
