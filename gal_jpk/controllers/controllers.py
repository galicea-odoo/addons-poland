# -*- coding: utf-8 -*-
from odoo import http
import werkzeug

class GalJpk(http.Controller):
     @http.route('/gal_jpk/document/<model("gal.jpk.document"):document>/<string:name>.xml', auth='user')
     def xml(self, document, name, **kw):
         return werkzeug.Response(
             headers={'Content-Type': "application/xml; charset=utf-8"},
             response=document.xml,
             status=200,
         )
