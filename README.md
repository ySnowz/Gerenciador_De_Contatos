# Gerenciador de Contatos 📖

Este é um **gerenciador de contatos** desenvolvido em Python que permite armazenar, buscar, atualizar e excluir informações de contatos, como nome, telefone e e-mail. Utilizando o banco de dados SQLite, o programa oferece uma solução simples e eficiente para gerenciar seus contatos de forma organizada. É um projeto ideal para quem deseja aprender ou praticar conceitos básicos de Python, manipulação de banco de dados e desenvolvimento de aplicações de linha de comando (CLI).

## Funcionalidades ✨

- **Criação de Tabela:** Cria automaticamente uma tabela de contatos no banco de dados SQLite.
- **Inserção de Contatos:** Adiciona contatos iniciais ao banco de dados.
- **Exibição de Contatos:** Mostra todos os contatos cadastrados.
- **Busca de Contatos:** Permite buscar um contato pelo nome.
- **Atualização de Contatos:** Atualiza o telefone ou e-mail de um contato existente.
- **Exclusão de Contatos:** Remove um contato do banco de dados.
- **Menu Interativo:** Interface de linha de comando (CLI) fácil de usar.

## Como Funciona ⚙️

1. **Banco de Dados:**
   - O programa utiliza o SQLite para armazenar os contatos em uma tabela chamada `Contatos`.
   - Cada contato possui um ID único, nome, telefone e e-mail.

2. **Operações Disponíveis:**
   - **Exibir Contatos:** Mostra todos os contatos cadastrados.
   - **Buscar Contato:** Busca um contato específico pelo nome.
   - **Atualizar Contato:** Permite atualizar o telefone ou e-mail de um contato.
   - **Deletar Contato:** Remove um contato do banco de dados.

3. **Interatividade:**
   - O programa oferece um menu interativo onde o usuário pode escolher entre as operações disponíveis.

## Por que Este Projeto?
  - Este projeto é ideal para:

  - Aprender conceitos básicos de Python e SQLite.

  - Praticar a manipulação de banco de dados em aplicações reais.

  - Desenvolver habilidades em criação de interfaces de linha de comando (CLI).

  - Servir como base para projetos mais complexos, como a adição de uma interface gráfica (GUI) ou integração com APIs.

## Como Executar ▶️

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador-contatos.git
   
2. Navegue até a pasta do projeto:
   ```bash
   cd gerenciador-contatos
   
3. Execute o programa:
   ```bash
   python contatos.py
