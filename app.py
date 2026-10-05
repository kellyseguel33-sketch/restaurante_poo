from presentacion.menu import cargar_menu
#cargar_menu()

from datos.repositorios.repo_cliente import listado_cliente
from prettytable import PrettyTable

tabla_clientes = PrettyTable()
clientes = listado_cliente()