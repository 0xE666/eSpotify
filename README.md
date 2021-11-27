# control-spotify-with-game-controller
ability to control spotify functions like pause, next song, volume with ps4 ( possibly xbox?) controller so you no longer have to tab out of games

create app in developer portal
https://developer.spotify.com/dashboard/applications

edit settings with redirect ui:
http://localhost:8081
https://e-e.tools/screenshots/EZdebsoIV6nm3x4.png

paste client credentials in config.json (client id client secret)
https://e-e.tools/screenshots/fZQ9YRVXiQzZ4tf.png

edit config as wanted and run the first time ran it should open the redirect ui in browser you may have to login if not accept the scope terms for spotify api

controller key codes:
x: 0
circle: 1
square: 2
triangle: 3
share: 4
PS: 5
options: 6
left_stick_click: 7
right_stick_click: 8
L1: 9
R1: 10
up_arrow: 11
down_arrow: 12
left_arrow: 13
right_arrow: 14
touchpad: 15

to do:
monitor the launch and close of specific application
