import numpy as np
from pathlib import Path

def read_text(filename):
    sequence = Path(filename).read_text()
    sequence = sequence.replace('\n', ' ').split(' ')
    return sequence

FOLDER = './File/'
ID = 'implant'
var = read_text(FOLDER + ID)

float_var = []
for number in var:
    number = float(number)
    float_var.append(number)


mean = np.mean(float_var)

summation = 0
index = 0
for numb in float_var:
    addition = (float_var[index] - mean) ** 2
    summation += addition
    index += 1

sample_variance = summation/(index-1)

