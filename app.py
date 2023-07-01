import streamlit as st
import pickle
model = pickle.load(open('RF_price_predicting_model.pkl', 'rb'))


def main():
    st.title("SISTEM PREDIKSI HARGA MOBIL 🚗")
    st.markdown("##### MENGGUNAKAN METODE REGRESI LINEAR\n##### DATA MINING ")

    # @st.cache(allow_output_mutation=True)
    # def get_model():
    #     model = pickle.load(open('RF_price_predicting_model.pkl','rb'))
    #     return model

    st.write('')
    st.write('')

    years = st.number_input(
        'Pada tahun berapa mobil ingin dibeli ?', 1990, 2020, step=1, key='year')
    Years_old = 2020-years

    Present_Price = st.number_input(
        'Jumlah rata - rata harga mobil', 0.00, 50.00, step=0.5, key='present_price')

    Kms_Driven = st.number_input(
        'Kilometer berapa yang akan pilih ?', 0.00, 500000.00, step=500.00, key='drived')

    Owner = st.radio(
        "Berapa unit mobil yang akan dibeli ?", (0, 1, 3), key='owner')

    Fuel_Type_Petrol = st.selectbox(
        'Jenis bahan bakar apa yang akan dipilih ?', ('Petrol', 'Diesel', 'CNG'), key='fuel')
    if (Fuel_Type_Petrol == 'Petrol'):
        Fuel_Type_Petrol = 1
        Fuel_Type_Diesel = 0
    elif (Fuel_Type_Petrol == 'Diesel'):
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 1
    else:
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 0

    Seller_Type_Individual = st.selectbox(
        'Apakah saudara seorang dealer atau pribadi ?', ('Dealer', 'Individual'), key='dealer')
    if (Seller_Type_Individual == 'Individual'):
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0

    Transmission_Mannual = st.selectbox(
        'Jenis transmisi apa yang akan dipilih ?', ('Manual', 'Automatic'), key='manual')
    if (Transmission_Mannual == 'Mannual'):
        Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0

    if st.button("Estimasi Harga", key='predict'):
        try:
            Model = model  # get_model()
            prediction = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel,
                                       Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(prediction[0], 2)
            if output < 0:
                st.warning("Data tidak ada !!")
            else:
                st.success(
                    "Harga mobil seharga {} 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")


if __name__ == "__main__":
    main()
