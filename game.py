import pygame
import random
import time 

pygame.init()


def game_func():
    pygame.mixer.music.load("colt.mp3")
    pygame.mixer.music.play()
    sound = pygame.mixer.Sound("anime.mp3")
    # змінна для створення таймеру
    start_time = time.time() 

    # список для збереження кольорів пуль
    colors = [(255,0,0),(0,255,0),(0,0,255)]

    # Ініціалізація вікна та кольорів
    back = (255, 229, 173)
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Shooter Game")
    window.fill(back)
    pygame.display.update()


    class Area():
        def __init__(self, x=0, y=0, width=10, height=10, color=None):
            self.rect = pygame.Rect(x, y, width, height)
            self.fill_color = back
            if color:
                self.fill_color = color

        def color(self, new_color):
            self.fill_color = new_color

        def fill(self):
            pygame.draw.rect(window, self.fill_color, self.rect)

        def collidepoint(self, x, y):
            return self.rect.collidepoint(x, y)

        def colliderect(self, rect):
            return self.rect.colliderect(rect)


            
    # Клас Picture
    class Picture(Area):
        def __init__(self, filename, x=0, y=0, width=10, height=10):
            Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
            self.image = pygame.image.load(filename)

        def draw(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

    # Клас Bullet (пуля)

    class Bullet(Area):
        def __init__(self, x, y, w, h, color):
            super().__init__(x, y, w, h, color)
            self.speed = 10

        def move(self):
            self.rect.y -= self.speed

    move_r = False
    move_l = False
    move_u = False
    move_d = False



    # Створення ворогів
    balls = []
    x = 0
    for _ in range(16):
        y = 10
        enemy = Picture('ball.png', x, y, 40, 30)
        balls.append(enemy)
        x = x + 30

    enemies = []
    x = 0
    for _ in range(16):
        y = 60
        enemy = Picture('tennis.png', x, y, 40, 30)
        enemies.append(enemy)
        x = x + 30

    blue = []
    x = 0
    for _ in range(16):
        y = 110
        enemy = Picture('blue.png', x, y, 40, 30)
        blue.append(enemy)
        x = x + 30

    # Створення гравця
    pushka = Picture('pushka.png', 200, 400, 50, 50)

    # Створення об'єктів для тексту
    f = pygame.font.Font(None,30) 
    f2 = pygame.font.Font(None,60) 

    # Створення гри
    clock = pygame.time.Clock()

    # списки для збереження пуль
    bullets = []
    bullets1 = []
    bullets2 = []

    score = 0 # змінна для рахунку
    s = 0 #сума пуль

    # генерація випадкового кольору
    color_name = ''
    choise = random.choice(colors)
    if choise == (255,0,0):
        color_name = 'червоний'
    elif choise == (0,255,0):
        color_name = 'зелений'
    elif choise == (0,0,255):
        color_name = 'синій'

    game = True
    while game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_d:
                    move_r = True
                if e.key == pygame.K_a:
                    move_l = True
                if e.key == pygame.K_r:
                    choise = random.choice(colors)
                if choise == (255,0,0):
                    color_name = 'червоний'
                elif choise == (0,255,0):
                    color_name = 'зелений'
                elif choise == (0,0,255):
                    color_name = 'синій'
                if e.key == pygame.K_SPACE:
                    sound.play()
                    bullet = Bullet(pushka.rect.centerx, pushka.rect.y,5,10,choise)
                    if choise == (255,0,0):
                        bullets.append(bullet)
                        s += 1
                    elif choise == (0,255,0):
                        bullets1.append(bullet)
                    elif choise == (0,0,255):
                        bullets2.append(bullet)
                    choise = random.choice(colors)
                    if choise == (255,0,0):
                        color_name = 'червоний'
                    elif choise == (0,255,0):
                        color_name = 'зелений'
                    elif choise == (0,0,255):
                        color_name = 'синій'

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_d:
                    move_r = False
                if e.key == pygame.K_a:
                    move_l = False
            
        
        if move_r:
            pushka.rect.x += 10
        if move_l:
            pushka.rect.x -= 10

        # умови програшу та виграшу
        if score < -4:
            fame = f2.render('Поразка', True, (1, 1, 1))
            b = f2.render(f'Рахунок: {score}', True, (1,1,1))
            window.fill(back)
            window.blit(b,(150,240))   
            window.blit(fame, (175, 200))
            pygame.display.update()
            pygame.time.delay(3000)  # Затримка 3 секунди перед завершенням гри
            game = False  # Зупиняємо гру

        suma = len(enemies) + len(blue) + len(balls)
        if suma == 0:
            fame = f2.render('Перемога', True, (1, 1, 1))
            b = f2.render(f'Рахунок: {score}', True, (1,1,1))
            window.fill(back)
            window.blit(b,(150,240))   
            window.blit(fame, (175, 200))
            pygame.display.update()
            pygame.time.delay(3000)  # Затримка 3 секунди перед завершенням гри
            game = False  # Зупиняємо гру
        



        # Рух пуль
        for bullet in bullets:
            bullet.move()
        for bullet1 in bullets1:
            bullet1.move()
        for bullet2 in bullets2:
            bullet2.move()
        # Видалення пуль, які виходять за межі екрану
        bullets = [bullet for bullet in bullets if bullet.rect.y > 0]
        
        bullets1 = [bullet1 for bullet1 in bullets1 if bullet1.rect.y > 0]

        bullets2 = [bullet2 for bullet2 in bullets2 if bullet2.rect.y > 0]

        # Видалення ворогів, які зіштовхуються з пулями
        for enemy in enemies:
            for bullet1 in bullets1:
                if enemy.rect.colliderect(bullet1.rect):
                    enemies.remove(enemy)
                    bullets1.remove(bullet1)
                    score += 1

        for enemy in blue:
            for bullet2 in bullets2:
                if enemy.rect.colliderect(bullet2.rect):
                    blue.remove(enemy)
                    bullets2.remove(bullet2)
                    score += 1

        for enemy in balls:
            for bullet in bullets:
                if enemy.rect.colliderect(bullet.rect):
                    balls.remove(enemy)
                    bullets.remove(bullet)
                    score += 1
        # видаллення пуль які попали не в свій колір
        for enemy in enemies:
            for bullet in bullets:
                if enemy.rect.colliderect(bullet.rect):
                    bullets.remove(bullet)
                    score -= 1

        for enemy in enemies:
            for bullet2 in bullets2:
                if enemy.rect.colliderect(bullet2.rect):
                    bullets2.remove(bullet2)
                    score -= 1


        for enemy in blue:
            for bullet in bullets:
                if enemy.rect.colliderect(bullet.rect):
                    bullets.remove(bullet)
                    score -= 1

        for enemy in blue:
            for bullet1 in bullets1:
                if enemy.rect.colliderect(bullet1.rect):
                    bullets1.remove(bullet1)
                    score -= 1

        for enemy in balls:
            for bullet1 in bullets1:
                if enemy.rect.colliderect(bullet1.rect):
                    bullets1.remove(bullet1)
                    score -= 1


        for enemy in balls:
            for bullet2 in bullets2:
                if enemy.rect.colliderect(bullet2.rect):
                    bullets2.remove(bullet2)
                    score -= 1           
        # Відображення гравця, ворогів і пуль
        window.fill(back)
        for enemy in enemies:
            enemy.draw()
        for b in balls:
            b.draw()
        for enemy in blue:
            enemy.draw()
        for bullet in bullets:
            bullet.fill()
        for bullet1 in bullets1:
            bullet1.fill()
        for bullet2 in bullets2:
            bullet2.fill()
    
        #відображення тексту
        
        b = f.render(f'Рахунок: {score}', True, (1,1,1)) 
        window.blit(b,(10,210))    
        t = int(time.time() - start_time) 
        time_text = f.render(f'Час {t} секунд', True, (1,1,1)) 
        window.blit(time_text,(10,240)) 
        next_color = f.render(f'Випущені пулі: {color_name}', True, (1,1,1)) 
        window.blit(next_color,(10,270)) 

        pushka.fill()
        pushka.draw()

        pygame.display.update()
        clock.tick(50)
