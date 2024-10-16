import numpy as np
import matplotlib.pyplot as plt

def make_predictions(model, val_ds):
    predictions = []
    labels = []
    images = []
    for imgs, lbls in val_ds:
        preds = model.predict(imgs)
        predictions.extend(np.argmax(preds, axis=1))
        labels.extend(lbls.numpy())
        images.extend(imgs)
    return images, labels, predictions

def plot_predictions(images, labels, predictions, n=9):
    plt.figure(figsize=(10, 10))
    for i in range(n):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i])
        plt.title(f"Verdadeiro: {labels[i]}, Predito: {predictions[i]}")
        plt.axis("off")
    plt.show()

def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    
    epochs = range(len(acc))
    
    plt.figure()
    plt.plot(epochs, acc, 'r', label='Training accuracy')
    plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.legend()
    
    plt.figure()
    plt.plot(epochs, loss, 'r', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    
    plt.show()
