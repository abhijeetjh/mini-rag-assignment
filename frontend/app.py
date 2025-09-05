import streamlit as st
import requests

st.title("Mini RAG Demo")

with st.form("Upload"):
    uploaded_file = st.file_uploader("Choose a text file")
    submitted = st.form_submit_button("Upload")
    if uploaded_file and submitted:
        files = {'file': uploaded_file}
        res = requests.post('http://localhost:8000/upload/', files=files)
        st.write(res.json())

query = st.text_input("Ask a question:")
if st.button("Submit"):
    res = requests.post('http://localhost:8000/query/', data={"q": query})
    st.write(res.json())
