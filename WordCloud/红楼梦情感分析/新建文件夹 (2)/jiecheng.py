'''def jie(a):
    if (a==0):
        return 1
    else:
        return a*jie(a-1)

n = eval(input("请输入一个整数："))
print(jie(n))
'''

'''dict = {'name':'robot','age':'99'}
print(dict['name'])
'''
import turtle

def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [00,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    turtle.setup(600,600)
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level=4
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    koch(400,level)
    turtle.left(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    koch(400,level)
    turtle.left(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
main()
