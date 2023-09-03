import streamlit as st
import pandas as pd
from datetime import datetime
import PyPDF2
import time
st.title("CypherDocx")
st.sidebar.header("CypherDocx")
global call_text
def encryp(text,key):
    encrypted=""
    for i in range(len(text)):
        if text[i]==" ":
            encrypted+=" "
            continue
        encrypted+=chr(ord(text[i])+int(key)+i)
    return encrypted
def dencryp(text,key):
    encrypted=""
    for i in range(len(text)):
        if text[i]==" ":
            encrypted+=" "
            continue
        encrypted+=chr(ord(text[i])-int(key)-i)
    return encrypted
st.sidebar.write("*Get your Files/Docs/PDFs encrypted by world's most advanced encryption algorithms*")
option=st.sidebar.radio('Select an Option',["About","Encrypt File","Decrypt File","Download","More From the Team"])
if option=="About":
    st.subheader("_*get your files encrypted by CypherDocx*_")
if option=="Encrypt File":
    uploaded_files = st.file_uploader("Choose Your File", accept_multiple_files=True)
    try:
        pdf_file = open(uploaded_files[0].name, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        all_text = ''
        for page_index in range(num_pages):
            page = pdf_reader.pages[page_index]
            all_text += page.extract_text()
    except:
        st.write("Upload File")
    col1,col2=st.columns(2)
    with col1:
        prev=st.button("Preview",type="primary",use_container_width=True)
    with col2:
        encr=st.button("Encrypt",type="primary",use_container_width=True)
    if prev:
        st.header("*Normal Text*")
        st.write(all_text)
    if encr:
        #number = st.number_input('Enter key')
        file_path = 'templo.txt'
        with open(file_path, 'w',encoding='utf-8') as file:
            file.write(encryp(all_text,9))
        progress_text = "File Encrypting. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        st.header("*Encrypted Text*")
        file_path = 'templo.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            st.write(file_contents)



if option=="Decrypt File":
    uploaded_files = st.file_uploader("Choose Your File", accept_multiple_files=True,key=99)
    if uploaded_files:
        try:
            pdf_file = open(uploaded_files[0].name, 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            call_text=" "
            for page_index in range(num_pages):
                page = pdf_reader.pages[page_index]
                call_text += page.extract_text()
        except:
            try:
                file_path = uploaded_files[0].name
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                call_text=file_contents
            except:
                st.write("Upload Files")
        col3,col4=st.columns(2)
        with col3:
            prev2 = st.button("Preview", type="primary", use_container_width=True,key=65)
        with col4:
            decr = st.button("Decrypt", type="primary", use_container_width=True)
        if decr:
            file_path = 'templo.txt'
            with open(file_path, 'w',encoding='utf-8') as file:
                file.write(dencryp(call_text,9))
            progress_text = "File Decrypting. Please wait."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            st.header("*Decrypted Text*")
            file_path = 'templo.txt'
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()
                st.write(file_contents)
        if prev2:
            st.write(call_text)
if option=="Download":
    st.header("Click below to download your file")
    file_path = 'templo.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        if len(file_contents)<5:
            st.write("No file Found")
        else:
            st.download_button('Download File', file_contents)
if option=="More From the Team":
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)



