
import streamlit as st

# 🎨 Background Color
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f4f8;
    }
    </style>
""", unsafe_allow_html=True)

# 💎 Stylish Centered Title
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>💪 BulkAI - Weight Gain Assistant</h1>", unsafe_allow_html=True)

# 🖼️ Banner Image
st.image("https://images.unsplash.com/photo-1517836357463-d25dfeac3438", use_container_width=True)

st.divider()

st.subheader("📋 Enter Your Details")

# 📦 Clean Column Layout
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Enter your weight (kg)", min_value=20.0)
    height = st.number_input("Enter your height (cm)", min_value=100.0)

with col2:
    age = st.number_input("Enter your age", min_value=10)
    gender = st.selectbox("Select Gender", ["Female", "Male"])

activity = st.selectbox("Activity Level", 
                        ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])

st.divider()

# 🚀 Stylish Button
if st.button("🚀 Generate My Plan"):
    st.success("Your personalized weight gain plan is ready!")
