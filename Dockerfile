# Use the official Python image as the base image
FROM python:3.8
#if required python 3.10
# FROM python:3.10 
#if required python 3.9
# FROM python:3.9 

# Set the working directory inside the container
WORKDIR /app

# Copy the OpenAI and pdfs folders first
COPY OpenAI /app/OpenAI/
COPY pdfs /app/pdfs/

# Copy the requirements file and install dependencies to take advantage of layer caching
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Set environment variables
ENV OPENAI_API_TYPE=<your_openai_api_type>
ENV OPENAI_API_VERSION=<your_openai_api_version>
ENV OPENAI_API_BASE=<your_openai_api_base>
ENV OPENAI_API_KEY=<your_api_key>

# Specify the command to run your Python script
CMD ["python", "Summarize_PDF_Chroma.py"]
