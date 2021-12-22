import matplotlib.pyplot as plt
import termcolor

repetition = 2000
a = 7**5
b = 0
m = 2**31 - 1

numbers_generated = []
y2 = []
z = []

def method_lcg():
    seed_number = 1
    for i in range(0, repetition):
        rn = (a * seed_number + b) % m
        numbers_generated.append(rn)
        seed_number = rn
        rn2 = (a * seed_number + b) % m
        y2.append(rn2)
        rn3 = (a * rn2 + b) % m
        z.append(rn3)

method_lcg()

termcolor.cprint('The random numbers generated are:', 'cyan')
print(numbers_generated)

termcolor.cprint('===========================================', 'green')

termcolor.cprint('The random numbers + 1 are:', 'cyan')
print(y2)

termcolor.cprint('===========================================', 'green')

termcolor.cprint('The random numbers + 2 are:', 'cyan')
print(z)

y = numbers_generated
x = []
i = 0
for number in numbers_generated:
    i += 1
    x.append(i)


plt.scatter(x, y)
plt.show()

ordered_numbers = sorted(numbers_generated)
counter = 0
variable = 100000000000
non_repeated_value = []
for numb in ordered_numbers:
    if numb != variable:
        counter += 1
        variable = numb
        non_repeated_value.append(numb)
    else:
        pass


termcolor.cprint('===========================================', 'green')

termcolor.cprint('The number of different values is:', 'cyan')
print(counter)



plt.scatter(numbers_generated, y2)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

ax1.scatter(numbers_generated, y2, z, c='g', marker='o')
ax1.view_init(-140, 60)
plt.show()