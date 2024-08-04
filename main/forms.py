from django import forms 
from .models import Task, Movie

#Model from connects it to the model
#simple from 
#modelform->database ko dekh k apna kaam kr lete #meta means extra data
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['name']

class MovieForm(forms.ModelForm):
     class Meta:
        model = Movie
        fields = '__all__' # double underscore with all calls all the fields(it will include all the fields of movie)