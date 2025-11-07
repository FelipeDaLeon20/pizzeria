from flask import Flask, render_template as render, request, redirect, make_response
from forms import PizzaForm
import json
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-segura'


@app.route('/index', methods=['GET', 'POST'])
def home():
    form = PizzaForm()
    pedidos = []
    ventas = []
    total_general = 0

    
    pedidos_cookie = request.cookies.get('pedidos')
    ventas_cookie = request.cookies.get('cookie_ventas')

    if pedidos_cookie:
        pedidos = json.loads(pedidos_cookie)
    if ventas_cookie:
        ventas = json.loads(ventas_cookie)

    
    if form.validate_on_submit():
        nombre = form.nombre.data
        direccion = form.direccion.data
        telefono = form.telefono.data
        tamano = form.tamano.data
        numero = form.numero.data
        ingredientes = []
        precioT = 0
        precioI = 0

        
        if tamano == 'chica':
            precioT = 40
        elif tamano == 'mediana':
            precioT = 80
        else:
            precioT = 120

        
        if form.jamon.data:
            precioI += 10
            ingredientes.append('Jamón')
        if form.pina.data:
            precioI += 10
            ingredientes.append('Piña')
        if form.champinones.data:
            precioI += 10
            ingredientes.append('Champiñones')

        total = (precioT + precioI) * numero

        
        pedido = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'tamano': tamano,
            'ingredientes': ingredientes,
            'numero': numero,
            'total': total
        }

        pedidos.append(pedido)

        
        resp = make_response(redirect('/index'))
        resp.set_cookie('pedidos', json.dumps(pedidos))
        return resp

    
    if request.args.get('eliminar'):
        indice = int(request.args.get('eliminar'))
        if 0 <= indice < len(pedidos):
            pedidos.pop(indice)
        resp = make_response(redirect('/index'))
        resp.set_cookie('pedidos', json.dumps(pedidos))
        return resp

    
    if request.args.get('terminar'):
        if pedidos:
            total_general = sum(p['total'] for p in pedidos)
            fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            
            venta = {
                'nombre': pedidos[-1]['nombre'],
                'direccion': pedidos[-1]['direccion'],
                'telefono': pedidos[-1]['telefono'],
                'fecha': fecha,
                'total': total_general
            }
            ventas.append(venta)

            
            resp = make_response(redirect('/index'))
            resp.set_cookie('cookie_ventas', json.dumps(ventas))
            resp.set_cookie('pedidos', json.dumps([]))  
            return resp

    
    if pedidos:
        total_general = sum(p['total'] for p in pedidos)

    return render('index.html', form=form, pedidos=pedidos,
                  total_general=total_general, ventas=ventas)


if __name__ == '__main__':
    app.run(debug=True)
