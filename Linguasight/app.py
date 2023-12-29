import time
import streamlit as st
import json
import joblib

from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
     with open(filepath, 'r')as f:
          return json.load(f)
     

model = joblib.load("model.joblib")

st.set_page_config(layout='wide')

animation = load_lottiefile('animation_lktu6n38.json')
title = st.container()
input_test = st.container()



with title:
    c1, c2, c3 = st.columns([1,3,1])
    with c2:
        st.markdown(
        """
            <style>
            .title{
                text-align: center;
                font-family: monospace;
                font-weight: bold;
            }
            .mainheading{
                text-align: center;
                font-family: monospace;
                font-size: 25px;
            }
            </style>
        """,
        unsafe_allow_html=True
        )
        st.markdown('<h1 class="title">Linguasight</h1>',unsafe_allow_html=True)
        st.markdown('<h2 class="mainheading"> Multilingual Language Detection Model</h2>',unsafe_allow_html=True)

st.write("<br>",unsafe_allow_html=True)

    


with input_test:
     c1,c2,c3 = st.columns([1,3,1])
     with c2:
        c11,c12,c13 = st.columns([1,1,1])
        with c12:
             st.write("<br>",unsafe_allow_html=True)
             st_lottie(animation,speed=1,reverse=False,quality='high',loop=True,width=250,height=250)
        st.write("<br>",unsafe_allow_html=True)
        html_code2 = f"""
<div style='
    font-family: Arial;
    text-align: bottom;
    '><h3>{'Enter a text below to detect its language'}</h3>
    </div>
        """
        st.markdown(html_code2,unsafe_allow_html=True)
        input_text = st.text_input('')
        predict = model.predict([input_text])[0]
        c21,c22,c23 = st.columns([1,1,1])
        with c22:
            with st.spinner(text='In progress'):
                if input_text == '':
                    st.success('Enter the Language')
                else:
                    st.success(predict)


st.write("<br>",unsafe_allow_html=True)
st.write("<br>",unsafe_allow_html=True)
st.write("<br>",unsafe_allow_html=True)

t = 'How LinguaSight Works:'
text = "LinguaSight operates on a sophisticated blend of natural language processing (NLP) and machine learning techniques, making it a proficient and reliable multilingual language detection model. When you input a text sample into LinguaSight, the model undergoes a series of steps to determine the language. First, the text is preprocessed to clean and normalize it, removing irrelevant characters and handling special symbols. Next, LinguaSight utilizes the TF-IDF vectorization technique to convert the preprocessed text into a unique numerical representation. By calculating the Term Frequency-Inverse Document Frequency (TF-IDF) values for character n-grams, LinguaSight creates a distinctive vector that captures the significance of each n-gram within the text. Leveraging its trained machine learning model, LinguaSight predicts the language based on the learned patterns and characteristics from diverse texts during its training phase. The language with the highest probability score is then determined as the detected language. With the results displayed through a user-friendly interface or API integration, LinguaSight offers seamless and intuitive language detection for a wide range of languages, including Arabic, Danish, Dutch, English, French, German, Greek, Hindi, Italian, Kannada, Malayalam, Portuguese, Russian, Spanish, Swedish, Tamil, and Turkish, among others. Its high accuracy and efficiency make it an invaluable tool for various applications, from content moderation and customer support to multilingual data analysis and global marketing. Experience the power of LinguaSight and unravel the hidden languages within your text data today."
lang = 'Arabic, Danish, Dutch, English, French, German, Greek, Hindi, Italian, Kannada, Malayalam, Portuguese, Russian, Spanish, Swedish, Tamil, and Turkish'
html_code = f"""
<div style='
    background-color: #2A2937;
    border-radius: 5px;
    padding: 20px;
    font-family: Arial;
    font-size: 20px;
    '><h4>{t}</h4>
    <P>{text}</P>
    <h4>{"Languages detected by the model"}</h4>
    <p>{lang}</p>
    <h4>{"Technique Used in Linguasight"}</h4>
    <P>{"LinguaSight leverages advanced techniques in natural language processing (NLP) and machine learning to deliver robust multilingual language detection capabilities. At the core of its language detection prowess lies the TF-IDF (Term Frequency-Inverse Document Frequency) vectorization technique. This process involves breaking down the input text into character n-grams and calculating their term frequency, measuring the importance of each n-gram within the specific text. Simultaneously, the inverse document frequency evaluates the significance of these n-grams across the entire corpus, considering their uniqueness or commonality. By combining these metrics, LinguaSight creates a TF-IDF vector that captures the distinctive linguistic features of each language, enabling accurate and efficient language identification.<br><br>The second pillar of LinguaSight's strength lies in its trained machine learning model. Through exposure to diverse texts in multiple languages, the model learns to recognize patterns and characteristics specific to each language. This acquired knowledge empowers LinguaSight to make informed decisions during language classification, accurately assigning the detected language. The model's adaptability to new texts and languages ensures continuous improvement, enhancing its performance over time.<br><br>The integration of TF-IDF vectorization and machine learning in LinguaSight's architecture offers several benefits. It provides robust multilingual support, allowing LinguaSight to handle various languages with distinct writing systems and vocabularies effectively. The resulting accuracy and efficiency make it a reliable solution for multilingual text analysis, enabling users to gain valuable insights and optimize language-specific processes. Additionally, LinguaSight's seamless integration through APIs and web interfaces facilitates easy incorporation into applications and workflows, making it an accessible and user-friendly tool."}</P>
    <br>
    <br>
    <br>
    <h3>{"-Team Divas"}</h3>
    </div>
        """
st.markdown(html_code,unsafe_allow_html=True)