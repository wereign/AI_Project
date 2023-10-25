from utils import bytes2file
import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import cv2
def use_camera():
    st.session_state['use_camera'] = not st.session_state['use_camera']
    



def inference_box(inference_function):

    with st.container():
        if not "use_camera" in st.session_state:
            st.session_state['use_camera'] = False

        st.markdown("# Computer Vision Inference")
        # st.markdown(":green[Inserting form for inference of tabular models]")

        st.button('Use camera',on_click=use_camera)

        if st.session_state['use_camera']:
            camera_image = st.camera_input("Take a picture")

            if camera_image is not None:

                final_image = Image.open(camera_image).copy() # for inference
                final_image = final_image.resize((28,28))
                final_image = ImageOps.grayscale(final_image)
                final_image = np.asarray(final_image)
                

                print(type(final_image))
                print("Final Image Shape:",final_image.shape)


                prediction = inference_function(final_image,source='camera')

                st.markdown(f"Final Prediction: {prediction}")        

        uploaded_image = st.file_uploader(label="Upload Image for Classification",
                        type=['png','jpeg'])
        
        if uploaded_image is not None:
            
            final_image = Image.open(uploaded_image).copy() # for inference
            final_image = np.asarray(final_image)

            prediction = inference_function(final_image,source='uploaded')

            st.markdown(f"Final Prediction: {prediction}")