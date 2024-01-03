from django.shortcuts import render,redirect
from .forms import AirQualityCheckForm
import pandas as pd
from .models import *
from .forms import *
from django.views.generic import FormView,CreateView,TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy



class LoginView(FormView):
    template_name="login.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        log_form=LogForm(data=request.POST)
        if log_form.is_valid():  
            us=log_form.cleaned_data.get('username')
            ps=log_form.cleaned_data.get('password')
            user=authenticate(request,username=us,password=ps)
            if user: 
                login(request,user)
                return redirect('h')
            else:
                return render(request,'login.html',{"form":log_form})
        else:
            return render(request,'login.html',{"form":log_form}) 
        

class RegView(CreateView):
     form_class=Reg
     template_name="reg.html"
     model=User
     success_url=reverse_lazy("log")  



# Load the CSV data
df = pd.read_csv('E:\Internship Luminar\Air Quality\city_day.csv')  # Replace with the actual path to your CSV file

# Define the prediction function
def predict_aqi(pm25, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toluene, xylene):
    # Use the input values to filter the DataFrame and calculate AQI
    filtered_data = df[
        (df['PM2.5'] == pm25) &
        (df['PM10'] == pm10) &
        (df['NO'] == no) &
        (df['NO2'] == no2) &
        (df['NOx'] == nox) &
        (df['NH3'] == nh3) & 
        (df['CO'] == co) &
        (df['SO2'] == so2) &
        (df['O3'] == o3) &
        (df['Benzene'] == benzene) &
        (df['Toluene'] == toluene) &
        (df['Xylene'] == xylene)
    ]
    
    if not filtered_data.empty:
        prediction = filtered_data['AQI_Bucket'].values[0]
    else:
        prediction = "No matching data found"

    return prediction

def predict_air_quality(request):
    if request.method == 'POST':
        form = AirQualityCheckForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data
            pm25 = user_input['pm25']
            pm10 = user_input['pm10']
            no = user_input['no']
            no2 = user_input['no2']
            nox = user_input['nox']
            nh3 = user_input['nh3']
            co = user_input['co']
            so2 = user_input['so2']
            o3 = user_input['o3']
            benzene = user_input['benzene']
            toluene = user_input['toluene']
            xylene = user_input['xylene']

            # Use the prediction function to predict AQI
            prediction = predict_aqi(pm25, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toluene, xylene)
            plot_url = create_pie_chart(pm25, pm10, no,no2,nox,nh3,co,so2,o3,benzene,toluene,xylene)
            context = {
                'form': form,
                'prediction': prediction,
                'plot_url':plot_url
            }
            return render(request, 'index.html', context)
    else:
        form = AirQualityCheckForm()

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
    


from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64



def create_pie_chart(pm25, pm10,no,no2,nox,nh3,co,so2,o3,benzene,toluene,x):
    plt.figure()
    labels = ['PM2.5', 'PM10', 'NO' ,'NO2','NOX','NH3','CO','SO2','O3','B','T','X']
    data = [pm25, pm10, no,no2,nox,nh3,co,so2,o3,benzene,toluene,x]
    colors = ['red', 'yellow', 'green','blue', 'gray', 'orange','cyan', 'lightcoral', 'violet','black','greenyellow','brown']

    plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Encode the image to base64 for embedding in HTML
    plot_url = base64.b64encode(image_stream.read()).decode('utf-8')

    return f'data:image/png;base64,{plot_url}'

