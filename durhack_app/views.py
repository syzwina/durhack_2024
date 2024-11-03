from django.shortcuts import render, redirect
from .forms import Step1Form, Step2Form, Step3Form, Step4Form
import pickle
from .models import Predictions
from .forms import Step1Form, Step2Form, Step3Form, Step4Form


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

def results_view(request):
    # Retrieve data from session
    age = request.session.get('age')
    gender = request.session.get('gender')
    sick = request.session.get('sick')
    lifeboat = request.session.get('lifeboat')

    # Prepare features for the model
    model_features = [[age, gender, sick, lifeboat]]

    # Load the model and make a prediction
    loaded_model = pickle.load(open("ml_model/initial_model.pkl", 'rb'))
    prediction = loaded_model.predict(model_features)[0]

    # Map prediction result to human-readable name
    prediction_dict = [{'name': 'survives'}, {'name': 'dead'}]
    prediction_name = prediction_dict[prediction]['name']

    # Save the prediction in the database
    Predictions.objects.create(
        age=age,
        gender=gender,
        sick=sick,
        went_to_lifeboat=lifeboat,
        prediction=prediction_name
    )

    # Render results page with the prediction
    return render(request, 'results.html', {'prediction_name': prediction_name})