FROM python:3.7-slim as builder

COPY AR/requirements.txt /tmp

RUN \
    python3 -m venv /tmp/venv && \
    /tmp/venv/bin/pip3 install --upgrade pip && \
    /tmp/venv/bin/pip3 install -r tmp/requirements.txt

FROM python:3.7-slim

COPY AR/static /app/static
COPY AR/web_ar.py /app
COPY --from=builder /tmp/venv /app/venv

WORKDIR /app
CMD ["venv/bin/python3", "web_ar.py" ]
EXPOSE 4000