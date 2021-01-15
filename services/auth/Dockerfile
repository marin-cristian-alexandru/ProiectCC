FROM python:3.6
COPY requirements.txt /tmp
ADD app.py /
RUN pip install -r /tmp/requirements.txt
EXPOSE 8014
CMD ["python3", "app.py"]