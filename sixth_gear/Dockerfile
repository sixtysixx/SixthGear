FROM frappe/bench:latest

USER frappe
WORKDIR /home/frappe

# Initialize a new bench using Python 3.10 (stable for Frappe v15)
RUN bench init --skip-redis-config-generation --frappe-branch version-15 --skip-assets --python python3.10 frappe-bench

WORKDIR /home/frappe/frappe-bench

# Copy app source code to the apps directory
COPY --chown=frappe:frappe . /home/frappe/frappe-bench/apps/sixth_gear

# Install the app dependencies
RUN ./env/bin/pip install -e ./apps/sixth_gear

# Ensure logs and sites have correct permissions
RUN mkdir -p logs sites && chmod -R 775 logs sites

# Configure the bench to use the external redis and db services
RUN bench set-config -g db_host db && \
    bench set-config -g redis_cache redis://redis:6379 && \
    bench set-config -g redis_queue redis://redis:6379 && \
    bench set-config -g redis_socketio redis://redis:6379
