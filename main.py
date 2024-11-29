import streamlit as st

# Set page configuration
st.set_page_config(page_title="CareerCoach", page_icon="🎓", layout="centered")

# Title Section
st.title("CareerCoach")

# Subheading and Updates Section
st.subheader("Recent Updates")
st.markdown("We have some exciting updates for you!")

# Button for Exam Key
if st.button("Click here to view the key of Exam on Nov 30, 2024"):
    st.info("Key redirection functionality will be added soon!")

# About Us Section
st.subheader("About Us")
st.markdown(
    """
    **CareerCoach** is a premier coaching center dedicated to empowering students 
    with the knowledge and skills they need to excel in their academic and professional journeys. 
    Join us to achieve your career goals with expert guidance and comprehensive resources.
    """
)
