# 1. This checks if the student is logged in
if "gate" not in str.session_state:
    str.session_state.gate = "locked"

# 2. If locked, show ONLY the login/register buttons
if str.session_state.gate == "locked":
    str.title("BSSS Student Entry Portal 🏫")
    
    # Simple choice box right on the first page
    choice = str.selectbox("Choose Action:", ["Login", "Register"])
    
    if choice == "Login":
        user = str.text_input("Username:")
        pas = str.text_input("Password:", type="password")
        if str.button("Enter Website"):
            str.session_state.gate = "unlocked"
            str.rerun()
            
    if choice == "Register":
        name = str.text_input("Your Full Name:")
        grade = str.text_input("Your Grade:")
        if str.button("Submit Registration"):
            str.success("Registered! Now change the box above to 'Login' to enter.")
            
    str.stop() # This stops the code here so they can't see the rest!
import streamlit as str

# --- SIDEBAR NAVIGATION ---
page = str.sidebar.selectbox("Navigate", ["Home", "About Us", "Contact Us"])

# --- HOME PAGE ---
if page == "Home":
    str.title("Welcome to BSSS/BEKOJI SPECIAL SECONDARY SCHOOL 🍎")
    str.subheader("Empowering Students for a Brighter Tomorrow")
    
    # Displays your campus photo
    str.image("bs.jpg", caption="Our Campus")
    
    # Your clickable links
    str.link_button("Oromia education bureau information", "https://t.me/OromiaEducationBureauOfficial")
    str.link_button("Join our Telegram group", "https://t.me/bekoji_special_secondary_school")
    
    str.markdown("---")
    str.warning("📣 Important Announcement: Summer registration is now open! Please visit the school office for details.")
    
    # Interactive student section
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
    str.title("Contact Us")
    str.write("📍 Location: Bekoji, Oromia, Ethiopia")
    str.write("📧 Email: contact@bekojispecialschool.edu")
    str.write("📞 Phone: +251 9XX XXX XXX")