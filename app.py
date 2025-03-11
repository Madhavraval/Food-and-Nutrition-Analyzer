import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini AI response
def get_gemini_response(prompt, images):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt] + images)
    return response.text

# Function to process uploaded images
def input_image_setup(uploaded_files):
    image_data_list = []
    
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            image_data_list.append({
                "mime_type": uploaded_file.type,  
                "data": bytes_data
            })
    
    return image_data_list if image_data_list else None

# Streamlit UI
st.set_page_config(page_title="Food Analyzer", layout="wide")
st.title("🍽️Food & Nutrition Analyzer")

st.write("Upload an image of your meal, and Gemini AI will analyze the food items and estimate calorie intake.")

# User input and file uploader
input_prompt = st.text_input("Enter any additional instructions (optional):", key="input")
uploaded_files = st.file_uploader("Upload food images:", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Display uploaded images in a fixed size
if uploaded_files:
    st.subheader("Uploaded Images:")
    
    # Define column layout (Max 3 images per row)
    num_cols = min(len(uploaded_files), 3)
    cols = st.columns(num_cols)

    for i, uploaded_file in enumerate(uploaded_files):
        image = Image.open(uploaded_file)
        with cols[i % num_cols]:  # Distribute images evenly in columns
            st.image(image, caption=f"Image {i+1}", width=250)  # Fixed width

submit = st.button("🔍 Analyze Food & Calories")

# AI prompt for nutrition analysis
nutrition_prompt = """
You are a professional nutritionist. Analyze the food items in the images and provide a calorie estimate.
The response should be structured as follows:

🍽️ **Meal Breakdown**:
1. Food Item 1 - Calories
2. Food Item 2 - Calories
---
🍎 **Total Estimated Calories**: XYZ kcal
🥗 **Health Suggestions**: (if necessary)
"""

# Generate response when button is clicked
if submit:
    image_data = input_image_setup(uploaded_files)
    
    if not image_data:
        st.error("⚠️ Please upload at least one image!")
    else:
        with st.spinner("Analyzing the food items... 🍕🥗"):
            response = get_gemini_response(nutrition_prompt + input_prompt, image_data)
        
        st.subheader("📊 Analysis Result:")
        st.write(response)