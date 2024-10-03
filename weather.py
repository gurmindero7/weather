import streamlit as st 
import requests
st.set_page_config("Weather Page")
import datetime
import pandas 
st.title("Weather App")
st.cache_data()
def weatherSearch(city):
    API_KEY = "6ee01bd686ddb245a7b5e0f7bd6547b0"

    
    if city_name:
        api_address = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + API_KEY
        
        try:
          res = requests.get(api_address)
          a = res.json()
        #   st.write(a)
          
          for i in a['list']:
              st.subheader(i['dt_txt'])
              v= i['dt_txt']
              date_obj = pandas.to_datetime(v).day_name()

            #   day_name = date_obj.strftime("%A")
              st.write(date_obj) 
              col1,col2= st.columns([1,1])
              with col1:   
                if i['weather'][0]['description']=="light rain":
                    st.image('rain.png', width=100)
                else:
                    st.image('cloud.png', width=100)
              with col2:    
                st.write(f":blue[Description] {i['weather'][0]['description']}")
                    
                st.write(f":blue[Temperature]  {i['main']['temp']-273}° C")
                st.write(f":Wind Speed  {i['wind']['speed']}km/hr")
                st.divider()
        except Exception as e:
            st.write("Error is",e)
          
        
        
city_name= st.text_input("Enter City Name")
weatherSearch(city_name)