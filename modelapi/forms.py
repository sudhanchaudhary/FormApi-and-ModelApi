from django import forms 
from .models import Contact

GENDER_FIELDS=(
    ('male','male'),
    ('female','female')
)

SUBJECT_FIELDS=(
    ('django','djano'),
    ('ai/ml','ai/ml'),
    ('data science','data science')
)

class ContactForm(forms.ModelForm):
   
    class Meta:
        model=Contact
        fields=['name','age','password','gender','subject']    #'__all__'   (for all)

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(choices=GENDER_FIELDS),
            'subject':forms.CheckboxSelectMultiple(choices=SUBJECT_FIELDS)
        }

