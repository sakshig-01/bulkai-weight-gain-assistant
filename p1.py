import streamlit as st

st.set_page_config(page_title="BulkAI", page_icon="💪")

st.title("💪 BulkAI - AI Weight Gain Assistant")

st.header("Enter Your Details")

weight = st.number_input("Enter your weight (kg)", min_value=20.0)
height = st.number_input("Enter your height (cm)", min_value=100.0)
age = st.number_input("Enter your age", min_value=10)

gender = st.selectbox("Select Gender", ["Female", "Male"])

activity = st.selectbox(
    "Activity Level",
    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
)

if st.button("Generate Plan"):

    # BMR calculation
    if gender == "Female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age + 5

    activity_multiplier = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }

    maintenance = bmr * activity_multiplier[activity]
    bulk_calories = maintenance + 400
    protein = weight * 2

    st.success("🔥 Your Personalized Bulking Plan")

    st.write(f"🍽 Daily Calories Needed: {round(bulk_calories)} kcal")
    st.write(f"🥩 Daily Protein Needed: {round(protein)} grams")

    st.subheader("📋 Simple Diet Suggestion")

    st.write("""
    **Breakfast:** Milk + Banana + Peanut Butter  
    **Lunch:** Rice + Dal + Sabzi + Curd  
    **Evening Snack:** Peanut butter sandwich + Milk  
    **Dinner:** Roti + Paneer/Chicken + Salad  
    **Before Bed:** Glass of Milk
    """)

