from flask.views import MethodView

class ContactView(MethodView):
    def get(self):
        return "<h6>João Paulo</h6>"

contact = ContactView.as_view('list')