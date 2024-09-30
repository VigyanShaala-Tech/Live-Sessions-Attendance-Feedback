#import necessary libraries
import streamlit as st
import pandas as pd
import pyperclip  # Import the pyperclip module for clipboard operations
import os
import requests
#from supabase_py import create_client,Client
#from supabase_py import create_client,Client
# Read the category dataset and extract unique categories

from io import StringIO  # Import StringIO directly from the io module
from io import BytesIO
from datetime import datetime
from supabase import create_client, Client
from supabase.client import ClientOptions


# Function to get the current timestamp
def get_timestamp():
    return datetime.now()

# Display the PNG image in the top left corner of the Streamlit sidebar with custom dimensions
image_path = 'https://twetkfnfqdtsozephdse.supabase.co/storage/v1/object/sign/stemcheck/VS-logo.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzdGVtY2hlY2svVlMtbG9nby5wbmciLCJpYXQiOjE3MjE5NzA3ODUsImV4cCI6MTc1MzUwNjc4NX0.purLZOGk272W80A4OlvnavqVB9u-yExhzpmI3dZrjdM&t=2024-07-26T05%3A13%3A02.704Z'
st.markdown(
    f'<div style="text-align:center"><img src="{image_path}" width="150"></div>',
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='color: black; font-weight: bold;'>Kalpana - She for STEM Accelerator 3.0 | Mentor Registration Form</h1>", 
    unsafe_allow_html=True
)


Name=st.text_input("Enter your full name")
Email_id=st.text_input("Enter your email address")
Number=st.text_input("Enter your WhatsApp number (with country code, DONOT ADD '+' ")
Profile=st.text_input("Enter your LinkedIn profile link here")
Institute=st.text_input("Enter your current Institute/University/Organization")
Current_job=st.text_input("Current Job title/Designation*")
primary_key = f"{Number}_{Name}"

selected_optionss = st.radio("Highest degree obtained *", ("B.Sc.","M.Sc.","B.E./B.Tech.","M.Tech.","B.Pharm.","M.Pharm.","MBA","Ph.D.","Other:"))
if selected_optionss == "Other":
    other_response = st.text_input("Other:")

country_names = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","The Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin",
"Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon",
"Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo, Democratic Republic of the Congo", "Republic of the","Costa Rica",
"Côte d’Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark",
"Djibouti","Dominica","Dominican Republic","East Timor (Timor-Leste)","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini",
"Ethiopia","Fiji","Finland","France","Gabon","The Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana"
"Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya",
"Kiribati","Korea", "North Korea", "South Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania",
"Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia, Federated States of","Moldova",
"Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar (Burma)","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger",
"Nigeria","North Macedonia","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia",
"Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","Spain","Sri Lanka",
"Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia",
"Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu",
"Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]
selected_status = st.selectbox('Country you currently reside in*', country_names)

city=st.text_input("Your current city*")

options = ['English','Hindi','Marathi','Malayalam','Kannada','Telgu','Assamese','Bengali','Gujarati','Manipuri','Tamil','Odia','Punjabi','Urdu','Maithili','Konkani','Kashmiri']
selected_options = st.multiselect("What communication languages are you comfortable in? * ", options)

language=st.text_input("List two languages (other than english) you are proficient in speaking, reading and writing. Example Hindi, Marathi.*")
option = st.radio("Would you be available to participate in a two-hour training session at the start of the program?", ("Yes","No"))

options = ['Basic Science-Physics','Basic Science-Chemistry','Basic Science-Life Science, Bio Chemistry','Basic Science-Botany/Zoology','Basic Science-Microbiology, Molecular Biology','Engg-BSC,BCA,IT,Computer Science','Engg-Mechanical,Civil,Production,Industrial,Mining','Engg- Electronics, Electronics and Telecomm,Electrical','Engg-Chemical/Mettalurgical/Material Science Engineering', 'Sp1: Agricultural, Aerospace/Aeronautical, Biomed/Bio Tech','Sp2:Marine,Petroleum,Thermal,Power plant,Nuclear','Not Applicable','Others']
selected_option = st.selectbox(' Main Subject Area (In case of no specialization, choose your favourite subject area)*', options)

keyword=st.text_input("Give us three keywords that associated with your current STEM work.*")
description=st.text_input("How would you explain your current work to a broad undergraduate STEM community? [Max 50 words]")
option2 = st.radio("How many hours per week are you wiling to commit for this mentoring program?", ("1-2","2-3","3-4","4-5",">5"))
option3 = st.radio("For conducting mentoring sessions, please indicate your preferred time slots (IST).", ("9 am - 12:00 noon IST","12 noon - 3 pm IST","3 pm - 6 pm IST","6 pm - 9 pm IST","9 pm - 12:00 am midnight IST"))
skills=st.text_input("What 4 technical skills/soft skills can you share with the mentees?*")
option4 = st.radio("Would you like to design a hands-on scientific project for this mentoring program?", ("Yes","No"))

