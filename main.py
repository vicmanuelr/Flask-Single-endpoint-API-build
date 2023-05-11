import requests
from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def get_objects():
    """Gets a list of 25 objects from the third API."""
    # Get the next endpoint from the request body.
    objects = []
    for i in range(25):
      # Make a request to the third API.
      response = requests.get("https://api.chucknorris.io/jokes/random")
      # Check the response status code.
      if response.status_code != 200:
          raise Exception("Error getting objects from third API")

      # Get the objects from the response body.
      objects.append(response.json())

    # Check that the objects are all different.
    for i in range(len(objects) - 1):
        if objects[i]["id"] == objects[i + 1]["id"]:
            raise Exception("Duplicate object id")
    objects_json = json.dumps(objects)
    # Return the objects.
    return objects


if __name__ == "__main__":
    app.run(debug=True)
