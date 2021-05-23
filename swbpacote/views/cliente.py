from flask.views import MethodView
from flask import render_template, redirect, url_for, abort

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from swbpacote.models.model import ClienteModel

class ClienteForm(FlaskForm):
            name = StringField(
                'Nome',
                validators=[DataRequired(),
                            Length(min=5, max=100,
                                message="Esse campo deve ter entre 5 e 100 caracteres."
                            )
                        ]
            )
            btn_save = SubmitField('Salvar')
        


class ClienteListDeleteView(MethodView):
    def get(self):
        clientes = ClienteModel.query.order_by(ClienteModel.id).all()                
        return render_template('cliente/clientes.html', clientes=clientes)

    def post(self, id):
        if not id:
            abort(404, "Cliente não existe.")

        cliente = ClienteModel.query.get(id)
        if not cliente:
            abort(404, "Cliente não existe.")

        cliente.delete()
        return redirect(url_for('clientes.list'))


class ClienteNewView(MethodView):
    def get(self):
        form = ClienteForm()
        return render_template('cliente/new.html', form=form)

    def post(self):
        form = ClienteForm()

        if form.validate_on_submit():
            cliente = ClienteModel(name=form.name.data)
            cliente.save()
            return redirect(url_for('clientes.list'))        
        return render_template('cliente/new.html', form=form)

class ClienteInformacaoView(MethodView):
    def get(self):
        #clientes = ClienteModel.query.order_by(ClienteModel.name).all()                
        return render_template('cliente/informacao.html')





cliente = ClienteListDeleteView.as_view('list')
cliente_new = ClienteNewView.as_view('new')
cliente_info = ClienteInformacaoView.as_view('info')
