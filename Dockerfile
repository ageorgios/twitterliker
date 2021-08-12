FROM python:3

WORKDIR /usr/src/app

RUN pip3 install tweepy 

COPY . .

CMD [ "python3","-u", "./example.py" ]
