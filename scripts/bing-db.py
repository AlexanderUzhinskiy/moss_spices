# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

subscription_key = "76003022336e40e58c6b33f57506396c"
search_term = "canadian rockies"

client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))
image_results = client.images.search(query=search_term)

if image_results.value:
    first_image_result = image_results.value[0]
    print("Total number of images returned: {}".format(len(image_results.value)))
    print("First image thumbnail url: {}".format(
        first_image_result.thumbnail_url))
    print("First image content url: {}".format(first_image_result.content_url))
else:
    print("No image results returned!")