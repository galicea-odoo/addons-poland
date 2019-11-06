# -*- coding: utf-8 -*-

from odoo import models, fields, api

@api.one
@api.depends('date_from', 'date_until')
def _computeName(self):
    self.name = '{} - {}'.format(
        self.date_from,
        self.date_until
    )

class DocumentSuite(models.Model):
    _name = 'gal.jpk.document_suite'
    _description = 'JPK document suite'

    date_from = fields.Date(
        'From date',
        required=True,
    )

    date_until = fields.Date(
        'Until date',
        required=True,
    )

    document_types = fields.Many2many(
        'gal.jpk.document_type',
    )

    documents = fields.One2many(
        'gal.jpk.document',
        inverse_name='suite'
    )

    name = fields.Char(
        compute=_computeName,
        store=False,
    )

    @api.model
    def create(self, values):
        ret = super(DocumentSuite, self).create(values)
        for document_type in ret.document_types:
            self.env['gal.jpk.document'].create({
                'suite': ret.id,
                'type': document_type.id,
            })
        return ret
