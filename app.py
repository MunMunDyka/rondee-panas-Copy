from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io
import os
import json

app = Flask(__name__)

# Load model
MODEL_PATH = os.path.join("model", "rondee-model-terbaru.h5")
print("🔥 Loading model from:", MODEL_PATH)
model = load_model(MODEL_PATH)
print("✅ Model berhasil diload!")

# Load labels.json
LABELS_PATH = os.path.join("model", "labels.json")
with open(LABELS_PATH, encoding="utf-8") as f:
    labels = json.load(f)
print("📖 labels.json berhasil dimuat!")

# Fungsi preprocessing gambar
def preprocess_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    img = img.resize((224, 224))  # Ukuran input model
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Endpoint prediksi
@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    img = preprocess_image(file.read())

    preds = model.predict(img)
    class_id = int(np.argmax(preds))
    confidence = float(np.max(preds))

    # Ambil nama label berdasarkan urutan
    label_key = list(labels.keys())[class_id]
    label_info = labels[label_key]

    return jsonify({
        "label": label_info["name"],
        "confidence": f"{confidence*100:.2f}%",
        "description": label_info["description"],
        "location": label_info["location"],
        "history": label_info["history"],
        "architecture": label_info["architecture"]
    })

# Jalankan server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
