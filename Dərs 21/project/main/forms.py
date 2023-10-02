from main.views import *

from django.forms import forms,ModelForm,TextInput


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['ad','metn']
        widgets = {
            
            'ad':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Ad'
                
            }),
            
            'metn':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Metn'
                
            })
            
            
            
        }
        
       
        