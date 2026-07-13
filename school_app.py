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