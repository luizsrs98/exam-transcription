import streamlit as st
import re

# Função para processar os dados dos exames
def process_exams(data):
    # Expressões regulares para capturar os exames e seus resultados
    results = {}

    # Exames típicos: se for necessário adicionar mais, basta seguir esse padrão
    exams = [
        "ALBUMINA",
        "CREATININA",
        "UREIA",
        "CÁLCIO",
        "POTÁSSIO",
        "MAGNÉSIO",
        "Hemácias",
        "Hemoglobina",
        "Hematócrito",
        "VCM",
        "HCM",
        "CHCM",
        "RDW-CV",
        "Leucócitos",
        "Neutrófilos",
        "Eosinófilos",
        "Basófilos",
        "Monócitos",
        "Linfócitos"
    ]

    # Usando expressões regulares para capturar o nome do exame e o valor
    for exam in exams:
        pattern = re.compile(r"({}.*?Resultado: (.*?)(?:\s|$))".format(exam), re.DOTALL)
        match = re.search(pattern, data)
        if match:
            exam_name = match.group(1).strip()
            result = match.group(2).strip()
            results[exam_name] = result
    
    return results

# Função principal para o aplicativo Streamlit
def main():
    st.title("Transcrição de Exames Laboratoriais")
    
    # Criando área para inserção do texto com os dados do exame
    st.write("Cole os dados brutos do exame abaixo:")
    data_input = st.text_area("Dados do Exame", height=300)
    
    if st.button("Processar Exame"):
        if data_input:
            # Processar os dados do exame e exibir o resultado formatado
            results = process_exams(data_input)
            if results:
                st.write("Exames Processados:")
                for exam, result in results.items():
                    st.write(f"{exam}: {result}")
            else:
                st.write("Nenhum exame encontrado ou dados no formato errado.")
        else:
            st.write("Por favor, insira os dados do exame.")

if __name__ == "__main__":
    main()
