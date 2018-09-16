


x = [2, 3, 5, 8]
y = [2, 4, 7, 6, 5]

z = []


for s in y:
    x_el = 0
    try:
        if y.index(s) < len(x):
            x_el = x[y.index(s)]
    except:
        x_el = 0

    r = s * x_el

    z.append(r)

print(z)


