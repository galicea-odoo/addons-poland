# -*- coding: utf-8 -*-

from odoo import models, fields, api, http

import importlib

@api.one
def _computeXmlFile(self):
    host = http.request.httprequest.environ.get('HTTP_HOST', '')
    self.xml_file = '//{}/gal_jpk/document/{}/{}.xml'.format(
        host,
        self.id,
        self.type.identifier,
    )

class Document(models.Model):
    _name = 'gal.jpk.document'
    _description = 'JPK document'

    type = fields.Many2one(
        'gal.jpk.document_type',
        required=True,
        readonly=True,
    )

    suite = fields.Many2one(
        'gal.jpk.document_suite',
        'The set of JPK documents corresponding to the particular period',
        readonly=True,
        required=True,
        ondelete='cascade',
    )

    name = fields.Char(
        'Document name',
        related='type.name',
        store=False,
    )

    xml = fields.Text(
        'XML content',
        readonly=True,
    )

    xml_file = fields.Char(
        'Generated file',
        compute=_computeXmlFile,
    )

    @api.multi
    def createFile(selfs):
        for self in selfs:
            module = importlib.import_module(self.type.python_module)
            binding = getattr(module, 'Element_{}'.format(self.type.root_element))(self)
            self.xml = binding.toXML()
