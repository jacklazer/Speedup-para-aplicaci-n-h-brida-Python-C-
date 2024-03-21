import ctypes

vector = [1.0, 2.0, 3.0]
scalar = 2.0
result = [0.0, 0.0, 0.0]
length = len(vector)

# fun = ctypes.CDLL("c:/Users/juanc/Desktop/Codigos/Codigos de la universidad/Infraestructuras paralelas y distribuidas/Speedup para aplicación híbrida (Python + C)/multescalar-avx.so")
# fun = ctypes.CDLL("/Users/juanc/Desktop/Codigos/Codigos de la universidad/Infraestructuras paralelas y distribuidas/Speedup para aplicación híbrida (Python + C)/multescalar-avx.so")
fun = ctypes.CDLL("./multescalar-avx.so")
# fun = ctypes.CDLL("/multescalar-avx.so")
# fun = ctypes.CDLL("multescalar-avx.so")

# fun = ctypes.CDLL("./multescalar-avx.dll")


fun.vectorScalarMultiply(vector, scalar, result, length)


##################################################################
##################################################################
##################################################################
##################################################################


# import ctypes

# # Cargar la biblioteca compartida
# libreria = ctypes.CDLL('./multescalar-avx.so')

# # Definir el tipo de los argumentos de la función
# libreria.vectorScalarMultiply.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int]

# # Llamar a la función
# vector = [1.0, 2.0, 3.0]  # Vector de ejemplo
# scalar = 2.0
# result = [0.0, 0.0, 0.0]  # Vector para almacenar el resultado
# length = len(vector)

# # Convertir los argumentos de Python a tipos C
# vector_c = (ctypes.c_double * length)(*vector)
# scalar_c = ctypes.c_double(scalar)
# result_c = (ctypes.c_double * length)(*result)
# length_c = ctypes.c_int(length)

# # Invocar la función
# libreria.vectorScalarMultiply(vector_c, scalar_c, result_c, length_c)

# # Imprimir el resultado
# resultado_python = list(result_c)
# print("Resultado desde Python:", resultado_python)
