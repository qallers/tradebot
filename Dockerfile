# Set base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the script and requirements file into the container
COPY tradebot.py .
COPY requirements.txt .

# Install required packages
RUN pip install -r requirements.txt

# Expose the necessary ports
EXPOSE 8080

# Run the script when the container starts
CMD ["python", "script.py"]
