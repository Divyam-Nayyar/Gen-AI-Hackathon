import streamlit as st
st.subheader("Register Your Company")

with st.form("company_form"):
    company_name = st.text_input("Company Name")
    sector = st.selectbox("Sector", ["Textile", "Automobile", "Electronics", "Pharmaceutical", "Others"])
    website = st.text_input("Company Website")
    contact_email = st.text_input("Contact Email")

    submitted = st.form_submit_button("Register")

if submitted:
    st.write(f"Company '{company_name}' has been registered successfully!")

company_data = []

if submitted:
    company_data.append({
        "name": company_name,
        "sector": sector,
        "website": website,
        "contact_email": contact_email
    })
    st.write("Thank you for registering! We will contact you soon.")

import streamlit as st
import random
from transformers import T5ForConditionalGeneration, T5Tokenizer

# T5 Model initialization
model_name = "google/flan-t5-base"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Function for generating responses using T5 Flan
def generate_response(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=50, num_beams=5)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit UI
st.title("AI-Powered Quality Control for Manufacturing")

# Feature 1: Customize Quality Standards
st.subheader("Customize Quality Standards")
industry = st.selectbox("Select Industry", ["Textile", "Automobile", "Electronics"])
defect_rate = st.slider("Acceptable Defect Rate (%)", 0, 20, 5)

def get_quality_standards(industry, defect_rate):
    input_text = f"Set quality standards for {industry} with a defect rate of {defect_rate}%."
    return generate_response(input_text)

if st.button("Get Quality Standards"):
    standards = get_quality_standards(industry, defect_rate)
    st.write(f"Generated Standards: {standards}")

# Feature 2: Real-Time Defect Detection and Predictive Maintenance
st.subheader("Real-Time Defect Detection and Predictive Maintenance")

def simulate_production_data():
    return {"sensor_data": random.randint(50, 100), "status": random.choice(["OK", "Defect"])}

def detect_defect(data):
    return "Defect Detected" if data['status'] == "Defect" else "No Defect"

def predictive_maintenance(data):
    return "Maintenance Required" if data['sensor_data'] < 60 else "No Maintenance Needed"

if st.button("Start Monitoring"):
    for _ in range(10):  # Simulate 10 rounds of production
        data = simulate_production_data()
        defect_status = detect_defect(data)
        maintenance_status = predictive_maintenance(data)
        st.write(f"Sensor Data: {data['sensor_data']}, Status: {defect_status}, Maintenance: {maintenance_status}")

# Feature 3: Submit Blueprint Design
st.subheader("Submit Production Assembly Line Blueprint")
uploaded_file = st.file_uploader("Upload your production assembly line blueprint (PDF/Image)", type=["pdf", "png", "jpg"])

def analyze_blueprint(file):
    return "Identified possible bottleneck at Station 3. Suggest installing buffer or adjusting machine speed."

if uploaded_file is not None:
    feedback = analyze_blueprint(uploaded_file)
    st.write("Blueprint Analysis Report:")
    st.write(feedback)

# Feature 4: Register Company Webpage
st.subheader("Register Your Company")
with st.form("company_form"):
    company_name = st.text_input("Company Name")
    sector = st.selectbox("Sector", ["Textile", "Automobile", "Electronics", "Pharmaceutical", "Others"])
    website = st.text_input("Company Website")
    contact_email = st.text_input("Contact Email")

    submitted = st.form_submit_button("Register")

if submitted:
    company_data.append({
        "name": company_name,
        "sector": sector,
        "website": website,
        "contact_email": contact_email
    })
    st.write(f"Company '{company_name}' has been registered successfully!")

