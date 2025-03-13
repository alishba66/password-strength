import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker")
st.title("Password Strength Checker")

st.markdown("""
    ## Welcome To The App Of Password Strength Checker!
    Use this simple tool to check the strength of your password.  
    Get suggestions on how to make it stronger.  
    We will give you helpful tips to create a **Strong Password**.
""")

password = st.text_input("Enter Password", type="password")

feedback = []
score = 0

if password:
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case letters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%^&*()_+={}\[\]:;"\'<>,.?/~]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character.")

    # Strength Evaluation
    if score == 4:
        feedback.append("✔ Your Password is **Strong!** ✅")
    elif score == 3:
        feedback.append("🟡 Your Password is **Medium Strength**. Consider making it stronger.")
    else:
        feedback.append("🔴 Your Password is **Weak!** Please improve it.")

    # Display suggestions
    st.markdown("## Improvement Suggestions")
    for tip in feedback:
        st.write(tip)

else:
    st.info("Please enter your password to get started.")
