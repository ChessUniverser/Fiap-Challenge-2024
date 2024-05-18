import streamlit as st
from PIL import Image
import os
import time

# Função para verificar se o link ou mensagem é suspeito de phishing
def verificar_phishing(conteudo):
    palavras_suspeitas = ["suspeito", "phishing", "fraude", "faça o pix", "numero do seu cartão", "código de segurança"]
    dominios_suspeitos = ["example.com", "unknown-domain.com"]

    for palavra in palavras_suspeitas:
        if palavra in conteudo.lower():
            return True

    for dominio in dominios_suspeitos:
        if dominio in conteudo:
            return True

    return False

# Função para enviar mensagem de warning
def enviar_warning(numero, mensagem):
    # Implementar o envio da mensagem para o número especificado (exemplo de integração com API)
    st.write(f"Enviando mensagem de warning para {numero}: {mensagem}")

# Simulação de recebimento de mensagens em tempo real
def receber_mensagens():
    mensagens = [
        "Confira nosso site example.com para mais detalhes!",
        "Por favor, faça o pix para 123456789 para confirmar sua compra.",
        "Este é um site seguro example.com",
        "Envie o número do seu cartão para completar a transação."
    ]
    for mensagem in mensagens:
        yield mensagem
        time.sleep(5)  # Simula o tempo de chegada de novas mensagens

# Interface do Streamlit
def main():
    st.set_page_config(page_title="Detector de Phishing no WhatsApp Business", page_icon=":shield:", layout="wide")
    
    # Verifica se a imagem existe
    image_path = 'header_image.png'
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, use_column_width=True)
    else:
        st.write("**Nota:** Imagem de cabeçalho não encontrada. Verifique o caminho do arquivo.")

    st.title("Detector de Phishing no WhatsApp Business")

    with st.sidebar:
        st.header("Configurações")
        api_key = st.text_input("API Key do WhatsApp Business", type="password")
        numero_whatsapp = st.text_input("Número do WhatsApp Business", placeholder="+55XXXXXXXXXX")

    st.header("Verificação de Conteúdo")
    conteudo = st.text_area("Insira o link ou mensagem recebida", placeholder="Digite ou cole o link ou mensagem recebida aqui...")

    # Botão de verificação manual
    if st.button("Verificar Conteúdo"):
        if verificar_phishing(conteudo):
            enviar_warning(numero_whatsapp, "Cuidado! Este conteúdo parece ser suspeito de phishing.")
            st.error("Conteúdo suspeito detectado! Mensagem de warning enviada.", icon="⚠️")
        else:
            st.success("O conteúdo parece ser seguro.", icon="✅")

    st.header("Verificação em Tempo Real")
    if st.button("Iniciar Verificação em Tempo Real"):
        st.write("Iniciando a verificação em tempo real de mensagens recebidas...")
        for mensagem in receber_mensagens():
            st.write(f"Mensagem recebida: {mensagem}")
            if verificar_phishing(mensagem):
                enviar_warning(numero_whatsapp, "Cuidado! Esta mensagem parece ser suspeita de phishing.")
                st.error(f"Mensagem suspeita detectada: {mensagem}", icon="⚠️")
            else:
                st.success(f"Mensagem segura: {mensagem}", icon="✅")

if __name__ == "__main__":
    main()
