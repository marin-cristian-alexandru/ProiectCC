FROM python:3.6
COPY requirements.txt /tmp
ADD dbadmin.py /
RUN pip install -r /tmp/requirements.txt
CMD ["python3", "dbadmin.py"]
