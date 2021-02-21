FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY password_vault code
RUN echo "> pwd"
RUN pwd
RUN echo "> ls"
RUN ls
WORKDIR /code

EXPOSE 8000