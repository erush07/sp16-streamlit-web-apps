# ================
# 03 INPUT WIDGETS
# ================
"""
You'll need to launch this python file in streamlit using one of these commands:
   WINDOWS:
     streamlit run concepts-and-syntax\03_you_try.py
     py -m streamlit run concepts-and-syntax\03_you_try.py
     python -m streamlit run concepts-and-syntax\03_you_try.py
   
   MAC:
     streamlit run concepts-and-syntax/03_you_try.py
     python -m streamlit run concepts-and-syntax/03_you_try.py
     python3 -m streamlit run concepts-and-syntax/03_you_try.py

# =============
# INPUT WIDGETS
# =============
Widgets are interactable visual elements, like textboxes or selectboxes. They
return values.

Example:
import streamlit as st

name = st.text_input("Enter your name:")
st.write("Hello,", name)

choice = st.selectbox("Make a choice", ["choice 1", "choice 2", "choice 3"], index=None)
st.write("your choice", choice)

"""

# YOU TRY:
# try adding text_input widgets to get the age and a name and use st.write to
# display what was entered.

import streamlit as st

name = st.text_input("Enter your name:")
st.write("Hello,", name)
favorite_color = st.selectbox("What is your favorite color?", ["Blue", "Green", "Red", "Orange", "Yellow", "Purple"])
st.write("Your favorite color is:", favorite_color)