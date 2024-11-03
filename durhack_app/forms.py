from django import forms

gender_choices =( 
    (0, "Female"), 
    (1, "Male"), 
) 

sick_choices =( 
    (0, "No"), 
    (1, "Yes"), 
)

went_to_lifeboat_choices =( 
    (0, "No"), 
    (1, "Yes"), 
) 





class Step1Form(forms.Form):
    age = forms.IntegerField()

class Step2Form(forms.Form):
    gender = forms.ChoiceField(choices = gender_choices)

class Step3Form(forms.Form):
    sick = forms.ChoiceField(choices = sick_choices)

class Step4Form(forms.Form):
    went_to_lifeboat = forms.ChoiceField(choices = went_to_lifeboat_choices)
