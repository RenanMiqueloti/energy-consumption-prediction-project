# image-classification-cnn

Experimento de visão computacional: classificador de imagens com **CNN sequencial** treinada no **CIFAR-10** usando TensorFlow.

---

## Arquitetura da CNN

```
Input (128×128×3)
  → Conv2D(32, 3×3, relu) → MaxPooling2D
  → Conv2D(64, 3×3, relu) → MaxPooling2D
  → Conv2D(128, 3×3, relu)
  → Flatten
  → Dense(64, relu)
  → Dense(10, softmax)   ← 10 classes CIFAR-10
```

Compilado com `adam` + `sparse_categorical_crossentropy`.

---

## Dataset — CIFAR-10

10 classes: avião, automóvel, pássaro, gato, cervo, cachorro, sapo, cavalo, navio, caminhão.
60.000 imagens 32×32 RGB (50k treino / 10k teste) — redimensionadas para 128×128 no pipeline.

Carregamento via `tensorflow_datasets` com normalização `[0, 1]`, cache e prefetch automáticos.

---

## Stack

- Python 3.11
- TensorFlow ≥ 2.15
- tensorflow-datasets ≥ 4.9
- NumPy ≥ 1.26
- Matplotlib ≥ 3.8

---

## Estrutura

```
.
├── main.py                    # Orquestra o fluxo completo
├── requirements.txt
└── src/
    ├── data_preprocessing.py  # Carrega CIFAR-10, normaliza, batchifica
    ├── model_training.py      # Constrói e treina a CNN
    └── make_predictions.py    # Predições + plots de resultado
```

---

## Como executar

```bash
git clone https://github.com/RenanMiqueloti/image-classification-cnn.git
cd image-classification-cnn
python -m venv .venv
# Windows: .venv\Scripts\activate | Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Na primeira execução o `tensorflow_datasets` baixa o CIFAR-10 automaticamente (~160 MB).

---

## Saídas

- Accuracy e loss por epoch (treino e validação)
- Grid 3×3 com imagens do conjunto de validação, label verdadeiro e predição
- Curvas de aprendizado (training vs validation accuracy/loss)
