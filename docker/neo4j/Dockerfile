FROM neo4j:5.16-community

# Set environment variables
ENV NEO4J_AUTH=neo4j/password
ENV NEO4J_PLUGINS=["apoc"]
ENV NEO4J_dbms_security_procedures_unrestricted=apoc.*
ENV NEO4J_dbms_security_procedures_allowlist=apoc.*

# Expose ports
EXPOSE 7474 7687

# Volumes for persistent data
VOLUME /data /logs /import
