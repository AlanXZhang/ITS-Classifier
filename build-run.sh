docker build -t my_image . 

docker run --rm -it -v "$(pwd):/app" my_image -p 8888:8888
