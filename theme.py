import streamlit as st


def apply_theme():

    theme = st.session_state.get("theme", "🌙 Dark")

    if theme == "🌙 Dark":

        st.markdown("""
        <style>

        .stApp{
            background:#0F172A;
            color:white;
        }

        /* Sidebar */
        [data-testid="stSidebar"]{
            background:#111827;
        }

        [data-testid="stSidebar"] *{
            color:white !important;
        }

        .stButton>button{
            background:#7C3AED;
            color:white;
            border:none;
            border-radius:12px;
            height:50px;
            font-weight:bold;
        }

        .stTextArea textarea{
            border-radius:12px;
        }

        .stSelectbox div{
            border-radius:12px;
        }

        h1,h2,h3,h4,h5,h6,p,label{
            color:white !important;
        }

        </style>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <style>

        .stApp{
            background:white;
            color:black;
        }

        /* Sidebar */
        [data-testid="stSidebar"]{
            background:#F8F9FA;
        }

        [data-testid="stSidebar"] *{
            color:black !important;
        }

        .stButton>button{
            background:#2563EB;
            color:white;
            border:none;
            border-radius:12px;
            height:50px;
            font-weight:bold;
        }

        .stTextArea textarea{
            border-radius:12px;
        }

        .stSelectbox div{
            border-radius:12px;
        }

        h1,h2,h3,h4,h5,h6,p,label{
            color:black !important;
        }

        </style>
        """, unsafe_allow_html=True)