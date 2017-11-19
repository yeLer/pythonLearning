#coding:utf-8
import pygame as pg
from pygame.locals import *
'''
    搭建界面 用于完成窗口和背景的显示
    使用面向对象的方式显示飞机，以及控制其左右移动
'''
class HeroPlane(object):
    #对我方飞机进行初始化
    def __init__(self, screen):
        # 用来保存飞机的x，y坐标
        self.x = 180
        self.y = 580

        #设置窗口需要显示的内容
        self.screen = screen

        # 用来保存英雄飞机需要的图片名字
        self.imageName = "./feiji/hero1.png"

        # 根据名字生成飞机图片
        self.image = pg.image.load(self.imageName)
    #显示我方飞机
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    #控制我方飞机向左移动
    def move_left(self):
        self.x-=5
    # 控制我方飞机向右移动
    def move_right(self):
        self.x+=5

#控制键盘操作的函数
def key_control(hero_plane):
    for event in pg.event.get():
        # 判断是否是点击了退出按钮
        if event.type == pg.QUIT:
            print("quit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print ("left")
                # 控制飞机向左移动
                hero_plane.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print ("right")
                hero_plane.move_right()
            elif event.key == K_SPACE:
                print('space')

def main():
    #1、创建一个窗口，用来显示内容  480*852的分辨率
    screen = pg.display.set_mode((420, 700), 0, 32)
    #2、创建一个和窗口大小一致的图片，用来充当背景
    background = pg.image.load("./feiji/background.png")
    #3、创建一个玩家飞机
    hero = HeroPlane(screen)

    #4、把背景图片放入到窗口中去显示
    while True:
        #设定需要显示的背景图
        screen.blit(background,(0,0))
        #设定显示玩家的飞机
        hero.display()
        #更新需要显示的内容
        pg.display.update()
        # 判断是否是点击了按钮
        key_control(hero)
        # 更新需要显示的内容
        pg.display.update()

if __name__ == "__main__":
    main()
