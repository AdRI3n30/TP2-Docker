FROM mongo:8.2
USER mongodb
COPY ./dbfiles /docker-entrypoint-initdb.d
EXPOSE 27017
