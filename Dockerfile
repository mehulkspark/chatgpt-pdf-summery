# Use the official Python image as the base image
FROM python:3.8
# FROM python:3.10 #if reqiored python 3.10
# FROM python:3.9 #if required python 3.9

# Set the working directory inside the container
WORKDIR /app
COPY OpenAI /app/OpenAI/
COPY pdfs /app/pdfs/
# Copy your Python script and other necessary files
COPY Summarize_PDF_Chroma.py /app/
# Copy other dependencies if needed

# Set environment variables
ENV OPENAI_API_TYPE=<your_openai_api_type>
ENV OPENAI_API_VERSION=<your_openai_api_version>
ENV OPENAI_API_BASE=<your_openai_api_base>
ENV OPENAI_API_KEY=<your_api_key>

# Install dependencies
RUN pip install PyPDF2 langchain

# Specify the command to run your Python script
CMD ["python", "Summarize_PDF_Chroma.py"]
