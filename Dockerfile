FROM python:latest

RUN apt-get update -y && \  
   apt-get install -y python-pip 


WORKDIR /usr/local/bin

COPY private_api.py testrail.py complex_data.csv valid_test_id.csv /usr/local/bin/

RUN pip install requests

RUN chmod +x /usr/local/bin/private_api.py

CMD ["python", "/usr/local/bin/private_api.py"]
