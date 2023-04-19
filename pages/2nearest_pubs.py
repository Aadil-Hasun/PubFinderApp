import os
import streamlit as st
import pandas as pd
import pickle

FILE_DIR = os.path.dirname(os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "Resources")
data_path = os.path.join(dir_of_interest, 'cleanPubData.csv')
model_path = os.path.join(dir_of_interest, 'model.sav')

df = pd.read_csv(data_path)
st.set_page_config(layout='wide')
st.title("Pub:green[Finder]:beer:")
st.subheader("Find Pubs near me")

pub_df = df[['latitude', 'longitude']].copy()
model = pickle.load(open(model_path, 'rb'))

lat = st.number_input('Enter Latitude: (For UK => min:49.9 -> max:60.84)', min_value=49.9, max_value=60.84)
lon = st.number_input('Enter Longitude: (For UK => min:-8.52 -> max:1.77)', min_value=-8.52, max_value=1.77)
find_btn = st.button("Find Near me")

if find_btn:

    input = [[lat, lon]]
    distances, indices = model.kneighbors(input)
    st.write('Red dots are the pubs near the entered location')
    st.map(pub_df.loc[indices[0]], zoom=10)
    st.subheader("Detail of found Pubs")
    st.dataframe(df.loc[indices[0]])
