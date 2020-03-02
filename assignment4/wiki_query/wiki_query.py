import argparse
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError


def string_item(item):
    return str(item)


parser = argparse.ArgumentParser(description='Mining Wikipedia.')

parser.add_argument('-item', required=True, type=string_item, nargs='+', help='contend to be searched')

args = parser.parse_args()

suffix = '_'.join(args.item)
service_url = "https://wikipedia.org/wiki/"

site_string = service_url + urllib.parse.quote(suffix)

try:
    cl_site = urllib.request.urlopen(site_string)
    soup = BeautifulSoup(cl_site, "html.parser")
    paragraphs = soup.select("p")
    for para in paragraphs:
        text = para.text
        print(text)
except HTTPError:
    print("No such wiki content")

