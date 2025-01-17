import requests
from urllib.parse import urlparse
import os


def download_image(url, image_name):
    response = requests.get(url)
    response.raise_for_status()
    with open(image_name, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    path = urlparse(url).path
    path, extension = os.path.splitext(path)
    return extension


def get_colour(service):
    colors = service.colors().get().execute()
    print(colors)
    # Print available calendarListEntry colors.
    for id, color in colors['calendar'].items():
        print('colorId: %s' % id)
        print('  Background: %s' % color['background'])
        print('  Foreground: %s' % color['foreground'])
    # Print available event colors.
    for id, color in colors['event'].item():
        print('colorId: %s' % id)
        print('  Background: %s' % color['background'])
        print('  Foreground: %s' % color['foreground'])