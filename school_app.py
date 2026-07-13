# 1. This initializes the gate and an empty list to hold registered students
if "gate" not in str.session_state:
    str.session_state.gate = "locked"
if "student_records" not in str.session_state:
    str.session_state.student_records = []  # This is where your data is stored!

# 2. IF LOCKED, SHOW ENTRY PORTAL
if str.session_state.gate == "locked":
    str.title("BSSS Student Entry Portal 🏫")
    
    choice = str.selectbox("Choose Action:", ["Login", "Register", "Owner Admin Panel"])
    
    if choice == "Login":
        user = str.text_input("Username:")
        pas = str.text_input("Password:", type="password")
        if str.button("Enter Website"):
            str.session_state.gate = "unlocked"
            str.rerun()
            
    elif choice == "Register":
        name = str.text_input("Your Full Name:")
        grade = str.selectbox("Your Grade:", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"])
        if str.button("Submit Registration"):
            if name:
                # This saves the student's name and grade into the list!
                str.session_state.student_records.append({"Name": name, "Grade": grade})
                str.success(f"Success! {name} is registered. Switch to 'Login' to enter.")
            else:
                str.error("Please enter your name.")
                
    elif choice == "Owner Admin Panel":
        str.markdown("### 🔒 Owner Secret Login")
        admin_user = str.text_input("Admin Username:")
        admin_pass = str.text_input("Admin Password:", type="password")
        
        if str.button("Access Records"):
            if admin_user == "admin" and admin_pass == "bekoji123": # ⬅️ Your secret owner password!
                str.markdown("---")
                str.subheader("📋 Registered Students List")
                
                if not str.session_state.student_records:
                    str.info("No students have registered yet.")
                else:
                    # Displays the student list as a beautiful table
                    str.table(str.session_state.student_records)
            else:
                str.error("Incorrect Admin credentials!")
            
    str.stop() # Stops regular users here# 1. This initializes the gate and an empty list to hold registered students
if "gate" not in str.session_state:
    str.session_state.gate = "locked"
if "student_records" not in str.session_state:
    str.session_state.student_records = []  # This is where your data is stored!

# 2. IF LOCKED, SHOW ENTRY PORTAL
if str.session_state.gate == "locked":
    str.title("BSSS Student Entry Portal 🏫")
    
    choice = str.selectbox("Choose Action:", ["Login", "Register", "Owner Admin Panel"])
    
    if choice == "Login":
        user = str.text_input("Username:")
        pas = str.text_input("Password:", type="password")
        if str.button("Enter Website"):
            str.session_state.gate = "unlocked"
            str.rerun()
            
    elif choice == "Register":
        name = str.text_input("Your Full Name:")
        grade = str.selectbox("Your Grade:", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"])
        if str.button("Submit Registration"):
            if name:
                # This saves the student's name and grade into the list!
                str.session_state.student_records.append({"Name": name, "Grade": grade})
                str.success(f"Success! {name} is registered. Switch to 'Login' to enter.")
            else:
                str.error("Please enter your name.")
                
    elif choice == "Owner Admin Panel":
        str.markdown("### 🔒 Owner Secret Login")
        admin_user = str.text_input("Admin Username:")
        admin_pass = str.text_input("Admin Password:", type="password")
        
        if str.button("Access Records"):
            if admin_user == "admin" and admin_pass == "bekoji123": # ⬅️ Your secret owner password!
                str.markdown("---")
                str.subheader("📋 Registered Students List")
                
                if not str.session_state.student_records:
                    str.info("No students have registered yet.")
                else:
                    # Displays the student list as a beautiful table
                    str.table(str.session_state.student_records)
            else:
                str.error("Incorrect Admin credentials!")
            
    str.stop() # Stops regular users here# 1. This initializes the gate and an empty list to hold registered students
if "gate" not in str.session_state:
    str.session_state.gate = "locked"
if "student_records" not in str.session_state:
    str.session_state.student_records = []  # This is where your data is stored!

# 2. IF LOCKED, SHOW ENTRY PORTAL
if str.session_state.gate == "locked":
    str.title("BSSS Student Entry Portal 🏫")
    
    choice = str.selectbox("Choose Action:", ["Login", "Register", "Owner Admin Panel"])
    
    if choice == "Login":
        user = str.text_input("Username:")
        pas = str.text_input("Password:", type="password")
        if str.button("Enter Website"):
            str.session_state.gate = "unlocked"
            str.rerun()
            
    elif choice == "Register":
        name = str.text_input("Your Full Name:")
        grade = str.selectbox("Your Grade:", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"])
        if str.button("Submit Registration"):
            if name:
                # This saves the student's name and grade into the list!
                str.session_state.student_records.append({"Name": name, "Grade": grade})
                str.success(f"Success! {name} is registered. Switch to 'Login' to enter.")
            else:
                str.error("Please enter your name.")
                
    elif choice == "Owner Admin Panel":
        str.markdown("### 🔒 Owner Secret Login")
        admin_user = str.text_input("Admin Username:")
        admin_pass = str.text_input("Admin Password:", type="password")
        
        if str.button("Access Records"):
            if admin_user == "admin" and admin_pass == "bekoji123": # ⬅️ Your secret owner password!
                str.markdown("---")
                str.subheader("📋 Registered Students List")
                
                if not str.session_state.student_records:
                    str.info("No students have registered yet.")
                else:
                    # Displays the student list as a beautiful table
                    str.table(str.session_state.student_records)
            else:
                str.error("Incorrect Admin credentials!")
            
    str.stop() # Stops regular users here# 1. This initializes the gate and an empty list to hold registered students
if "gate" not in str.session_state:
    str.session_state.gate = "locked"
if "student_records" not in str.session_state:
    str.session_state.student_records = []  # This is where your data is stored!

# 2. IF LOCKED, SHOW ENTRY PORTAL
if str.session_state.gate == "locked":
    str.title("BSSS Student Entry Portal 🏫")
    
    choice = str.selectbox("Choose Action:", ["Login", "Register", "Owner Admin Panel"])
    
    if choice == "Login":
        user = str.text_input("Username:")
        pas = str.text_input("Password:", type="password")
        if str.button("Enter Website"):
            str.session_state.gate = "unlocked"
            str.rerun()
            
    elif choice == "Register":
        name = str.text_input("Your Full Name:")
        grade = str.selectbox("Your Grade:", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"])
        if str.button("Submit Registration"):
            if name:
                # This saves the student's name and grade into the list!
                str.session_state.student_records.append({"Name": name, "Grade": grade})
                str.success(f"Success! {name} is registered. Switch to 'Login' to enter.")
            else:
                str.error("Please enter your name.")
                
    elif choice == "Owner Admin Panel":
        str.markdown("### 🔒 Owner Secret Login")
        admin_user = str.text_input("Admin Username:")
        admin_pass = str.text_input("Admin Password:", type="password")
        
        if str.button("Access Records"):
            if admin_user == "admin" and admin_pass == "bekoji123": # ⬅️ Your secret owner password!
                str.markdown("---")
                str.subheader("📋 Registered Students List")
                
                if not str.session_state.student_records:
                    str.info("No students have registered yet.")
                else:
                    # Displays the student list as a beautiful table
                    str.table(str.session_state.student_records)
            else:
                str.error("Incorrect Admin credentials!")
            
    str.stop() # Stops regular users here
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