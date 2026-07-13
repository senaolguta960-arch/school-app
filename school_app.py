import streamlit as str

# Set up the page title and icon
str.set_page_config(page_title="BSSS/Highschool", page_icon="🏫", layout="centered")

# --- NAVIGATION SIDEBAR ---
# Added "Login" and "Registration" directly into your radio choices
page = str.sidebar.radio("Navigate", ["Home", "About Us", "Contact Us", "Login", "Registration"])

# --- HOME PAGE ---
if page == "Home":
    str.title("Welcome to BSSS/BEKOJI SPECIAL SECONDARY SCHOOL 🍎")
    str.subheader("Empowering Students for a Brighter Tomorrow")
    
    str.image("bs.jpg", caption="Our Campus")
    str.link_button("oromia education bureau information", "https://t.me/OromiaEducationBureauOfficial")
    str.link_button("Join our Telegram group", "https://t.me/bekoji_special_secondary_school")
    str.markdown("---")
    str.warning("📣 Important Announcement: Summer registration is now open! Please visit the school office for details.")
    
    grade = str.selectbox("Select your grade:", ["choose", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])
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
    
    # Simple form fields from your second screenshot
    with str.form("inquiry_form"):
        name = str.text_input("Your Name")
        email = str.text_input("Your Email Address")
        message = str.text_area("Your Message or Question")
        
        submitted = str.form_submit_button("Submit")
        
    if submitted:
        if name and email and message:
            str.success(f"Thank you, {name}! Your message has been received. We will contact you at {email}.")
        else:
            str.error("Please fill out all the fields before submitting.")

# --- LOGIN PAGE ---
elif page == "Login":
    str.title("🔑 Student Login Portal")
    str.write("Enter your credentials below to access your student profile account.")
    
    student_id = str.text_input("Student ID Number:")
    password = str.text_input("Password:", type="password")
    
    if str.button("Login"):
        if student_id and password:
            str.success(f"Welcome back! Student ID {student_id} logged in successfully.")
        else:
            str.error("Please enter both your Student ID and password.")

# --- REGISTRATION PAGE ---
elif page == "Registration":
    str.title("📝 New Student Registration Form")
    str.write("Please complete this application form to register at BSSS.")
    
    first_name = str.text_input("First Name:")
    last_name = str.text_input("Last Name:")
    reg_grade = str.selectbox("Registering for Grade:", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"])
    
    if str.button("Submit Registration"):
        if first_name and last_name:
            str.success(f"Thank you, {first_name}! Your registration application for {reg_grade} has been sent successfully.")
        else:
            str.error("Please fill in your first and last name before submitting.")