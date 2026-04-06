# =================================
# 04 HOW STREAMLIT RERUNS YOUR CODE
# =================================
"""
You'll need to launch this python file in streamlit using one of these commands:
   WINDOWS:
     streamlit run concepts-and-syntax\04_you_try.py
     py -m streamlit run concepts-and-syntax\04_you_try.py
     python -m streamlit run concepts-and-syntax\04_you_try.py
   
   MAC:
     streamlit run concepts-and-syntax/04_you_try.py
     python -m streamlit run concepts-and-syntax/04_you_try.py
     python3 -m streamlit run concepts-and-syntax/04_you_try.py

# =========================
# HOW STREAMLIT RERUNS CODE
# =========================
Every time you interact with an element, streamlit reruns your entire .py file
from top to bottom again. This is how it updates values from the widgets. You
need to be aware of this, because this means most variables you make will be
overwritten if you aren't careful.


Example:
import random
import streamlit as st

st.write(random.randrange(0, 101))  # Why does this generate a new number every time the button is clicked?
st.button("Click Me")

"""

# YOU TRY:
# Copy the code from above into this .py file, save it, and then try pressing
# the button. Notice that every time you click it the number above changes.
# Thats because your entire file is being rerun. Understanding this is key.

import random
import streamlit as st

st.write(random.randrange(0, 101))  # Why does this generate a new number every time the button is clicked?
st.button("Click Me")