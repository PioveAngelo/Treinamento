# Projeto de Automação com Python

Este projeto tem como objetivo explorar e integrar diversas bibliotecas Python voltadas para automação de tarefas, manipulação de dados, geração de arquivos e envio de e-mails.

## Cronograma de Aprendizado

### 07/08/2025
- Introdução aos conceitos de automação:
  - **Automação Assistida**
  - **Automação Não Assistida**
- Aprendizado sobre **Git** e **GitHub**:
  - Funcionamento básico
  - Uso prático para versionamento de código

### 08/08/2025
- Estudo de bibliotecas Python:
  - **pandas**: Estruturação de dados em tabelas
    ```plaintext
        Name      Age     City
        Alice     25      Curitiba
        Bob       30      São Paulo
        Charlie   35      Belém
    ```
  - **openpyxl**:
    - Criação de arquivos `.xlsx` com `Workbook`
    - Leitura de arquivos com `load_workbook`
    - Estilização de células com `Font` (cores RGB)
    - Testes com gráficos usando `BarChart` e `Reference`
  - **smtplib**: Envio de e-mails via servidor Gmail

### 11/08/2025
- Início do projeto integrando as bibliotecas estudadas
- Teste bem-sucedido com `smtplib` para envio de e-mail

### 12/08/2025
- Desenvolvimento de um sistema de geração e envio de Boletos:
  - Criação de arquivos `.xlsx` com dados de fornecedores
  - Geração de modelos Boletos personalizados
  - Automação do envio de e-mails com os arquivos anexados

## Bibliotecas Utilizadas
- `pandas`
- `openpyxl`
- `smtplib`
- `email`
- `locale`
- `datetime`

## Estrutura do Projeto
- `boleto.xlsx`: Modelo de "Boleto"
- `config.py`: Script para criação de planilhas e envio de e-mails com anexos
- `main.py`: Script que importa o config.py e chama as funções feitas

---

Este projeto é parte de um treinamento prático em automação com Python, com foco em aplicações reais e integração de ferramentas.
