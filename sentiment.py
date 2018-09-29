#!/usr/bin/python
# -*- coding: latin-1 -*-

import credentials

subscription_key = credentials.credentials['msft_text_analytics_api_key']
assert subscription_key
text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
language_api_url = text_analytics_base_url + "languages"
print(language_api_url)


documents = { 'documents': [
    { 'id': '1', 'text': 'This is a document written in English.' },
    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
    { 'id': '3', 'text': '这是一个用中文写的文件' },
    { 'id': '4', 'text': 'Αυτό το έγγραφο είναι γραμμένο στα Ελληνικά'}
]}

print "'documents' is : ", documents


import requests
from pprint import pprint
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)

# from IPython.display import HTML
# table = []
# for document in languages["documents"]:
#     text  = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]
#     langs = ", ".join(["{0}({1})".format(lang["name"], lang["score"]) for lang in document["detectedLanguages"]])
#     table.append("<tr><td>{0}</td><td>{1}</td>".format(text, langs))
# HTML("<table><tr><th>Text</th><th>Detected languages(scores)</th></tr>{0}</table>".format("\n".join(table)))

sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)
print

while True:
	my_text = raw_input("\tPlease describe your experience: ")
	print "You typed: ", my_text
	documents = {'documents' : [
		{'id': '1', 'language': 'en', 'text': my_text},
	]}

	headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
	response  = requests.post(sentiment_api_url, headers=headers, json=documents)
	sentiments = response.json()
	pprint(sentiments)
	