from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['Post'])
def cliente_ci():
    ci = request.json.get('ci')
    print("Headers:", request.headers)
    print(f"Buscando el cliente con CI: {ci}...")

    codRes, menRes, accion, data = inicializarVariables(ci)

    salida = {
        "codRes": codRes,
        "menRes": menRes,
        "accion": accion,
        "ci": ci
    }

    if data:
        salida.update(data)

    return jsonify(salida)

# return jsonify(salida, salida)

def inicializarVariables(ci):
    clientes = {
        "6513401": {
            "nombre": "Miguel Angel",
            "apellidos": "Paniagua Leiva",
            "cel": "0983453104",
            "dir": "Barrio Obrero"
        }
    }

    codRes = "SIN_ERROR"
    menRes = "OK"
    accion = "Success"
    data = None

    try:
        print("Buscando cliente...")
        if ci in clientes:
            print("Cliente encontrado")
            data = clientes[ci]
        else:
            print("Cliente no encontrado")
            codRes = "ERROR"
            menRes = "Error cliente"
            accion = "Cliente no está en el sistema"
    except Exception as e:
        print("ERROR:", str(e))
        codRes = "ERROR"
        menRes = f"Msg: {str(e)}"
        accion = "Error interno"

    return codRes, menRes, accion, data
