import streamlit as st
from PIL import Image
from pathlib import Path

from model_iris_keras import IrisKeras
from model_iris_pytorch import IrisPyTorch
from model_mnist_pytorch import MNISTPyTorch
from model_mnist_keras import MNISTKeras 
from model_mnist_gan import GANPyTorch


from components.cv_inference import inference_box
from components.tabular_inference import tabular_inference
from components.components import st_card,colored_headings


root_dir = Path.cwd()
models = {"cv":[MNISTPyTorch(root_dir),MNISTKeras(root_dir)],
          "tabular":[IrisKeras(root_dir),IrisPyTorch(root_dir)],
        #   "gan":[GANPyTorch(root_dir)]
          }


def set_model_page_id(model_id,model_type):    
    st.session_state['page_mode'] = 'model_page'
    st.session_state['model_id'] = model_id 
    st.session_state['model_type'] = model_type   

def set_page_main():
     st.session_state['page_mode'] = 'main_page'


def main_page():
    st.session_state['page_mode'] = 'main_page'


    colored_headings("Computer Vision Models",heading_level=2,color="FF6AC2")
    cv_columns = st.columns(len(models['cv']))

    for i, col in enumerate(cv_columns):
        with col:
            model = models['cv'][i]
            h3_title = model.model_name
            content = model.short_description
            st_card(h3_content=h3_title,content=content,button_callback=set_model_page_id,button_args=[i,'cv'])

    colored_headings("Tabular Models",heading_level=2,color="FF6AC2")
    cv_columns = st.columns(len(models['tabular']))

    for i, col in enumerate(cv_columns):
        with col:
            model = models['tabular'][i]
            h3_title = model.model_name
            content = model.short_description
            st_card(h3_content=h3_title,content=content,button_callback=set_model_page_id,button_args=[i,'tabular'])


    colored_headings("Generative Adversarial Models",heading_level=2,color="FF6AC2")
    cv_columns = st.columns(len(models['gan']))

    for i, col in enumerate(cv_columns):
        with col:
            model = models['gan'][i]
            h3_title = model.model_name
            content = model.short_description
            st_card(h3_content=h3_title,content=content,button_callback=set_model_page_id,button_args=[i,'gan'])

def model_page(model_id,type):

    st.button(label=":arrow_backward: Main Page",on_click=set_page_main)
    model_obj = models[type][model_id]

    st.markdown("# About the model")

    with st.expander("Expand"):
        st.markdown("## Model Description")
        st.markdown(model_obj.description)

        st.markdown("## Model Architecture")
        architecture_image = Image.open(model_obj.architecture)
        st.image(architecture_image)

        st.link_button(":green[Model Training History]",url=model_obj.cometml_url)

    if model_obj.type == 'cv':
        inference_box(model_obj.inference)
    
    elif model_obj.type == "tabular":
        tabular_inference(model_obj.inference)

    # elif model_obj.type == 'gan':
    #     st.markdown("## Generate Images")
    #     num_images = st.number_input(':orange[Number of Images to generate:]',min_value=1,max_value=80)
        
    #     all_images = model_obj.inference(num_images)

    #     st.image(all_images,clamp=True)


if not "page_mode" in st.session_state:
        st.session_state['page_mode'] = 'main_page'
    
    
if not "model_id" in st.session_state:
        st.session_state['model_id'] = 0


if st.session_state['page_mode'] == "main_page":
    main_page()

elif st.session_state['page_mode'] == 'model_page':
    model_page(st.session_state['model_id'],st.session_state['model_type'])