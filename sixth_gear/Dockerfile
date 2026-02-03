FROM frappe/bench:latest

USER frappe
WORKDIR /home/frappe/frappe-bench

# Copy app source code to the apps directory
COPY --chown=frappe:frappe . /home/frappe/frappe-bench/apps/sixth_gear

# Install the app dependencies
# We use '|| true' to prevent build failure if the environment is not yet initialized
RUN if [ -d "./env" ]; then ./env/bin/pip install -e ./apps/sixth_gear; else echo "Environment not found, skipping pip install"; fi
