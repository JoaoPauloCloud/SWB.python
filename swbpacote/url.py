from flask import Blueprint

from .views.contact import contact, contact_new

bp_contact = Blueprint('contact', __name__)

bp_contact.add_url_rule('/contacts',view_func=contact, methods=['Get'])

bp_contact.add_url_rule('/contacts/new/',view_func=contact_new, methods=['Get', 'POST'])