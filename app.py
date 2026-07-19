import streamlit as st

st.markdown(
    """
    <style>
    .fancy-title {
        font-size: 60px;
        font-weight: 800;
        background: linear-gradient(90deg, #ff6ec4, #7873f5, #4ade80);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px 0;
    }
    </style>
    <div class="fancy-title">🌍 Endangered Species Tracker 🐾</div>
    """,
    unsafe_allow_html=True
)

st.write("App is up and running 🎉")