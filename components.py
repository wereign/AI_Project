import streamlit as st

def st_card(h3_content,content,button_link):
    st.markdown(
        f"""
        <div>
            <h3 style="color: #7752FE;">{h3_content}</h3>
            <p>{content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )   
    
    st.link_button(label="Expand",url=button_link)


def colored_headings(content,heading_level:int=1,color="ffff"):

    headings = ['blenk','h1','h2','h3','h4']
    chosen_level = headings[heading_level]
    

    html_code = f"""
        <{chosen_level} style="color: #{color}">{content}</{chosen_level}>
        """
    st.markdown(html_code,unsafe_allow_html=True)