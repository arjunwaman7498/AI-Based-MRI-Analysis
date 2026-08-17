import cv2
import numpy as np
import tensorflow as tf


def generate_gradcam(model, img_path, last_conv_layer_name):

    img = tf.keras.preprocessing.image.load_img(
        img_path,
        target_size=(224, 224)
    )

    img_array = tf.keras.preprocessing.image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    img_array = img_array / 255.0

    grad_model = tf.keras.models.Model(
        model.inputs,
        [
            model.get_layer(
                last_conv_layer_name
            ).output,
            model.output
        ]
    )

    with tf.GradientTape() as tape:

        conv_outputs, predictions = grad_model(
            img_array
        )

        predicted_class = tf.argmax(
            predictions[0]
        )

        loss = predictions[
            :,
            predicted_class
        ]

    gradients = tape.gradient(
        loss,
        conv_outputs
    )

    pooled_gradients = tf.reduce_mean(
        gradients,
        axis=(0, 1, 2)
    )

    conv_outputs = conv_outputs[0]

    heatmap = tf.reduce_sum(
        pooled_gradients * conv_outputs,
        axis=-1
    )

    heatmap = np.maximum(
        heatmap,
        0
    )

    heatmap /= (
        np.max(heatmap) + 1e-8
    )

    return heatmap