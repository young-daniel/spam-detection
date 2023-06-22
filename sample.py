# Sample invocation of API

import requests

# this assumes API port mapped to localhost 5000
address = "127.0.0.1:5000"
api_endpoint = "http://{}/api/v1/predict".format(address)

sample_messages = [
    "Text Jingles to 500500 for your free audiobook",
    "Just left, be there in fifteen",
]

for message in sample_messages:
    print("Sending POST request with message: {}".format(message))
    sample = requests.post(api_endpoint, data={"message": message})
    result = sample.json()
    print("Received result {}".format(result))

