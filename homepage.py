import streamlit as st
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "Resources")
data_path = os.path.join(dir_of_interest, 'cleanPubData.csv')
img_path = os.path.join(dir_of_interest, 'the-old-english-pub.jpg')

if __name__ == '__main__':
    df = pd.read_csv(data_path)
    pub_df = df[['latitude', 'longitude']].copy()
    st.set_page_config(layout='wide')
    st.title("Pub:green[Finder]:beer:")
    st.subheader("Welcome visitor")
    img = Image.open(img_path)
    st.image(img)
    st.write('''A pub (short for public house) is a drinking establishment licensed to serve alcoholic drinks for 
    consumption on the premises.''')
    st.subheader('MAP: Pubs in UK')
    st.map(pub_df, use_container_width=True, zoom=5)

    st.subheader('Data Analysis')
    col1, col2 = st.columns(2)
    fig1 = plt.figure()
    temp = pd.DataFrame(df['local_authority'].value_counts()[:25].sort_values())
    plt.barh(np.array(temp.index), np.array(temp.values).reshape(1, -1)[0])
    plt.title('Top 25 Local Authorities with highest number of pubs')
    plt.xlabel("Number of Pubs")

    fig2 = plt.figure()
    temp = df['local_authority'].value_counts().sort_values()[:25]
    plt.barh(np.array(temp.index), np.array(temp.values).reshape(1, -1)[0])
    plt.title('Local Authorities with smallest number of pubs')
    plt.xlabel("Number of Pubs")

    col1.pyplot(fig1)
    col2.pyplot(fig2)

    st.dataframe(df)
