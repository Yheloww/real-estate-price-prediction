FROM python:3.10

WORKDIR /test-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./Deployement/app ./Deployement/app

CMD ["python", "./Deployement/app/app.py"]

#docker build -t predict-app .
#docker run -t -i -p 5000:5000 predict-app