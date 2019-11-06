# -*- coding: utf-8 -*-
from odoo import models, fields, api, _, tools
import re



class JpkInvoice(models.Model):
    _name = 'gal.jpk.vat.invoice'
    _table = 'gal_jpk_vat_invoice_view'
    _description = "Rejestry VAT"
    _auto = False
    _order = 'date'

    id = fields.Integer('ID', readonly=True)
    date = fields.Date('Data', readonly=True)
    date_invoice = fields.Date('Data Faktury', readonly=True)
    name = fields.Char('Opis', readonly=True)
    inv_number = fields.Char('Nume faktury sprzedaży', readonly=True)
    inv_ref = fields.Char('Nume faktury zakupu', readonly=True)
    partner_id = fields.Many2one('res.partner', 'Partner', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', readonly=True)
    currency_id = fields.Many2one('res.currency', 'Currency', readonly=True)
    amount = fields.Float('Kwota', readonly=True)
    write_date  = fields.Date('Data Utworzenia', readonly=True)
    amount_total = fields.Float('Wartość', readonly=True)
    amount_tax = fields.Float('Podatek', readonly=True)
    amount_untaxed = fields.Float('Zwolnione', readonly=True)
    state = fields.Char('state', readonly=True)
    journal_id = fields.Integer('journal id', readonly=True)
    inv_type = fields.Selection([('out_invoice','out_invoice'),('in_invoice','in_invoice')])

    @api.model_cr
    def init(self):
#        tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute("""create or replace view %s as
select 
move.id id, 
move.date date, 
date_invoice, 
move.name "name",
inv.number inv_number,
inv.reference inv_ref,
move.partner_id,
move.company_id,
move.currency_id,
move.amount, 
move.write_date,
amount_total_company_signed amount_total,
amount_tax,
amount_untaxed,
move.state,
move.journal_id,
inv.type inv_type
from account_move move
left outer join account_invoice inv on move.id=inv.move_id
where move.state='posted' """ % self._table)
#        _logger.info('model.init')



class JpkVAT_zakup(models.Model):
    _name = 'gal.jpk.zakup'
    _description = 'Zakup'

    jpk_vat_id = fields.Many2one('gal.jpk.vat', 'JPK', index=True) # ondelete='cascade',- w bazie danych, wtedy nie można unlink
    LpZakupu = fields.Char('Lp') #. wiersza ewidencji zakupu VAT')
    NrDostawcy = fields.Char('NIP lub inny numer ew.') #  Numer, za pomocą którego dostawca (kontrahent) jest zidentyfikowany  na potrzeby podatku lub podatku od wartości dodanej
    NazwaDostawcy = fields.Char('Imię i nazwisko lub nazwa dostawcy (kontrahenta)')
    AdresDostawcy = fields.Char('Adres dostawcy (kontrahenta)')
    DowodZakupu = fields.Char('Numer dowodu zakupu')
    DataZakupu = fields.Date('Data wystawienia dowodu zakupu')
    DataWplywu = fields.Date('Data wpływu (opcjonalnie)')

    K_43 = fields.Float('Netto ST') # – Nabycie towarów i usług zaliczanych u podatnika do środków trwałych (pole opcjonalne)
    K_44 = fields.Float('VAT naliczony ST') #– Nabycie towarów i usług zaliczanych u podatnika do środków trwałych (pole opcjonalne)
    K_45 = fields.Float('Zakupy Netto') #Nabycie towarów i usług pozostałych (pole opcjonalne
    K_46 = fields.Float('VAT naliczony') # Nabycie towarów i usług pozostałych (pole opcjonalne)
    K_47 = fields.Float('korekta VAT ST') #nabycia środków trwałych (pole opcjonalne)
    K_48 = fields.Float('korekta VAT pozostałe') # (pole opcjonalne)
    K_49 = fields.Float('VAT nalicz. - nieuregulowane (ust. 89b.1)') # (pole opcjonalne)
    K_50 = fields.Float('VAT nalicz. - nieureg. zwiększenie (ust. 89b.4)') # (pole opcjonalne)

    LiczbaWierszyZakupow = fields.Integer('Liczba wierszy ewidencji zakupow')
    PodatekNaliczony = fields.Float('Podatek naliczony wg ewidencji zakupow w okresie którego')


#    @api.depends(K_44, K_46, K_47, K_48, K_49, K_50)
    @api.one
    def _compute_PodatekNalezny(self):
        self.PodatekNalezny=K_44 + K_46 + K_47 + K_48 + K_49 + K_50


class JpkVAT_sprzedaz(models.Model):
    _name = 'gal.jpk.sprzedaz'
    _description = 'Sprzedaz'

    jpk_vat_id = fields.Many2one('gal.jpk.vat', 'JPK', index=True)
    LpSprzedazy = fields.Integer('LP') #Liczba porządkowa wiersza ewidencji sprzedaży VAT
    NrKontrahenta = fields.Char('NIP lub "brak"')
    NazwaKontrahenta = fields.Char('Imię i nazwisko lub nazwa kontrahenta')
    AdresKontrahenta = fields.Char('Adres kontrahenta')
    DowodSprzedazy = fields.Char('Numer faktury')
    DataWystawienia = fields.Date('Data wystawienia faktury')
    DataSprzedazy = fields.Date('Data sprzedaży (lub puste)')
    K_10 = fields.Float('Netto - zwolnione') # – Dostawa towarów oraz świadczenie usług na terytorium kraju, zwolnione od podatku (pole opcjonalne)
    K_11 = fields.Float('Netto – eksport')
    K_12 = fields.Float('Netto – usługi z w art. 100 / 1 pkt 4')
    K_13 = fields.Float('Netto – kraj, 0%')
    K_14 = fields.Float('Netto – 0%, zwrot podróżnemu / art. 129')
    K_15 = fields.Float('Netto – 5%') # Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 5% (pole opcjonalne)
    K_16 = fields.Float('VAT należn. - kraj 5%') # – Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 5% (pole opcjonalne)
    K_17 = fields.Float('Netto – 7 lub 8% ') #Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 7% albo 8% (pole opcjonalne)
    K_18 = fields.Float('VAT należn. – 7 lub 8%') # Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 7% albo 8% (pole opcjonalne)
    K_19 = fields.Float('Netto – 22 lub 23%') # Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 22% albo 23% (pole opcjonalne)
    K_20 = fields.Float('VAT należn. – 22 lub 23%') # Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 22% albo 23% (pole opcjonalne)
    K_21 = fields.Float('Netto – eksport UE') # Wewnątrzwspólnotowa dostawa towarów (pole opcjonalne)
    K_22 = fields.Float('Netto – Eksport towarów') #  (pole opcjonalne)
    K_23 = fields.Float('Netto – import UE') # Wewnątrzwspólnotowe nabycie towarów (pole opcjonalne)
    K_24 = fields.Float('VAT należn. import UE') #  – Wewnątrzwspólnotowe nabycie towarów (pole opcjonalne)
    K_25 = fields.Float('Netto – Import / uproszcz. art. 33a') # podlegający rozliczeniu zgodnie z art. 33a ustawy (pole opcjonalne)
    K_26 = fields.Float('VAT należn. – Import / uproszcz. art. 33a') # Import towarów podlegający rozliczeniu zgodnie z art. 33a ustawy (pole opcjonalne)
    K_27 = fields.Float('Netto – Import usług - z wyłączeniem zwoln. /art. 28b') # Import usług z wyłączeniem usług nabywanych od podatników podatku od wartości dodanej, do których stosuje się art.
                                        # 28b ustawy (pole opcjonalne)
    K_28 = fields.Float('VAT należn. - Import usłg - z wyłączeniem zwol. - art. 28b') # – Import usług z wyłączeniem usług
        # nabywanych od podatników podatku od wartości dodanej, do których stosuje się art. 28b ustawy (pole opcjonalne)
    K_29 = fields.Float('Netto – Import usług - zwoln. / art. 28b')#
        # nabywanych od podatników podatku od
        # wartości dodanej, do których stosuje się art. 28b ustawy (pole opcjonalne)
    K_30 = fields.Float('VAT należn. – Import usług - zwoln. / art. 28b')
      #Import usług nabywanych od podatników podatku od wartości dodanej, do których stosuje się art. 28b ustawy (pole opcjonalne)
    K_31 = fields.Float('Netto – Odwrócony, wypełnia dostawca - / art. 17. 1 pkt 7 lub 8')
# podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy
# (wypełnia dostawca) (pole opcjonalne)
    K_32 = fields.Float('Netto – Odwrócony / art. 17.1 pkt 5 ')
    K_33 = fields.Float('VAT należn. – Odwrócony / art. 17.1 pkt 5 ')
    K_34 = fields.Float('Netto – Odwrócony, wypełnia nabywca / art. 17. 1 pkt 7 lub 8 ')
    K_35 = fields.Float('VAT należn. – Odwrócony, wypełnia nabywca / art. 17. 1 pkt 7 lub 8')
    K_36 = fields.Float('VAT należn. od spiseu z natury, art. 14. 5')
    K_37 = fields.Float('Zwrot / zakup kas rejestrujących - art. 111.6 ')
    K_38 = fields.Float('VAT należn. - wewnątrzwspólnotowe nabycie środków transportu')
    #, podlegająca wpłacie w terminie, o którym mowa w art. 103 ust. 3, w związku z ust. 4 ustawy 
    # (pole opcjonalne)
    K_39 = fields.Float('Kwota podatku od importu paliw - art. 103. 5a i 5b')



    LiczbaWierszySprzedazy = fields.Integer('Liczba wierszy ewidencji sprzedaży')
    PodatekNalezny = fields.Float('Podatek należny wg ewidencji sprzedaży w okresie którego')


 #   @api.depends(K_16,K_18,K_20,K_24,K_26,K_28,K_30, K_33, K_35,K_36,K_37,K_38,K_39)
    @api.one
    def _compute_PodatekNalezny(self):
        self.PodatekNalezny=K_16+K_18+K_20+K_24+K_26+K_28+K_30+ K_33+ K_35+K_36+K_37-(K_38+K_39)



class JpkVAT(models.Model):
    _name = 'gal.jpk.vat'
    _description = 'JPK - VAT'
    _rec_name = 'DataWytworzeniaJPK'


    CelZlozenia = fields.Integer('Wersja', default=0)
    DataWytworzeniaJPK = fields.Datetime('Czas utworzenia', required=True, default=fields.Datetime.now)
    DataOd = fields.Date('Data - Od')
    DataDo = fields.Date('Data - Do')
    komentarz = fields.Char('Komentarz')
    NazwaSystemu = 'Odoo-gal'


    NIP = fields.Char('NIP', compute='_compute_company')
    PelnaNazwa = fields.Char('PelnaNazwa', compute='_compute_company')
    email = fields.Char('email', compute='_compute_company')

    # stare
    DomyslnyKodWaluty = fields.Char('DomyslnyKodWaluty')
    KodUrzedu = fields.Char('KodUrzedu')
    REGON = fields.Char('Regon')
    # //

    zakup_ids = fields.One2many('gal.jpk.zakup', 'jpk_vat_id', 'Zakupy')
    sprzedaz_ids = fields.One2many('gal.jpk.sprzedaz', 'jpk_vat_id', 'Sprzedaż')
    #        copy=True, readonly=False,
    #    states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})

    company_id = fields.Many2one('res.company', 'Company', readonly=True)



#    @api.one
#    def _compute_DataWytworzenia(self):
#        pass


    @api.onchange('id','CelZlozenia','DataOd')
    def _compute_company(self):
        self.company_id = self.env.user.company_id
        self.email=self.company_id.email
        self.NIP=self.company_id.vat
        self.PelnaNazwa=self.company_id.name



    def get_addr(self, addr):
      res=''
      if (addr['invoice']):
        addr_id = addr['invoice']
      elif addr['contact']:
        addr_id = addr['contact']
      else:
        addr_id = 0
      if addr_id:
        contact=self.env['res.partner'].browse(addr_id)
        res=contact.contact_address if contact.contact_address else ''
#OK        res='%s' % re.sub(' +', ' ', re.sub(u"[^a-z,A-Z,ąćĘęłńóśźżĄĆĘŁŃÓŚŹŻ\ ]",' ', res.replace('\n',' ')))
        res='%s' % re.sub(' +', ' ', re.sub(u"[^0-9,a-z,A-Z,ąćĘęłńóśźżĄĆĘŁŃÓŚŹŻ\ \-\/\,]",' ', res.replace('\n',', ')))
        if res[-1:]==' ':
            res=res[:-1]
      return res[:128]

    def prepare_jpk(self,jpk_vat_id,delete_old):
#      self.search([('id','=',jpk_vat_id)])
      sales = self.env['gal.jpk.vat.invoice'].search([('inv_type','=','out_invoice'),('state','=','posted')])
      sprzedaz = self.env['gal.jpk.sprzedaz']
      if delete_old:
        sprzedaz.search([('jpk_vat_id', '=', jpk_vat_id)]).unlink()
      lp=0
      for sale in sales:
        if sale.date_invoice:
            dt=sale.date_invoice
        elif sale.date:
            dt=sale.date
        else:
            dt=sale.write_date
        adr=self.get_addr(sale.partner_id.address_get(['invoice']))
        if (dt>=self.DataOd) and (dt<=self.DataDo):
          lp+=1
          sprzedaz.create({
          'jpk_vat_id': jpk_vat_id,
          'LpSprzedazy': lp,
          'NrKontrahenta':sale.partner_id.vat,
          'NazwaKontrahenta':sale.partner_id.name,
          'AdresKontrahenta':adr,
          'DowodSprzedazy': sale.inv_number, # inv_ref
          'DataWystawienia': dt,
#          'K_10': sale.amount_untaxed,
          'K_19': sale.amount_untaxed,
          'K_20': sale.amount_tax
        })
      purchases = self.env['gal.jpk.vat.invoice'].search([('inv_type','=','in_invoice'),('state','=','posted')])
      zakup = self.env['gal.jpk.zakup']
      if delete_old:
        zakup.search([('jpk_vat_id', '=', jpk_vat_id)]).unlink()
      lp=0
      for purchase in purchases:
          if purchase.date:
              dt = purchase.date
          else:
              dt = purchase.write_date
          if (dt >= self.DataOd) and (dt <= self.DataDo):
            lp += 1
            adr = self.get_addr(purchase.partner_id.address_get(['invoice']))
            zakup.create({
          'jpk_vat_id': jpk_vat_id,
          'LpZakupu': lp,
          'NrDostawcy': purchase.partner_id.vat,
          'NazwaDostawcy': purchase.partner_id.name,
          'AdresDostawcy': adr,
          'DowodZakupu': purchase.inv_ref,
          'DataZakupu': dt,
#          'DataWplywu': = fields.Date('Data wpływu (opcjonalnie)')
#          'K_43
        # 'K_44'
          'K_45': purchase.amount_total-purchase.amount_tax,
          'K_46': purchase.amount_tax
#          'K_47': = fields.Float('korekta VAT ST')  # nabycia środków trwałych (pole opcjonalne)
#          'K_48': = fields.Float('korekta VAT pozostałe')  # (pole opcjonalne)
#          'K_49': = fields.Float('VAT nalicz. - nieuregulowane (ust. 89b.1)')  # (pole opcjonalne)
#          'K_50': = fields.Float('VAT nalicz. - nieureg. zwiększenie (ust. 89b.4)')  # (pole opcjonalne)
          })

