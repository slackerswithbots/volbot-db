FROM python:3-onbuild
RUN pip install -r requirements.txt
RUN python -m SimpleHTTPServer 8000

EXPOSE 8080

CMD [ "python", "app.py" ]