import streamlit as st
import google.generativeai as genai

# Set up your API key here
api_key = 'AIzaSyDZAM2I9feua7e54H_v071RKXZjgQTwqNg'
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# Adjusted function to match the expected input structure for the Gemini API
def generate_content_with_gemini(prompt_text):
    # The API might be expecting a structured dict with a 'parts' key
    request_content = {
        "parts": [{"text": prompt_text}],
        # Add other keys like 'max_length' if needed by the API
    }
    response = model.generate_content(request_content)
    return response.text


# Set page config to wide mode for better spacing
st.set_page_config(layout="wide", page_title="Yoga Flow Guide")

# Custom CSS for styling
st.markdown("""
    <style>
        .textbox {
            background-color: #f0f0f0;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
        }
        .big-title {
            font-size: 300%;
            font-weight: bold;
        }
        .guide-title {
            font-size: 120%;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .yoga-sequence {
            font-family: "Lucida Console", Monaco, monospace;
            background-color: #fafafa;
            border-radius: 5px;
            padding: 20px;
            margin-top: 20px;
            border: 1px solid #ccc;
        }
        .pose-title {
            font-weight: bold;
            font-size: 110%;
        }
        .step {
            margin-left: 20px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for user input
with st.sidebar:
    st.markdown('<div class="textbox">', unsafe_allow_html=True)
    st.markdown('<div class="guide-title">Yoga Practice Planner</div>', unsafe_allow_html=True)
    st.markdown("""
    Provide details about your current situation and needs for your yoga practice. The guide will be generated to be easily followed by voice instruction.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar form for input collection
    with st.form(key='yoga_planner_form'):
        experience_level = st.selectbox(
            "Select your experience level:",
            options=["Beginner", "Intermediate", "Advanced"],
            help="Choose a level that best describes your yoga proficiency."
        )
        focus_areas = st.multiselect(
            "What are your focus areas?",
            options=["Flexibility", "Strength", "Balance", "Relaxation"],
            help="Select one or more areas you want to focus on during your practice."
        )
        special_considerations = st.text_area(
            "Any special considerations?",
            help="Let us know if you have any injuries or preferences."
        )
        submit_button = st.form_submit_button(label='Generate Yoga Flow')

# Main area for title and generated yoga flow
st.markdown('<p class="big-title"> 🧘🏻 Your Customized Yoga Sequence</p>', unsafe_allow_html=True)

# Generate content when the form is submitted
if submit_button:
    # Build the text prompt for the API call
    prompt_text = f"Create a yoga flow for someone with experience level: {experience_level}, " \
                  f"focus areas: {', '.join(focus_areas)}, " \
                  f"and the following considerations: {special_considerations}"
    
    yoga_flow = generate_content_with_gemini(prompt_text)
    st.markdown(yoga_flow, unsafe_allow_html=True)


