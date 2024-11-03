from django.shortcuts import render
from .forms import ModelForm
import pickle
from .models import Predictions

def predict_model(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            age = form.cleaned_data['age']
            pclass = form.cleaned_data['pclass']
            sex = form.cleaned_data['sex']
            can_swim = form.cleaned_data['can_swim']
            cabin = form.cleaned_data['cabin']
            cabin_location = form.cleaned_data['cabin_location']

            # Run new features through ML model
            model_features = [
                [age, pclass, sex, can_swim, cabin, cabin_location]]
            loaded_model = pickle.load(
                open("ml_model/initial_model.pkl", 'rb'))
            
            prediction = loaded_model.predict(model_features)[0]

            prediction_dict = [{'name': 'dead'},
                                {'name': 'survives'}]

            prediction_name = prediction_dict[prediction]['name']

            Predictions.objects.create(age=age,
                                        pclass=pclass,
                                        sex=sex,
                                        can_swim=can_swim,
                                        cabin=cabin,
                                        cabin_location=cabin_location,
                                        prediction=prediction_name)

            return render(request, 'home.html', {'form': form, 'prediction': prediction,
                                        'prediction_name': prediction_name})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm()

    return render(request, 'home.html', {'form': form})