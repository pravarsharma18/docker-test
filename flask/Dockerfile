FROM python:3.11-slim

WORKDIR /flask

COPY requirements.txt .

RUN python -m venv /opt/f_env

ENV PATH="/opt/f_env/bin:$PATH"

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x run.sh

CMD ["./run.sh"]