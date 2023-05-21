from __future__ import absolute_import
from generate_mcq import GenerateMCQ
import streamlit as st
from Questgen.encoding import encoding
MCQ = GenerateMCQ()
st.title("MCQ Generation jusing NLP")
sentence = st.text_area('Enter Your Text Here:-')
if sentence:
    st.write('\nGenerating MCQs...')
    response = MCQ.get_mcq(sentence)
    st.write('Here are the Generated MCQs:-/n')  
    st.write(response)       

