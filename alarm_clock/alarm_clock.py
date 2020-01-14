# https://downloads.khinsider.com/game-soundtracks/album/happy-mario-20th-super-mario-sound-collection
import os, sys, time
from playsound import playsound

# sound_file = '01 overworld bgm.mp3'
# sound_file = '02 course clear fanfare.mp3'
# sound_file = '03 underground bgm.mp3'
# sound_file = '04 underwater bgm.mp3'
# sound_file = '01 overworld bgm.mp3'
sound_file = '06 world clear fanfare.mp3'

audio_path = os.path.join('sound_lib', sound_file)

print('How much time later should the alarm go off ?\n')

alarm_time = {}
alarm_time['hrs'] = int(input('how many hours ?\n'))
alarm_time['mins'] = int(input('how many minutes ?\n'))
alarm_time['secs'] = int(input('how many seconds ?\n'))

print('Tha alarm will go off in {} hrs {} mins {} secs\n'.format(alarm_time['hrs'], alarm_time['mins'], alarm_time['secs']))

# Number of time you want the alarm to repeat
n_rings = 2

# start time
tick = time.time()

rang = False

while not rang:
    total_time = time.time() - tick
    m, s = divmod(total_time, 60)
    h, m = divmod(m, 60)

    print('alarm going off in {} : {} : {}'.format(int(alarm_time['hrs']) - h, int(alarm_time['mins']) - m, int(alarm_time['secs']) - s))     

    if h == alarm_time['hrs'] and m == alarm_time['mins'] and int(s) == alarm_time['secs']:
        print('\nALARM RINGING !')
        for i in range(n_rings):
            playsound(audio_path)
        rang = True