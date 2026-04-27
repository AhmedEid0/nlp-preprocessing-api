FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv sync

RUN uv run python -m nltk.downloader punkt punkt_tab stopwords wordnet omw-1.4

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]