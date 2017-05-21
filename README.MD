# WavNN
## Dependencies
Python 3
```glob``` for python (included in most distributions)
```ffmpeg``` (binary for mac included)
```pydub``` for python (pip install pydub)
## Friday, May 19, 2017
Added ```corpus_gen.py``` and ```ffmpeg```. ffmpeg is a unix binary built for Mac OS X to convert audio compression formats. ```corpus_gen.py``` is the initial dataset creation script. Basically, place all mp3 files scraped from youtube and other forms (if using youtube, I recommend using a playlist and downlaoding en masse using downvids.net - this can be sped up usig a simple jquery select to open every generated download link at once, and then the output mp3 can be cleaned using a simple bash loop to rename song titles so that it appears in pretty form without spaces) into the MP3 folder. I have not included mp3 files here due to copyright claims. Then, run the script and the corpus folder will have generated waveforms.
