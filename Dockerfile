FROM debian:latest

RUN apt update && apt install -y python3 python3-venv python3-pip git curl

WORKDIR /app

COPY . /app/

RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
