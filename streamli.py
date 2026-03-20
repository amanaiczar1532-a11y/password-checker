import streamlit as st

st.title("Password Strength Checker")

password = st.text_input("Enter your password to check if it's strong or weak", type="password")

if password:
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_char = "!@#$%^&*()_+-="
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_char:
            has_special = True
    
    score = 0
    
    if length > 8:
        score += 1
    else:
        st.warning("Length not met")
    
    if has_upper == True:
        score += 1
    else:
        st.warning("No upper case found")
        score -= 1
    
    if has_lower == True:
        score += 1
    else:
        st.warning("No lower case found")
        score -= 1
    
    if has_digit == True:
        score += 1
    else:
        st.warning("No digit found")
        score -= 1
    
    if has_special == True:
        score += 1
    else:
        st.warning("No special character found")
        score -= 2
    
    if score > 3:
        st.success("Strong Password ,  This is accepted !")
    if score < 3:
        st.error("Weak Password , Please try again !")
