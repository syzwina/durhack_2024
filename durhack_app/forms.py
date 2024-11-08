from django import forms
import pandas as pd

# Load the dataset
df = pd.read_csv('./training_modified.csv')

cabin = df['Cabin'].astype('category').cat.categories
cabin_choices = tuple((idx, category) for idx, category in enumerate(cabin))

cabin_location = df['Cabin location'].astype('category').cat.categories
cabin_location_choices = tuple((idx, category) for idx, category in enumerate(cabin_location))

sex_choices =( 
    (0, "Female"), 
    (1, "Male"), 
) 

can_swim_choices =( 
    (0, "No"), 
    (1, "Yes"), 
) 

class ModelForm(forms.Form):
    age = forms.DecimalField() 
    pclass = forms.IntegerField()
    sex = forms.ChoiceField(choices = sex_choices)
    can_swim = forms.ChoiceField(choices = can_swim_choices)
    cabin = forms.ChoiceField(choices = cabin_choices)
    cabin_location = forms.ChoiceField(choices = cabin_location_choices)

class Step1Form(forms.Form):
    age = forms.IntegerField()

class Step2Form(forms.Form):
    pclass = forms.IntegerField()

class Step3Form(forms.Form):
    sex = forms.ChoiceField(choices = sex_choices)

class Step4Form(forms.Form):
    can_swim = forms.ChoiceField(choices = can_swim_choices)

class Step5Form(forms.Form):
    cabin = forms.ChoiceField(choices = cabin_choices)

class Step6Form(forms.Form):
    cabin_location = forms.ChoiceField(choices = cabin_location_choices)