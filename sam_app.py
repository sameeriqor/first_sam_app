import streamlit
import pandas
iomport requests
fruityvice_response=requests.get"(https://fuityvice.com//api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
