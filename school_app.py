import streamlit as str
import streamlit as str

# Set up the page title and icon
str.set_page_config(page_title="BSSS/Highschool", page_icon="🏫", layout="centered")

# --- NAVIGATION SIDEBAR ---
page = str.sidebar.radio("Navigate", ["Home", "About Us", "Contact Us"])

# --- HOME PAGE ---
if page == "Home":
    str.title("Welcome to BSSS/BEKOJI SPECIAL SECONDARY SCHOOL🏫")
    str.subheader("Empowering Students for a Brighter Tomorrow")
    
    str.image("bs.jpg", caption="Our Campus")
    
    str.markdown("---")
    str.warning("📢 Important Announcement: Summer registration is now open! Please visit the school office for details.")
    grade = str.selectbox("Select your grade:", ["choose","Grade 9", "Grade 10", "Grade 11", "Grade 12"])
    user_name = str.text_input("Enter your name:")
if str.button("Click here for a surprise!"):
    str.success("Welcome to our school community! 🎉")
if user_name:
    str.write(f"Hello {user_name}, welcome to our website!")
    str.write(f"You selected: {grade}")
# --- ABOUT US PAGE ---
elif page == "About Us":
    str.title("About Our School")
    str.write("""
    Founded with a vision to provide quality education, our school focuses on academic excellence, 
    character development, and community engagement. 
    
    We offer a supportive environment where every student can thrive and discover their true potential.
    """)
    
    str.subheader("Our Core Values")
    str.markdown("- ✨ Integrity\n- 📚 Excellence\n- 🤝 Respect")

# --- CONTACT US PAGE ---
elif page == "Contact Us":
    str.title("Contact / Inquiry Form")
    str.write("Have questions? Fill out the form below and our administration team will get back to you.")
    
    # Simple form fields
    with str.form("inquiry_form"):
        name = str.text_input("Your Name")
        email = str.text_input("Your Email Address")
        message = str.text_area("Your Message or Question")
        
        submitted = str.form_submit_button("Submit")
        
        if submitted:
            if name and email and message:
                str.success(f"Thank you, {name}! Your message has been received. We will contact you at {email}.")
                # (Later, we can write code here to save this data or email it!)
            else:
                str.error("Please fill out all the fields before submitting.")