#!/usr/bin/env python

from flask import Flask, render_template, request
from flask.ext.triangle import Triangle
from flask.json import dumps
import os
from facturas.database import init_db, db_session
from facturas.models import Entrada


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, static_path='/static', template_folder=tmpl_dir)
Triangle(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/<mes>/')
def mes_view(mes=None):
    return render_template('index.html', mes=mes)

@app.route('/api/<mes>/lineas/linea/', methods=['GET', 'POST'])
def entradas_view(mes=None):
    if request.method == 'POST':
        numero = request.form['numero']
	dia = request.form['dia']
	empresa = request.form['empresa']
	base_imponible = request.form['base_imponible']
        iva = request.form['iva']
        e = Entrada(numero=numero,dia=dia,empresa=empresa,base_imponible=base_imponible,iva=iva,mes=mes)
        db_session.add(e)
        db_session.commit()
        return "success", 201
    else:
        entradas = Entrada.query.filter(Entrada.mes == mes).all()
        return dumps([e.as_dict() for e in entradas]), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

