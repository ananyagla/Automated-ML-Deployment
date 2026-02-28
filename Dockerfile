FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Train all models during build
RUN python train_all.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]