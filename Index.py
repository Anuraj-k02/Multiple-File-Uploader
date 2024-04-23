import streamlit as st
import pandas as pd

st.title("Multiple File Uploader")

def multi_file_uploader():
    df_list = [] 
    
    uploaded_files = st.file_uploader("Choose multiple files...", accept_multiple_files=True)
    
    if uploaded_files:
        for file in uploaded_files:
            df = pd.read_excel(file)
            df_t = df.T
            df_list.append(df_t) 
    
        combined_df = pd.concat(df_list, axis=1)
        filename_input = st.text_input("Enter file name:", "File Name")  # Text input for file name
        filename = filename_input.strip()  # Remove leading/trailing spaces
        
        if st.button("Combined Excel File"):
            try:
                combined_df.to_excel(filename, index=False)
                with open(filename, "rb") as file:
                    file_data = file.read()
                st.download_button(
                    label="Click here to download",
                    data=file_data,
                    file_name=filename,
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
            except PermissionError:
                st.error("Error: Insufficient permissions to save the file. Please ensure you have write permissions to the specified directory.")
            except Exception as e:
                st.error(f"Error saving Excel sheet: {e}")

multi_file_uploader()
