# Import library yang dibutuhkan
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file csv
data = pd.read_csv('/content/drive/MyDrive/Analisa_Data_Python/PRSA_Data_Gucheng_20130301-20170228.csv')

# Menampilkan judul aplikasi
st.title('Aplikasi Analisis Tingkat Polutan Udara')

# Menampilkan deskripsi singkat aplikasi
st.write('Aplikasi ini bertujuan untuk menganalisis tingkat polutan udara di stasiun Gucheng di Beijing, Cina, dari Maret 2013 hingga Februari 2017. Data ini berisi 17.475 pengamatan dengan 18 variabel, termasuk tanggal, waktu, PM2.5, PM10, SO2, NO2, CO, O3, TEMP, PRES, DEWP, RAIN, wd, WSPM, station, dan cbwd.')

# Membuat list polutan yang tersedia
polutan = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

# Membuat dropdown untuk memilih polutan
pilihan = st.selectbox('Pilih polutan yang ingin dianalisis:', polutan)

# Membuat histogram untuk polutan yang dipilih
st.write(f'Histogram untuk polutan {pilihan}:')
fig, ax = plt.subplots()
sns.histplot(data[pilihan], ax=ax)
st.pyplot(fig)

# Membuat boxplot untuk polutan yang dipilih
st.write(f'Boxplot untuk polutan {pilihan}:')
fig, ax = plt.subplots()
sns.boxplot(data[pilihan], ax=ax)
st.pyplot(fig)

# Membuat slider untuk memilih jumlah sampel
n = st.slider('Pilih jumlah sampel untuk ditampilkan:', 1, 100, 10)

# Menampilkan sampel data secara acak
st.write(f'Sampel {n} data secara acak:')
st.write(data.sample(n))