import streamlit as st
from datetime import datetime
from io import BytesIO
from PIL import Image


def bytes2file(bytes_obj,file_name=None):

    if file_name is None:
        file_name = f'{datetime.now()}.jpg' # naming conventions etc need to be changed.
        
    with open(f"./{file_name}","wb") as write_file:
        bytes_data = bytes_obj.getvalue()
        
        write_file.write(bytes_data)

def use_camera():
    st.session_state['use_camera'] = not st.session_state['use_camera']
    

if not "use_camera" in st.session_state:
    st.session_state['use_camera'] = False

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


with st.container():

    st.markdown("# Computer Vision Inference")
    # st.markdown(":green[Inserting form for inference of tabular models]")
    uploaded_image = st.file_uploader(label="Upload Image for Classification",
                     type=['png','jpeg'])
    
    if uploaded_image is not None:

        file_name = uploaded_image.name
        image = Image.open(uploaded_image) # for inference
        
        bytes2file(uploaded_image,file_name=file_name)

    st.button('Use camera',on_click=use_camera)

    if st.session_state['use_camera']:
        camera_image = st.camera_input("Take a picture")

        if camera_image is not None:

            bytes2file(camera_image,'from_camera.png')
    

    
    
