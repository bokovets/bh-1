FROM python:3
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \ 
   python3-pymysql 
RUN pip3 install pipenv    

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pipenv install 






