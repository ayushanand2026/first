import streamlit as st 
st.header("Radio")
value = st.radio("Pick one:", ["A", "B", "C"])
st.write(f"Radio value: {value}")
st.write("---")
st.header("Checkbox")
value = st.checkbox("Show Text")
st.write(f"Checkbox value: {value}")
st.write("---")