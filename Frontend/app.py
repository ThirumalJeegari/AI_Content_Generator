import streamlit as st
import requests

server_url = st.secrets["backend_url"]


st.title("AI Content Generator")

with st.form("Generate Blogs, LinkedIn Posts, Captions, Emails and many more"):
    topic = st.text_input("Enter the Topic to Generate the Context")

    technology = st.selectbox("Enter the Technology",["Python","MySQL","Power BI","React Js","Node Js","Fast API","AI","Gen AI","MERN"])

    content =  st.selectbox("Content Type",["LinkedIn Post","Blog","Instagram Caption","Twitter Post","Email","YouTube Description"]) 

    tone = st.selectbox("Enter the tone",["Professional","Semi-Professional","Technical","Friendly","Casual","Marketing"])

    Submit_Button = st.form_submit_button("Submit")

    if Submit_Button:

        if topic == "":
            st.error("Please Enter the Topic Name")

        else:
            st.spinner("Generating Content...")


            response = requests.post(f"{server_url}/generate",params ={"topic":topic,"technology":technology,"content":content,"tone":tone})

            if response.status_code == 200:

                data = response.json()
                st.success("Content Generated Successfully")
                st.write(data["response"])


   