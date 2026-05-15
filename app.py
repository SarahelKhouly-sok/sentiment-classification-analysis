import streamlit as st
import joblib

# Load model
model = joblib.load("model.joblib")

# Load vectorizer
vectorizer = joblib.load("tfidf.joblib")
import os
print(os.listdir())




# ----------------------------
# Page config
# ----------------------------
st.set_page_config(page_title="Emotion Classifier", layout="centered")

# ----------------------------
# Predict emotion using REAL model
# ----------------------------
def get_emotion(text):
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]

    # If your model already outputs labels, return directly
    # Otherwise map numeric labels here
    label_map = {
        0: "joy",
        1: "fear",
        2: "angry"
    }

    # Handle both string or numeric outputs
    if isinstance(pred, str):
        return pred.lower()
    else:
        return label_map.get(pred, "neutral")


# ----------------------------
# Background + emoji styling
# ----------------------------
def set_background(emotion):
    styles = {
        "joy": ("#1e90ff", "#ffffff", "😄"),
        "fear": ("#ffcc00", "#000000", "😨"),
        "angry": ("#ff3b30", "#ffffff", "😡"),
        "neutral": ("#000000", "#ffffff", "😐")
    }

    bg, txt, emoji = styles.get(emotion, ("#000000", "#ffffff", "😐"))

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg};
            color: {txt};
        }}

        textarea {{
            color: black !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    return emoji


# ----------------------------
# UI
# ----------------------------
st.title("🧠 Emotion Classification (ML Model)")

text = st.text_area("Enter your text:")

if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        emotion = get_emotion(text)
        emoji = set_background(emotion)

        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:90px;
                margin-top:20px;">
                {emoji}
            </div>

            <div style="
                text-align:center;
                font-size:30px;
                font-weight:bold;">
                DETECTED EMOTION: {emotion.upper()}
            </div>
            """,
            unsafe_allow_html=True
        )