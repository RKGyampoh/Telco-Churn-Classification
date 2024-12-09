import streamlit as st
 
def home_page():
    
    st.title("Integrating Machine Learning into a GUI with Streamlit")
    st.title("The Telco Churn App")
 
 
    st.markdown("""
        This app uses Machine Learning to predict whether or not a customer will churn.
    """)
 
    st.subheader("Instructions")
    st.markdown("""
                - Upload a CSV file 
                - Select features for classififcation
                - Choose a Machine Learning (ML) model from the dropdown 
                - Click on Predict to get the predicted results
                - The app gives you a report on the performance of the ML model
                - The app provides a performance report with metrics such as accuracy, precision, recall, f1-score, etc.
    """)
   
    st.header("App features")
    st.markdown("""
 
        - **Data View**: View the uploaded data
        - **Prediction View**: Get the predicted results from the ML model
        - **Dashboard**: View the performance of the ML model
    """)    
 
    st.subheader("User Benefits")
    st.markdown("""
                **Data Driven Approach**: Informed decision making based on the data
 
                **Streamlined Process**: Streamlined process for churn prediction
               
                **Real-time Predictions**: Allows users to input customer data and instantly receive churn predictions, enabling quick interventions to retain customers.
               
                **Interactive Insights**: Explore interactive visualizations and dashboards, helping to analyze trends, customer behaviors, and key churn drivers intuitively.
               
                **User-friendly Customization**: Provides options to adjust input parameters, filters, and thresholds, tailoring predictions and insights to specific business needs without requiring technical expertise.
               
                **Cost-Effective**: Streamlined process and cost-effective approach to churn prediction
     """)
   
    st.divider()
    st.subheader("Watch Tutorial on how to use the App")
  #  st.write('Watch video below')
  #  st.video(r"C:\Users\rolan\OneDrive\Desktop\Telco\data\Screen Recording 2024-12-05 154638.mp4")
    
 
    st.divider()
    st.subheader("Need Further Assistance?")
    st.write('Contact Us via rolandgyampoh@gmail.com')
    st.markdown("""
        This App uses machine learning to predict the likelihood of  a customer churning
        
        You can perform both single or bulk predictions
     
     """ )
   
    
     