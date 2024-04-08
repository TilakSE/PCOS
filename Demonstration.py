import streamlit as st

def main():
    st.title("Application Form")

    # Get user inputs
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150, step=1)
    email = st.text_input("Email")
    gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
    occupation = st.text_input("Occupation")
    education = st.selectbox("Education Level", options=["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
    experience = st.slider("Years of Experience", min_value=0, max_value=50, step=1)

    # Display submitted information
    if st.button("Submit"):
        st.success("Application submitted successfully!")
        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Email:", email)
        st.write("Gender:", gender)
        st.write("Occupation:", occupation)
        st.write("Education Level:", education)
        st.write("Years of Experience:", experience)

if __name__ == "__main__":
    main()
