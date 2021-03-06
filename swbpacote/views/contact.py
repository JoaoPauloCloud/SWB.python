from flask.views import MethodView
from flask import render_template, redirect, url_for, abort

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length

from swbpacote.models.model import ContactModel

class ContactForm(FlaskForm):
            telefone = IntegerField(
                'Telefone', 
            )
            btn_save = SubmitField('Salvar')
        


class ContactListDeleteView(MethodView):
    def get(self):
        contacts = ContactModel.query.order_by(ContactModel.id).all()                
        return render_template('contact/list.html', contacts=contacts)

    def post(self, id):
        if not id:
            abort(404, "Contato inexistente.")

        contact = ContactModel.query.get(id)
        if not contact:
            abort(404, "Contato inexistente.")

        contact.delete()
        return redirect(url_for('contacts.list'))


class ContactNewView(MethodView):
    def get(self):
        form = ContactForm()
        return render_template('contact/new.html', form=form)

    def post(self):
        form = ContactForm()

        if form.validate_on_submit():
            contact = ContactModel(telefone=form.telefone.data)
            contact.save()
            return redirect(url_for('contacts.list'))        
        return render_template('contact/new.html', form=form)


contact = ContactListDeleteView.as_view('list')
contact_new = ContactNewView.as_view('new')