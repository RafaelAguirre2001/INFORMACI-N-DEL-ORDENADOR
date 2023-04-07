#vamos a sacar las caracteristicas de nuestra pc con python
#bien comenzamos importando la libreria platform

import platform

# vamos a obtener la informacion del sistema operativo

operating_system = platform.system()

# ahora obtendremos el nombre de la computadora

node_name = platform.node()

# ahora tambien queremos el nombre de la version del sistema operativo
operating_system_version = platform.version()

# obtendremos aqui la informacion del procesador en este caso su arquitectura

processor_architecture =platform.machine()

# ahora obtendremos info sobre el procesador pero ya de forma mas detallada

processor_details = platform.processor()
#imprimimos los resutados

print("Sistema Operativo: ", operating_system)
print("Nombre del nodo : ", node_name)
print("version del sistema operativo: ", operating_system_version)
print("Arquitectura del procesador: ", processor_architecture)
print("Detalle del procesador : ", processor_details )

# por ultimo probamos nuestro codigo :D