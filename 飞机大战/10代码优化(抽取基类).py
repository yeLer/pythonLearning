#coding:utf-8
import pygame as pg
import time
import random
from pygame.locals import *
'''
    让敌方飞机发射子弹
'''
#定义飞机的基类
class Plane(object):
    #对我方飞机进行初始化
    def __init__(self, screen,image):
        #设置窗口需要显示的内容
        self.screen = screen
        # 爆炸效果用的如下属性
        self.hit = False  # 表示是否要爆炸
        # 根据名字生成飞机图片
        self.image = pg.image.load(image)

        # 用来存储英雄飞机发射的所有子弹
        self.bulletList = []

    #显示我方飞机及其发射的子弹
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        #用来存放需要删除的对象的引用
        need_del_item_list = []
        #保存需要删除的对象
        for i in self.bulletList:
            if i.judge():
                need_del_item_list.append(i)
        # 删除self.bulletList中需要删除的对象
        for i in need_del_item_list:
            self.bulletList.remove(i)

        for bullet in self.bulletList:
            bullet.display()  # 显示当前子弹的位置
            bullet.move()  # 让这个子弹进行移动，下次再显示的时候就会看到子弹在修改后的位置

class HeroPlane(Plane):
    #对我方飞机进行初始化
    def __init__(self, screen):
        super(HeroPlane,self).__init__(screen,"./feiji/hero1.png")
        # 用来保存飞机的x，y坐标
        self.x = 180
        self.y = 580
    #控制我方飞机向左移动
    def move_left(self):
        self.x-=5
    # 控制我方飞机向右移动
    def move_right(self):
        self.x+=5
    #英雄飞机发射子弹功能
    def she_bullet(self):
        new_bullet = Bullet(self.x, self.y, self.screen,"hero")
        self.bulletList.append(new_bullet)

class EnemyPlane(Plane):
    def __init__(self, screen):
        super(EnemyPlane, self).__init__(screen, "./feiji/enemy0.png")
        # 设置敌方飞机的默认位置
        self.x = 0
        self.y = 0
        # 设置初始方向向右
        self.direction = "right"

    def move(self):
        # 如果碰到了右边界，就往左走  如果碰到了左边界就往右走
        if self.direction == "left":
            self.x -= 4
        elif self.direction == "right":
            self.x += 4

        if self.x > 400:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    # 控制敌方飞机发射子弹
    def shoot_bullet(self):
        num = random.randint(1, 60)
        if num == 33:
            new_bullet = Bullet(self.x, self.y, self.screen,"enemy")
            self.bulletList.append(new_bullet)

#定义子弹类
class Bullet(object):
    #定义子弹的初始化函数
    def __init__(self,x,y,screen,plane_name):
        self.name = plane_name
        self.screen = screen
        if self.name == "hero":
            self.x = x+40
            self.y = y-20
            image_name = "./feiji/bullet.png"
        elif self.name == "enemy":
            self.x = x + 30
            self.y = y + 30
            image_name = "./feiji/bullet1.png"
        self.image = pg.image.load(image_name)

    #定义子弹移动函数
    def move(self):
        if self.name == "hero":
            self.y -= 5
        elif self.name == "enemy":
            self.y += 4

    #显示飞机发射的子弹
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y < 0 or self.y>680:
            return True
        else:
            return False

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
    #创建一个敌方飞机
    enemy_plane = EnemyPlane(screen)
    #5、把背景图片放入到窗口中去显示
    while True:
        #设定需要显示的背景图
        screen.blit(background,(0,0))
        #设定显示玩家的飞机和敌方飞机
        hero.display()
        enemy_plane.display()
        #让敌方飞机移动
        enemy_plane.move()
        #敌方飞机发射子弹
        enemy_plane.shoot_bullet()
        # 判断是否按下按键或者点击退出按钮
        key_control(hero)
        # 更新需要显示的内容
        pg.display.update()
        #对程序运行进行延时
        time.sleep(0.01)

if __name__ == "__main__":
    main()
