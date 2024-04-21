import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Include FontAwesome
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)

# Set background color to black
st.markdown(
    """
    <style>
    body {
        background-color: #000000 !important;
        color: white;
    }
    .sidebar-toggle-btn {
        border: none;
        background: transparent;
        cursor: pointer;
        color: white;
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set favicon with a custom logo (PNG)
favicon_url = "https://example.com/favicon.png"
st.markdown(f'<link rel="shortcut icon" type="image/png" href="{favicon_url}">', unsafe_allow_html=True)

# Load the model and CountVectorizer
model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

def main():
    st.sidebar.markdown('<button id="sidebar-toggle" class="sidebar-toggle-btn"><i class="fas fa-bars"></i></button>', unsafe_allow_html=True)

    # Adjust the width of the logo column as needed
    logo_col, title_col = st.columns([0.2, 1])

    with logo_col:
        # Adjust width as needed
        st.image("CyberBlockLogo.png", width=100)

    with title_col:
        st.title(" :violet[SPAM EMAIL DETECTOR]")
        st.write(":green[Build By MAKSQUARE]")

    activities = ["SPAM EMAIL DETECTION", "About"]
    choice = st.sidebar.selectbox("CHOOSE YOUR REQUIREMENT", activities)
    
    if choice == "SPAM EMAIL DETECTION":
        msg = st.text_input("Enter The Suspicious Email:")
        
        if st.button(":red[CHECK]"):
            data = [msg]
            vec = cv.transform(data).toarray()
            result = model.predict(vec)
            if result[0] == 0:
                st.success("This is Not A Spam Email")
            else:
                st.error("This is A Spam Email")
            
    else:
        st.write(':green[Spam Email Detection]')
        st.write("            ")
        st.write("Filter out Suspicious Emails")
        st.write("            ")
        st.write('Filter out you Suspicious By using this Spam Mail Detector Tool that will tell You Weather a Email is a Malicious Email or not. This Spam Email detector saves users valuable time and enhances productivity by ensuring that only relevant and legitimate messages reach their inboxes. Moreover, they serve as a frontline defense against various cyber threats, such as phishing attempts, malware distribution, and scams, thereby bolstering security and protecting sensitive information. Ultimately, This Email Spam detector fosters a positive email experience by delivering a clean and trustworthy inbox, thereby enhancing user satisfaction and trust in email communication.')
        st.write("            ")
    
    st.markdown('<div class="footer">MAKSQUARE &copy; All Rights Reserved</div>', unsafe_allow_html=True)   

if __name__ == "__main__":
    main()




