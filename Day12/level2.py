import random
def list_of_hexa(amount = 1):
    hexa = []
    for i in range(0,amount,1):
        hexa.append('#' + '%06x' % random.randint(0, 0xFFFFFF))
    return hexa

def list_of_rgb_color(amount = 1):
    rgb = list()
    for i in range(0,amount,1):
        color1 = random.randrange(0,255)
        color2 = random.randrange(0,255)
        color3 = random.randrange(0,255)
        rgb.append('rgb ({},{},{})'.format(color1,color2,color3))
    return rgb

def generate_colors():
    amount = random.randint(1,100)
    print(amount)
    if amount % 2 == 0:
        return list_of_hexa(amount)
    else:
        return list_of_rgb_color(amount)