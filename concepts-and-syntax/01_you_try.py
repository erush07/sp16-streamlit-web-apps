# ===================================
# 01 INSTALLING AND RUNNING STREAMLIT
# ===================================
"""
The `streamlilt` library isn't part of the Python standard library, so you need
to install it using `pip` before importing it. We're also going to install
`watchdog`, which is optional, but it helps streamlit detect when you make
changes to your files.

In the Terminal (not the normal Python file, you'll probably need to go to
Terminal > New Terminal at the top of the screen) type this and then press enter:

WINDOWS:
    py -m pip install streamlit watchdog
    python -m pip install streamlit watchdog

MAC:
    python -m pip install streamlit watchdog
    python3 -m pip install streamlit watchdog

Occasionally, some students have trouble getting this to work. If that's the
case, don't worry about it. We'll make sure to get you up and running when you
come to class. If you can't get it installed, you won't be able to run any of
the code below, so just look through it and maybe ask AI questions or read your
textbook, then you can give yourself full credit on the class prep report.

# =======
# YOU TRY
# =======

1. Use your terminal (not this notebook) to install streamlit, then try
   importing it below. If you can import it and run python on this file, you
   installed it correctly.

2. To see your streamlit page, you need to tell streamlit to run in the terminal
   which means you do NOT press run like you normally would. Instead in the 
   terminal try one of these commands:
      
   WINDOWS:
     streamlit run concepts-and-syntax\01_you_try.py
     py -m streamlit run concepts-and-syntax\01_you_try.py
     python -m streamlit run concepts-and-syntax\01_you_try.py
   
   MAC:
     streamlit run concepts-and-syntax/01_you_try.py
     python -m streamlit run concepts-and-syntax/01_you_try.py
     python3 -m streamlit run concepts-and-syntax/01_you_try.py

   The first time you do this, you might have to press enter/return because it
   will ask for your email. Just skip that. It should open up your default
   web browser and you should see some text as shown in the code below.

3. To stop streamlit, in the terminal, press CTRL + C (whether you are on 
   Windows or Mac, it is still CTRL). You can also just click the trash can icon
   in your terminal.
"""


import streamlit as st

st.title("Streamlit Import Check")
st.success("Nice work — Streamlit imported correctly.")
st.write("If you can see this page, your installation is working.")
st.write("If this page opened in your browser, you successfully ran a Streamlit app.")
st.info("Try editing this file, saving it, and then clicking Rerun in the browser.")
