FROM python:3-alpine3.23
RUN pip install mysql-connector-python fastapi uvicorn
COPY main.py .
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]

