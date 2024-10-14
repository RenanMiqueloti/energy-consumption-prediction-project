
# Projeto de Classificação de Imagens com CNN

Este repositório contém um projeto de classificação de imagens usando Redes Neurais Convolucionais (CNN) com TensorFlow.

## Índice
- [Descrição](#descrição)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição

Este projeto tem como objetivo classificar imagens do conjunto de dados **CIFAR-10** utilizando uma CNN construída com TensorFlow. O modelo é treinado para reconhecer 10 classes de objetos presentes no conjunto de dados.

## Estrutura do Projeto

```
image-classification-project/
│
├── src/                       # Scripts Python para processamento de dados e modelagem
│   ├── __init__.py            # Indica que 'src' é um pacote Python
│   ├── data_preprocessing.py  # Carregamento e pré-processamento de dados
│   ├── model_training.py      # Definição, treinamento e avaliação do modelo
│   └── make_predictions.py    # Predições e visualização de resultados
│
├── main.py                    # Script principal para executar o projeto
├── README.md                  # Documentação do projeto
├── requirements.txt           # Lista de dependências
└── .gitignore                 # Arquivos e diretórios a serem ignorados pelo Git
```

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/RenanMiqueloti/energy-consumption-prediction-project.git
    cd energy-consumption-prediction-project
    ```

2. **Crie um ambiente virtual e instale as dependências:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scriptsctivate`
    pip install -r requirements.txt
    ```

    O arquivo `requirements.txt` inclui:

    ```
    tensorflow
    tensorflow_datasets
    numpy
    matplotlib
    ```

## Como Usar

1. **Execute o script principal:**

    ```bash
    python main.py
    ```

    O script realizará as seguintes ações:

    - **Carregamento e preprocessamento dos dados:** O conjunto CIFAR-10 será baixado automaticamente.
    - **Treinamento do modelo:** A CNN será treinada usando os dados de treinamento.
    - **Predições:** O modelo realizará predições com os dados de validação.
    - **Exibição de gráficos:** Serão exibidos gráficos das predições e do desempenho do treinamento.

2. **Personalizações:**

    - **Parâmetros de treinamento:** Ajuste o número de épocas, o tamanho do batch ou as dimensões da imagem nos scripts em `src/`.
    - **Arquitetura da CNN:** Modifique a função `build_model` em `model_training.py` para experimentar diferentes arquiteturas de rede.

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. **Faça um fork do projeto.**
2. **Crie uma branch:**

    ```bash
    git checkout -b feature/nova-feature
    ```

3. **Faça commit das suas alterações:**

    ```bash
    git commit -m "Adicionei nova feature"
    ```

4. **Faça push para a branch:**

    ```bash
    git push origin feature/nova-feature
    ```

5. **Abra um Pull Request.**

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.