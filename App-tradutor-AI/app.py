import streamlit as st
from deep_translator import GoogleTranslator

# --- Configuração da Página ---
# Define um layout mais amplo e um título para a aba do navegador
st.set_page_config(layout="wide", page_title="Tradutor Moderno")

# --- Barra Lateral (Sidebar) ---
# Adiciona um cabeçalho à barra lateral
st.sidebar.header("Opções de Tradução")

# Dicionário de idiomas expandido para oferecer mais opções
linguas = {
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it",
    "Japonês": "ja",
    "Russo": "ru",
    "Chinês (Simplificado)": "zh-CN",
    "Coreano": "ko",
    "Árabe": "ar",
    "Holandês": "nl",
    "Sueco": "sv"
}

# Componente de seleção de idiomas na barra lateral para melhor organização
idiomas_escolhidos = st.sidebar.multiselect(
    "Selecione os idiomas de destino:",
    options=list(linguas.keys()),
    default=["Inglês", "Espanhol"] # Mantém os idiomas padrão
)

st.sidebar.info("Este aplicativo de tradução utiliza a biblioteca `deep-translator` para se conectar à API do Google Tradutor.")
st.sidebar.markdown("---")


# --- Página Principal ---
st.title("🌐 Tradutor de Textos Aprimorado")
st.markdown("Digite um texto em português e selecione os idiomas na barra à esquerda. As traduções aparecerão abaixo.")

# Área de texto com altura ajustada e um placeholder mais convidativo
texto_para_traduzir = st.text_area(
    "Digite sua frase aqui:",
    "Olá! Estou aprendendo a programar em Python e a usar modelos de inteligência artificial.",
    height=150,
    placeholder="Escreva algo para traduzir..."
)

# Botão de tradução com mais destaque usando o argumento 'type'
if st.button("Traduzir Texto", type="primary", use_container_width=True):
    # Validações: verificar se o texto não está vazio e se algum idioma foi selecionado
    if not texto_para_traduzir.strip():
        st.warning("⚠️ Por favor, digite uma frase para traduzir!")
    elif not idiomas_escolhidos:
        st.warning("⚠️ Por favor, selecione pelo menos um idioma de destino na barra lateral!")
    else:
        st.success("Traduções geradas com sucesso!")
        
        # Itera sobre os idiomas escolhidos para traduzir
        for nome_idioma in idiomas_escolhidos:
            codigo_idioma = linguas[nome_idioma]

            try:
                # Realiza a tradução
                traducao = GoogleTranslator(source='pt', target=codigo_idioma).translate(texto_para_traduzir)

                # Apresenta cada tradução em um container expansível (expander) para melhor visualização
                with st.expander(f"Tradução para {nome_idioma} ({codigo_idioma})"):
                    st.text_area("Texto Traduzido:", value=traducao, height=100, disabled=True, key=f"trad_{codigo_idioma}")
                    st.caption(f"Texto Original: '{texto_para_traduzir}'")

            except Exception as e:
                st.error(f"Ocorreu um erro ao traduzir para {nome_idioma}: {e}")
