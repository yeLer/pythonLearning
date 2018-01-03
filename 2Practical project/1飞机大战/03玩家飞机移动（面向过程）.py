#coding:utf-8
import pygame as pg
from pygame.locals import *
'''
    搭建界面 用于完成窗口和背景的显示
'''
def main():
    #1、创建一个窗口，用来显示内容  480*852的分辨率
    screen = pg.display.set_mode((420, 700), 0, 32)
    #2、创建一个和窗口大小一致的图片，用来充当背景
    background = pg.image.load("./feiji/background.png")
    #3、创建一个玩家飞机
    hero = pg.image.load("./feiji/hero1.png")
    # 用来保存飞机的x，y坐标
    x = 180
    y = 580

    #4、把背景图片放入到窗口中去显示
    while True:
        #设定需要显示的背景图
        screen.blit(background,(0,0))
        #设定显示玩家的飞机
        #screen.blit(hero, (180, 580))
        screen.blit(hero, (x, y))
        #更新需要显示的内容
        pg.display.update()
        # 判断是否是点击了退出按钮
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("quit")
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    print ("left")
                    #控制飞机向左移动
                    x-=5
                elif event.key==K_d or event.key==K_RIGHT:
                    print ("right")
                    x+=5
                elif event.key == K_SPACE:
                    print('space')
        # 更新需要显示的内容
        pg.display.update()

if __name__ == "__main__":
    main()
