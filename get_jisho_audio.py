import urllib.request
import urllib.parse
import sys
from bs4 import BeautifulSoup
import re
import os 

PATH = "C:\\Users\\ejnkns\\AppData\\Roaming\\Anki2\\User 1\\collection.media\\"

raw_input_word = sys.argv[1]
input_word = urllib.parse.quote(raw_input_word)

print("Looking up \"" + raw_input_word + "\" in jisho.org")
response = urllib.request.urlopen('https://jisho.org/search/' + input_word)
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
(soup.find("div", {"id" : "no-matches"}))
if soup.find("div", {"id" : "no-matches"}):
    print("No matches for " + input_word)
else:
    if soup.audio.contents:
        audios = soup.audio.contents
    else:
        print("No audio for match")
    result_word = soup.audio.get("id")[6:].partition(":")[0]
    print("Getting audio for: " + result_word)

    for audio in audios:
        str_audio = str(audio)
        contents = re.findall('"([^"]*)"', str_audio)
        if contents[1] == "audio/mpeg":
            audio_url = "https:" + contents[0]
            # might want this to be result_word sometimes?
            urllib.request.urlretrieve(audio_url, PATH + raw_input_word + ".mp3")
            print("File saved to: " + PATH + raw_input_word + ".mp3")
