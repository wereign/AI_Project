import streamlit as st




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
            st.write(str(prediction))

if __name__ == "__main__":
    tabular_inference()
