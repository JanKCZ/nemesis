echo "starting BTN server on background - project Nemesis"

./vlc_play.sh

sleep 5

screen python3 /Users/honzak/Downloads/nemesis/PI-VLC_server/app.py -dmS nemesis_server

