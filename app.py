import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# To Add External CSS
with open('css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Application Backend
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = [medicines.iloc[i[0]].Drug_Name for i in medicines_list]
    return recommended_medicines

# Application Frontend

# Title of the Application
st.title('Medicine Recommender System')

# Searchbox
selected_medicine_name = st.selectbox(
    'Type your medicine name whose alternative is to be recommended',
    medicines['Drug_Name'].values
)

# Recommendation Program
if st.button('Recommend Medicine'):
    recommendations = recommend(selected_medicine_name)
    for j, recommended_medicine in enumerate(recommendations, start=1):
        st.write(j, recommended_medicine)
        st.write(f"Click here -> https://pharmeasy.in/search/all?name={recommended_medicine}")

# Image load
image = Image.open('images/medicine-image.jpg')
st.image(image, caption='Recommended Medicines')
