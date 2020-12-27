FROM python:3.6
COPY requirements.txt /tmp
ADD dbadmin.py /
RUN pip install -r /tmp/requirements.txt
EXPOSE 4444
CMD ["python3", "dbadmin.py"]
