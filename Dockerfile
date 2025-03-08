# This is a python project, so the base image should be for python
FROM python:3.13.2-slim

# Set working directory
WORKDIR /barber-appointment-scheduler-app

# Install `uv`
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy project files
COPY . .

# Create a new virtual environment inside the container
RUN python -m venv /app/.venv

# Activate venv and install dependencies using uv
RUN /app/.venv/bin/uv pip install

# Set the virtual environment as the default Python
ENV PATH="/app/.venv/bin:$PATH"

# Run the application (change this based on your app)
CMD ["python", "bot.py"]

