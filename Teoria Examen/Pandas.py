import pandas as pd
import mainpandas

#df = pd.read_csv("Pima_tr.csv")
#print(df)
#df.rename(columns={"Unnamed: 0": "id"}) #cambiar nombre de una columna, pero esto no lo cambia realmente tal y como estamos, necesita que variable = df.rename...
df = pd.read_csv("Pima_tr.csv")
df = df.rename(columns={"Unnamed: 0": "id"})
#print(df)

#para aceder a los valores de una columna:
ped = df['ped']
#print(ped)

#para aceder a los valores de una column:
one_row = df.loc[0]
five_rows = df.loc[0:5] #DANGER, aqui imprimimos de 0 a 5, no de 0 a 4 como estamos acostumrbados
#print(one_row)
#print(five_rows)
#print(dict(one_row)) puedes hacer esto y crear un dict facil y sencillo de la column que quieras

#para saber que columnas tenemos (el header):
#print(df.columns) #para tener una lista en condiciones --> print(list(df.columns))

#para acceder a las rows y filtrar valores:
by_type = df.loc[df['type'] == 'Yes']
by_npreg = df.loc[df['npreg'] > 5] #para hacer un rango, es 3 < df['npreg'] > 5, nada de and o or, o poner las condiciones que quieras en parentesis y dividarlas con un & y or con |
#print(by_type)

#para ver el type de las columnas:
#print(df.dtypes)

#para cambiar el type de una columna:
df.npreg = df.npreg.astype(float)
#print(df)

#para contar los valores de una columna:
counter = df['type'].value_counts()
print(counter)
#te imprime todos los valores DIFERENTES (si hay dos iguales solo imprime uno) y el numero de veces que se repite cada uno
#para que todos los valores se queden guardados en una lista:
counter_list = counter.index #sin parentesis --> index() nop
print(counter_list)
#entonces, si haces counter_list = len(counter.index), te dara el numero total de valores que tienes pero sin repetirse, como un len(set(... que usabamos

#print(list(df.index))

result = mainpandas.calculate_2(df['type'])
#print(mainpandas.print_values(result))

#para ordenar rows according yo certain column
ordered_by_age = df.sort_values(by = ['age'], ascending=False) #esto ultimo hace que vaya de mayor a menor, si eso va de menor a mayor
#print(ordered_by_age)

#borrar columnas:
delate_type = df.drop(['type'], axis=1) #esto ultimo es para decirle que estamos borrando columnas, no rows
#print(delate_type)

#borrar rows:
delate_row = df.drop([0])
#print(delate_row)

delate_type.to_csv("Pima_wo_type.csv") #te crea un csv sin la columna que hemos quitado
delate_type.to_html("Pima_wo_type.html")








































