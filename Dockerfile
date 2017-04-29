FROM python:3-onbuild
RUN pip install -r requirements.txt
RUN python -m SimpleHTTPServer 8000

CMD [ "python", "app.py" ]