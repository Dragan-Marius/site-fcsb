# Imagine de bază
FROM python:3.10

# Setăm directorul de lucru în container
WORKDIR /app

# Copiem tot codul în container
COPY . .

# Instalăm dependințele
RUN pip install --no-cache-dir -r requirements.txt

# Expunem portul pe care Flask îl va folosi
EXPOSE 10000

# Comanda de start
CMD ["python", "app.py"]