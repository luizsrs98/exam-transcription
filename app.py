import openai
import streamlit as st

# Substitua pela sua chave da API do OpenAI
openai.api_key = "SUA_CHAVE_DE_API_AQUI"

# Função para enviar os dados para o ChatGPT e obter a resposta
def analyze_with_chatgpt(text_input):
    prompt = f"Por favor, analise os seguintes dados laboratoriais e forneça uma interpretação detalhada:\n{text_input}"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Ou outro modelo de sua preferência
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].text.strip()  # Retorna a resposta gerada pelo ChatGPT
    except Exception as e:
        return f"Erro ao chamar o ChatGPT: {str(e)}"

# Função principal para o aplicativo Streamlit
def main():
    st.title("Análise de Dados Laboratoriais com ChatGPT")
    
    # Criando área para inserção do texto bruto
    st.write("Cole os dados brutos dos exames abaixo:")
    data_input = st.text_area("Dados do Exame", height=300)
    
    if st.button("Enviar para Análise"):
        if data_input:
            # Enviar os dados para o ChatGPT e obter a análise
            analysis = analyze_with_chatgpt(data_input)
            
            st.write("Análise do ChatGPT:")
            st.text(analysis)
        else:
            st.write("Por favor, insira os dados dos exames.")

if __name__ == "__main__":
    main()
