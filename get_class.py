import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

def get_class(model_path, labels_path, image_path):
    np.set_printoptions(suppress=True)

    # TFLite modeli yükle
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    # Giriş ve çıkış detaylarını al
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Etiketleri oku
    class_names = open(labels_path, "r", encoding="utf-8").readlines()

    # Görseli hazırla
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image).astype(np.float32)
    normalized_image_array = (image_array / 127.5) - 1
    input_data = np.expand_dims(normalized_image_array, axis=0)

    # Girdiyi modele ver
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Tahmini al
    output_data = interpreter.get_tensor(output_details[0]['index'])
    index = np.argmax(output_data)
    class_name = class_names[index]
    confidence_score = output_data[0][index]

    return (class_name[2:], confidence_score)