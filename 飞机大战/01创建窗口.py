#coding:utf-8
import pygame as pg
'''
    搭建界面 用于完成窗口和背景的显示
'''
def main():
    #1、创建一个窗口，用来显示内容  480*852的分辨率
    screen = pg.display.set_mode((480, 852), 0, 32)
    #2、创建一个和窗口大小一致的图片，用来充当背景
    background = pg.image.load("./feiji/background.png")
    #3、把背景图片放入到窗口中去显示
    while True:
        #设定需要显示的背景图
        screen.blit(background,(0,0))
        #更新需要显示的内容
        pg.display.update()
        #设置程序退出
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

if __name__ == "__main__":
    main()
