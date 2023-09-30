import pandas as pd
import numpy as np
import streamlit as st

from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

page = st.sidebar.selectbox("ページを選択", ("HOME", "教授の紹介"))

def home_page():
    def run():
        st.set_page_config(
            page_title="武蔵野大学データサイエンス学部",
            page_icon="💻",
            )

        st.write("# 武蔵野大学データサイエンス学部紹介ページ")

        st.sidebar.success("知りたいコンテンツを選択してください。")

        st.markdown(
            """
            このwebアプリでは、武蔵野大学データサイエンス学部の活動や学校生活に関して紹介します。
        
            - 武蔵野大学のホームページは[こちら](https://www.musashino-u.ac.jp/)
        """
        )
        if __name__ == "__main__":
            run()
        
def about_page():
    st.write("このページでは、中西先生の紹介をさせていただきます。")
    st.write("また、表示されている先生のイメージ画像は生成系AIを使って、先生の特徴をPromptして生成したものです。")


if page == "HOME":
    home_page()
elif page == "教授の紹介":
    about_page()
