from flask.views import MethodView
from flask import render_template

class LivroInformacaoView(MethodView):
    def get(self):
        #clientes = ClienteModel.query.order_by(ClienteModel.name).all()                
        return render_template('inicial.html')


inicial = LivroInformacaoView.as_view('info')
