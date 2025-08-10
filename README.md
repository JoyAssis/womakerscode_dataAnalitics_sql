# Desafios de SQL para Análise de Dados

![SQL](https://img.shields.io/badge/SQL-PostgreSQL-blue.svg) ![Data Analysis](https://img.shields.io/badge/Análise-De%20Dados-green.svg)

# Projeto de Banco de Dados com Python e SQLite

![Python](https://img.shields.io/badge/Python-3-blue.svg) ![SQLite](https://img.shields.io/badge/SQLite-Database-orange.svg)

## 1. Resumo do Projeto

Este projeto prático demonstra o ciclo de vida completo de manipulação de um banco de dados SQLite utilizando a biblioteca `sqlite3` nativa do Python. O script cria um banco de dados do zero, define o schema de múltiplas tabelas, insere dados em massa e realiza uma série de consultas, desde operações básicas de CRUD (Create, Read, Update, Delete) até junções de tabelas (`JOINs`).

Este trabalho foi desenvolvido como parte do bootcamp de Análise de Dados da **WoMakersCode**.

## 2. Principais Habilidades Demonstradas

Este script é uma demonstração prática das seguintes competências:

#### **Conceitos de Banco de Dados e SQL:**
* **DDL (Data Definition Language):** Uso de `CREATE TABLE` para definir a estrutura e os tipos de dados das tabelas.
* **DML (Data Manipulation Language):** Execução de operações `INSERT`, `UPDATE` e `DELETE` para gerenciar os registros.
* **DQL (Data Query Language):** Realização de consultas com `SELECT`, filtragem com `WHERE` e ordenação com `ORDER BY`.
* **Funções de Agregação:** Utilização de `COUNT()`, `AVG()` e `MAX()` para realizar cálculos sumarizados sobre os dados.
* **Junção de Tabelas:** Aplicação de `INNER JOIN` para combinar dados de tabelas relacionadas e gerar relatórios complexos.
* **Constraints e Chaves:** Definição de `PRIMARY KEY` e `FOREIGN KEY` para garantir a integridade e o relacionamento dos dados.

#### **Integração com Python (`sqlite3`):**
* Conexão com um banco de dados SQLite usando `sqlite3.connect()`.
* Criação de um `cursor` para executar comandos SQL.
* Execução de comandos únicos com `.execute()` e múltiplos com `.executemany()`.
* Recuperação de resultados de consultas com `.fetchall()` e `.fetchone()`.
* Gerenciamento de transações com `.commit()` para persistir as alterações.
* Fechamento da conexão com `.close()` como boa prática de gerenciamento de recursos.

## 3. Estrutura do Script

O script está organizado em uma sequência lógica de operações:

1.  **Tabela `alunos`:** Criação da tabela e demonstração de operações CRUD básicas, consultas com filtros, ordenação e contagem.
2.  **Tabela `clientes`:** Demonstração de inserção de múltiplos registros de uma só vez (`executemany`) e realização de consultas com funções de agregação para calcular saldo médio, saldo máximo e contagem condicional.
3.  **Tabela `compras` e Junção (`JOIN`):** Criação de uma terceira tabela com chave estrangeira, estabelecendo um relacionamento com a tabela `clientes`. O ponto alto do script é a consulta final que utiliza `JOIN` para combinar dados das duas tabelas, gerando um relatório consolidado de compras por cliente.

## 4. Como Executar o Projeto

Este projeto não requer a instalação de pacotes externos, pois a biblioteca `sqlite3` já vem incluída na instalação padrão do Python 3.

1.  Clone este repositório.
2.  Navegue até a pasta do projeto pelo terminal.
3.  Execute o script Python:
    ```bash
    python3 exercicio.py
    ```
4.  Ao ser executado, o script criará um arquivo de banco de dados chamado `banco` no mesmo diretório e imprimirá no terminal os resultados de todas as consultas realizadas.
