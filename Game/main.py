# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import yaml

with open('data/heroes.yaml') as yml:
    heroes = yaml.safe_load(yml)

list_of_hero_types = list(heroes.keys())

WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)

WINDOW_SIZE = (400, 600)
RECT_FIRST_HERO  = Rect(20, 200, 100, 300)
RECT_SECOND_HERO = Rect(220, 200, 100, 300)

def main():
    # 初期化
    pygame.init()
    # ウィンドウサイズの指定
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Test") 

    while(True):
        # 背景色の指定
        screen.fill((0,0,0,))
        # 四角枠
        pygame.draw.rect(screen, WHITE, RECT_FIRST_HERO, 1)
        pygame.draw.rect(screen, WHITE, RECT_SECOND_HERO, 1)
        # テキスト
        font = pygame.font.Font(None, 20)
        for i, hero in enumerate(heroes):
            #print(heroes[hero]['HP'])
            # name
            text = font.render(hero, True, WHITE)
            screen.blit(text, [20 + i * 200, 200])
            # HP
            text = font.render(str(heroes[hero]['HP']), True, WHITE)
            screen.blit(text, [20 + i * 200, 220])
            # MP
            text = font.render(str(heroes[hero]['MP']), True, WHITE)
            screen.blit(text, [20 + i * 200, 240])
            # ATK
            text = font.render(str(heroes[hero]['STR']), True, WHITE)
            screen.blit(text, [20 + i * 200, 260])
            # DEF
            text = font.render(str(heroes[hero]['DEF']), True, WHITE)
            screen.blit(text, [20 + i * 200, 280])
        # 画面更新
        pygame.display.update()
        # 終了処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()