if_yes=st.text_input("If yes, how would you design a home-lab based and/or computational hands-on scientific project for mentoring Kalpana fellows?")


#uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
uploaded_file = st.file_uploader(" Upload your Curriculum Vitae/Resume *", accept_multiple_files=False, type=["csv", "txt"])

if uploaded_file is not None:
    # Check file size
    if len(uploaded_file.getvalue()) <= 10*1024*1024:  # Check if file size is within the limit (10MB)
        file_contents = uploaded_file.getvalue()
        st.write("File uploaded successfully. Content:")
    else:
        st.write("File size exceeds the limit of 10MB. Please upload a smaller file.")


comments=st.text_input("If you have any comments, suggestions you want us to think about, please let us know.")

def create_feedback_dataframe(primary_key, Name, Email_id, Number, Profile, Institute, Current_job, selected_optionss, selected_status, city, selected_options, language, option, selected_option, keyword, description, option2, option3, skills, option4, if_yes):
    data = {
        'Unique ID': primary_key,
        'Enter your full name': Name,
        'Enter your email address': Email_id,
        "Enter your WhatsApp number (with country code, DONOT ADD '+'": Number,
        'Enter your LinkedIn profile link here': Profile,
        'Enter your current Institute/University/Organization': Institute,
        'Current Job title/Designation*': Current_job,
        'Highest degree obtained *': selected_optionss,
        'Country you currently reside in*': selected_status,
        'Your current city*': city,
        'What communication languages are you comfortable in? *': selected_options,
        'List two languages (other than english) you are proficient in s': language,
        'Would you be available to participate in a two-hour training se': option,
        'Main Subject Area (In case of no specialization, choose your fa': selected_option,
        'Give us three keywords that associated with your current STEM w': keyword,
        'How would you explain your current work to a broad undergraduat': description,
        'How many hours per week are you wiling to commit for this mento': option2,
        'For conducting mentoring sessions, please indicate your preferr': option3,
        'What 4 technical skills/soft skills can you share with the ment': skills,
        'Would you like to design a hands-on scientific project for this': option4,
        'If yes, how would you design a home-lab based and/or computatio': if_yes,
        'If you have any comments, suggestions you want us to think abou': comments,
        'Upload your Curriculum Vitae/Resume *': uploaded_file.name if uploaded_file else None
    }

    feedback_df = pd.DataFrame([data])
    return feedback_df



url: str = 'https://twetkfnfqdtsozephdse.supabase.co'
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR3ZXRrZm5mcWR0c296ZXBoZHNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE5Njk0MzcsImV4cCI6MjAzNzU0NTQzN30.D76H5RoTel0M7Wj6PTRSAXxxYGic7K25BSaeQDZqIN0'
# Create a Supabase client
supabase: Client = create_client(url, key,
  options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
  ))


combined_button_text = "Submit"   

if st.button(combined_button_text):
    feedback_df = create_feedback_dataframe(primary_key, Name, Email_id, Number, Profile, Institute, Current_job, selected_optionss, selected_status, city, selected_options, language, option, selected_option, keyword, description, option2, option3, skills, option4, if_yes)

    # Prepare the JSON data
    json_data = feedback_df[['Unique ID', 'Enter your full name', 'Enter your email address',"Enter your WhatsApp number (with country code, DONOT ADD '+'",'Enter your LinkedIn profile link here','Enter your current Institute/University/Organization','Current Job title/Designation*','Highest degree obtained *','Country you currently reside in*','Your current city*','What communication languages are you comfortable in? *','List two languages (other than english) you are proficient in s','Would you be available to participate in a two-hour training se','Main Subject Area (In case of no specialization, choose your fa','Give us three keywords that associated with your current STEM w','How would you explain your current work to a broad undergraduat','How many hours per week are you wiling to commit for this mento','For conducting mentoring sessions, please indicate your preferr','What 4 technical skills/soft skills can you share with the ment','Would you like to design a hands-on scientific project for this','If yes, how would you design a home-lab based and/or computatio']].to_dict(orient='records')[0]

    table_name = "Registration"

    # Insert the JSON data into Supabase
    response_json = supabase.table(table_name).insert([json_data]).execute()

    
   


    
