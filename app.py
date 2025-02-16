import streamlit as st
import re

# Função para processar os dados do exame
def process_exam_data(exam_text):
    # Regex para capturar exames e valores numéricos
    pattern = r"([A-Za-z\s]+):\s*([0-9.,]+)"
    exams = re.findall(pattern, exam_text)
    formatted_data = ""
    for exam in exams:
        formatted_data += f"{exam[0]}: {exam[1]}\n"
    return formatted_data

# Título do aplicativo
st.title("Transcrição de Exames de Sangue")

# Formulário para inserir os dados dos exames
exam_text = st.text_area("Cole os dados dos exames aqui:")

# Quando o botão é pressionado, processa os dados
if st.button("Processar Exame"):
    if exam_text:
        result = process_exam_data(exam_text)
        st.subheader("Resultado da Transcrição")
        st.text(result)
    else:
        st.warning("Por favor, cole os dados do exame.")
