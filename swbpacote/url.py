from flask import Blueprint

from .views.contact import contact, contact_new

bp_contact = Blueprint('contacts', __name__)
bp_contact.add_url_rule('/contacts',view_func=contact, methods=['GET'])
bp_contact.add_url_rule('/contacts/new/',view_func=contact_new, methods=['GET', 'POST'])
bp_contact.add_url_rule('/contacts/<int:id>/',view_func=contact, methods=['GET', 'POST'])