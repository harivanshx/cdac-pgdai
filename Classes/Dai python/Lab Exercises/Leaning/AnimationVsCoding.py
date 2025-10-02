
# # b = "string"
# # a = b[0:2]
# # for i in b:
# #     print(i)
# # print(a)
# # print("Hello World")



# # a = "1234"
# # while not a.isprintable():
# #     print(a.upper())
# # else:
# #     print(a)



# # bomb = ['Bang' , 'BOOM','BAM','Pow','Poof','Pah']

# # print(*bomb)
# # print(*bomb)
# # print(*bomb)

# # # import turtle 
# # # t = turtle.Turtle()
# # # t.speed("fastest")
# # # t.pensize(10)
# # # while True:

# # #     t.right(170)
# # #     t.forward(400)
# # #     t.left(170)
# # #     t.forward(400)
# # #     turtle.bye()


# # import string as ammo 
# # gun = list(ammo.ascii_uppercase)
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())
# # print(gun.pop())



# # import matplotlib.pyplot as plt
# # import numpy as np
# # val =  np.random.randint(1,10,5)
# # plt.errorbar(range(len(val)),val,val,fmt='o',capsize=6)
# # # plt.bar(range(len(val)),val)
# # plt.plot(range(20),color='red')
# # plt.title(label='Title',fontsize=20,rotation = 90,loc='right')
# # x = np.arange(0,30,0.1)
# # y= np.cos(x)
# # plt.plot(x,y)
# # plt.show()

# # import pygame
# # pygame.init()
# # screen = pygame.display.set_mode((4000,2000))
# # clock = pygame.time.Clock()
# # square_pos = pygame.Rect(1920,1080,50,50)
# # circle_pos = pygame.Vector2(1200,900)
# # circle_spd = pygame.Vector2()
# # circle_rad = 0.20
# # circle_acc = 0.01
# # circle_spd_mul = 0.99
# # bounce_str= 1.0


# # while True:
# #     if pygame.event.get(pygame.QUIT): break
# #     keys = pygame.key.get_pressed()
# #     if keys[pygame.K_UP]:
# #         square_pos.y -=5
# #     if keys[pygame.K_DOWN]:
# #         square_pos.y +=5
# #     if keys[pygame.K_LEFT]:
# #         square_pos.x -=5
# #     if keys[pygame.K_RIGHT]:
# #         square_pos.x +=5
    
# #     circle_spd *= circle_spd_mul
# #     circle_spd += (yellow.get_pos()-circle_pos)*circle_acc
# #     screen.fill("black")
# #     pygame.draw.rect(screen,"red", square_pos)
# #     pygame.display.flip()
# #     clock.tick()
# # pygame.quit()





import pygame

pygame.init()
screen = pygame.display.set_mode((4000, 2000))
clock = pygame.time.Clock()

square_pos = pygame.Rect(1920, 1080, 50, 50)
circle_pos = pygame.Vector2(1500, 1500)
circle_spd = pygame.Vector2()
circle_rad = 5
circle_acc = 0.01
circle_spd_mul = 0.99
bounce_str = 1.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square_pos.y -= 20
    if keys[pygame.K_DOWN]:
        square_pos.y += 20
    if keys[pygame.K_LEFT]:
        square_pos.x -= 20
    if keys[pygame.K_RIGHT]:
        square_pos.x += 20

    circle_spd += (pygame.Vector2(square_pos.center) - circle_pos) * circle_acc
    circle_pos += circle_spd
    circle_spd[0] *= circle_spd_mul
    circle_spd[1] *= circle_spd_mul

    if circle_pos[0] < circle_rad or circle_pos[0] > screen.get_width() - circle_rad:
        circle_spd[0] = -circle_spd[0] * bounce_str
        circle_pos[0] = max(circle_rad, min(screen.get_width() - circle_rad, circle_pos[0]))

    if circle_pos[1] < circle_rad or circle_pos[1] > screen.get_height() - circle_rad:
        circle_spd[1] = -circle_spd[1] * bounce_str
        circle_pos[1] = max(circle_rad, min(screen.get_height() - circle_rad, circle_pos[1]))

    screen.fill("black")
    pygame.draw.rect(screen, "red", square_pos)
    pygame.draw.circle(screen, "yellow", circle_pos, circle_rad)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()




list = [1,2,3,4,5,6,7]
# sum = 0 
# for i in list:
#     sum += i


# print(sum)


# Q2: Write a Python program to get the largest number from a list.

# largest = 0

# for i in list:
#     if i >= largest:
#         largest = i

# print(largest)

# import sys
# smallest = sys.maxsize
# for i in list:
#     if i <= smallest:
#         smallest = i


# print(smallest)


# Q4: Write a Python program to display the first and last colors from the following list.
#  color_list = ["Red","Gree

# color_list = ["Red","Green","White" ,"Black"]

# print(color_list[0],color_list[-1])






import pandas as pd

# data in dictionary format
data = {
    "Name": ["Ravi", "Meera", "Arjun"],
    "Age": [10, 12, 11],
    "Favorite Color": ["Blue", "Red", "Green"]
}

# creating the DataFrame
df = pd.DataFrame(data)

# showing the table
print(df)
