# servers do not connect with anything, only clients do
# well-known-port: puertos que se usan si no das ningun puerto cuando ponwe www.noseque... 80 es el mas comun
# el sistema operativo le da un random port al client
# si pones exit() y lo paras manualmente, te saldra -1, lo que significa que no ha funcionado bien. Con break te sale 0, osea que guay.
# si sale 1, eso significa que se ha cerrado por una excepcion, rollo un ValueError
# resumen: 0 esto funciona guay, -1 es algo manual y 1 es por un fallo
