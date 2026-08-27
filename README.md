# 🏥 Clinical Coding AI

An AI-powered healthcare backend platform for processing clinical documents and supporting future automated ICD and CPT coding workflows.

The project is designed as a scalable backend system that manages patients, clinical encounters, documents, extracted clinical information, medical codes, predictions, and human review workflows.

---

## 🚀 Features

* 👤 Patient management
* 🏥 Clinical encounter management
* 📄 Clinical document management
* 🧠 Clinical entity extraction workflow
* 🏷️ ICD and CPT code management
* 🔮 Prediction workflow
* 👨‍⚕️ Human review workflow
* 🔌 RESTful API architecture
* 🗄️ PostgreSQL database integration
* 📚 Automatic API documentation

---

## 🛠️ Tech Stack

### Backend

* Python
* Django
* Django REST Framework

### Database

* PostgreSQL
* Django ORM

### API

* REST APIs
* JSON
* Swagger / OpenAPI

### Tools

* Git
* GitHub
* Postman
* pgAdmin

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │   API Client / UI   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Django REST API  │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
   │   Patients   │    │  Encounters  │    │  Documents   │
   └──────────────┘    └──────────────┘    └──────────────┘
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Clinical Processing │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
        ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
        │Clinical      │ │   Medical    │ │ Predictions  │
        │Entities      │ │    Codes     │ │   & Reviews  │
        └──────────────┘ └──────────────┘ └──────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    PostgreSQL DB    │
                    └─────────────────────┘
```

---

## 📂 Project Structure

```text
clinical-coding-ai/
│
├── app/
│   ├── api/
│   │   ├── dependencies.py
│   │   └── v1/
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── models/
│   │
│   ├── schemas/
│   │   ├── patient.py
│   │   ├── document.py
│   │   ├── clinical_entity.py
│   │   ├── code.py
│   │   ├── prediction.py
│   │   └── review.py
│   │
│   └── main.py
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

## 🗄️ Database Design

The application uses PostgreSQL to manage the healthcare workflow.

### Core Tables

| Table               | Purpose                        |
| ------------------- | ------------------------------ |
| `users`             | Application users              |
| `patients`          | Patient information            |
| `encounters`        | Clinical encounters            |
| `documents`         | Clinical documents             |
| `clinical_entities` | Extracted clinical information |
| `codes`             | ICD/CPT medical codes          |
| `predictions`       | Predicted medical codes        |
| `reviews`           | Human review and validation    |

---

## 🔌 API Endpoints

### Health Check

```http
GET /
```

### Create Patient

```http
POST /api/v1/patients
```

Example request:

```json
{
  "external_id": "PAT-10001"
}
```

### Get Patient

```http
GET /api/v1/patients/{patient_id}
```

More endpoints will be added as the project evolves.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/NehalRahate/clinical-coding-ai.git
```

### 2. Navigate to the Project

```bash
cd clinical-coding-ai
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure PostgreSQL

Create a PostgreSQL database:

```text
clinical_coding_ai
```

Configure your database connection in the project environment settings.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/clinical_coding_ai
```

### 6. Run Database Migrations

```bash
alembic upgrade head
```

### 7. Start the Application

```bash
uvicorn app.main:app --reload
```

The application will be available locally at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

Once the application is running, open:

```text
http://127.0.0.1:8000/docs
```

Interactive API documentation is available through Swagger UI.

---

## 🧪 Example API Request

Create a patient:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/patients" \
-H "Content-Type: application/json" \
-d '{
  "external_id": "PAT-10001"
}'
```

Example response:

```json
{
  "id": 1,
  "external_id": "PAT-10001"
}
```

---

## 🧠 Future Roadmap

The following features are planned for future development:

* [ ] PDF and clinical document upload
* [ ] Clinical text extraction
* [ ] ICD-10 prediction
* [ ] CPT prediction
* [ ] NLP-based clinical entity extraction
* [ ] Confidence scoring
* [ ] Human-in-the-loop review
* [ ] Automated prediction evaluation
* [ ] Authentication and role-based access control
* [ ] Docker containerization
* [ ] AWS deployment

---

## 🎯 Project Goal

The goal of this project is to build a scalable healthcare backend platform that can process clinical documentation and support intelligent medical coding workflows.

The long-term vision is to combine:

```text
Clinical Document
       ↓
Text Processing
       ↓
Clinical Entity Extraction
       ↓
ICD / CPT Prediction
       ↓
Confidence Scoring
       ↓
Human Review
       ↓
Final Structured Output
```

---

## ⚠️ Disclaimer

This project is intended for educational and research purposes.

The system is not intended to replace qualified medical professionals or certified medical coders. Any future AI-generated coding predictions should be reviewed and validated by qualified healthcare professionals before use in real clinical or billing workflows.

---

## 👨‍💻 Author

**Nehal Rahate**

Python Developer | Backend Developer

GitHub: https://github.com/NehalRahate

LinkedIn: https://www.linkedin.com/in/nehal-rahate

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Contributions, suggestions, and feedback are welcome!
