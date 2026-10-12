import streamlit as st
import string
import secrets

st.set_page_config(page_title="Password Generator", page_icon="🔒", layout="centered")

st.title("🔒 Secure Password Generator")
st.write("Generate strong, cryptographically secure passwords instantly using Python.")

# Controls for password customization
length = st.slider("Password Length", min_value=6, max_value=64, value=16)

col1, col2 = st.columns(2)
with col1:
    use_upper = st.checkbox("Uppercase (A-Z)", value=True)
    use_lower = st.checkbox("Lowercase (a-z)", value=True)
with col2:
    use_digits = st.checkbox("Numbers (0-9)", value=True)
    use_symbols = st.checkbox("Symbols (!@#$%)", value=True)

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation
        
    if not char_pool:
        return None
        
    return ''.join(secrets.choice(char_pool) for _ in range(length))

# Generate button and output
if st.button("Generate Password", type="primary"):
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    
    if password is None:
        st.error("Please select at least one character type.")
    else:
        st.success("Here is your secure password:")
        st.code(password, language="")