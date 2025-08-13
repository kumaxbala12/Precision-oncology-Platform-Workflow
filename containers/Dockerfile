
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt dev-requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r dev-requirements.txt
COPY . .
CMD ["pytest", "-q"]
