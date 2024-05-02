FROM python:3.10

RUN apt-get update && \
    apt-get install -y \
    git \
    gcc \
    python3-dev \
    libssl-dev \
    python3-pip \
    python3-venv \
    vim \
    curl \
    libev-dev \
    libvirt-dev \
    libffi-dev \
    libyaml-dev \
    lsb-release && \
    apt-get clean all

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
