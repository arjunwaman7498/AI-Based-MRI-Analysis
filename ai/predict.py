import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from ai.gradcam import generate_gradcam
import os

model = tf.keras.models.load_model(
    "../ml/brain_tumor_model.keras"
)
base_model = model.layers[0]

print("\nLAST 20 LAYERS:\n")

for layer in base_model.layers[-20:]:
    print(layer.name)
print(model.summary())

classes = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary",
]


def predict_brain_tumor(img_path):

    img = image.load_img(
        img_path,
        target_size=(224, 224)
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    img_array = img_array / 255.0

    prediction = model.predict(img_array)

    print("Raw output:", prediction)

    predicted_index = np.argmax(prediction)

    print("Predicted index:", predicted_index)

    predicted_class = classes[predicted_index]

    print("Predicted class:", predicted_class)

    confidence = prediction[0][predicted_index] * 100

    return predicted_class, round(confidence, 2)