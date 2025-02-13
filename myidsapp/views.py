from django.shortcuts import render,HttpResponse,redirect
import pickle
# Create your views here.
def home(request):
    return render(request,"index.html")

def getPredictions(pclass,age,sibsp,fare,parch,embark):
    model = pickle.load(open('finalized_model.sav', 'rb'))
    #scaled = pickle.load(open('scaler.pkl', 'rb'))
    
    prediction = model.predict([
    [pclass, age, sibsp, fare, parch, embark]
])

    #prediction = model.predict(scaled.transform([
    #   [pclass,age,sibsp,fare,parch,embark]
    #]))
    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'

def result(request):
    
    pclass = int(request.GET['pclass'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    

    result = getPredictions(pclass,age,sibsp,parch, fare, embC)

    return render(request, 'result.html', {'result': result})