FROM python:alpine3.8
COPY . /app
WORKDIR /app
#install python app
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]
EXPOSE 8080