import streamlit as st
from PIL import Image

from model import mnist_pytorch



from components.cv_inference import inference_box
from components.tabular_inference import iris_inference
from components.components import st_card,colored_headings


cv_models = [mnist_pytorch.MNISTPyTorch(),mnist_pytorch.MNISTPyTorch2(),mnist_pytorch.MNISTPyTorch3()]



def main_page():
    colored_headings("Computer Vision Models",heading_level=2,color="FF6AC2")
    columns = st.columns(3)

    for i, col in enumerate(columns):
        with col:
            model = cv_models[i]
            h3_title = model.model_name
            content = model.short_description
            url = "https://www.youtube.com/watch?v=S3IQwuYX_ls"
            st_card(h3_content=h3_title,content=content,button_link=url,button_callback=model_page,button_args=model)


def model_page(model_obj):

    global page_mode
    page_mode = 'model_page'
    print("In Function" ,page_mode)
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


page_mode = 'main_page'


if page_mode == "main_page":
    main_page()

elif page_mode == 'model_page':
    pass

print(page_mode)