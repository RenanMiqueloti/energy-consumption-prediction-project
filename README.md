# Energy Consumption Prediction Project

Este repositório contém um projeto de previsão de consumo de energia usando técnicas de aprendizado de máquina.

## Índice
- [Descrição](#descrição)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

<<<<<<< HEAD
- `notebooks/`: Jupyter notebooks for exploration and model training.
- `src/`: Python scripts for data preprocessing, model training, and making predictions.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies.
=======
## Descrição
Este projeto tem como objetivo prever o consumo de energia com base em dados históricos. Utilizamos diversas técnicas de pré-processamento de dados, exploração de dados e modelos de machine learning para atingir esse objetivo.
>>>>>>> d46b04c (fix/README)

## Estrutura do Projeto
energy-consumption-prediction-project/
│
├── notebooks/ # Notebooks Jupyter para exploração e treinamento de modelos
│ ├── exploratory.ipynb # Análise exploratória dos dados
│ ├── preprocessing.ipynb # Pré-processamento dos dados
│ └── training.ipynb # Treinamento e avaliação dos modelos
│
├── src/ # Scripts Python para processamento de dados e modelagem
│ ├── data/ # Scripts para carregamento e pré-processamento de dados
│ ├── models/ # Scripts para definição, treinamento e avaliação de modelos
│ └── utils/ # Funções utilitárias
│
├── data/ # Diretório para armazenar datasets (não incluso no repositório)
│
├── README.md # Documentação do projeto
├── requirements.txt # Lista de dependências
└── .gitignore # Arquivos e diretórios a serem ignorados pelo Git

markdown
Copy code

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/RenanMiqueloti/energy-consumption-prediction-project.git
    cd energy-consumption-prediction-p**reject**
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Uso
1. Prepare os dados colocando-os na pasta `data/`.
2. Execute os notebooks em `notebooks/` para realizar a análise exploratória, pré-processamento e treinamento dos modelos.
3. Use os scripts em `src/` para automatizar as etapas de processamento e predição.

## Contribuição
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:
1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adicionar nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhe