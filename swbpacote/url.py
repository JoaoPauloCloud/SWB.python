from swbpacote.views import inicial
from flask import Blueprint

from .views.contact import contact, contact_new
from .views.cliente import cliente, cliente_new, cliente_info
from .views.livro import livro, livro_new, livro_info
from .views.inicial import inicial


################## Tela Inicial ####################
bp_inicial = Blueprint('inicial', __name__)
bp_inicial.add_url_rule('/',view_func=inicial, methods=['GET'])
#bp_livro.add_url_rule('/livros/informacao/',view_func=livro_info, methods=['GET'])
#bp_livro.add_url_rule('/livros/new/',view_func=livro_new, methods=['GET', 'POST'])
#bp_livro.add_url_rule('/livros/<int:id>/',view_func=livro, methods=['GET', 'POST'])


################## livros ####################
bp_livro = Blueprint('livros', __name__)
bp_livro.add_url_rule('/livros',view_func=livro, methods=['GET'])
bp_livro.add_url_rule('/livros/informacao/',view_func=livro_info, methods=['GET'])
bp_livro.add_url_rule('/livros/new/',view_func=livro_new, methods=['GET', 'POST'])
bp_livro.add_url_rule('/livros/<int:id>/',view_func=livro, methods=['GET', 'POST'])

################## Clientes ####################
bp_cliente = Blueprint('clientes', __name__)
bp_cliente.add_url_rule('/clientes',view_func=cliente, methods=['GET'])
bp_cliente.add_url_rule('/clientes/informacao/',view_func=cliente_info, methods=['GET'])
bp_cliente.add_url_rule('/clientes/new/',view_func=cliente_new, methods=['GET', 'POST'])
bp_cliente.add_url_rule('/clientes/<int:id>/',view_func=cliente, methods=['GET', 'POST'])

################## Telefones ####################
bp_contact = Blueprint('contacts', __name__)
bp_contact.add_url_rule('/contacts',view_func=contact, methods=['GET'])
bp_contact.add_url_rule('/contacts/new/',view_func=contact_new, methods=['GET', 'POST'])
bp_contact.add_url_rule('/contacts/<int:id>/',view_func=contact, methods=['GET', 'POST'])