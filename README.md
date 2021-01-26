# Grayscaler_cherrypy
A CherryPy web application for converting an image to its grayscale version. 

# Instructions
The grayscale folder contains a CherryPy web application for converting an image to its grayscale version. A Dockerfile is provided.
Follow the instructions below:
1. In a terminal window, build the docker image from the `/grayscale` directory:
 ``` bash
 docker build -t grayscale .
 ```
2. Run the docker container:
```bash
 docker run -p 8080:8080 grayscale
```
You should see some CherryPy logs in the terminal.

3. The application is up and running. Go to your web browser at localhost:8080 or a different IP (check the actual IP with `docker-machine ip` command)

4. Following the instructions from the web page, it is possible to upload an image and download its grayscale version.

