import streamlit as st

def submit_button_callback(label_values):
    print(label_values)

    st.markdown(str(label_values))


def iris_inference():

    labels = ['Sepal Length (cm)',
            "Sepal Width (cm)",
            "Petal Length (cm)",
            "Petal Width (cm)"]

    label_values = []


    columns = st.columns(len(labels))

    for i,label in enumerate(labels):
        
        with columns[i]:
            label_values.append(st.number_input(label=label,
                        min_value=0.0, step=0.1))


    st.button("Predict Species",on_click=submit_button_callback,args=[label_values])


if __name__ == "__main__":
    iris_inference()
