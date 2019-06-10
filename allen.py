
from aylienapiclient import textapi

client = textapi.Client("3c4e267d", "788f25424b9fddec41a53cc696beeee8")

sentiment = client.Sentiment({'text': 'she abuses him '})

print(sentiment)