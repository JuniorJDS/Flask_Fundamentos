from flask import render_template, redirect, url_for
from app import app
from app.forms import cliente_form
from app import db
from app.models import cliente_model


@app.route("/cadastrar_cliente", methods=['GET', 'POST'])
def cadastrar_cliente():
    form = cliente_form.ClientForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data

        cliente = cliente_model.Cliente(nome=nome, email=email, data_nascimento=data_nascimento,
                                        profissao=profissao, sexo=sexo)
        try:
            db.session.add(cliente)
            db.session.commit()
            return redirect(url_for("listar_clientes"))
        except:
            print("Cliente não cadastrado!")

    return render_template("clientes/form.html", form=form)


@app.route("/login")
def login():
    form = cliente_form.ClientForm()

    return render_template("clientes/login.html", form=form)


@app.route("/listar_clientes", methods=["GET"])
def listar_clientes():
    clientes = cliente_model.Cliente.query.all()
    return render_template("clientes/lista_clientes.html", clientes=clientes)

@app.route("/listar_cliente/<int:id>")
def listar_cliente(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return cliente.nome
