
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page 
st.set_page_config(page_title="Movie Review Sentiment Analyzer (VADER)", layout="centered")

# Title
st.title("🎬 Movie Review Sentiment Analyzer (VADER)")

# Input
review = st.text_area("Enter your movie review here:")

# Button 
if st.button("Analyze Sentiment"):
    if review:
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(review)
        compound = score['compound']

        if compound >= 0.05:
            st.success(f"✅ Positive Review (Score: {compound:.2f})")
        elif compound <= -0.05:
            st.error(f"❌ Negative Review (Score: {compound:.2f})")
        else:
            st.info(f"😐 Neutral Review (Score: {compound:.2f})")
    else:
        st.warning("Please enter a review to analyze.")

