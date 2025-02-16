import turtle
import random

w = 500
h = 500
fs = 10
d = 100


offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


direction_angles = {
    "up": 90,
    "down": 270,
    "left": 180,
    "right": 0
}


def r():
    global snake, direction, food_pos, cam
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    direction = "up"
    food_pos = generate_food_position()
    food.goto(food_pos)
    game_loop()


def game_loop():
    global direction

    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[direction][0]
    new_head[1] = snake[-1][1] + offsets[direction][1]

    if new_head in snake[:-1]:
        r()
    else:
        snake.append(new_head)

        if not check_food_collision():
            snake.pop(0)

        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < -w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

        cam.clearstamps()


        cam.shape("triangle")
        cam.color("black")
        cam.shapesize(1.5, 1.5)
        cam.setheading(direction_angles[direction])
        cam.goto(snake[-1][0], snake[-1][1])
        cam.stamp()


        for i in range(len(snake) - 1):
            cam.shape("circle")
            if i % 2 == 0:
                cam.color("black")
            else:
                cam.color("white")
            cam.shapesize(0.7, 0.7)
            cam.goto(snake[i][0], snake[i][1])
            cam.stamp()

        screen.update()
        turtle.ontimer(game_loop, d)


def check_food_collision():
    global food_pos
    if calculate_distance(snake[-1], food_pos) < 20:
        food_pos = generate_food_position()
        food.goto(food_pos)
        return True
    return False


def generate_food_position():
    x = random.randint(-w / 2 + fs, w / 2 - fs)
    y = random.randint(-h / 2 + fs, h / 2 - fs)
    return (x, y)


def calculate_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


def move_up():
    global direction
    if direction != "down":
        direction = "up"


def move_right():
    global direction
    if direction != "left":
        direction = "right"


def move_down():
    global direction
    if direction != "up":
        direction = "down"


def move_left():
    global direction
    if direction != "right":
        direction = "left"


screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake Game")
screen.bgcolor("#343a40")
screen.tracer(0)

cam = turtle.Turtle()
cam.penup()
cam.speed(0)

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(fs / 20)
food.penup()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")

r()
turtle.done()