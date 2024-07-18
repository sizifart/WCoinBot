FROM python:3.12.3-alpine3.18

WORKDIR app/

COPY requirements.txt requirements.txt
# Update the package index and install necessary packages for building Python dependencies
RUN apk update && \
    apk add --no-cache build-base

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --no-warn-script-location --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py", "-a", "2"]