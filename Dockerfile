FROM python:3.12.8-slim

WORKDIR /app

# Copy project files
COPY . .

RUN python -m pip install .

# Expose port
EXPOSE 8000

# Run the FastAPI server
CMD [ "uvicorn", "park.main:app", "--host", "0.0.0.0" ]