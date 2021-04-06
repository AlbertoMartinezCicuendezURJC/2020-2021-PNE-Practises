import pandas

def calculate(column):
    number_values = len(column.value_counts())
    if number_values == 2:
        result = column.value_counts()
        indexes = result.index
        return indexes, result[indexes[0]], result[indexes[1]] #result[indexes[0]], result[indexes[1]] es para acceder a los contadores de cada valor diferente, en vez de cada valor
#or

def calculate_2(column):
    number_values = len(column.value_counts())
    if number_values == 2:
        return column.value_counts()
    else:
        return column.mean(), column.median(), column.max(), column.min()

def print_values(result):
    if len(result) == 2:
        for index, row in result.items():
            print("The value is: " + str(index) + " and the repetitions are: " + str(row))

    else:
        print("The value is: ", result[0])
        print("The value is: ", result[1])
        print("The value is: ", result[2])
        print("The value is: ", result[3])



