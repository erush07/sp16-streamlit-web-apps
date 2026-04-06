# ======================
# 05 USING SESSION_STATE
# ======================
"""
You'll need to launch this python file in streamlit using one of these commands:
   WINDOWS:
     streamlit run concepts-and-syntax\05_you_try.py
     py -m streamlit run concepts-and-syntax\05_you_try.py
     python -m streamlit run concepts-and-syntax\05_you_try.py
   
   MAC:
     streamlit run concepts-and-syntax/05_you_try.py
     python -m streamlit run concepts-and-syntax/05_you_try.py
     python3 -m streamlit run concepts-and-syntax/05_you_try.py

# ===================
# USING SESSION STATE
# ===================
Because your code reruns after every interaction with a widget, and that can
lead to variables being overwritten, Streamlit gives you access to a dictionary
that will not be overwritten with each run. It is stored in `st.session_state`.

Example:

import streamlit as st
regular_counter = 0

if "counter" not in st.session_state:
    st.session_state["counter"] = 0

if st.button("Increment"):
    st.session_state["counter"] += 1
    regular_counter += 1

st.write("Normal counter value", regular_counter)
st.write("session_state counter value:", st.session_state["counter"])
"""

# YOU TRY:
# Copy the code from above into your `you_try.py` file, save it, and then try
# pressing the button. Notice that every time you click it the counter stored in
# `session_state` keeps going up, but the regular counter can't go past 1.
# That's because the variable stored in `session_state` persists even when your
# code is being rerun.



