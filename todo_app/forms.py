from django import forms
from django.forms import SelectDateWidget

from todo_app.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        required=False,
        widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
    )

    class Meta:
        model = Task
        fields = "__all__"
