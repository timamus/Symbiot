import pyautogui
import time
import random
from random import randint, choice
from math import ceil


def pascal_row(n):
    # This returns the nth row of Pascal's Triangle
    result = [1]
    x, numerator = 1, n
    for denominator in range(1, n//2+1):
        # print(numerator,denominator,x)
        x *= numerator
        x /= denominator
        result.append(x)
        numerator -= 1
    if n & 1 == 0:
        # n is even
        result.extend(reversed(result[:-1]))
    else:
        result.extend(reversed(result))
    return result


def make_bezier(xys):
    # xys should be a sequence of 2-tuples (Bezier control points)
    n = len(xys)
    combinations = pascal_row(n - 1)

    def bezier(ts):
        # This uses the generalized formula for bezier curves
        # http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization
        result = []
        for t in ts:
            tpowers = (t**i for i in range(n))
            upowers = reversed([(1-t)**i for i in range(n)])
            coefs = [c*a*b for c, a, b in zip(combinations, tpowers, upowers)]
            result.append(
                list(sum([coef*p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))
        return result
    return bezier


def mouse_bez(init_pos, fin_pos, deviation, speed):
    '''
    GENERATE BEZIER CURVE POINTS
    Takes init_pos and fin_pos as a 2-tuple representing xy coordinates
        variation is a 2-tuple representing the
        max distance from fin_pos of control point for x and y respectively
        speed is an int multiplier for speed. The lower, the faster. 1 is fastest.

    '''

    # time parameter
    ts = [t / (speed * 100.0) for t in range(speed * 101)]

    # bezier centre control points between (deviation / 2) and (deviaion) of travel distance, plus or minus at random
    control_1 = (
        init_pos[0] + choice((-1, 1)) * abs(ceil(fin_pos[0]) - ceil(init_pos[0])) * 0.01 * randint(deviation / 2,
                                                                                                   deviation),
        init_pos[1] + choice((-1, 1)) * abs(ceil(fin_pos[1]) -
                                            ceil(init_pos[1])) * 0.01 * randint(deviation / 2, deviation)
    )
    control_2 = (
        init_pos[0] + choice((-1, 1)) * abs(ceil(fin_pos[0]) - ceil(init_pos[0])) * 0.01 * randint(deviation / 2,
                                                                                                   deviation),
        init_pos[1] + choice((-1, 1)) * abs(ceil(fin_pos[1]) -
                                            ceil(init_pos[1])) * 0.01 * randint(deviation / 2, deviation)
    )

    xys = [init_pos, control_1, control_2, fin_pos]
    bezier = make_bezier(xys)
    points = bezier(ts)

    return points


def random_mouse_move(field_width=200, field_height=200, duration_seconds=60):
    '''
    :param field_width: your screen width
    :param field_height: your screen height
    :param hours: How many hours will the mouse move
    '''
    # Define center of screen and field size
    center_x, center_y = pyautogui.size(
    )[0] // 2, pyautogui.size()[1] // 2  # Detect screen center

    # Previous point, the first value is the center of the field
    old_point = [center_x, center_y]
    interval = 0  # Interval when fast move apply

    t_end = time.time() + duration_seconds
    while time.time() < t_end:
        interval += 1
        
        # Generate random point using random.random()
        random_point = [random.random(), random.random()]
        point = [random_point[0] * field_width + center_x - field_width // 2,
                 random_point[1] * field_height + center_y - field_height // 2]

        point1 = [round(old_point[0]), round(old_point[1])]
        point2 = [round(point[0]), round(point[1])]

        # Get an array of points of the Bezier curve
        points = mouse_bez(point1, point2, 2, 1)

        if interval < 3:
            for x in points:
                pyautogui.moveTo(x[0], x[1])
        else:
            # Move mouse cursor to point quickly
            pyautogui.moveTo(point[0], point[1], duration=0.5)
            interval = 0

        old_point = point  # Remember previous point
        
        #time.sleep(0.5)  # задержка в полсекунды
        pyautogui.click()  # click the mouse
        # pyautogui.scroll(randint(1, 10))  # scroll up 10 "clicks"
        # pyautogui.scroll(-randint(1, 4))  # scroll down 4 "clicks"

        # Pause briefly to simulate human behavior
        time.sleep(random.uniform(0.4, 0.6))
