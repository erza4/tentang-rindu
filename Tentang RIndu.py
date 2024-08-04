import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Ku hanya diam", 0.1),
        ("Menggenggam menahan", 0.13),
        ("Segala Kerinduan", 0.14),
        ("Memanggil namamu", 0.18),
        ("Disetiap malam", 0.16),
        ("Ingin engkau datang dan hadir", 0.17),
        ("Dimimpiku", 0.16),
        
    ]
    delays = [0.1, 3.5, 6.5, 9.5, 12.5, 15.5, 16.5 ]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()