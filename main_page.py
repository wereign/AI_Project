import streamlit as st
from PIL import Image

from model import mnist_pytorch



from components.cv_inference import inference_box
from components.tabular_inference import iris_inference
from components.components import st_card,colored_headings


models = [mnist_pytorch.MNISTPyTorch(),mnist_pytorch.MNISTPyTorch2(),mnist_pytorch.MNISTPyTorch3()]



def set_model_page_id(model_id):    
    st.session_state['page_mode'] = 'model_page'
    st.session_state['model_id'] = model_id    

def set_page_main():
     st.session_state['page_mode'] = 'main_page'


def main_page():
    st.session_state['page_mode'] = 'main_page'


    colored_headings("Computer Vision Models",heading_level=2,color="FF6AC2")
    columns = st.columns(len(models))

    for i, col in enumerate(columns):
        with col:
            model = models[i]
            h3_title = model.model_name
            content = model.short_description
            url = "https://www.youtube.com/watch?v=S3IQwuYX_ls"
            st_card(h3_content=h3_title,content=content,button_link=url,button_callback=set_model_page_id,button_args=[i])


def model_page(model_id):

    st.button(label=":arrow_backward: Main Page",on_click=set_page_main)
    model_obj = models[model_id]

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
        iris_inference()



# colored_headings("Tabular Models",heading_level=2,color="FF6AC2")

# columns = st.columns(3)

# for i, col in enumerate(columns):

#     with col:
#         h3_title = f"Model_{i}"
#         content = f"CV Model_{i}.\nOkay, lets face it. Nothing can come between you and I."
#         url = "https://www.youtube.com/watch?v=S3IQwuYX_ls"
#         st_card(h3_content=h3_title,content=content,button_link=url)



if not "page_mode" in st.session_state:
        st.session_state['page_mode'] = 'main_page'
    
    
if not "model_id" in st.session_state:
        st.session_state['model_id'] = 0


if st.session_state['page_mode'] == "main_page":
    main_page()

elif st.session_state['page_mode'] == 'model_page':
    model_page(st.session_state['model_id'])