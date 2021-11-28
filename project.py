#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-11-01
Purpose: Gifts Catcher
"""

import pygame
import random
from pygame.locals import *
import sys


# Text in the game
def print_text(scr, my_font, x, y, text, color):
    imgText = my_font.render(text, True, color)
    scr.blit(imgText, (x, y))


def game(screen, lives, scores):
    # scores and lives
    font = pygame.font.Font(None, 40)
    # Initial position of the sock
    catch_x, catch_y, catch_w = 300, 400, 200
    # Initial position of the gift
    gift_x, gift_y = random.randint(20, 680), -100
    # Initial speed of the gift
    vel_y = 5
    pygame.mixer.music.load(
        "Resources/Intro.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

    get_gift = pygame.mixer.Sound(
        "Resources/Get.mp3")
    get_gift.set_volume(0.4)
    miss_gift = pygame.mixer.Sound(
        "Resources/Lose.mp3")
    miss_gift.set_volume(1)

    # Game loop
    while lives > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if catch_x <= 0:
                        catch_x -= 0
                    else:
                        catch_x -= 60
                if event.key == K_RIGHT:
                    if catch_x >= 800 - catch_w:
                        catch_x += 0
                    else:
                        catch_x += 60

        width = 1000
        height = 560
        window = pygame.display.set_mode((width, height))
        bg_img = pygame.image.load('Resources/Christmas.jpg')
        bg_img = pygame.transform.scale(bg_img, (width, height))
        screen.blit(bg_img, (0, 0))

        # Set the gift
        gift_y += vel_y
        gift = pygame.image.load("Resources/Gift.png")
        gift = pygame.transform.scale(gift, (100, 100))
        screen.blit(gift, (gift_x, gift_y))

        # Set the sock
        catch = pygame.image.load("Resources/Sock.png")
        catch = pygame.transform.scale(catch, (150, 150))
        screen.blit(catch, (catch_x, catch_y))

        # Identify if the gift is caught
        if gift_y >= 480:
            miss_gift.play()
            lives -= 1
            gift_x, gift_y = random.randint(20, 680), -100
        elif (catch_y - gift_y) <= 60 and catch_x - 70 < gift_x < (catch_x + catch_w - 20):
            get_gift.play()
            scores += 1

            # Modify the speed of the gift
            if 5 <= scores < 10:
                vel_y = 6
            if 10 <= scores < 15:
                vel_y = 7
            if 15 <= scores < 20:
                vel_y = 8
            if 20 <= scores < 25:
                vel_y = 9
            if 25 <= scores < 30:
                vel_y = 10
            gift_x, gift_y = random.randint(20, 680), -100
        else:
            gift_y += vel_y

        print_text(screen, font, 10, 10, "Lives:" + str(lives), (60, 179, 113))
        print_text(screen, font, 850, 10, "Scores:" +
                   str(scores), (60, 179, 113))

        pygame.display.update()
        pygame.time.delay(10)

    return lives, scores


def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Resources/Christmas")
    lives = 3
    scores = 0
    end_font = pygame.font.Font(None, 60)

    while True:
        lives, scores = game(screen, lives, scores)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                lives = 3
                scores = 0


        print_text(
            screen, end_font, 150, 180, "You caught " + 
            str(scores) + " gift!", (60, 179, 113)
        )
        print_text(
            screen, end_font, 150, 260, "Merry Christmas!", (60, 179, 113)
        )
        print_text(
            screen, end_font, 150, 340, "Click to restart the game.", (
                60, 179, 113)
        )
        pygame.display.update()


if __name__ == '__main__':
    main()
