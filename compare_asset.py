import pandas as pd
import streamlit as st


st.title('Asset Unschedule Reports')

up_asset = st.sidebar.file_uploader('Upload File Asset', type=['xlsx','xls'])
up_prev = st.sidebar.file_uploader('Upload File Preventive Schedule', type=['xlsx','xls'])

def read_excel(file):
    try:
        return pd.read_excel(file)
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
        return None

if up_asset is not None and up_prev is not None:
    df_asset = pd.read_excel(up_asset)
    df_prev = pd.read_excel(up_prev)
    
    if df_asset is not None and df_prev is not None:
        kolom_asset = df_asset[['ID', 'Name','Category','Location']]
        kolom_asset = kolom_asset.rename(columns={'ID':'Item ID','Name': 'Item Name','Category':'Item Category'})
        kolom_prev = df_prev[['Item ID','Ticket ID','Task Type']]
        df_merged = pd.merge(kolom_asset,kolom_prev, on='Item ID', how='outer')
        unschedule_item = df_merged[df_merged['Ticket ID'].isnull()]

        # Filter 
        kolom_option = ["All"] + kolom_asset['Item Category'].unique().tolist()
        pilih_kolom = st.selectbox('Filter Berdasarkan Category', options=kolom_option)
        
        if pilih_kolom != "All":
            filter_item = unschedule_item[unschedule_item["Item Category"] == pilih_kolom]
        else:
            filter_item = unschedule_item

        st.write('Data Item yang belum masuk Preventive Maintenance')
        st.dataframe(filter_item, hide_index=True, use_container_width=True)
else:
    st.write('Upload data terlebih dahulu')
            