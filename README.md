# Challenge_Engie_repo

Let’s proceed to build the image with the command below:

docker image build -t flask_docker .

After successfully building the image, the next step is to run an instance of the image. Here is how to perform this:

docker run -p 8888:8888 -d flask_docker

The API it's running on the container on http://localhost:8888/

We go to the web page and you can copy paste the json.
Below, you can see the result to the json file sended.