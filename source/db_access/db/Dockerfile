FROM postgres
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_DB neumonia
COPY init.sql /docker-entrypoint-initdb.d/
