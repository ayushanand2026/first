import streamlit as st
if "count" not in st.session_state:
    st.session_state.count=0
if st.button("increment"):
    st.session_state.count+=1

st.write("counter:",st.session_state.count)