import streamlit as st
import pandas as pd
from pandas.io.formats.style import subset_args

#Streamlit title
st.title("Employee Check- Process Excel Data")

#File uploaded for Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Load the Excel file into a DataFrame
    df= pd.read_excel(uploaded_file)

    #Display tge first few rows of the DataFrame to confirm the data
    st.subheader("Preview of the Uploaded data")
    st.dataframe(df.head())

    # Convert 'Allocation End Date' column to Date-time format
    df['Allocation End Date']= pd.to_datetime(df['Allocation End Date'], format='%d/%m/%Y', errors='coerce')

    # Sort by 'Employee Number' and 'Allocation End Date' (Descending order)
    df_sorted= df.sort_values(by=['Employee Number', 'Allocation End Date'], ascending=[True, False])

    #Format the sorted 'Allocation End Date' back to string in the desired format ('dd/mm/yyyy')
    df_sorted['Allocation End Date']= df_sorted['Allocation End Date'].dt.strftime('%d/%m/%Y')

    # Drop duplicates based on 'Employee Number', keeping the row with the latest 'Allocation End Date'
    distict_employee_df= df_sorted.drop_duplicates(subset='Employee Number', keep='first')

    #Convert allocation end date to String again for saving it in the correct format
    distict_employee_df['Allocation End Date'] = pd.to_datetime(distict_employee_df['Allocation End Date'], format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

    # Display the resulting Dataframe with distinct Employee numbers
    st.subheader("Processed Data")
    st.dataframe(distict_employee_df)

    # option to download the resulting DataFrame as an Excel File
    output_file= "distinct_employee_numbers_latest.xlsx"
    distict_employee_df.to.excel(output_file, index=False)