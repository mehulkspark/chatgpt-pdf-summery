Nessasory Requirement

1. Put Your OPEN API Data into OPEnPAI Folder
2. Put Your PDF into pdfs
3. Replace you open API Key into Docker File

Build Docker Image

1. Create Docker Image 
docker build -t pdfsummery .

2. Create Container from Image 
docker run --name my_pdf_summary_container pdfsummary

3. Inside Container Run Code 

Steps
1. docker exec -it my_pdf_summary_container /bin/bash
2. cd /app
3. python Summarize_PDF_Chroma.py



With docker-compose.yml
Create the Docker Image:
1. docker build -t pdfsummary .
2. docker-compose up



