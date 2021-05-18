from flask import Blueprint

from .views.contact import contact

bp_contact = Blueprint('contact', __name__)

bp_contact.add_url_rule('/contacts',view_func=contact, methods=['Get'])