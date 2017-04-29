FROM python:3-onbuild
RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "app.py" ]