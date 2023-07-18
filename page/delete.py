import streamlit as st 

import controller.cliente as cliente
def deletar():
    st.title ('deletar dados')
    produtos = ['nome','validade ','preco']
    id = ['1', '2', '3']
    with st.form(key='insert'):
        input_id = st.text_input(label= 'Insira o id:')

        buttom_submit = st.form_submit_button('deletar')

        if buttom_submit:
            cliente.excluir (input_id)
            st.success('Produto removido com sucesso')