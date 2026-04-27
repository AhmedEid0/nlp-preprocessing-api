# NLP Preprocessing API

A modular FastAPI backend for preprocessing and normalizing Arabic and English text.

The project focuses on clean backend architecture, multilingual NLP preprocessing, logging, API documentation, and Docker-based deployment.

---

# Features

## English Text Preprocessing

* Lowercasing
* Punctuation removal
* Number removal
* Stopword removal
* Lemmatization
* Whitespace normalization
* Non-ASCII cleanup

---

## Arabic Text Preprocessing

* Arabic diacritics removal
* Tatweel removal
* Alef normalization
* Ya normalization
* Ta Marbuta normalization
* Repeated character normalization
* URL removal
* Punctuation removal
* Whitespace normalization

---

## Backend Features

* FastAPI REST API
* Modular project structure
* Pydantic request/response validation
* Logging system
* Swagger API documentation
* Docker support
* Docker Compose support

---

# Project Structure

```txt id="b2d9wo"
project/
│
├── logs/
│   └── app.log
│
├── src/
│   │
│   ├── main.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── models/
│   │   └── preprocess_schema.py
│   │
│   ├── routers/
│   │   └── preprocess_router.py
│   │
│   ├── services/
│   │   └── preprocessing_service.py
│   │
│   ├── utils/
│   │   ├── arabic_cleaning.py
│   │   ├── english_cleaning.py
│   │   ├── language_detection.py
│   │   └── logger.py
│   │
│   └── __init__.py
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# API Endpoint

## POST `/preprocess`

Preprocesses Arabic and English text.

---

# Example Request

```json id="rvk85p"
{
  "text": "السَّلام عليكم Hello!!!"
}
```

---

# Example Response

```json id="9rggwi"
{
  "cleaned_text": "السلام عليكم hello"
}
```

---

# Running Locally

## 1. Clone Repository

```bash id="g8z2zj"
git clone https://github.com/AhmedEid0/nlp-preprocessing-api.git
```

```bash id="a5kfe4"
cd nlp-preprocessing-api
```

---

## 2. Install Dependencies

Using uv:

```bash id="v8e58d"
uv sync
```

---

## 3. Run the API

```bash id="e8rkdk"
uv run uvicorn src.main:app --reload
```

---

# API Documentation

After running the server:

```txt id="wdq0wt"
http://localhost:8000/docs
```

Swagger UI provides:

* endpoint testing
* request schemas
* response schemas
* interactive API documentation

---

# Run with Docker

## Pull Docker Image

```bash
docker pull ahmedeid0/nlp-preprocessing-api
```

---

## Run Container

```bash
docker run -p 8000:8000 ahmedeid0/nlp-preprocessing-api
```

---

# Access API Documentation

After the container starts running:

http://localhost:8000/docs

Swagger UI provides interactive API testing and documentation.

---

# Technologies Used

* FastAPI
* Python
* NLTK
* Docker
* Docker Compose
* Pydantic
* uv



