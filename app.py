import streamlit as st
import joblib
import re

# ------------------ LOAD MODEL ------------------ #
model = joblib.load("models_v2/mnb.pkl")
vectorizer = joblib.load("models_v2/vectorizer.pkl")

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="Spam SMS Detector",
    page_icon="📩",
    layout="centered"
)

st.title("📩 Spam / Scam SMS Detector")
st.write("Paste an SMS to check its **risk level**.")

# ------------------ INPUT ------------------ #
message = st.text_area(
    "Enter SMS text",
    placeholder="Example: Your bank account has been suspended. Verify now..."
)

risk = None
color = None
spam_proba = None

# ------------------ PREDICTION ------------------ #
if st.button("Predict"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        msg = message.lower()

        # -------- Rule 1: OTP override (very low risk) -------- #
        if (
            re.search(r"\b\d{4,8}\b", msg)
            and "otp" in msg
            and "click" not in msg
            and "link" not in msg
        ):
            spam_proba = 0.05
            risk = "Low Risk 🟢"
            color = "green"

        else:
            # ML prediction
            vector = vectorizer.transform([message])
            spam_proba = model.predict_proba(vector)[0][1]

            # -------- Rule 2: Dangerous intent + link boost -------- #
            danger_words = [
                "verify", "suspended", "restricted",
                "urgent", "refund", "account", "blocked"
            ]

            if any(w in msg for w in danger_words) and "http" in msg:
                spam_proba = max(spam_proba, 0.85)

            # -------- Risk buckets -------- #
            if spam_proba < 0.10:
                risk = "Likely Legit 🟢"
                color = "green"
            elif spam_proba < 0.80:
                risk = "Promotional / Suspicious 🟡"
                color = "orange"
            else:
                risk = "High Risk Scam 🔴"
                color = "red"

# ------------------ OUTPUT ------------------ #
if risk:
    st.markdown(
        f"<h3 style='color:{color}'>{risk}</h3>",
        unsafe_allow_html=True
    )
    st.write(f"Spam confidence: **{spam_proba * 100:.1f}%**")
    st.caption("⚠️ This is a risk estimate. Always verify the sender.")
