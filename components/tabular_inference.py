import streamlit as st
from components.components import colored_headings



def tabular_inference(inference_function):

    labels = ['Sepal Length (cm)',
            "Sepal Width (cm)",
            "Petal Length (cm)",
            "Petal Width (cm)"]

    label_values = []


    with st.form("tabular_inference_form"):
        columns = st.columns(len(labels))

        for i,label in enumerate(labels):
            
            with columns[i]:
                label_values.append(st.number_input(label=label,
                            min_value=0.0, step=0.1))
        
        submitted = st.form_submit_button("Predict Species")

        if submitted:
            prediction = inference_function(*label_values)
            colored_headings(str(prediction),heading_level=4,color="A0E9FF")

if __name__ == "__main__":
    tabular_inference()
