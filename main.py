# main.py

from src.data_preprocessing import load_and_preprocess_data
from src.model_training import build_model, train_model
from src.make_predictions import make_predictions, plot_predictions, plot_history

def main():
    # Carregar e preprocessar os dados
    train_ds, val_ds = load_and_preprocess_data()

    # Construir o modelo
    model = build_model()

    # Treinar o modelo
    history = train_model(model, train_ds, val_ds)

    # Fazer predições
    predictions, labels = make_predictions(model, val_ds)

    # Obter imagens para plotar
    images = []
    for img_batch, _ in val_ds.take(1):
        images.extend(img_batch)

    # Plotar predições
    plot_predictions(images, labels, predictions)

    # Plotar histórico de treinamento
    plot_history(history)

if __name__ == "__main__":
    main()
