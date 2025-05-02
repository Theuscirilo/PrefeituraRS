# 🎥 Sistema de Orçamento de Gravação – Prefeitura Municipal de Rosário do Ivaí

Sistema web interativo desenvolvido com [Streamlit](https://streamlit.io/) para gerenciamento de solicitações de orçamento de gravação audiovisual feitas à Prefeitura Municipal. O sistema permite que cidadãos solicitem orçamentos diretamente pela plataforma e que a administração visualize, avalie e exporte as solicitações em formato CSV.

---

## 📋 Funcionalidades

### Para Cidadãos
- Solicitação de orçamento de gravação por formulário interativo.
- Seleção de tipo de filmagem (curto, médio ou longo).
- Opção para uso de drone.
- Escolha do local de gravação.
- Confirmação de envio com feedback visual.

### Para Administração (Acesso Restrito)
- Login seguro com senha para acesso ao painel administrativo.
- Visualização completa das solicitações recebidas.
- Exportação das solicitações para arquivo CSV.
- Possibilidade de sair do modo administrativo com um clique.

---

## 🚀 Tecnologias Utilizadas

- [Python 3.9+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

---

## 🛠️ Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/sistema-orcamento-gravacao.git
cd sistema-orcamento-gravacao
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador, geralmente em `http://localhost:8501`.

---

## 🔐 Senha Administrativa

A senha padrão para acesso administrativo está definida diretamente no código como:

```python
st.session_state.senha_administrador = "prefeitura123"
```

> **Recomendação:** Para maior segurança, utilize variáveis de ambiente ou arquivos `.env` para armazenar senhas sensíveis em produção.

---

## 📁 Estrutura do Projeto

```
sistema-orcamento-gravacao/
│
├── app.py                 # Código principal da aplicação
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## ✅ Requisitos

- Python 3.9 ou superior
- pip

---

## 📌 Possíveis Melhorias Futuras

- Integração com banco de dados (SQLite, PostgreSQL, etc.).
- Envio automático de e-mails de confirmação para solicitantes.
- Autenticação mais robusta com múltiplos usuários.
- Interface personalizada com logo e identidade visual da Prefeitura.
- Dashboard com estatísticas e filtros.

---

## 📝 Licença

Este projeto é de uso interno da Prefeitura Municipal de Rosário do Ivaí, podendo ser adaptado por outras prefeituras mediante solicitação. Para uso comercial, entre em contato com comigo!.

---

