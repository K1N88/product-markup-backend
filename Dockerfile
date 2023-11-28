FROM python:3.10.8-slim
WORKDIR /prosept_app
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
COPY app/ .
CMD ["uvicorn", "prosept_app.main:app", "--host", "0.0.0.0", "--port", "80"]
