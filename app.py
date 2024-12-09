import streamlit as st 
from home import home_page
from data import data_page
from prediction import predict_page
from dashboard import dashboard_page
from auth import authenticate
#from PIL import Image



st.set_page_config(page_title="Streamlit App", layout="centered", initial_sidebar_state="auto")

#image = Image.open(r"C:\Users\rolan\OneDrive\Pictures\Screenshots\download.png")
#st.image(image)
 
# Authentication and login logic
def authenticate():
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = False
 
    if not st.session_state['authentication_status']:
        login_form()
    else:
        show_authentication_page()
 
def login_form():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
 
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state['authentication_status'] = True
            st.rerun()
        else:
            st.error("Username/password is incorrect")
 
def show_authentication_page():
    st.title("Welcome")
   
   
    if st.button("Logout"):
        logout()
 
def logout():
    st.session_state.clear()
    st.rerun()
 
# Main function for handling navigation
def main():
 
 #   st.set_page_config(page_title="Streamlit App", layout="centered", initial_sidebar_state="auto")
    # Call authentication function
    authenticate()
 
    # Only display navigation if authenticated
    if st.session_state.get('authentication_status'):
        # Sidebar navigation
        st.sidebar.title("Navigator")
        st.sidebar.write("Select a page to view:")
       
        # Sidebar navigation options
        page = st.sidebar.selectbox(
            ":book:",
            ["Home", "Data", "Predict", "Dashboard"]
        )
 
        # Display the selected page content
        if page == "Home":
            home_page()
        elif page == "Data":
            data_page()
        elif page == "Predict":
            predict_page()
        elif page == "Dashboard":
            dashboard_page()
      
# Run the main function
if __name__ == "__main__":
    main()
