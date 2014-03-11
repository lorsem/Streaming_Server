Streaming_Server
================

All files needed for my small local streaming server

== The Scripts ==
I will soon arrange them to be better structured and more comfortable to use
They should be run one after the other, on a directory containing video files. The script at the moment won't look
inside directories
* Renamer-MOVE.py: for every file in Current Working Directory, create a diretory and name it like the file.
                   Move the file in that directory, rename the file to video.*original extension* . This is
                   supposed to be used with video files to be added to the server (will add howto)
* AddContentHtml.py: in every directory, create a 'content.html' file that contains the appropriate <video> tag
                    (html5) to stream the file inside the directory
* Indexer.py: will add an 'index.html' file containing links to all the 'content.html' pages created before. Sitename
                    is '192.168.1.150' (local, static ip). 
                    
                    
== The server ==
The server is a standard Apache2 server. I am hosting it on a RaspberryPi connected to the local network.
On the server, /var/www/video/index.html is the index of the videos (the one you create with Indexer.py).
Videos are stored in /var/www/video/*directory*/video.*format*, the structure is created using Rename-MOVE.py

All my videos are stored on an external HDD, mounted directly in /var/www/video for ease of use. The root of the
HDD is the /video of the server.
