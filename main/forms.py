from django import forms 
from .models import Task

#Model from connects it to the model
#simple from 
#modelform->database ko dekh k apna kaam kr lete #meta means extra data
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['name']