import streamlit as st
import pickle
import string
import os
from text_transformation import transform_text
import os

import nltk

try:
    nltk.data.find("tokenizers/punkt")
except:
    nltk.download("punkt")

try:
    nltk.data.find("tokenizers/punkt_tab")
except:
    nltk.download("punkt_tab")

try:
    nltk.data.find("corpora/stopwords")
except:
    nltk.download("stopwords")

base_path = os.path.dirname(__file__)

tfidf_path = os.path.join(base_path, "vectorizer.pkl")
model_path = os.path.join(base_path, "model.pkl")

tfidf = pickle.load(open(tfidf_path, "rb"))
model = pickle.load(open(model_path, "rb"))

st.set_page_config(page_title="Spam Classifier", page_icon="📧", layout="centered")

st.markdown("""
    <h1 style='text-align:center; color:#4A90E2;'>📧 Email Spam Classifier</h1>
    <p style='text-align:center; font-size:17px; color:gray;'>
        Enter a message and let the AI detect whether it's <b>Spam</b> or <b>Not Spam</b>.
    </p>
""", unsafe_allow_html=True)

with st.container():
    st.write("### ✍️ Enter your message below:")
    input_sms = st.text_area("", height=150, placeholder="Type message here...")


if st.button("🔍 Predict", use_container_width=True):

    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message first.")
    else:
        # preprocess
        transformed_sms = transform_text(input_sms)

        # vectorize
        vector_input = tfidf.transform([transformed_sms])

        # predict
        result = model.predict(vector_input)[0]


        if result == 1:
            st.markdown("""
                <div style='padding:16px; border-radius:10px; background-color:#ffcccc; text-align:center;'>
                    <h2 style='color:#cc0000;'>🚨 Spam Detected!</h2>
                    <p>This message appears to be <b>Spam</b>.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style='padding:16px; border-radius:10px; background-color:#ccffcc; text-align:center;'>
                    <h2 style='color:#006600;'>✅ Not Spam</h2>
                    <p>This message looks <b>safe</b>.</p>
                </div>
            """, unsafe_allow_html=True)


# st.markdown("""
#     <br><hr>
#     <p style='text-align:center; color:gray; font-size:14px;'>
#         Built with ❤️ using Streamlit
#     </p>q
# """, unsafe_allow_html=True)
