from utils import bytes2file
import streamlit as st
from PIL import Image


def use_camera():
    st.session_state['use_camera'] = not st.session_state['use_camera']
    



def inference_box():

    with st.container():
        if not "use_camera" in st.session_state:
            st.session_state['use_camera'] = False

        st.markdown("# Computer Vision Inference")
        # st.markdown(":green[Inserting form for inference of tabular models]")

        st.button('Use camera',on_click=use_camera)

        if st.session_state['use_camera']:
            camera_image = st.camera_input("Take a picture")

            if camera_image is not None:

                bytes2file(camera_image,'from_camera.png')
        

        uploaded_image = st.file_uploader(label="Upload Image for Classification",
                        type=['png','jpeg'])
        
        if uploaded_image is not None:

            file_name = uploaded_image.name
            image = Image.open(uploaded_image) # for inference
            
            bytes2file(uploaded_image,file_name=file_name)
        
        
