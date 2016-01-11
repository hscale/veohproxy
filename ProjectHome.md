# Veoh-Proxy #

## **Note: Ninjavideo is currently not working** ##
**NinjaVideo changed their server layout and now employ encryption. I already cracked and reimplemented it but won't have time to implement their new storage host for videos until next year.**

## Description ##
Veoh-Proxy, a local Web Server that streams **high quality content** from **Veoh** - the originally uploaded version, not the FLV-compressed version with low quality.

It also replaces the [NinjaVideo](http://NinjaVideo.net) helper software with less restrictions than the original program (No referral checking, etc.).

So now, any online video website could use this helper (or a derrivate work) to supply viewers with high quality video content hosted on Veoh.

The program is mainly developed for the great [XBMC](http://xbmc.org) XBox Media Center, but should run on any platform that knows how to deal with python files. Just install python for your operating system and start the default.py file.

It can stream content from the following websites:
  * **Veoh**
  * **Messagefromme / Streamplug**
  * **Ninjavideo**

## Technical Stuff ##
If you like a download manager, you can use resuming and multipart downloading with it. With this, you should be able to grab the veoh videos with full speed. I was able to download at 20Mbyte/s from a university server.

It currently supports Videos from Veoh, Ninjavideo and Streamplug (messagefromme.com).
It supports HTTP proxies. It should use the proxy settings of your operating system. If it does not, simply edit the default.py file and change the PROXY line.

## Usage ##

To start the program, you need to install [Python](http://python.org) first. Then you can probably just double-click the default.py fine and a console should show up. If this doesn't work, open up a command window, change to the directory you unzipped the files to using 'CD \path\to\files' on windows. Now tell python to open that file. Type:

`\path\you\installed\python\to\python.exe default.py`

for example

`C:\python25\python.exe default.py`

Now it should output some stuff and run in the console.

To try the program, please search for Veoh videos on their Website. If you click on any of the results, you will get to a URL like:
http://www.veoh.com/videos/v280192es88wEr4?searchId=3295803849254710272&rank=1
Take the cryptic part starting with the letter "v" and append it to the local webserver URL:
http://127.0.0.1:64653/v280192es88wEr4. (_The port has been changed in version 1.3. Used to be 64652._)
You can just type it in your browser and it should download or show the file. Or you can pass the URL directly to your favourite media player.

The NinjaVideo website should run without any problems. If the program doesn't show any errors and videos don't work, you should check your video player settings or try downloading the video file instead.

To download messagefromme videos, you need to have a look into the source code of the website showing the video (Ctrl-U in Firefox). Search (Ctrl-F) for ".ogm" without the quotes and you should see an embedded video URL. Now you need to encode that url in base64, maybe using [this](http://base64-encoder-online.waraxe.us/) online base64 encoder. Then just attach /streamplug/ + the base64 string to the url, for example if the real URL is:
http://diffuser4.messagefromme.com:80/myvideoregistry/video_12402.ogm, the base64-encoded string is:
aHR0cDovL2RpZmZ1c2VyNC5tZXNzYWdlZnJvbW1lLmNvbTo4MC9teXZpZGVvcmVnaXN0cnkvdmlkZW9fMTI0MDIub2dt

and the resulting download/stream URL is:
http://0.0.0.0:64653/streamplug/aHR0cDovL2RpZmZ1c2VyNC5tZXNzYWdlZnJvbW1lLmNvbTo4MC9teXZpZGVvcmVnaXN0cnkvdmlkZW9fMTI0MDIub2dt


Sorry for the base64 thing. I developed Veoh-Proxy for XBMC where this makes at least some sense.