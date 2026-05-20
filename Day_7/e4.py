import random

def generate_colors(type,amount):
    colors = []
    for i in range(amount):
      if type == 'rgb':
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        colors.append(f"rgb({r},{g},{b})")

      elif type == 'hexa':
        hex_chars = '0123456789abcdef'
        color = '#'
        for j in range(6):
            color += random.choice(hex_chars)
            colors.append(color)
    return colors

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))

print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
