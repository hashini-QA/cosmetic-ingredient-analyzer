import streamlit as st
import pandas as pd
from PIL import Image

from backend.analyzer import load_db, analyze_ingredients
from services.ocr import extract_text_from_image
from services.llm_normalizer import normalize_ingredients_from_ocr
from services.ai_insights import generate_ai_insights
from services.chatbot import chatbot_answer

from db.repo import create_user, save_search


if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "ingredients_text" not in st.session_state:
    st.session_state.ingredients_text = None


st.set_page_config(
    page_title="AI Beauty Product Ingredient Analyzer",
    layout="wide"
)

st.title("AI Beauty Product Ingredient Analyzer")

name = st.text_input("Your Name")
email = st.text_input("Your Email")

skin_type = st.selectbox(
    "Skin Type",
    ["Oily", "Dry", "Sensitive", "Normal", "Combination"]
)

uploaded_image = st.file_uploader(
    "Upload ingredient label image",
    type=["jpg", "jpeg", "png"]
)

if st.button("Analyze Product"):
    if not name or not email:
        st.error("Please enter your name and email.")
    elif not uploaded_image:
        st.error("Please upload an ingredient label image.")
    else:
        # OCR
        image = Image.open(uploaded_image)
        ocr_text = extract_text_from_image(image)

      
        ingredients = normalize_ingredients_from_ocr(ocr_text)

        if not ingredients:
            st.error("Could not extract ingredients from the image.")
        else:
            ingredient_db = load_db("ingredients.json")

            result = analyze_ingredients(
                ingredients_list=ingredients,
                db=ingredient_db,
                skin_type=skin_type
            )

            
            st.session_state.analysis_result = result
            st.session_state.ingredients_text = ", ".join(ingredients)
            st.session_state.chat_messages = []  # reset chat

if st.session_state.analysis_result:
    result = st.session_state.analysis_result

    st.subheader("Ingredients")
    st.markdown(f"**({st.session_state.ingredients_text})**")

    st.subheader("Analysis Scores")
    col1, col2 = st.columns(2)
    col1.metric("Safety Score", result["summary"]["safety_score"])
    col2.metric("Avg Comedogenic Score", result["summary"]["avg_comedogenic"])

    st.subheader("Flagged Ingredients")
    if result["summary"]["flagged_items"]:
        flagged_df = pd.DataFrame(result["summary"]["flagged_items"])
        st.dataframe(flagged_df, width="stretch")
    else:
        st.success("No medium or high-risk ingredients detected.")

    st.subheader("Ingredient Uses & Benefits")
    details_df = pd.DataFrame(result["details"])[
        ["Ingredient", "Category", "Benefits", "Risk", "Comedogenic"]
    ]
    st.dataframe(details_df, width="stretch")

    st.subheader("AI Insights")
    insights = generate_ai_insights(
        product="Uploaded Product",
        skin_type=skin_type,
        analysis=result
    )
    st.write(insights)
   
    try:
        user_id = create_user(name, email)

        save_search(
            user_id=user_id,
            ingredients=st.session_state.ingredients_text,
            safety_score=result["summary"]["safety_score"],
            avg_comed=result["summary"]["avg_comedogenic"]
        )

        st.success("Your analysis has been saved successfully.")

    except Exception as e:
        st.error("Database error while saving results.")
        st.exception(e)


st.subheader("Ask the Skincare Assistant")


for msg in st.session_state.chat_messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


user_input = st.chat_input("Ask a question about this product")

if user_input:
    
    st.session_state.chat_messages.append(
        {"role": "user", "content": user_input}
    )

    
    with st.spinner("Thinking..."):
        reply = chatbot_answer(
            messages=st.session_state.chat_messages,
            analysis=st.session_state.analysis_result,
            skin_type=skin_type
        )

   
    st.session_state.chat_messages.append(
        {"role": "assistant", "content": reply}
    )

    
    st.rerun()

