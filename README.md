# Control spotify with game controller ( playstation / xbox)

this will allow you control spotify functions like pause, next song, volume with ps4 ( possibly xbox? ) controller so you no longer have to take your hands off the controller for keyboard binds or tab out. feel free to make issues with suggestions or fork and improve


# Setup Instructions

[create a spotify developer app in developer portal](https://developer.spotify.com/dashboard/applications)

[edit the redirect ui for the created app](https://e-e.tools/screenshots/EZdebsoIV6nm3x4.png) : "http://localhost:8081"

[paste the client credentials into config.json ( client id, client secret ) ](https://e-e.tools/screenshots/fZQ9YRVXiQzZ4tf.png)

edit config as wanted and run the first time ran it should open the redirect ui in browser you may have to login if not accept the scope terms for spotify api, this is far from perfect threw together in a few hours, please make a issue if bugs are found

[controller key codes](https://raw.githubusercontent.com/hdhdhfhfirjf/control-spotify-with-game-controller/main/files/controllerKeys.json)

To do:
monitor the launch and close of a specific application
