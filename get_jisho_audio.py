import urllib.request
import urllib.parse
import sys
from bs4 import BeautifulSoup
import re

PATH = "C:\\Users\\ejnkns\\Desktop\\"

input_word = urllib.parse.quote(sys.argv[1])

print("Looking up \"" + input_word + "\" in jisho.org")
response = urllib.request.urlopen('https://jisho.org/search/' + input_word)
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
(soup.find("div", {"id" : "no-matches"}))
if soup.find("div", {"id" : "no-matches"}):
    print("No matches for " + input_word)
else:
    audios = soup.audio.contents
    result_word = soup.audio.get("id")[6:].partition(":")[0]
    print("Getting audio for: " + result_word)

    for audio in audios:
        str_audio = str(audio)
        contents = re.findall('"([^"]*)"', str_audio)
        if contents[1] == "audio/mpeg":
            audio_url = "https:" + contents[0]
            urllib.request.urlretrieve(audio_url, PATH + result_word + ".mp3")
            print("File saved to: " + PATH + result_word + ".mp3")
