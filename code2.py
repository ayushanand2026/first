import streamlit as st
st.title("hello")
a = st.checkbox("green")
b = st.checkbox("red")

color = st.selectbox("select your fav", ['green', 'blue', 'red'])
st.write(color)
multi = st.multiselect("select your fav", ['green', 'blue', 'red'])
st.write(multi)

import pandas as pd
df = pd.DataFrame({'name': ['a', 'b', 'c'], 'marks': [20, 30, 40]})
st.write(df)