import sys
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="007996051f4a428fae985499cd9e53fb",
    api_version="2024-02-01",
    azure_endpoint = "https://horiabranchuwhisper.openai.azure.com/"
)

deployment_id = "whisperme" #This will correspond to the custom name you chose for your deployment when you deployed a model."
audio_test_file = sys.argv[1]

result = client.audio.transcriptions.create(
    file=open(audio_test_file, "rb"),
    model=deployment_id,
    language="en"
)

print(result.text)
