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

class ModelForm(forms.Form):
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices = gender_choices)
    sick = forms.ChoiceField(choices = sick_choices)
    went_to_lifeboat = forms.ChoiceField(choices = went_to_lifeboat_choices)