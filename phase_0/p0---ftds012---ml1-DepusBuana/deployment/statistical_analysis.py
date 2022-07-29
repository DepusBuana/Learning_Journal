import streamlit as st
import numpy as np
import statistics
import pandas as pd
from scipy import stats



# app1.py
def app():

    st.header('Welcome to statistical analysis dashboard!')

    ################## case 4 ###############
    df_user = pd.read_csv(r'user_country_age.csv')

    st.subheader('The look customers age')

    selected3 = st.selectbox('Select category',['Female','Male'])
    if selected3 == "Female":
        selected3 = "F"
    else:
        selected3 = "M"

    gender = df_user[df_user['gender'] == selected3]

    female_data = []
    for i in gender.index:
        b = gender.loc[i,'num_of_item']
        age = gender.loc[i,'age']

        while b > 0 :
            female_data.append(age)
            b = b - 1

    female_age = pd.DataFrame()
    female_age['age'] = female_data
    
    if st.checkbox('show data for the age'):
        st.write('checked')
        st.write(female_age)

    st.write('age mean: ', female_age.age.mean(), '; modus: ' , statistics.mode(female_age.age), '; nilai tengah: ', female_age.age.median())   

    st.write('Proses data yang dilakukan yakni pertama menyiapkan data frekuensi usia pembeli berdasarkan data yang diperoleh dari big querry dan kemudian menghitung rata-rata, median dan modus')
    st.write('Dari perhitungan ini dapat diketahui bahwa rata-rata usia pelanggan wanita yaitu 40.9 dengan pembelian terbanyak dilakukan oleh pelanggan berusia 22 dan nilai tengah dari usia pelanggan wanita yaitu 41. Sedangkan pada pria, rata-rata usia pelanggan yakni 41.06 dengan pembelian terbanyak dilakukan oleh pelanggan berusia 54 dan nilai tengah usia pelanggan yakni 41. Hasil pengolahan data ini menunjukan bahwa segmen usia pada wanita yaitu berkisar pada usia 22 dan pada pria pada usia 54.')

    ################# case5 ##############'
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.subheader('Recomended mean of inventory created per month:')

    df_inventory = pd.read_csv(r'inv.csv')
    df_inventory.head(3)
    df_invstat = df_inventory.copy()
    df_invstat=df_invstat.dropna()
    df_invstat['month'] = pd.DatetimeIndex(df_invstat['sold_at']).month
    df_invstat['year'] = pd.DatetimeIndex(df_invstat['sold_at']).year

    st.write('Proses pengolahan data dimulai dari mengubah data kolom sold at yang null menjadi inventory item dan non-null menjadi sold item, sehingga dapat dihitung jumlah item yang terjual dan yang masih menjadi inventory')
    st.write('Kemudian data dikelompokkan berdasarkan bulan dan tahun, sehingga bisa dicari rata-rata produk yang terjual serta standardeviasinya untuk dihitung dengan confidence interval')
    st.write('Dari pengolahan data ini, dapat ditentukan rekomendasi jumlah inventory (berdasarkan confidence interval ini) karena CI mencakup 95% kemungkinan jumlah barang yang terjual dalam 1 bulan')
    st.write('Rekomendasi jumlah created inventory perbulan dan percatogry dapat dilihat dibawah ini:')
    selected4 = st.selectbox('Select category',df_invstat['product_category'].unique())
    
    if st.checkbox('show data for the category'):
        st.write('checked')
        st.write(df_invstat)

    data_CI = df_invstat[df_invstat['product_category'] == selected4].groupby(["year","month"])[["product_category"]].count()
    data_CI=data_CI.reset_index()
    ci = np.round(stats.norm.interval(0.95,data_CI.product_category.mean(), data_CI.product_category.std()),0)
    st.write(ci[1])

    st.write('jumlah created inventory aktual perbulannya juga dapat dihitung dengan checkbox dibawah ini: (proses perhitungan membutuhkan waktu yang lumayan lama)')
    if st.checkbox('calculate current mean of inventory created permonth'):
        st.write('checked')
        df_created = pd.read_csv(r'createdat.csv')
        df_created.head(3)
        df_created['month'] = pd.DatetimeIndex(df_created['created_at']).month
        df_created['year'] = pd.DatetimeIndex(df_created['created_at']).year
        dfmean_created = df_created[df_created['product_category'] == selected4].groupby(["year","month"])[["product_category"]].count()
        dfmean_created=dfmean_created.reset_index()
        st.write(np.round(dfmean_created.product_category.mean(),0))

    

