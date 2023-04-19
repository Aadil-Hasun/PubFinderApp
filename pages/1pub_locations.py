import os
import streamlit as st
import pandas as pd

FILE_DIR = os.path.dirname(os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "Resources")
data_path = os.path.join(dir_of_interest, 'cleanPubData.csv')

df = pd.read_csv(data_path)
st.set_page_config(layout='wide')
st.title("Pub:green[Finder]:beer:")
st.subheader("Pubs in your area")
post_code = st.selectbox('Select a Postal Code: ', df['postcode'].unique())
post_btn = st.button("Search with Postal Code")
if post_btn:
    temp_df = df[df['postcode'] == post_code]
    st.dataframe(temp_df)
    pub_df = temp_df[['latitude', 'longitude']].copy()
    st.map(pub_df, use_container_width=True)

local_auth = st.selectbox('Select a Local Authority: ', df['local_authority'].unique())
auth_btn = st.button("Search with Local Authority")
if auth_btn:
    temp_df = df[df['local_authority'] == local_auth]
    st.dataframe(temp_df)
    pub_df = temp_df[['latitude', 'longitude']].copy()
    st.map(pub_df, use_container_width=True)
