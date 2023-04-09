FROM python:3.10.8-alpine
COPY . /app
WORKDIR /app
RUN pip install flask bandit
CMD ["python", "app.py"]