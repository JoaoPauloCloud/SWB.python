from flask.views import MethodView
from flask import render_template, redirect, url_for, abort

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

from swbpacote.models.model import LivroModel



class LivroForm(FlaskForm):
    name = StringField(
        'Nome',
        validators=[DataRequired(),
                    Length(min=5, max=100,
                           message="Esse campo deve ter entre 5 e 100 caracteres."
                           )
                    ]
    )
    quantidade = IntegerField(
        'Quantidade',
    )
    btn_save = SubmitField('Salvar')
        


class LivroListDeleteView(MethodView):
    def get(self):
        livros = LivroModel.query.order_by(LivroModel.id).all()
        return render_template('livro/livros.html', livros=livros)

    def post(self, id):
        if not id:
            abort(404, "Livro inexistente.")

        livro = LivroModel.query.get(id)
        if not livro:
            abort(404, "Livro inexistente.")

        livro.delete()
        return redirect(url_for('livros.list'))

class LivroNewView(MethodView):
    def get(self):
        form = LivroForm()
        return render_template('livro/new.html', form=form)

    def post(self):
        form = LivroForm()

        if form.validate_on_submit():
            livro = LivroModel(name=form.name.data)
            #livro = LivroModel(quantidade=form.quantidade)
            livro.save()
            return redirect(url_for('livros.list'))        
        return render_template('livro/new.html', form=form)

class LivroInformacaoView(MethodView):
    def get(self):
        #clientes = ClienteModel.query.order_by(ClienteModel.name).all()                
        return render_template('livro/informacao.html')


livro = LivroListDeleteView.as_view('list')
livro_new = LivroNewView.as_view('new')
livro_info = LivroInformacaoView.as_view('info')