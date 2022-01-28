FROM docker.io/python:3.10.2-slim-buster

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="ChRIS Plugin Title" \
      org.opencontainers.image.description="A ChRIS ds plugin that..."

WORKDIR /usr/local/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install --use-feature=in-tree-build .

CMD ["commandname", "--help"]
