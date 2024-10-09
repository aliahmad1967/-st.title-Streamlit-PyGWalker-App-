import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="StWalker App", layout="wide")

# Load Data Function
def load_data(data):
    return pd.read_csv(data)

def main():
    st.title("Streamlit PyGWalker App")
    
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        # Form
        with st.form("upload_form"):
            data_file = st.file_uploader("Upload a CSV File", type=["csv", "txt"])
            submitted = st.form_submit_button("Submit")
        
        if submitted and data_file is not None:
            df = load_data(data_file)
            st.dataframe(df)
            
            # Generate PyGWalker HTML
            pyg_html = pyg.to_html(df)
            
            # Render PyGWalker using components
            components.html(pyg_html, height=1000, scrolling=True)
    else:
        st.subheader("About")

if __name__ == "__main__":
    main()