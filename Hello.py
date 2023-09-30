import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
        page_title="武蔵野大学データサイエンス学部",
        page_icon="💻",
        )

page = st.sidebar.selectbox("ページを選択", ("HOME", "教授の紹介"))

def home_page():
    st.title("武蔵野大学データサイエンス学部紹介ページ")
    st.markdown(
        """
        このwebアプリでは、武蔵野大学データサイエンス学部の活動や学校生活に関して紹介します。
        
        - 武蔵野大学のホームページは[こちら](https://www.musashino-u.ac.jp/)
    """
    )
        
def about_page():
    st.write("このページでは、中西先生の紹介をさせていただきます。")
    st.write("また、表示されている先生のイメージ画像は生成系AIを使って、先生の特徴をPromptして生成したものです。")


if page == "HOME":
    home_page()
elif page == "教授の紹介":
    about_page()
