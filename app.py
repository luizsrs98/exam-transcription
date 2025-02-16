import streamlit as st
import re

# Função para processar os dados dos exames (removendo unidades de medida e valores de referência)
def process_exams(data):
    # Exames que você solicitou
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
        "Linfócitos",
        "Exame Qualitativo de Urina"
    ]

    results = {}

    # Usando expressões regulares para capturar o nome do exame e o resultado, sem as unidades de medida e valores de referência
    for exam in exams:
        # A regex captura o nome do exame e o resultado, ignorando as faixas de referência
        pattern = re.compile(r"({}.*?Resultado: (.*?)(?:\s|$))".format(exam), re.DOTALL)
        match = re.search(pattern, data)
        if match:
            exam_name = match.group(1).strip()  # Nome do exame
            result = match.group(2).strip()  # Resultado do exame
            
            # Remove unidades de medida
            result = re.sub(r'[a-zA-Z/ ]+', '', result).strip()

            # Armazenando o nome do exame e seu resultado
            results[exam_name] = result
    
    # Formatação final: criando uma string única para exibir os resultados
    formatted_results = "\n".join([f"{exam}: {result}" for exam, result in results.items()])
    return formatted_results

# Função principal para o aplicativo Streamlit
def main():
    st.title("Transcrição de Exames Laboratoriais")
    
    # Criando área para inserção do texto com os dados do exame
    st.write("Cole os dados brutos do exame abaixo:")
    data_input = st.text_area("Dados do Exame", height=300)
    
    if st.button("Processar Exame"):
        if data_input:
            # Processar os dados do exame e exibir o resultado formatado
            formatted_results = process_exams(data_input)
            if formatted_results:
                st.write("Exames Processados:")
                st.text(formatted_results)
            else:
                st.write("Nenhum exame encontrado ou dados no formato errado.")
        else:
            st.write("Por favor, insira os dados do exame.")

if __name__ == "__main__":
    main()
