# Desafio 021 - Referente aula Fase08
# Faça um programa em Python que abra
# e reproduza o áudio de um arquivo MP3.

# Versão 01

from pygame import mixer

# Iniciando o funcionalidade 'mixer'
mixer.init()

# Carregar a música
mixer.music.load("music.mp3")

# Configuração do Volume
mixer.music.set_volume(0.7)

# Iniciar a música
mixer.music.play()

funcao = input('Aperte qualquer tecla para cancelar')
