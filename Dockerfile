FROM python:3.9-slim

WORKDIR /app

COPY . .

# ✅ ADD THIS LINE (VERY IMPORTANT)
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "--html=report.html", "--self-contained-html"]