# -*- coding: utf-8 -*-

from odoo import models, fields, api

@api.one
@api.depends('identifier')
def _computePythonModule(self):
    self.python_module = 'odoo.addons.gal_jpk.schemas.generated.{}.models'.format(self.identifier)

class DocumentType(models.Model):
    _name = 'gal.jpk.document_type'
    _description = 'JPK document type'

    name = fields.Char(
        'Name of the document',
        readonly=True,
        required=True,
    )

    identifier = fields.Char(
        'Short identifier, URL- and Python-friendly',
        readonly=True,
        required=True,
    )

    python_module = fields.Char(
        compute=_computePythonModule,
    )
    root_element = fields.Char(
        'Main XML element name',
        required=True
    )
