import streamlit as st
from streamlit_card import card as st_card_2

from components import st_card,colored_headings

st_card_2('Oof this is a card','Lmao',on_click=lambda: print("clicked"))
st.write("# Models")


colored_headings("Tabular Models",heading_level=2,color="FF6AC2")


columns = st.columns(3)

for i, col in enumerate(columns):

    with col:
        h3_title = f"Tabular Model_{i}"
        content = f"Model_{i}.\nOkay, lets face it. Nothing can come between you and I."
        url = "https://www.youtube.com/watch?v=S3IQwuYX_ls"
        st_card(h3_content=h3_title,content=content,button_link=url)



st.write("## Computer Vision Models")
colored_headings("Computer Vision Models",heading_level=2,color="FF6AC2")

columns = st.columns(3)

for i, col in enumerate(columns):

    with col:
        h3_title = f"Model_{i}"
        content = f"CV Model_{i}.\nOkay, lets face it. Nothing can come between you and I."
        url = "https://www.youtube.com/watch?v=S3IQwuYX_ls"
        st_card(h3_content=h3_title,content=content,button_link=url)
