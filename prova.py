import streamlit as st
st.title("Cena di classe")
st.markdown(
    """ 
    Qui potete capire quanto vi viene a persona.
    """
)



people_paying = st.slider("Numero di studenti", 1, 100)

people_professors = st.slider("Numero di professori", 0, 50)

price =  st.number_input(
    "Prezzo a persona", value=None, placeholder="Type a number...")

if price:
    total_price = (people_paying+people_professors)*price
else:
    total_price = 0
st.metric(label = " That's how much you pay", value = round(total_price/people_paying))

