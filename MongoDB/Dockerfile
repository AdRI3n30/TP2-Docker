FROM mongo:8.0
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY ./dbfiles /docker-entrypoint-initdb.d
EXPOSE 27017
