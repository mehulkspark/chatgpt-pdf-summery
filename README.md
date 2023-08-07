<!DOCTYPE html>
<html>
<head>
  <title>PDF Summary Docker Setup</title>
</head>
<body>

<h1>PDF Summary Docker Setup</h1>

<p>Get started with PDF summarization using Docker and unleash the power of automation! Follow the steps below to set up your environment:</p>

<h2>🔑 Necessary Requirements</h2>

<ol>
  <li>Place your OPEN API data into the 'OPEnPAI' folder. 📂</li>
  <li>Put your PDF files into the 'pdfs' folder. 📚</li>
  <li>Replace your OPEN API Key in the Dockerfile. 🔑</li>
</ol>

<h2>🛠️ Build Docker Image</h2>

<ol>
  <li>Create the Docker Image:</li>
</ol>
<code>docker build -t pdfsummary .</code>

<ol start="2">
  <li>Create a Container from the Image:</li>
</ol>
<code>docker run --name my_pdf_summary_container pdfsummary</code>

<ol start="3">
  <li>Run the Code Inside the Container:</li>
</ol>
<ol>
  <li>Access the Container's shell:</li>
</ol>
<code>docker exec -it my_pdf_summary_container /bin/bash</code>

<ol start="2">
  <li>Change to the app directory:</li>
</ol>
<code>cd /app</code>

<ol start="3">
  <li>Run the Python script for PDF summarization:</li>
</ol>
<code>python Summarize_PDF_Chroma.py</code>

<h2>🚀 Using docker-compose.yml</h2>

<p>To simplify the setup process, you can use Docker Compose:</p>

<ol>
  <li>Create and start containers defined in docker-compose.yml:</li>
</ol>
<code>docker-compose up</code>

<p>By following these steps, you'll be ready to generate PDF summaries with ease using Docker containers. Happy summarizing! 📑</p>

</body>
</html>
