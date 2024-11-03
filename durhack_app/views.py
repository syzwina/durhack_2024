from django.shortcuts import render, redirect
from .forms import Step1Form, Step2Form, Step3Form, Step4Form, Step5Form, Step6Form
import pickle
from .models import Predictions
from .forms import Step1Form, Step2Form, Step3Form, Step4Form, Step5Form, Step6Form


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
            request.session['pclass'] = form.cleaned_data['pclass']
            return redirect('step3')
    else:
        form = Step2Form()
    return render(request, 'step2.html', {'form': form})

def step3_view(request):
    if request.method == "POST":
        form = Step3Form(request.POST)
        if form.is_valid():
            request.session['sex'] = form.cleaned_data['sex']
            return redirect('step4')
    else:
        form = Step3Form()
    return render(request, 'step3.html', {'form': form})

def step4_view(request):
    if request.method == "POST":
        form = Step4Form(request.POST)
        if form.is_valid():
            request.session['can_swim'] = form.cleaned_data['can_swim']
            return redirect('step5')
    else:
        form = Step4Form()
    return render(request, 'step4.html', {'form': form})

def step5_view(request):
    if request.method == "POST":
        form = Step5Form(request.POST)
        if form.is_valid():
            request.session['cabin'] = form.cleaned_data['cabin']
            return redirect('step6')
    else:
        form = Step5Form()
    return render(request, 'step5.html', {'form': form})

def step6_view(request):
    if request.method == "POST":
        form = Step6Form(request.POST)
        if form.is_valid():
            request.session['cabin_location'] = form.cleaned_data['cabin_location']
            return redirect('results')
    else:
        form = Step6Form()
    return render(request, 'step6.html', {'form': form})

def results_view(request):
    # Retrieve data from session
    age = request.session.get('age')
    pclass = request.session.get('pclass')
    sex = request.session.get('sex')
    can_swim = request.session.get('can_swim')
    cabin = request.session.get('cabin')
    cabin_location = request.session.get('cabin_location')
    

    # Prepare features for the model
    model_features = [[age, pclass, sex, can_swim, cabin, cabin_location]]

    # Load the model and make a prediction
    loaded_model = pickle.load(open("ml_model/initial_model.pkl", 'rb'))
    prediction = loaded_model.predict(model_features)[0]

    # Map prediction result to human-readable name
    prediction_dict = [{'name': 'survives'}, {'name': 'dead'}]
    prediction_name = prediction_dict[prediction]['name']

    # Save the prediction in the database
    Predictions.objects.create(
        age=age,
        pclass=pclass,
        sex=sex,
        can_swim=can_swim,
        cabin=cabin,
        cabin_location=cabin_location,
        prediction=prediction_name
    )

    # Render results page with the prediction
    return render(request, 'results.html', {'prediction_name': prediction_name})