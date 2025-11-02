import streamlit as st
import pandas as pd
import numpy as np
import kagglehub
from kagglehub import KaggleDatasetAdapter
 
# Set the path to the file you'd like to load
file_path = ""
 
# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "starbucks/store-locations",
  file_path,
  # Provide any additional arguments like
  # sql_query or pandas_kwargs. See the
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)
 
print("First 5 records:", df.head())
st.title('Starbucks Locations Worldwide')
st.subheader('Raw data')    
st.write(df)