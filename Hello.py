import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


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
