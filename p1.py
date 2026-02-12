import streamlit as st

st.title("💪 BulkAI - Weight Gain Assistant")

st.header("Enter Your Details")

weight = st.number_input("Enter your weight (kg)", min_value=20.0)
height = st.number_input("Enter your height (cm)", min_value=100.0)
age = st.number_input("Enter your age", min_value=10)

gender = st.selectbox("Select Gender", ["Female", "Male"])
activity = st.selectbox("Activity Level", 
                        ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])

if st.button("Calculate Plan"):

    # BMR Calculation
    if gender == "Female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age + 5

    # Activity multiplier
    activity_multiplier = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }

    maintenance = bmr * activity_multiplier[activity]

    bulk_calories = maintenance + 400
    protein = weight * 2

    st.success("🔥 Your Bulking Plan")

    st.write(f"Daily Calories Needed: {round(bulk_calories)} kcal")
    st.write(f"Daily Protein Needed: {round(protein)} grams")

    st.subheader("Simple Diet Suggestion")
    st.write("""
    🍳 Breakfast: 4 eggs / paneer + milk + banana  
    🍚 Lunch: Rice + dal + sabzi + curd  
    🥜 Evening: Peanut butter sandwich + milk  
    🍗 Dinner: Roti + chicken / paneer + salad  
    🥛 Before bed: Milk
    """)

