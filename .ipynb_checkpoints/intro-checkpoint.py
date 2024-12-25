import time
import streamlit as st
import streamlit as st
# import pandas as pd
import pandas as pd
from streamlit import progress

#
# st.set_page_config(layout = "wide", page_title = "Lecture")
st.set_page_config(layout = "wide", page_title = "Lecture")
#
# st.title("Sagar's Streamlit app")
st.title("Sonu Streamlit app")
# st.header("Header text")
st.title("Header text")
# st.subheader("First subheading")
st.subheader("First subheading")
#
# st.write("This is the text line using write function")
st.write("this is the text line using write function")
#
# st.code("""
st.code("""

# def show_date(name):
def show_date(name):
#     print("Hi", name)
    print("Hi",name)
# """)
#
# df = pd.DataFrame(
df = pd.DataFrame([['Andhra Pradesh', 'Adilabad', 19.284513950073435,
         78.81321233480176, 2741239],
        ['Andhra Pradesh', 'Anantapur', 14.312065561843148,
        77.4601584478577, 4081148]])

#     [['Andhra Pradesh', 'Adilabad', 19.284513950073435,
#         78.81321233480176, 2741239],
#        ['Andhra Pradesh', 'Anantapur', 14.312065561843148,
#         77.4601584478577, 4081148]]
# )
# st.dataframe(df)
st.dataframe(df)
#
# st.json(df)
st.json(df)

#
# col1, col2 = st.columns(2)
col1, col2 = st.columns(2)
# with col1:
with col1:
#     st.image("Superstore_bg.jpg")
    st.image("Superstore_bg.jpg")  # Adjust the path as necessary
# with col2:
with col2:
#     st.dataframe(df)
    st.dataframe(df)
#
# # st.video()
#st.video()
# # st.audio()
#st.audio()
#
# st.metric("Total Cases", "250", "-50%", help = "These are total cases of Corona Virus pandemic")
st.metric("Total cases", "250","-50%",help="These are total cases of corona Virus pandemic")
#
# st.markdown("""
st.markdown("""
python Frameworks-
-Tkinter
-Dash
-Flask
-Streamlit
""")
# ### Python Frameworks
# - Tkinter
# - Dash
# - Flask
# - Streamlit
# """)
#
# st.error("Some Error Occurred")
st.error("Some Error occurred")
# st.success("Successful")
st.success("Sucessful")
# st.info("Information")
st.info("Information")
# st.warning("Warn")
st.warning("warn")
#
# st.sidebar.title("This is a sidebar")
st.sidebar.title("This is a sidebar")
#
# st.button("OKAY")
st.button("OKAY")
#
# st.sidebar.button("Login")
st.sidebar.button("Login")
#
# st.selectbox("Select an option", ["Option 1", "Option 2", "Option"])
st.selectbox("Select an option",["option 1" , "Option 2" , "Option"])
#
# st.checkbox("Checkbox 1")
st.checkbox("checkbox 1")
#
# st.slider("My slider", 0, 100)
st.slider("My slider",0,100)
#
# st.text_input("Enter your name")
st.text_input("Enter Your name")
#
# st.number_input("Enter age", min_value=0.0, max_value=100.5, step=0.5)
st.number_input("Enter age" , min_value=0.0 ,max_value=100.5, step=0.5)
#
# st.text_area("address")
st.text_area("address")
#
# st.date_input("DOB")
import streamlit as st

# Correct usage for date input
dob = st.date_input("DOB")
#
# st.file_uploader("Upload resume")
st.file_uploader("Upload resume")
#
# st.radio("Gender", ["Male", "Female"])
st.radio("Gender",["Male" , "Female"])

st.title("Login Form")

email = st.text_input("Enter Email")
password = st.text_input("Password")

login_btn = st.button("Login")
if login_btn:
    if email == "test@gmail.com" and password == "9898":
        st.balloons()
        st.snow()
        st.success("Login Successful")
    else:
        st.error("Invalid")
#
# a = st.progress(0)
a = st.progress(0)
#
# progress_text = "Operation in progress. Please wait."
progress_text = "operation in progress. Please wait"
# my_bar = st.progress(0, text=progress_text)
my_bar = st.progress(0, text=progress_text)
#
# for percent_complete in range(100):
for percent_complete in range(100):
    time.sleep(0.01)
#     time.sleep(0.01)

#     my_bar.progress(percent_complete + 1, text=progress_text)
my_bar.progress(percent_complete + 1 , text=progress_text)
# time.sleep(1)
time.sleep(1)
# my_bar.empty()
my_bar.empty()
#
# st.button("Rerun")
st.button("Rerun")
#
#
# with st.spinner('Wait for it...'):
with st.spinner('Wait for it...'):
    time.sleep(5)
#     time.sleep(5)
# st.success('Done!')
st.success("Done!")

