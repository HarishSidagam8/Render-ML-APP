# 🧠 Diabetes Prediction API (FastAPI + Render)

This is a simple machine learning web API built with **FastAPI**, deployed on **Render**, and powered by a pre-trained model for predicting diabetes based on input features.

---

## 🚀 Live Demo

🌐 [View the Live API on Render](https://render-ml-app-2.onrender.com)  
📈 Example: `https://your-render-url.onrender.com/predict?x=3.2&y=4.5`

> Replace with your actual Render URL after deployment.

---

## 📂 Project Structure

├── Diabetes_app.py # Main FastAPI app
├── model.pkl # Pretrained ML model (Pickle format)
├── requirements.txt # Python dependencies
├── Procfile # Start command for Render (optional)
├── render.yaml # Render deployment configuration (optional)
└── README.md # This file

yaml
Copy
Edit

---

## ⚙️ Setup Locally

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/diabetes-fastapi-api.git
cd diabetes-fastapi-api
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app locally
bash
Copy
Edit
uvicorn Diabetes_app:app --reload
Visit: http://127.0.0.1:8000

🎯 API Endpoints
GET /
Check if the API is live.

Response:

json
Copy
Edit
{
  "message": "ML model is live on Render!"
}
GET /predict?x=<value>&y=<value>
Run a prediction by passing numerical values as query parameters.

Example:

bash
Copy
Edit
/predict?x=5.4&y=3.2
Response:

json
Copy
Edit
{
  "prediction": [1]
}
Customize this based on your actual feature names.

🛠️ Deployment on Render
Push the project to a public GitHub repository.

Go to https://render.com.

Create a new Web Service.

Connect your GitHub repo.

Set:

Start Command: uvicorn Diabetes_app:app --host 0.0.0.0 --port $PORT

Build Command: (leave blank or use pip install -r requirements.txt)

(Optional) Add any environment variables if needed.

Click Deploy and wait for your app to go live.

✅ Dependencies
fastapi

uvicorn

scikit-learn

numpy

pickle (builtin)

Install with:

bash
Copy
Edit
pip install fastapi uvicorn scikit-learn numpy
🙋‍♂️ Author
Harish Sidagam
🧑‍💻 Machine Learning Enthusiast
📫 LinkedIn

📃 License
This project is licensed under the MIT License.

yaml
Copy
Edit
