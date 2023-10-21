import streamlit as st
from datetime import datetime
from io import BytesIO
from PIL import Image


from cv_inference import inference_box

st.markdown("# About the model")

with st.expander("# About the model"):
    st.markdown("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Morbi nec iaculis nisl. Mauris nec venenatis ligula. 
            Suspendisse enim justo, fermentum non urna vitae, molestie malesuada urna. 
            Praesent blandit rutrum urna, sit amet viverra dui consequat a. 
            Pellentesque sollicitudin, diam id feugiat sagittis, neque neque porta felis, non semper enim diam vitae tortor. 
            Donec aliquet fringilla malesuada. In viverra quam velit, vitae maximus tortor gravida id. 
            Donec luctus lorem ac ligula consectetur, vel elementum lacus fringilla. 
            Aenean dignissim, ligula eget tempus fermentum, orci nibh congue sapien, a lacinia augue arcu sed leo. 
            Ut sagittis, sem in ornare aliquam, nibh est scelerisque erat, ac placerat enim nunc a mi.""")


    st.markdown("## Model Architecture")
    st.image('./media/visualization.jpeg')

inference_box()