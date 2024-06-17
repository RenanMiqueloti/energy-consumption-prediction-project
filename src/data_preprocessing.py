import tensorflow as tf
import tensorflow_datasets as tfds

def load_and_preprocess_data(dataset_name='cifar10', img_size=(128, 128), batch_size=32):
    (train_ds, val_ds), ds_info = tfds.load(
        dataset_name,
        split=['train', 'test'],
        shuffle_files=True,
        as_supervised=True,
        with_info=True
    )

    def normalize_img(image, label):
        """Normalizar imagens para [0, 1]."""
        return tf.image.resize(image, img_size) / 255.0, label

    train_ds = train_ds.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
    train_ds = train_ds.cache()
    train_ds = train_ds.shuffle(ds_info.splits['train'].num_examples)
    train_ds = train_ds.batch(batch_size)
    train_ds = train_ds.prefetch(tf.data.AUTOTUNE)

    val_ds = val_ds.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
    val_ds = val_ds.batch(batch_size)
    val_ds = val_ds.cache()
    val_ds = val_ds.prefetch(tf.data.AUTOTUNE)

    return train_ds, val_ds
