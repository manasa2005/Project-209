import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

SERVER = None
PORT = 12345
IP_ADDRESS = '127.0.0.1'

def setup():
    global SERVER, PORT, IP_ADDRESS
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print(f"Connected to server {SERVER}:{PORT}")

def getMusicFiles():
    global song_counter
    music_files = []

    for root, _, files in os.walk("/path/to/music/directory"):
        for file in files:
            if file.lower().endswith((".mp3", ".wav")):
                song_counter += 1
                music_files.append(os.fsdecode(file))

    return music_files

def play(song_selected):
    global song_counter
    mixer.music.load(song_selected)
    mixer.music.play()
    

def stop():
    mixer.music.stop()

def main():
    setup()
    musicWindow()

if __name__ == "__main__":
    main()
