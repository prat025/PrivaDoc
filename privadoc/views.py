from email.mime import base
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import TransferMoney
import pickle
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import ipfsapi
from pathlib import Path
import pandas as pd
from keras.models import load_model 
from sklearn import preprocessing
from sklearn.cluster import KMeans, k_means




def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form=UserCreationForm()
    return render(request, 'hospital/signup.html', {'form':form}) 
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            global user
            user=form.get_user()
            login(request, user)
     #       p=Account.objects.filter(holder=user)
            return redirect('http://127.0.0.1:8000/enter_secretCode/')
    else:
        form=AuthenticationForm()
        return render(request, 'hospital/login.html', {'form':form})
def log_out(request):
    if request.method=='GET':
        logout(request)
        return redirect('http://127.0.0.1:8000/')
def welcome(request):
   #     global money
    #    money=p[0].amount
        return render(request, 'hospital/welcome.html',{'user':user})
def Add_Balance(request):
    if request.method=='GET':
        t='QmWtNq3Qu8Zr79NenapqA7BQwW6W5gqcqimJZGSK7e8EXE.txt'
        data=pd.read_csv(t, sep=',')
        pickle_in=open("privadoc/insurance.pickle","rb")
        linear=pickle.load(pickle_in)
        X=data.iloc[4,:3].to_numpy()
        if X[2]=='True':
            X[2]=1
        else:
            X[2]=0
        prediction=linear.predict(X.reshape(1,-1))
        return render(request, 'hospital/money_sent.html',{'pred':int(prediction[0])})
    else:
        return redirect('http://127.0.0.1:8000/welcome/')
        

def transfer_money(request):
    if request.method=='GET':
        form=TransferMoney()
        return render(request, 'hospital/transfer_money.html', {'form':form})
    else:
        global g
        form=TransferMoney(request.POST)
        if form.is_valid():
            g=form.cleaned_data.get("amount") 
            api = ipfsapi.Client(host='https://ipfs.infura.io')
            api.get(g)
            p = Path(g)
            p.rename(p.with_suffix('.txt'))
            return redirect('http://127.0.0.1:8000/welcome/')
        else:
            form=TransferMoney()
            return render(request, 'hospital/transfer_money.html', {'form':form})
def Money_Sent(request):
    if request.method=='GET':
        t=g+'.txt'
        data=pd.read_csv(t, sep=',')
        data=data.iloc[[1]]
        le=preprocessing.LabelEncoder()
        data=list(data)
        data=le.fit_transform(data)
        clf = pickle.load(open("hospital/mental.pickle", "rb"))
        predict=clf.predict(data.reshape(1,-1))
        if predict==0:
            predict='Patient needs therapy'
        else:
            predict="Patient doesn't need therapy"
        return render(request, 'hospital/mental.html',{'pred':predict})
def Money_Received(request):
    if request.method=='GET':
        t=g+'.txt'
        mod=load_model("hospital/neural.h5")
        data=pd.read_csv(t, sep=',')
        X=data.iloc[2,:8]
        X = np.asarray(X).astype(np.float32)
        predict=mod.predict(X.reshape(1,-1))
        classes = np.argmax(predict, axis = 1)
        if classes[0]==0:
            predict="Patient doesn't have Diabetes"
        else:
            predict='Patient is Diabatic'
        return render(request, 'hospital/diabetes.html',{'pred':predict})
def machine_learning(request):
    if request.method=='GET':
        t=g+'.txt'
        data=pd.read_csv(t, sep=',')
        pickle_in=open("hospital/breast_cancer.pickle","rb")
        clf=pickle.load(pickle_in)
        X=data.iloc[6,:4].to_numpy()
        prediction=clf.predict(X.reshape(1,-1))
        if prediction[0]==0:
            prediction='No Breast Cancer Detected'
        else:
            prediction='Patient has Breast Cancer'
        return render(request, 'hospital/cancer.html',{'pred':prediction})
        
       
        
        



            

            

            
            





