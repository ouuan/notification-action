# Container image that runs your code
FROM python:3-slim

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh main.py /
COPY webhook2message /webhook2message

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
