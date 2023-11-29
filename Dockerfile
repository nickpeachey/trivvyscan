FROM aquasec/trivy:latest

WORKDIR /app
ENV username=nickpeachey
ENV password=wessex12

COPY entrypoint.sh /usr/local/bin/
COPY reporter.py /app/
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN apk add --no-cache python3 py3-pip

ENTRYPOINT [ "entrypoint.sh" ]