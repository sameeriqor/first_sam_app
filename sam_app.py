import streamlit
import pandas
import requests
fruityvice_response=requests.get"(https://fuityvice.com//api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
