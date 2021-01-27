"""
重写坦克大战
坦克类：
属性：hp，图片，坐标，方向，速度
方法：move，发射，

子弹类：
属性：伤害
方法：move

墙类：
属性：hp
方法：block

老鹰类：
属性：hp
方法：

"""
import pygame
pygame.init()

WINDOW_W = 1200
WINDOW_H = 720
WINDOW = pygame.display.set_mode((WINDOW_W,WINDOW_H))   #创建窗口



class Tank:
    def __init__(self,x,y):
        self.hp = 1
        self.speed = 1
        self.direction = "U"
        self.image = pygame.image.load(f"images/enemy1{self.direction}.gif")

        #获取图片rect属性
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        if self.direction =="U":
            self.rect.y -=self.speed if self.rect.y >0 else 0
        if self.direction =="D":
            self.rect.y +=self.speed if self.rect.y <WINDOW_H-60 else 0
        if self.direction =="R":
            self.rect.x += self.speed if self.rect.x <WINDOW_W-60 else 0
        if self.direction =="L":
            self.rect.x -=self.speed if self.rect.x >0 else 0

    def fire(self):
        pass

class Bullet:
    def __init__(self):
        self.伤害 = 1

    def move(self):
        pass

class Wall:
    def __init__(self):
        self.hp = 3

    def block(self):
        pass

class Eagle:
    def __init__(self):
        self.hp = 1

class Game:
    def __init__(self):
        # 设置窗口标题
        pygame.display.set_caption("重写坦克大战")
        # 设置logo图标
        logo = pygame.image.load("images/222.jpg")
        pygame.display.set_icon(logo)

        #加载背景图
        self.bg_img = pygame.image.load("images/111魁拔.jpg")

        #创建坦克
        self.tank = Tank(500,500)

    def draw(self):
        """贴图"""
        #贴背景图
        WINDOW.blit(self.bg_img,(0,0))
        #贴坦克图
        WINDOW.blit(self.tank.image,(self.tank.rect.x,self.tank.rect.y))

    def move(self):
        #元素移动
        self.tank.move()

    def update(self):
        #刷新界面
        pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            #1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("点击关闭窗口按钮")
                exit()    #关闭程序

    def run(self):
        while True:
            #贴图
            self.draw()
            # 调用事件
            self.event()
            #调用移动方法
            self.move()
            #刷新
            self.update()


tankgame = Game()
tankgame.run()