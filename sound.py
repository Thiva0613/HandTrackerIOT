#!/usr/bin/env python3
"""
@Filename:    sound.py
@Author:      dulanj
@Time:        2021-09-23 17.06
"""
import threading

from playsound import playsound


class Sound:
    p=0
    def __init__(self):
        
        ...

    def _play(self, sound):
        self.p = threading.Thread(target=playsound, args=(sound,), daemon=True)
        self.p.start()
        
    def _stop(self):
        self.p.terminate()
    
    def click(self):
        #threading.Thread(target=playsound, args=('data/sound/click.mp3',), daemon=True).start()
        #threading.Thread(target=playsound, args=('data/sound/click.wav',), daemon=True).start()
         #D:\TestProj\HandTracker-main\data
         
         #self.play('D:\TestProj\HandTracker-main\data\sound\click.mp3)
         self._play('data\sound\click.wav')

    def double_click(self):
        #threading.Thread(target=playsound, args=('data/sound/click2.mp3',), daemon=True).start()
        #threading.Thread(target=playsound, args=('data/sound/click2.wav',), daemon=True).start()
        #self._play('data\sound\click.wav')
        self._stop()
        #pass

if __name__ == '__main__':
    sound = Sound()
    sound.click()
    sound.double_click()
