from django import forms
from .models import Diary


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('date', 'title', 'text',)
        excude = ('id', 'created_at', 'updated_at',)
        widgets = {
            'date':forms.DateInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.TextInput(attrs={'class':'form-control'}),
        }