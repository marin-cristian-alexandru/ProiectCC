FROM python:3.6
COPY requirements.txt /tmp
ADD client.py /
RUN pip install -r /tmp/requirements.txt
EXPOSE 5000
CMD ["python3", "client.py"]

