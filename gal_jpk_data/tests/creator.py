# -*- coding: utf-8 -*-
from odoo import models, fields, api, _, tools
# do testów
# produkcyjnie generowanie w gal_jpk

class JpkVatWizard(models.TransientModel):
    _name = 'gal.jpk.vat.wizard'
    _description = 'JPK-VAT Wizard'

    jpk_vat_id = fields.Many2one('gal.jpk.vat', string='JPK')
    delete_old = fields.Boolean('Usunąć z zestawienia stare dane', default=False)

    def step2(self, domain, form_view):
      self = self.with_context(active_model=self._name, active_id=self.id)
      try:
        form_id = self.env.ref(form_view).id
        views = [(form_id, 'form')]
      except:
        views = []
      return {
      'type': 'ir.actions.act_window',
      'name': 'JPK',
      'res_model': self._name,
      'view_type': 'form',
      'view_mode': 'form',
      'readonly': True,
      'domain': domain,
      'views': views,
      'target': 'new',
      'nodestroy': False
      }

    @api.multi
    def gal_jpk_vat_wizard_fill(self): # wypełnienie danych
        self.ensure_one()
        if self.jpk_vat_id:
          self.env['gal.jpk.vat'].prepare_jpk(self.jpk_vat_id.id,self.delete_old)
        return self.step2([],'gal_jpk_data.vat_wizard2')

    @api.multi
    def gal_jpk_vat_wizard_close(self):  # wyniki
        return {'type': 'ir.actions.act_window_close'}
