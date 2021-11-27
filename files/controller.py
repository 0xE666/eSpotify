from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, json, os, winsound
from files.spotify import spotifyController

class controllerMonitor:
    def __init__(self) -> None:
        self.s = spotifyController()
        self.volume = 50
        with open("config.json") as f:
            self.config = json.load(f)

        self.nextSong = self.config["controls"]["nextSong"]
        self.nextSongBool = self.config["controlBools"]["nextSong"]

        self.prevSong = self.config["controls"]["prevSong"]
        self.prevSongBool = self.config["controlBools"]["prevSong"]

        self.volumeUp = self.config["controls"]["volumeUp"]
        self.volumeUpBool = self.config["controlBools"]["volumeUp"]

        self.volumeDown = self.config["controls"]["volumeDown"]
        self.volumeDownBool = self.config["controlBools"]["volumeDown"]

        self.pause = self.config["controls"]["pause"]
        self.pauseBool = self.config["controlBools"]["pause"]

        self.beep = self.config["beepOnActivation"]

        self.active = False
        self.controllerCheck = False
        self.joystickCount = 0
        self.joysticks = []

    def activate(self):
        self.active = not self.active
        if self.beep:
            winsound.Beep(400, 200)
    
    def checkControllerConnection(self):
        pygame.init()
        self.joystickCount = pygame.joystick.get_count()
        if self.joystickCount > 0:
            for joystick in range(self.joystickCount):
                self.joysticks.append(pygame.joystick.Joystick(joystick))
            for joystick in self.joysticks:
                joystick.init()
            return True
        return False

    def monitor(self):
        self.controllerCheck = self.checkControllerConnection()
        if self.controllerCheck != False:
            self.s.changeVolume(self.volume)
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    try:
                        if event.button == self.volumeUp:
                            if self.volumeUpBool:
                                if self.volume >= 100:
                                    pass
                                if self.volume <= 0:
                                    pass
                                self.volume += 5
                                self.s.changeVolume(self.volume)
                        if event.button == self.volumeDown:
                            if self.volumeDownBool:
                                if self.volume >= 100:
                                    pass
                                if self.volume <= 0:
                                    pass
                                self.volume -= 5
                                self.s.changeVolume(self.volume)
                        if event.button == self.prevSong:
                            if self.prevSongBool:
                                self.s.previousTrack()
                        if event.button == self.nextSong:
                            if self.nextSongBool:
                                self.s.nextTrack()
                        if event.button == self.pause:
                            if self.pauseBool:
                                self.s.pause()
                    except:
                        pass
