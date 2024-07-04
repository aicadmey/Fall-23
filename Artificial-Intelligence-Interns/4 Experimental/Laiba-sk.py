x1 = 0.5
x2 = 0.7
x3 = 0.8
x4 = 0.9
x5 = 0.2

w1 = 1
w2 = 2
w3 = 3
w4 = 4
w5 = 5
w6 = 6
w7 = 7
w8 = 8
w9 = 9
w10 = 2
w11 = 3
w12 = 5
w13 = 9
w14 = 3
w15 = 1
w16 = 9
w17 = 3
w18 = 8
w19 = 1
w20 = 5
w21 = 4
w22 = 3
w23 = 8

# Bias term
bias = 10  # Adjust the bias value as needed

c1 = x1 * w1 + x2 * w4 + x3 * w7 + x4 * w10 + x5 * w13 + bias
c2 = x1 * w2 + x2 * w5 + x3 * w8 + x4 * w11 + x5 * w14 + bias
c3 = x1 * w3 + x2 * w6 + x3 * w9 + x4 * w12 + x5 * w15 + bias
print("C1 value: ", c1)
print("C2 value: ", c2)
print("C3 value: ", c3)

y1 = c1 * w16 + c2 * w18 + c3 * w20 + bias
y2 = c1 * w17 + c2 * w19 + c3 * w21 + bias

print("Y1 value: ", y1)
print("Y2 value: ", y2)

z = y1 * w22 + y2 * w23 + bias
print("The Final value is: ", z)

if z > 100:
    print("z is greater than 100")
elif z < 0:
    print("z is less than 0")
else:
    print("z is between 0 and 100")
