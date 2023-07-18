import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Mercado Virtual')
    produtos = ['Arroz','Feijao','Macarrao']
    validade = ['2023-07-01', '2023-06-25','2023-06-30']
    preco = ['8.50','12.75','4.20']

    
    with st.form(key='insert'):
        
        input_nome = st.radio(label = 'informe o nome do produto: ', options = produtos )
        
        input_validade = st.selectbox(label = 'informe a validade que preferir pro produto: ', options = validade )
        
        input_preco = st.radio(label = "preco dos produtos:", options =preco )

       
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_nome, input_validade, input_preco )
            st.success('Cliente incluido com sucesso')

