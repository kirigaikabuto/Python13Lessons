# найти способ как скачивать видео с ютуба с помощью python
# файл поместить в определенную папку
# pip install pytube
# pip -> это бинарник или bat,sh file который находится внутри папки (venv) и он необходим чтобы скачивать библиотеки
# install -> настройка чтобы скачать
# pytube -> название библиотеки
from pytube import YouTube

pathToFile = YouTube("https://www.youtube.com/watch?v=95OlYy1M228").streams.first().download()
print(pathToFile)
