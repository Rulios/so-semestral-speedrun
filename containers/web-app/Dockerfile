FROM python


ARG SERVER_PORT


ADD requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt

ADD main.py /

EXPOSE $SERVER_PORT

CMD [ "python", "./main.py" ]