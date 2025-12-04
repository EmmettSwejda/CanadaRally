from django import forms
from website.models import Location, Event, Stage, Result




class locationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['name','location','admin']




class eventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['location','startDate','endDate','conditions']




class stageForm(forms.ModelForm):

    class Meta:
        model = Stage
        fields = ['event','length']




class resultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ['driver','codriver', 'car','carclass','time','stage']