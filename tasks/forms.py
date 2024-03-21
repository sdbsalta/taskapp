from django import forms

from .models import Task, TaskGroup

'''
class TaskForm(forms.Form):
     name = forms.CharField(label="Task Name", max_length=100)
     due_date = forms.DateTimeField(label="Task Due", 
         widget=forms.TextInput(
            attrs={"type": "datetime-local"}
             )
        )
     taskgroup = forms.ModelChoiceField(
        label="Task Group", 
        queryset=TaskGroup.objects.all()
        )
'''

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "due_date":forms.TextInput(
                attrs={"type": "datetime-local"}
            )
        }