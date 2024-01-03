from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LogForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control","style":"border-radius: 0.75rem; "}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control","style":"border-radius: 0.75rem; "}))


class Reg(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']   
    first_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Firstname","class":"form-control","style":"border-radius: 0.5rem;padding:10px 50px;"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Lastname","class":"form-control","style":"border-radius: 0.5rem;padding:10px 50px; "}))    
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control","style":"border-radius: 0.5rem;padding:10px 50px; "}))
    email=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email","class":"form-control","style":"border-radius: 0.5rem;padding:10px 50px; "}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control","style":"border-radius: 0.5rem;padding:10px 50px; "}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password","class":"form-control","style":"border-radius: 0.5rem;padding:10px 50px; "})) 




class AirQualityCheckForm(forms.Form):
    pm25 = forms.FloatField(label='PM2.5',widget=forms.TextInput(attrs={"placeholder":"PM2.5","class":"form-control","id":"pm25"}))
    pm10 = forms.FloatField(label='PM10',widget=forms.TextInput(attrs={"placeholder":"PM10","class":"form-control","id":"pm10"}))
    no = forms.FloatField(label='NO',widget=forms.TextInput(attrs={"placeholder":"NO","class":"form-control"}))
    no2 = forms.FloatField(label='NO2',widget=forms.TextInput(attrs={"placeholder":"NO2","class":"form-control"}))
    nox = forms.FloatField(label='NOx',widget=forms.TextInput(attrs={"placeholder":"NOX","class":"form-control"}))
    nh3 = forms.FloatField(label='NH3',widget=forms.TextInput(attrs={"placeholder":"NH3","class":"form-control"}))
    co = forms.FloatField(label='CO',widget=forms.TextInput(attrs={"placeholder":"CO","class":"form-control"}))
    so2 = forms.FloatField(label='SO2',widget=forms.TextInput(attrs={"placeholder":"CO2","class":"form-control"}))
    o3 = forms.FloatField(label='O3',widget=forms.TextInput(attrs={"placeholder":"O3","class":"form-control"}))
    benzene = forms.FloatField(label='Benzene',widget=forms.TextInput(attrs={"placeholder":"BENZENE","class":"form-control"}))
    toluene = forms.FloatField(label='Toluene',widget=forms.TextInput(attrs={"placeholder":"TOLUENE","class":"form-control"}))
    xylene = forms.FloatField(label='Xylene',widget=forms.TextInput(attrs={"placeholder":"XYLENE","class":"form-control"}))
