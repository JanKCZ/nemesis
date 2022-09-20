vlc --http-password 23372 --http-host 127.0.0.1 --fullscreen

curl -v -u :23372 http://127.0.0.1:8080/requests/status.xml\?command\=in_play\&fullscreen\&input\=/Users/honzak/Downloads/video.mp4
