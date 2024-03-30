run:
    flask run

docker-build:
    docker build -t iris_model .

docker-run:
    docker run -p 5000:5000 iris_model