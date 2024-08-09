# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install SQLite command-line tool
RUN apt-get update && apt-get install -y sqlite3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Exposer le port sur lequel l'application va fonctionner
EXPOSE 5000

# Specify the command to run the application
CMD ["python", "app/main.py"]
