from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)

# Load model
MODEL_PATH = os.path.join("model", "rondee-model-terbaru.h5")
print("🔥 Loading model from:", MODEL_PATH)
model = load_model(MODEL_PATH)
print("✅ Model berhasil diload!")

# Label kelas - ganti sesuai jumlah output model
class_names = [
    'balai-adat-melayu',
    'bukit-kursi-meriam',
    'gedung-tabib',
    'makam-engku-putri',
    'makam-raja-ali-haji',
    'masjid-raya-sultan-riau',
    'rumah-hakim'
]

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

    return jsonify({
        "label": class_names[class_id],
        "confidence": f"{confidence*100:.2f}%"
    })

# Jalankan server
if __name__ == "__main__":
    print("🚀 Menjalankan Flask API di http://localhost:5000 ...")
    app.run(debug=True, port=5000)
