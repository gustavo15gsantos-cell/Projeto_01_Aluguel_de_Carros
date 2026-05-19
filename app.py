import streamlit as  st
st.title("ALUGA Car!")
st.sidebar.title("Escolha o seu modelo")
st.sidebar.image("logo.png")

carros = ["logo","BMW" ,"Porche" ,"volkswagen" ,"Audi" ,"Ferrari"]

opcao = st.sidebar.selectbox("Escolha o carro que foi Alugado", carros)

st.image(f"{opcao}.png")
st.markdown(f"## você alugou o modelo: {opcao}")
st.markdown("---")

dias = st.text_input(f"por quantos dias o {opcao} foi alugado? ")
km = st.text_input(f"quantos km você rodou com o {opcao}? ")