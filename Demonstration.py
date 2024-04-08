import streamlit as st

def main():
    st.title("Polycystic Ovary Syndrome Detection")
    # Get user inputs
    age = st.number_input("Age", min_value=0, max_value=150, step=1)
    weight = st.number_input("Weight", min_value=20, max_value=150, step=1)
    height = st.number_input("Height", min_value=100, max_value=200, step=1)
    bmi = st.number_input("BMI", min_value=10, max_value=40, step=0.1, format='%.2f')
    st.write("Blood Group options: [11: ,12: ,13: ,14: ,15: ,16: ,17: ,18: ")
    bloodGroup = st.number_input("Blood Group", min_value=11, max_value=18, step=1)
'''
    # Get user inputs
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7243924/
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150, step=1)
    email = st.text_input("Email")
    gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
    occupation = st.text_input("Occupation")
    education = st.selectbox("Education Level", options=["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
    experience = st.slider("Years of Experience", min_value=0, max_value=50, step=1)
'''

'''
     Age (yrs)	Weight (Kg)	Height(Cm) 	BMI	Blood Group	Pulse rate(bpm) 	RR (breaths/min)	Hb(g/dl)	Cycle(R/I)	Cycle length(days)	Marraige Status (Yrs)	Pregnant(Y/N)	No. of abortions	  I   beta-HCG(mIU/mL)	II    beta-HCG(mIU/mL)	FSH(mIU/mL)	LH(mIU/mL)	FSH/LH	Hip(inch)	Waist(inch)	Waist:Hip Ratio	TSH (mIU/L)	AMH(ng/mL)	PRL(ng/mL)	Vit D3 (ng/mL)	PRG(ng/mL)	RBS(mg/dl)	Weight gain(Y/N)	hair growth(Y/N)	Skin darkening (Y/N)	Hair loss(Y/N)	Pimples(Y/N)	Fast food (Y/N)	Reg.Exercise(Y/N)	BP _Systolic (mmHg)	BP _Diastolic (mmHg)	Follicle No. (L)	Follicle No. (R)	Avg. F size (L) (mm)	Avg. F size (R) (mm)	Endometrium (mm)
'''
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
