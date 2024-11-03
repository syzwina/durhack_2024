from django.shortcuts import render
from .forms import Step1Form, Step2Form, Step3Form, Step4Form
import pickle
from .models import Predictions
from .forms import Step1Form, Step2Form, Step3Form, Step4Form

def predict_model(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            sick = form.cleaned_data['sick']
            went_to_lifeboat = form.cleaned_data['went_to_lifeboat']

            # Run new features through ML model
            model_features = [
                [age, gender, sick, went_to_lifeboat]]
            loaded_model = pickle.load(
                open("ml_model/initial_model.pkl", 'rb'))
            
            prediction = loaded_model.predict(model_features)[0]

            prediction_dict = [{'name': 'survives'},
                                {'name': 'dead'}]

            prediction_name = prediction_dict[prediction]['name']

            Predictions.objects.create(age=age,
                                        gender=gender,
                                        sick=sick,
                                        went_to_lifeboat=went_to_lifeboat,
                                        prediction=prediction_name)

            return render(request, 'home.html', {'form': form, 'prediction': prediction,
                                        'prediction_name': prediction_name})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm()

    return render(request, 'home.html', {'form': form})






def step1_view(request):
    if request.method == "POST":
        form = Step1Form(request.POST)
        if form.is_valid():
            request.session['age'] = form.cleaned_data['age']
            return redirect('step2')  
    else:
        form = Step1Form()
    return render(request, 'step1.html', {'form': form})

def step2_view(request):
    if request.method == "POST":
        form = Step2Form(request.POST)
        if form.is_valid():
            request.session['gender'] = form.cleaned_data['gender']
            return redirect('step3')
    else:
        form = Step2Form()
    return render(request, 'step2.html', {'form': form})

def step3_view(request):
    if request.method == "POST":
        form = Step3Form(request.POST)
        if form.is_valid():
            request.session['sick'] = form.cleaned_data['sick']
            return redirect('step4')
    else:
        form = Step3Form()
    return render(request, 'step3.html', {'form': form})

def step4_view(request):
    if request.method == "POST":
        form = Step4Form(request.POST)
        if form.is_valid():
            request.session['lifeboat'] = form.cleaned_data['lifeboat']
            return redirect('results')
    else:
        form = Step4Form()
    return render(request, 'step4.html', {'form': form})
