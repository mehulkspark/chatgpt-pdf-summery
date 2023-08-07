<!DOCTYPE html>
<html>
<head>
  <title>PDF Summary Docker Setup</title>
</head>
<body>

<h1>PDF Summary Docker Setup</h1>

<p>Follow the steps below to set up and run the PDF summarization process using Docker.</p>

<h2>Necessary Requirements</h2>

<ol>
  <li>Place your OPEN API data into the 'OPEnPAI' folder.</li>
  <li>Put your PDF files into the 'pdfs' folder.</li>
  <li>Replace your OPEN API Key in the Dockerfile.</li>
</ol>

<h2>Build Docker Image</h2>

<ol>
  <li>Create the Docker Image:<br>
    <code>docker build -t pdfsummary .</code></li>
  
  <li>Create a Container from the Image:<br>
    <code>docker run --name my_pdf_summary_container pdfsummary</code></li>
  
  <li>Run the Code Inside the Container:<br>
    <ol>
      <li>Access the Container's shell:<br>
        <code>docker exec -it my_pdf_summary_container /bin/bash</code></li>
      
      <li>Change to the app directory:<br>
        <code>cd /app</code></li>
      
      <li>Run the Python script for PDF summarization:<br>
        <code>python Summarize_PDF_Chroma.py</code></li>
    </ol>
  </li>
</ol>

<h2>Using docker-compose.yml</h2>

<p>To simplify the setup process, you can use Docker Compose:</p>

<ol>
  <li>Create and start containers defined in docker-compose.yml:<br>
    <code>docker-compose up</code></li>
</ol>

<p>By following these steps, you'll be able to set up and run the PDF summarization process using Docker containers.</p>

</body>
</html>
