import pickle
import numpy as np
import streamlit as st
# Load the saved model from the pickle file and do predictions on the new dataset
# loaded_model = pickle.load(open("C:/Users/Hp/Desktop/AI-heart-diseaseModel/final_model.pkl", "rb"))

pickle_in = open("files/final_model.pkl", "rb")
final_model = pickle.load(pickle_in)

# Function to predict the rating
def patient_test(input_data):

    input_data_numpy_array = np.array(input_data, dtype=object)
    input_data_reshaped = input_data_numpy_array.reshape(1, -1)
    prediction = final_model.predict(input_data_reshaped)

    return prediction[0]


def main():
    st.title("Heart disease Prediction Application")

    # Get the features input from patient
    age = st.number_input("Enter  ages ", min_value=0)
    sex = st.number_input(
        "Enter 1 for male 0 for female gender", min_value=0, max_value=1)
    chest_pain_type = st.number_input(
        "Enter  chest pain type", min_value=0, max_value=3)
    resting_blood_pressure = st.number_input(
        "Enter resting blood pressure in mm Hg", min_value=0)
    resting_electrocardiogram = st.number_input(
        "resting electrocardiographic results, o for normal\n 1 for having ST-T wave abnormality\n 2 for showing probable or definite left ventricular hypertrophy by Estes ", min_value=0, max_value=2)
    cholesterol = st.number_input(
        "Enter serum cholestoral in mg/dl", min_value=0)
    fasting_blood_sugar = st.number_input(
        "Enter fasting blood sugar > 120 mg/dl, 1 for true, 0 for false", min_value=0, max_value=1)
    max_heart_rate_achieved = st.number_input(
        "maximum heart rate achieved", min_value=0)
    exercise_induced_angina = st.number_input(
        "exercise induced angina 1 for yes, 0 for no", min_value=0, max_value=1)
    st_depression = st.number_input(
        "ST depression induced by exercise relative to rest", min_value=0.00, )

    st_slope = st.number_input(
        "Enter the slope of the peak exercise ST segment\n 0 for upsloping, 1 for flat, 2 for downsloping", min_value=0, max_value=2)
    num_major_vessels = st.number_input(
        "Enter the number of major vessels (0-3) colored by flourosopy ", min_value=0, max_value=3)
    thalassemia = st.number_input(
        "Enter the thalassemia 0 for NAN, 1 for fixed defect, 2 for normal, 3 for reversable defect", min_value=0, max_value=3)

    rating = ""

    if st.button("Predict"):
        rate = patient_test([age, sex, chest_pain_type, resting_blood_pressure, cholesterol, fasting_blood_sugar, resting_electrocardiogram,
                              max_heart_rate_achieved, exercise_induced_angina, st_depression, st_slope, num_major_vessels, thalassemia])
        if rate is not None:
            if rate==0:
                rating = f"You are Healthy, you don't have a heart Disease."
            else:
                rating = f"You have a heart Disease."

    st.success(rating)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        st.write("Error: ", e)

