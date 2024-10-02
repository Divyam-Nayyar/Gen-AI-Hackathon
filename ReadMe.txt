*Run this on https://gen-ai-hackathon-dazzelers.streamlit.app/ *

AI-Powered Quality Control for Manufacturing
This project is a Streamlit web application designed to assist companies in optimizing their quality control processes using AI. The application offers features for customizing quality standards, real-time defect detection, predictive maintenance, blueprint analysis, and company registration.

Features
1. Customize Quality Standards
This feature allows users to set quality standards for different industries (Textile, Automobile, Electronics) and specify an acceptable defect rate.

Industry Selection: Choose your industry from a dropdown.
Defect Rate: Adjust the acceptable defect rate using a slider.
AI-Generated Standards: The system generates quality standards based on your inputs using the T5 model.
2. Real-Time Defect Detection and Predictive Maintenance
This section simulates real-time production data, detecting potential defects and determining if maintenance is required.

Simulated Production Data: Random sensor data and defect status are generated.
Defect Detection: AI detects any defects in the production line.
Predictive Maintenance: The system recommends whether maintenance is needed based on sensor data.
3. Submit Production Assembly Line Blueprint
Users can upload their production assembly line blueprints (PDF/PNG/JPG). The app analyzes the blueprint and identifies bottlenecks, providing suggestions to improve efficiency.

Blueprint Upload: Upload a file for analysis.
AI Feedback: The system provides an analysis report suggesting areas of improvement.
4. Register Your Company
This feature allows companies to register their details, including the company name, sector, website, and contact email.

Company Registration Form: Fill in your company details.
Confirmation: Successful registration is confirmed with a message.
Technology Stack
Streamlit: The web framework used to build the application.
Transformers (Hugging Face): T5 model for generating AI responses for quality standards.
Python: The core language used for building the app.
Random: To simulate production data in real-time.
How to Run
Install Dependencies: Make sure to install all required libraries using:

bash
Copy code
pip install streamlit transformers torch
Run the Application: Start the Streamlit app using the following command:

bash
Copy code
streamlit run app.py
Open in Browser: After running the above command, the app will be available at http://localhost:8501/ in your browser.

Future Improvements
Add more detailed blueprint analysis using advanced AI.
Include additional industries and more refined defect detection algorithms.
Implement real-time monitoring integration with external hardware sensors.
Contributing
Feel free to open issues or submit pull requests if you wish to contribute.
