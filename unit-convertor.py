import streamlit as st


st.write("# Unit Convertor")
st.markdown("### Coverts Length, Weight, And Time Instantly")
st.write("##### Welcome! Select a category, enter a value and get the Converted result in real-time")


category =st.selectbox("choose a category", ["Length", "Weight", "Time"])

#value =st.number_input("Enter a value")


#using nested if-elif in function
def convert_Length(category, value, unit):
    if category == "Length":
        if unit == "kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to Kilograms":
            return value / 2.20462
    
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit =="hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24
    return 0
    
if category == "Length":
    unit = st.selectbox("Select a unit", ["kilometers to Miles", "Miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select a unit", ["Kilograms to pounds", "pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select a unit", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])

value =st.number_input("Enter a value to convert")

if st.button("converts"):
    result =convert_Length(category, value, unit)
    st.success(f"the result is {result: 2f}")
    
     
