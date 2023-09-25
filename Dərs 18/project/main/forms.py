from main.views import *
from django.forms import ModelForm, forms, TextInput

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__' #[ 'name',]
        widgets = {
            'ad' :TextInput(attrs={'class':'form-control',
            'placeholder':'Ad'
            
            }),
            
            'metn' :TextInput(attrs={'class':'form-control',
            'placeholder':'Metn'
            }),
            
            
            
        }

