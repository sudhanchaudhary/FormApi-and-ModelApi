from django import forms


GENDER_FIELDS=(
    ('male','male'),
    ('female','female')
)

SUBJECT_FIELDS=(
    ('django','django'),
    ('mern','mern'),
    ('ai/ml','ai/ml')
)

class StudentForm(forms.Form):
    name=forms.CharField(min_length=3,max_length=70,label='Full name',required=True,strip=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    gender=forms.ChoiceField(choices=GENDER_FIELDS,widget=forms.RadioSelect)
    subject=forms.MultipleChoiceField(choices=SUBJECT_FIELDS,widget=forms.CheckboxSelectMultiple)
    