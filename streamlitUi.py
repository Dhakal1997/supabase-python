import streamlit as st
from supabase_client import supabase


st.subheader("Login")
email = st.text_input("Email", key="login_email")
password = st.text_input("Password", type="password", key="login_pass")
st.button("Login")
# st.link("Click to Signup here")
# Title and Metric Summary
st.title("✅ Task Dashboard")
response = supabase.table("todo").select("*").execute()
st.slider("Pick a number",0,20)
col1, col2, col3 = st.columns(3)
col1.metric("Total Todos", len(response.data))
col2.metric("Completed", "2", delta="40%")
col3.metric("Remaining","3",delta="-60%")