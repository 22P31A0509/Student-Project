import streamlit as st
import google.generativeai as genai




# -------- ADD YOUR GEMINI API KEY HERE --------
genai.configure(api_key="your api key")




# Load Gemini model
model = genai.GenerativeModel("gemini-flash-latest")

# Function to get nutrition info
def get_nutrition(food_items):
    prompt = f"""
    Provide detailed nutritional information for the following foods:
    {food_items}

    Include:
    - Calories
    - Protein
    - Carbohydrates
    - Fat
    - Vitamins
    - Minerals
    """

    response = model.generate_content(prompt)
    return response.text


# -------- STREAMLIT UI --------

st.title("NutriAI - Instant Nutritional Information")

food_items = st.text_area(
    "Enter food items separated by commas"
)

if st.button("Get Nutrition Info"):
    if food_items:
        with st.spinner("Analyzing food items..."):
            result = get_nutrition(food_items)
            st.write(result)
    else:
        st.error("Please enter food items first.")

