FROM postgres:15-alpine

# Set environment variables
ENV POSTGRES_DB=daw_memory
ENV POSTGRES_USER=daw_user
ENV PGDATA=/var/lib/postgresql/data

# Expose PostgreSQL port
EXPOSE 5432

# Volume for persistent data
VOLUME /var/lib/postgresql/data
