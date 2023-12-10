with open("C:/Users/PC/Desktop/adventcode/1/a.txt", 'r') as data_file:
    data = data_file.readlines()

def function(a):
    current_list = []
    for i in data[a]:
        try:
            int(i)
            current_list.append(i)
        except ValueError:
            pass

    len_lista = len(current_list)
    lista_concatenada_final = [int(str(current_list[0]) + str(current_list[len_lista-1]))]
    lista_concatenada_final = int(lista_concatenada_final[0])
    return lista_concatenada_final

lista_sumatoria = []

for k in range(0, 1000, 1):
    lista_sumatoria.append(function(k))

print(lista_sumatoria)
print(sum(lista_sumatoria))