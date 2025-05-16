import streamlit as st
from src.pipeline import main

st.title("Product Review Analyzer")
st.write("This app analyzes product reviews and sentiment of it.")
st.write("Please enter the product review below:")
review = st.text_area("Enter Product Review", height=200)
if st.button('Analyze'):
    
    if review:
        with st.spinner('Analyzing...'):
            result = main(review)
            st.success("Analysis Complete!")
            st.write("Analysis Result:")
            st.json(result)
    else:
        st.warning("Please enter a review to analyze.")