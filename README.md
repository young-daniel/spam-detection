# spam-detection

This repo contains the deployment for the model here: https://www.kaggle.com/code/youngdaniel/spam-detection/notebook

The Docker image is available on Docker Hub here: https://hub.docker.com/r/doyoung04/spam-detection/

The application can be started with `docker run --publish 5000:5000 spam-detection:0.6`

The Python CLI can be found in `inference.py`. run `python inference.py -h` for usage.
