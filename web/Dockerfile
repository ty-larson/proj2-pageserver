FROM python:3.9-slim
LABEL maintainer="Ty Larson <tyl@uoregon.edu>"
RUN apt-get update -y
RUN apt-get install -y build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]