# Base image
FROM python:3.12-alpine

# Create a non-root user
RUN adduser -D expert

# Set working directory
WORKDIR /gist-app

# Copy only the files required for the installation first (better caching)
COPY requirements.txt .

# Install dependencies
RUN  pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY gist-app/ ./gist-app/

# Change ownership of the files to the non-root user to avoid permission issues
RUN chown -R expert:expert /gist-app

# Switch to the non-root user
USER expert

# Expose port for the application
EXPOSE 8080

# Run the application
CMD ["python", "gist_app.py"]