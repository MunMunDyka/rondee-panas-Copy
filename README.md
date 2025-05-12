# 🏝️ Rondee API - Image Classifier Landmark Pulau Penyengat

## Overview

Rondee API is a simple image classification API that helps you recognize cultural and historical landmarks on Penyengat Island, Tanjungpinang, Indonesia. Built with Flask and TensorFlow, this API gives you not only the predicted label but also full context like description, location, history, and architecture.

---

## 💡 What's Inside?

* 📸 **Input**: Image of a landmark (JPG/PNG)
* 🤖 **Model**: Trained TensorFlow `.h5` model (7 classes)
* 📦 **Output**: JSON with label, confidence %, and complete info
* 🚀 **Deployment**: Docker + Render (free tier)

---

## 🛠️ Tech Stack

* Python + Flask
* TensorFlow (Image classification model)
* Docker (Containerization)
* Render.com (Free cloud deploy)

---

## 📚 Landmark Classes (7 Total)

The model can recognize:

1. **Balai Adat Melayu**
2. **Bukit Kursi & Meriam**
3. **Gedung Tabib**
4. **Makam Engku Putri**
5. **Makam Raja Ali Haji**
6. **Masjid Raya Sultan Riau**
7. **Rumah Hakim Raja Ali Haji**

Each class has metadata stored in `labels.json`, including:

* `name`
* `description`
* `location`
* `history`
* `architecture`

---

## 📂 Project Structure

```
rondee-api/
├── app.py                  # Main Flask API
├── model/
│   ├── rondee-model-terbaru.h5
│   └── labels.json         # Label metadata
├── requirements.txt        # Python deps
├── Dockerfile              # Docker config
├── .dockerignore           # Docker exclude
└── README.md
```

---

## 🌐 API Documentation

### `POST /predict`

Endpoint to submit an image and get the prediction.

#### Request

* Method: `POST`
* Content-Type: `multipart/form-data`
* Field: `file` (your image)

#### Example `curl`

```bash
curl -X POST https://rondee-panas.onrender.com/predict \
     -F "file=@test.jpg"
```

#### Response (200 OK)

```json
{
  "label": "Masjid Raya Sultan Riau",
  "confidence": "99.87%",
  "description": "Masjid Raya Sultan Riau adalah salah satu masjid tertua...",
  "location": "Pulau Penyengat, Tanjungpinang...",
  "history": "Masjid ini dibangun sekitar tahun 1803...",
  "architecture": "Menggunakan putih telur sebagai perekat..."
}
```

#### Errors

* `400 Bad Request`: No file uploaded
* `500 Internal Server Error`: If model or label fails to load

---

## 🚀 How to Deploy (Docker + Render)

1. Push your project to GitHub
2. Go to [https://render.com](https://render.com)
3. New → Web Service
4. Select your repo
5. Choose environment: `Docker`
6. Port: `5000`
7. Deploy!

---

## 🔥 Live API

> Ready to test?

**Base URL**
[https://rondee-panas.onrender.com](https://rondee-panas.onrender.com)

**Prediction Endpoint**
[https://rondee-panas.onrender.com/predict](https://rondee-panas.onrender.com/predict)

---

## ✨ Credits

Made with ❤️ by Vinsen & Aichan for Pulau Penyengat AI project.

Designed to educate and promote cultural tourism through tech!

---
