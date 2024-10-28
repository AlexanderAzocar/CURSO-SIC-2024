import time

# Diccionario de usuarios anidado
users = {
    '123': {
        'name': 'Jenny',
        'cuenta': 'Ahorro',
        'saldo': 50000,
    },
    '456': {
        'name': 'Anderson',
        'cuenta': 'Corriente',
        'saldo': 2000,
    },
    '789': {
        'name': 'Diego',
        'cuenta': 'ahorro',
        'saldo': 100000,
    } 
}

# Función para verificar si el usuario existe
def verificar_usuario(registro, id_usuario):
    if id_usuario in registro:
        return registro[id_usuario]
    else:
        return None

# Función para mostrar el estado de cuenta
def edo_cuenta(us):
    return us['saldo']
# Función para hacer depósitos
def deposito(us, cant):
    us['saldo'] += cant
    return us['saldo']

# Función para hacer retiros
def retiro(us, cant):
    if cant > us['saldo']:
        return "Fondos insuficientes"
    us['saldo'] -= cant
    return us['saldo']

# Inicializar el número de intentos
intentos = 5

try:
    while intentos != 0:
        id_usuario = input('Ingrese su ID: ')
        
        # Verificar si el usuario existe
        usuario = verificar_usuario(users, id_usuario)
        
        if usuario is None:
            print('Clave errónea!')
            intentos -= 1
            if intentos == 2:
                print('Espere 10 segundos...')
                time.sleep(10)  # Espera 10 segundos tras varios intentos fallidos
        else:
            print(f"Bienvenido, {usuario['name']}")
            while True:
                # Menú de opciones
                opcion = int(input('''
                Seleccione la operación que desea realizar:
                1. Estado de Cuenta
                2. Depósito
                3. Retiro
                4. Salir
                Opción: '''))

                if opcion == 1:
                    print(f'Su saldo es: {edo_cuenta(usuario)}')
                    print(f'su cuenta es: {usuario['cuenta']}')
                elif opcion == 2:
                    monto = float(input('Ingrese el monto a depositar: '))
                    print(f'Saldo Final: {deposito(usuario, monto)}')
                elif opcion == 3:
                    monto = float(input('Ingrese el monto a retirar: '))
                    resultado_retiro = retiro(usuario, monto)
                    if resultado_retiro == "Fondos insuficientes":
                        print('Fondos insuficientes para realizar el retiro.')
                    else:
                        print(f'Saldo Final: {resultado_retiro}')
                elif opcion == 4:
                    print("Saliendo...")
                    break
                else:
                    print('Opción no válida, intente de nuevo.')
                    break
        if intentos == 0:
            print('Excedió el número de intentos, su cuenta ha sido bloqueada.')
            break

except:
    print(f'Ocurrió un error:')
