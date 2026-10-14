import streamlit as st

st.set_page_config(
    page_title="pantherphysics",
    page_icon="🐱",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.markdown(
    "<h1 style='text-align: center'>pantherphysics 🐱</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    """
This website was designed to streamline in-class data 
visualization and analysis tasks for students in 
Dr. Barooni's Studio Physics course.

Features include:
- **Graph and Fit your Data**: Make a scatter plot of your data, specify a model, and fit.
- **Photos to Spectra**: Upload a photo and see it reimagined as a spectrum of light.
- **Visualize 1D Motion**: Define **x(t)**, **v(t)**, or **a(t)** and visualize all three simultaneously.

Explore the tools using the sidebar on the left. 

Please email ksharifi1@gsu.edu with any questions, feedback, or app ideas!

"""
)
