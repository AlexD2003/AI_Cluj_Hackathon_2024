# Packages required:
import base64
from mimetypes import guess_type
from gtts import gTTS
import requests
import json
import sys
import os
# import pyttsx3


# get first parameter from command line
first_param = sys.argv[1]

# Function to encode a local image into data URL
def local_image_to_data_url(image_path):
    # Guess the MIME type of the image based on the file extension
    mime_type, _ = guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Default MIME type if none is found

    # Read and encode the image file
    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Construct the data URL
    return f"data:{mime_type};base64,{base64_encoded_data}"

image_path = sys.argv[1]
data_url = local_image_to_data_url(image_path)

api_base = 'https://horiabranchuus.openai.azure.com/'
deployment_name = 'testmemaster'
API_KEY = '006596a90f95486b8eb28126a798a3d6'

base_url = f"{api_base}openai/deployments/{deployment_name}"
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY
}

cmd = sys.argv[2]


# Prepare endpoint, headers, and request body
endpoint = f"{base_url}/chat/completions?api-version=2023-12-01-preview"
data = {
    "messages": [
        { "role": "system", "content": "You are a helpful assistant, helping blind people getting around" },
        { "role": "user", "content": [
            {
                "type": "text",
                "text": cmd
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": data_url
                }
            }
        ] }
    ],
    "max_tokens": 2000
}

# Make the API call
response = requests.post(endpoint, headers=headers, data=json.dumps(data))
json = response.json()

msg = json['choices'][0]['message']['content']

status = ""

if msg == "1":
    status = "1"
    msg = "I am sorry, there is no text"
elif msg == "2":
    status = "2"
    msg = "I am sorry, the image is not clear please try again"

elif msg == "-1":
    status = "-1"
    msg = "I am sorry, I cannot help you with that please try again"
else:
    print(msg + " check")

tts = gTTS(text=msg, lang='en', slow=False)

tts.save("./output.mp3")

os.system("mpv ./output.mp3 --no-video")

if status == "2" or status == "-1":
    os.system("./lost_in_room")

