import streamlit as str

# Set up the page title and icon
str.set_page_config(page_title="BSSS/Highschool", page_icon="🏫", layout="centered")

# --- NAVIGATION SIDEBAR ---
page = str.sidebar.radio("Navigate", ["Home", "About Us", "Contact Us"])

# --- WELCOME TITLE (Shows on every page) ---
str.title("Welcome to BSSS/BEKOJI SPECIAL SECONDARY SCHOOL 🍎")
str.subheader("Empowering Students for a Brighter Tomorrow")

# --- FIRST ENTRY: PORTALS AT THE VERY TOP ---
str.markdown("### 🔑 Student Portal Access")
# This creates two clean columns side-by-side on the front page entry
col1, col2 = str.columns(2)

with col1:
    str.markdown("#### Login")
    student_id = str.text_input("Student ID Number:", key="login_id")
    password = str.text_input("Password:", type="password", key="login_pass")
    if str.button("Login"):
        if student_id and password:
            str.success(f"Welcome back! ID {student_id} logged in.")
        else:
            str.error("Enter ID and password.")

with col2:
    str.markdown("#### Register New Student")
    first_name = str.text_input("First Name:", key="reg_first")
    last_name = str.text_input("Last Name:", key="reg_last")
    reg_grade = str.selectbox("Grade:", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"], key="reg_grade")
    if str.button("Submit Registration"):
        if first_name and last_name:
            str.success(f"Thank you, {first_name}! Form sent.")
        else:
            str.error("Please fill in names.")

str.markdown("---") # Visual divider line

# --- HOME PAGE CONTENT ---
if page == "Home":
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