#coding:utf-8
import pygame as pg
from pygame.locals import *
'''
    搭建界面 用于完成窗口和背景的显示
    使用面向对象的方式显示飞机，以及控制其左右移动
    新增玩家飞机发射子弹功能
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

        # 用来存储英雄飞机发射的所有子弹
        self.bulletList = []

    #显示我方飞机及其发射的子弹
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bulletList:
            bullet.display()  # 显示当前子弹的位置
            bullet.move()  # 让这个子弹进行移动，下次再显示的时候就会看到子弹在修改后的位置

    #控制我方飞机向左移动
    def move_left(self):
        self.x-=5
    # 控制我方飞机向右移动
    def move_right(self):
        self.x+=5

    #英雄飞机发射子弹功能
    def she_bullet(self):
        new_bullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(new_bullet)

#定义子弹类
class Bullet(object):
    #定义子弹的初始化函数
    def __init__(self,x,y,screen):
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image = pg.image.load("./feiji/bullet.png")
    #定义子弹移动函数
    def move(self):
        self.y -= 5
    #显示英雄飞机发射的子弹
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

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
                hero_plane.she_bullet()

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
