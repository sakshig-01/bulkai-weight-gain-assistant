import streamlit as st

st.title("💪 BulkAI - Fitness Assistant")

st.header("Enter Your Details")

# User Inputs
weight = st.number_input("Enter your weight (kg)", min_value=20.0)
height = st.number_input("Enter your height (cm)", min_value=100.0)
age = st.number_input("Enter your age", min_value=10)

gender = st.selectbox("Select Gender", ["Female", "Male"])

activity = st.selectbox(
    "Activity Level",
    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
)

goal = st.selectbox("Select Your Goal", ["Weight Gain", "Weight Loss"])

# Activity multipliers
activity_multipliers = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725
}

if st.button("Generate Plan"):

    # Convert height to meters
    height_m = height / 100

    # BMI Calculation
    bmi = weight / (height_m ** 2)

    # BMR Calculation (Mifflin-St Jeor Equation)
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # TDEE
    tdee = bmr * activity_multipliers[activity]

    if goal == "Weight Gain":
        target_calories = tdee + 400
        recommendation = "Calorie Surplus for Healthy Weight Gain 💪"
    else:
        target_calories = tdee - 400
        recommendation = "Calorie Deficit for Healthy Weight Loss 🔥"

    st.subheader("📊 Your Results")

    st.write(f"**BMI:** {bmi:.2f}")
    st.write(f"**Estimated Daily Calories:** {int(target_calories)} kcal")
    st.write(f"**Plan Type:** {recommendation}")

    if bmi < 18.5:
        st.info("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are in the obese range.")
