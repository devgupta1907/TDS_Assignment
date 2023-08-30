import streamlit as st
st.write("""
# Streamlit Project - Dev Gupta
         ## 22f2000888@ds.study.iitm.ac.in
""")


num1 = st.number_input("Enter First Number", value=0, step=1)
num2 = st.number_input("Enter Second Number", value=0, step=1)
num3 = st.number_input("Enter Third Number", value=0, step=1)

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

st.write("The largest number is: ", largest)