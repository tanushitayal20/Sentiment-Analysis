###
# streamlit run <folder_name>\sentiment_analysis.py
###
#This code has been written by Tanushi Tayal

#Library for NLP: TextBlob
#Library for making a dataset and representing analysis per sentence: Pandas
#Library for data visualisation: Plotly
#Framework to host the project: Streamlit 
from textblob import TextBlob
import streamlit as st
import pandas as pd
import plotly.express as px

#func that will analyse the polarity
def analyse(text=""):
    results = []
    blob = TextBlob(text)
    for sentence in blob.sentences:
        out = get_sentiment(sentence.sentiment.polarity)
        results.append({
            'sentence': sentence.string,
            'sentiment': out,
            'polarity': sentence.sentiment.polarity
    })
    df = pd.DataFrame(results)
    return df

#func that will assign the sentiment type according to different polarity ranges.
def get_sentiment(score):
    if score > 0 and score <= 0.5:
        return 'Slighly Positive'
    elif score > 0.5 and score <= 1:
        return 'Positive'
    elif score >= -0.5 and score < 0:
        return 'Slightly Negative'
    elif score > -1 and score < -0.5:
        return 'Negative'
    else:
        return 'neutral'

#Heading
st.title("Sentiment Analysis")

#Introduction
st.write("Sentiment analysis computationally identifies and categorizes opinions expressed in a piece of text. It determines whether the writer's/speaker's attitude towards a particular topic, product, etc. is positive, negative, or neutral.")
st.write("This project will help you analyse whether the text being input holds a positive or a negative sentiment overall.")
st.write("Index:")
st.write("1. Postive: Sentences that implicate postive emotions like happiness, satisfaction, excitement, etc. These sentences have polarity ranging from 0.5 to 1.")
st.write("2. Slightly Postive: Sentences that implicate postive emotions like happiness, satisfaction, excitement, etc but on a slightly lesser intensity. These sentences have polarity ranging from 0 to 0.5.")
st.write("3. Postive: Sentences that implicate neither postive nor negative emotions. These sentences have polarity of 0.")
st.write("4. Slightly Negative: Sentences that implicate negative emotions like sadness, anxiety, disappointment, etc but on a slightly lesser intensity. These sentences have polarity ranging from -0.5 to 0.")
st.write("5. Negative: Sentences that implicate negative emotions like sadness, anxiety, disappointment, etc. These sentences have polarity ranging from -1 to -0.5.")

st.write("You may enter your text on the sidebar for sentiment analysis.")

#User Input in sidebar
st.sidebar.header("User input area")

f = st.sidebar.form("userform")
content = f.text_area("Enter your text", height=250,placeholder="Enter your text for sentiment analysis here")
btn = f.form_submit_button("Submit")

#Once the text gets submitted, the  analysis is presented.
if btn and content:
    st.write("According to the text input by the user, we can analyse the text as given below:")
    results = analyse(content)
    st.write(results)
    st.subheader("Sentiment Analysis")
    sentiment =results.sentiment.value_counts().reset_index()
    fig_sentiment = px.pie(sentiment, values=sentiment['sentiment'], names=sentiment['index'], title="Sentiment Analysis")
    st.plotly_chart(fig_sentiment)

#Using the content as a footer
st.divider()
st. write("This project has been made by Tanushi Tayal. Thank you!")


#Thank you!
    


