from flask.templating import render_template_string
from flask.views import MethodView
from flask import render_template

from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired

from swbpacote.models.model import ContactModel


class ContactView(MethodView):
    def get(self):
        contacts = ContactModel.query.order_by(ContactModel.name).all()
        
        return render_template('contact/list.html', contacts=contacts)

class ContactNew(MethodView):
    def get(self):
        class ContactForm(FlaskForm):
            name = StringField('name', validators=[DataRequired()])
        form = ContactForm()
        return render_template('contact/new.html', form=form)
contact = ContactView.as_view('list')
contact_new = ContactNew.as_view('new')