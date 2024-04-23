import streamlit as st
import random

# Set page config to wide mode for better spacing
st.set_page_config(layout="wide", page_title="Yoga Flow Guide")

# Custom CSS for styling
custom_css = """
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
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Define a simple function to generate a yoga flow based on user input
def generate_yoga_flow(experience_level, focus_areas, special_considerations):
    # Placeholder dictionaries for each experience level
    poses = {
        'Beginner': [
            ('Mountain Pose', 'Tadasana', 'Stand with your feet together, hands at sides. Take a deep breath.'),
            # ... Add more beginner poses here
        ],
        'Intermediate': [
            ('Tree Pose', 'Vrikshasana', 'Stand on one leg, place the other foot on your inner thigh. Balance and breathe.'),
            # ... Add more intermediate poses here
        ],
        'Advanced': [
            ('King Pigeon Pose', 'Rajakapotasana', 'From a lunge, bend your back leg and reach back to grab your ankle.'),
            # ... Add more advanced poses here
        ]
    }
    
    # Select a random pose based on experience level
    pose_name, pose_sanskrit, instructions = random.choice(poses[experience_level])
    
    # Create the HTML content for the pose
    yoga_flow_html = f"""
    <div class="yoga-sequence">
        <div class="pose-title">{pose_name} ({pose_sanskrit})</div>
        <div class="step">{instructions}</div>
    </div>
    """
    
    return yoga_flow_html

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
st.markdown('<p class="big-title">Your Customized Yoga Pose</p>', unsafe_allow_html=True)

# Process the input and generate the yoga flow when the submit button is clicked
if submit_button:
    yoga_flow = generate_yoga_flow(experience_level, focus_areas, special_considerations)
    st.markdown(yoga_flow, unsafe_allow_html=True)
