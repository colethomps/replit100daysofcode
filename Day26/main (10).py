from replit import audio
import os, time
def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback

while True:
  os.system("clear")
  # Show the menu
  print("1. Play")
  print("2. Exit")
  options = input("")
  time.sleep(1)
  if options == '1':
    play()
    continue
  elif options == '2':
    break
  else:
    continue