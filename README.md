# energy-consumption-prediction-project

Apesar do nome do repositorio, o codigo atual nao implementa previsao de consumo de energia. O estado atual do projeto e um pipeline de classificacao de imagens com TensorFlow usando o dataset CIFAR-10 via `tensorflow_datasets`.

## Estado atual

Hoje o repositorio contem um experimento de visao computacional com:

- carregamento e preprocessamento de imagens
- treinamento de uma CNN simples
- geracao de predicoes no conjunto de validacao
- visualizacao de resultados e historico de treino

## Stack

- Python
- TensorFlow
- tensorflow-datasets
- NumPy
- Matplotlib

## Estrutura

```text
.
|-- main.py
|-- requirements.txt
`-- src/
    |-- data_preprocessing.py
    |-- model_training.py
    `-- make_predictions.py
```

## Como executar

```bash
git clone https://github.com/RenanMiqueloti/energy-consumption-prediction-project.git
cd energy-consumption-prediction-project
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Na primeira execucao, o `tensorflow_datasets` pode baixar automaticamente o dataset usado no experimento.

## Fluxo do projeto

1. `src/data_preprocessing.py` carrega o CIFAR-10 e redimensiona as imagens.
2. `src/model_training.py` monta e treina uma CNN sequencial.
3. `src/make_predictions.py` executa predicoes e plota resultados.
4. `main.py` orquestra o fluxo completo.

## Observacao importante

Se a intencao deste repositorio for realmente previsao de consumo de energia, o nome e a documentacao historica nao refletem o codigo atual. Este README descreve o que esta versionado neste momento.
