# -*- coding: utf-8 -*-

from odoo import models, fields, api, http, tools

import importlib
from datetime import datetime
#from Document import _computeXmlFile


class DocumentVAT(models.Model):
    _inherit = 'gal.jpk.vat'
    _description = 'JPK Docment - VAT'
# type = 4 # vat | Ewidencje zakupu i sprzedaży VAT

    document =fields.Many2one(
        'gal.jpk.document',
        required=False,
        readonly=True,
    )

    type = fields.Many2one(
        'gal.jpk.document_type',
        compute= '_compute_type',
        readonly=True,
    )

    xml = fields.Text(
        'XML content',
        readonly=True,
        related = 'document.xml'
    )

    xml_file = fields.Char(
        'Wygeneowany plik',
        readonly=True,
        compute='_computeXmlFile',
    )

    @api.one
    @api.depends('document')
    def _compute_type(self):
        self.type=self.document.type

    @api.one
    @api.depends('document')
    def _computeXmlFile(self):
      if self.document:
        host = http.request.httprequest.environ.get('HTTP_HOST', '')
        self.xml_file = '//{}/gal_jpk/document/{}/{}.xml'.format(
            host,
            self.document.id,
            self.document.type.identifier,
        )

    def create_file(self,jpk_vat_id):
        self=self.search([('id', '=', jpk_vat_id)])
        if self:
          self = self.with_context(active_model=self._name, active_id=self.id)
          if not self.document:
            date_from=self.DataOd #,"%Y-%m-%d"
            date_until=self.DataDo
            suite_id = self.env['gal.jpk.document_suite'].create(
                {
                'date_from' : date_from,
                'date_until': date_until,
                'document_types': [4,]
                }
                ).id
            self.document = self.document.create({
                'suite': suite_id,
                'type': 4,
            })
#   values = {}
#          values = values + { 'document' : doc.id }
#          ret = super(DocumentVAT, self).create(values)
          module = importlib.import_module(
                self.document.type.python_module
          )
          binding = module.Element_JPK(self) #.document)
          self.document.xml = binding.toXML()
#?          self.document.write()

    @api.multi
    def action_create_file(self):
        self.ensure_one()
        self.create_file(self.id)



class CreateFileWizard(models.TransientModel):
    _name = 'gal.jpk.vat.wizard'

    jpk_vat_id = fields.Many2one('gal.jpk.vat', string='JPK-VAT',
        required=True,
#        readonly=True,
    )
    delete_old = fields.Boolean('Usunąć z zestawienia stare dane', default=False)
    skip = fields.Boolean('Pomiń ten krok', default=True)
    error = fields.Text(default='', readonly=True)

    @api.multi
    def gal_jpk_vat_wizard_fill(self): # wypełnienie danych
        self.ensure_one()
        self = self.with_context(active_model=self._name, active_id=self.id)
        if (self.jpk_vat_id) and (not self.skip):
            self.jpk_vat_id.prepare_jpk(self.jpk_vat_id.id,self.delete_old)
        try:
            form_id = self.env.ref('gal_jpk.vat_xml_wizard').id
            views = [(form_id, 'form')]
        except:
            views = []
        if self.jpk_vat_id:
          domain= [('jpk_vat_id', '=', self.jpk_vat_id.id)]
        else:
          domain=[]
        return {
            'type': 'ir.actions.act_window',
            'name': 'JPK',
            'res_model': self._name,
            'view_type': 'form',
            'view_mode': 'form',
            'readonly': True,
            'domain': domain,
            'context': {},
            'views': views,
            'target': 'new',
            'nodestroy': False,
            'res_id':self.id,
        }

    @api.multi
    def gal_jpk_vat_wizard_xml(self):
        self.ensure_one()
        self = self.with_context(active_model=self._name, active_id=self.id)
        form_id = self.env.ref('gal_jpk.vat_finish_wizard').id
        self.error='OK'
        if (self.jpk_vat_id):
#          jpk_vat=self.env['gal.jpk.vat']
          try:
              if self.env.user.company_id.vat:
#                  self._compute_company()
#              if self.jpk_vat_id.NIP:
                self.jpk_vat_id.create_file(self.jpk_vat_id.id)
              else:
                form_id = self.env.ref('gal_jpk.braknip').id
          except Exception as e:
              self.error='Błąd generowania %s' % e
        views = [(form_id, 'form')]
        return {
              'type': 'ir.actions.act_window',
              'name': 'JPK',
              'res_model': self._name,
              'view_type': 'form',
              'view_mode': 'form',
              'readonly': True,
              'domain': [],
              'views': views,
              'target': 'new',
              'nodestroy': False,
              'res_id':self.id
          }


    @api.multi
    def gal_jpk_vat_wizard_close(self):
        return {'type': 'ir.actions.act_window_close'}

    def action_open_vat_data_wizard(self):
        self = self.with_context(active_model=self._name, active_id=self.id)
        return {
            'type': 'ir.actions.act_window',
            'name': 'JPK',
            'res_model': 'gal.jpk.vat.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'form_id': 'gal_jpk.vat_data_wizard',
            'readonly': True,
            'domain': [],
            'context': {},
      #      'views': views,
            'target': 'new',
            'nodestroy': False,
            'res_id':self.id,
        }

