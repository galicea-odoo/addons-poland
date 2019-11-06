# Signature <<<128f6eb2>>>
# -*- coding: utf-8 -*-

import decimal
import datetime
from .bindings import Namespace
from xsd2xml import xmlgen
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import models as etd
# vvv ONLY EDIT CODE BELOW THIS LINE vvv {imports}
from odoo import models, fields, api, _, tools
from openerp.api import Environment
# ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ecf8427e}

import logging

_logger = logging.getLogger(__name__)


class TNaglowek(object):
    """Nagłówek JPK_VAT"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek}
    def __init__(self, data):
        self.data=data
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getCelZlozenia(self):
        """@returns long"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getCelZlozenia}
        # TODO: Fill in the actual data
        return self.data.CelZlozenia
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getDataDo(self):
        """Data końcowa okresu, którego dotyczy JPK_VAT

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataDo}
        # TODO: Fill in the actual data
        return self.data.DataDo #datetime.datetime.strftime(fields.Date.from_string(self.data.DataDo),'%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {4f0d6227}

    def getDataOd(self):
        """Data początkowa okresu, którego dotyczy JPK_VAT

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataOd}
        # TODO: Fill in the actual data
        return self.data.DataOd #datetime.datetime.strftime(fields.Date.from_string(self.data.DataOd),'%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {4f0d6227}

    def getDataWytworzeniaJPK(self):
        """Data i czas wytworzenia JPK_VAT

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataWytworzeniaJPK}
        # TODO: Fill in the actual data
        dt = self.data.DataWytworzeniaJPK

        return dt[:10] + 'T'+dt[11:]+'Z' #datetime.datetime.strdtime(fields.Date.from_string(self.data.DataWytworzeniaJPK),'%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8ee2a179}

    def getKodFormularza(self):
        """@returns TNaglowek_KodFormularza"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getKodFormularza}
        # TODO: Fill in the actual data
        return TNaglowek_KodFormularza()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {840267e6}

    def getNazwaSystemu(self):
        """Nazwa systemu, z którego pochodzą dane

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getNazwaSystemu}
        # TODO: Fill in the actual data
        return "NazwaSystemu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {33b601b6}

    def getWariantFormularza(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getWariantFormularza}
        # TODO: Fill in the actual data
        return 3
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {cf23ef9c}


class TNaglowek_KodFormularza(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_KodFormularza}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_KodFormularza:getContent}
        # TODO: Fill in the actual data
        return "JPK_VAT"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {23ece332}

    def getkodSystemowy(self):
        """@returns string"""
        return "JPK_VAT (3)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "1-1"


class Element_JPK(object):
    """Jednolity plik kontrolny dla ewidencji zakupu i sprzedaży VAT"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK}
    def __init__(self, document):
        """@param document odoo.addons.gal_jpk.models.Document"""
        self.document = document
        self.doc_id = document.id
        self.zcount = 0
        self.zsum = 0.0
        self.scount = 0
        self.ssum = 0.0
        self.domain = [('jpk_vat_id', '=', self.doc_id)]
        doksprzedazy = self.document.env['gal.jpk.sprzedaz'].search(self.domain)
        self.slista = []
        for sprzedaz in doksprzedazy:
            self.slista.append(Element_JPK_SprzedazWiersz(sprzedaz))
            self.scount+=1
            self.ssum=self.ssum+(sprzedaz.K_16 + sprzedaz.K_18 + sprzedaz.K_20 + sprzedaz.K_24 +
                                 sprzedaz.K_26 + sprzedaz.K_28 + sprzedaz.K_30 + sprzedaz.K_33 +
                                 sprzedaz.K_35 + sprzedaz.K_36 + sprzedaz.K_37)
        self.zlista = []
        domain = [('jpk_vat_id', '=', self.doc_id)]
        zakupy = self.document.env['gal.jpk.zakup'].search(domain)
        for zakup in zakupy:
            self.zlista.append(Element_JPK_ZakupWiersz(zakup))
            self.zcount+=1
            self.zsum=self.zsum+(zakup.K_44 + zakup.K_46 + zakup.K_47 + zakup.K_48 + zakup.K_49 + zakup.K_50)


    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """Nagłówek JPK_VAT

        @returns TNaglowek
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek(self.document)
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {98f6a537}

    def getPodmiot1(self):
        """@returns Element_JPK_Podmiot1"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPodmiot1}
        # TODO: Fill in the actual data
#        domain = [('id','=',self.doc_id)]
 #       dane = self.document.env['gal.jpk.vat'].search(domain)
        return Element_JPK_Podmiot1(self.document)
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1be705e0}

    def getSprzedazCtrl(self):
        """Sumy kontrolne dla ewidencji sprzedaży VAT

        @returns Element_JPK_SprzedazCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getSprzedazCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_SprzedazCtrl(self.scount, self.ssum) if self.scount > 0 else None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ea8aa461}

    def getSprzedazWiersz(self):
        """Ewidencja sprzedaży oraz nabyć towarów i usług dla których podmiot
        obowiązany jest naliczyć podatek należny - tj. wewnątrzwspólnotowe
        nabycia towarów, import towarów podlegających rozliczeniu zgodnie z art.
        33 a ustawy, import usług z wyłączeniem usług nabywanych od podatników
        podatku od wartości dodanej, do których stosuje się art. 28 b ustawy,
        import usług nabywanych od podatników podatku od wartości dodanej, do
        których stosuje się art. 28 b ustawy, dostawa towarów, dla których
        podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wypełnia
        nabywca), dostawa towarów, dla których podatnikiem jest nabywca zgodnie
        z art. 17 ust. 1 pkt 7 lub 8 ustawy (wypełnia nabywca)

        @returns Element_JPK_SprzedazWiersz[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getSprzedazWiersz}
        # TODO: Fill in the actual data
        return self.slista
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {24a3eb94}

    def getZakupCtrl(self):
        """Sumy kontrolne dla ewidencji zakupu VAT

        @returns Element_JPK_ZakupCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getZakupCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_ZakupCtrl(self.zcount, self.zsum) if self.zcount > 0 else None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {d17d5878}

    def getZakupWiersz(self):
        """Ewidencja zakupu VAT

        @returns Element_JPK_ZakupWiersz[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getZakupWiersz}
        # TODO: Fill in the actual data
        return self.zlista
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c46227a8}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['JPK'], self).toxml()


class Element_JPK_ZakupWiersz(object):
    """Ewidencja zakupu VAT"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz}
    def __init__(self, zakupy):
        self.zakupy = zakupy
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresDostawcy(self):
        """Adres dostawcy (kontrahenta)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getAdresDostawcy}
        # TODO: Fill in the actual data
        try:
          _logger.info('Adres dost?')
          s=unicode(self.zakupy.AdresDostawcy[:255])
          _logger.info('Adres dost: %s ' % s)
          return s
        except Exception as e:
          _logger.info( "Blad: Adres Dostawcy: %s" % str(e) )
          return '??'
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f445b3be}

    def getDataWplywu(self):
        """Data wpływu dowodu zakupu

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getDataWplywu}
        # TODO: Fill in the actual data
        return self.zakupy.DataWplywu if self.zakupy.DataWplywu else None
#        return datetime.datetime.strptime('2006-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
#        return datetime.datetime.strptime(self.zakupy.DataWplywu, '%Y-%m-%d %H:%M:%S')

        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b5511aea}

    def getDataZakupu(self):
        """Data wystawienia dowodu zakupu

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getDataZakupu}
        # TODO: Fill in the actual data
        return self.zakupy.DataZakupu if self.zakupy.DataZakupu else None
#        return datetime.datetime.strptime('2006-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
#        return datetime.datetime.strptime(self.zakupy.DataZakupu, '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b5511aea}

    def getDowodZakupu(self):
        """Numer dowodu zakupu

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getDowodZakupu}
        # TODO: Fill in the actual data
        return self.zakupy.DowodZakupu
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {15627751}

    def getK_43(self):
        """Kwota netto - Nabycie towarów i usług zaliczanych u podatnika do
        środków trwałych

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getK_43}
        # TODO: Fill in the actual data
        return self.zakupy.K_43
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_44(self):
        """Kwota podatku naliczonego - Nabycie towarów i usług zaliczanych u
        podatnika do środków trwałych

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getK_44}
        # TODO: Fill in the actual data
        return self.zakupy.K_44
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_45(self):
        """Kwota netto - Nabycie towarów i usług pozostałych

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getK_45}
        # TODO: Fill in the actual data
        return self.zakupy.K_45
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_46(self):
        """Kwota podatku naliczonego - Nabycie towarów i usług pozostałych

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getK_46}
        # TODO: Fill in the actual data
        return self.zakupy.K_46
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_47(self):
        """Korekta podatku naliczonego od nabycia środków trwałych

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getK_47}
        # TODO: Fill in the actual data
        return self.zakupy.K_47
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_48(self):
        """Korekta podatku naliczonego od pozostałych nabyć

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getK_48}
        # TODO: Fill in the actual data
        return self.zakupy.K_48
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_49(self):
        """Korekta podatku naliczonego, o której mowa w art. 89b ust. 1 ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getK_49}
        # TODO: Fill in the actual data
        return self.zakupy.K_49
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_50(self):
        """Korekta podatku naliczonego, o której mowa w art. 89b ust. 4 ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getK_50}
        # TODO: Fill in the actual data
        return self.zakupy.K_50
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getLpZakupu(self):
        """Lp. wiersza ewidencji zakupu VAT

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getLpZakupu}
        # TODO: Fill in the actual data
        return self.zakupy.LpZakupu
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getNazwaDostawcy(self):
        """Imię i nazwisko lub nazwa dostawcy (kontrahenta)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getNazwaDostawcy}
        # TODO: Fill in the actual data
        try:
          _logger.info( "Nazwa Dost?" )
          s=unicode(self.zakupy.NazwaDostawcy[:255])
          _logger.info( u"Nazwa Dost: %s" % s )
          return s
        except Exception as e:
          _logger.info( "Bledna Nazwa Dostawcy: %s" % str(e) )
          return '?'
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {77df7a23}

    def getNrDostawcy(self):
        """Numer, za pomocą którego dostawca (kontrahent) jest zidentyfikowany
        na potrzeby podatku lub podatku od wartości dodanej

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupWiersz:getNrDostawcy}
        # TODO: Fill in the actual data
        return self.zakupy.NrDostawcy
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {33a0a60b}


class Element_JPK_ZakupCtrl(object):
    """Sumy kontrolne dla ewidencji zakupu VAT"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupCtrl}
    def __init__(self, zcount, zsum):
        self.zcount=zcount
        self.zsum=zsum
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaWierszyZakupow(self):
        """Liczba wierszy ewidencji zakupu, w okresie którego dotyczy JPK

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupCtrl:getLiczbaWierszyZakupow}
        # TODO: Fill in the actual data
        return self.zcount # if self.zcount>0 else return None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getPodatekNaliczony(self):
        """Razem kwota podatku naliczonego do odliczenia - suma kwot z elementów
        K_44, K_46, K_47, K_48, K_49 i K_50

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZakupCtrl:getPodatekNaliczony}
        # TODO: Fill in the actual data
        return self.zsum
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_SprzedazWiersz(object):
    """Ewidencja sprzedaży oraz nabyć towarów i usług dla których podmiot
    obowiązany jest naliczyć podatek należny - tj. wewnątrzwspólnotowe nabycia
    towarów, import towarów podlegających rozliczeniu zgodnie z art. 33 a
    ustawy, import usług z wyłączeniem usług nabywanych od podatników podatku od
    wartości dodanej, do których stosuje się art. 28 b ustawy, import usług
    nabywanych od podatników podatku od wartości dodanej, do których stosuje się
    art. 28 b ustawy, dostawa towarów, dla których podatnikiem jest nabywca
    zgodnie z art. 17 ust. 1 pkt 5 ustawy (wypełnia nabywca), dostawa towarów,
    dla których podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8
    ustawy (wypełnia nabywca)
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz}
    def __init__(self, sprzedaz):
        self.sprzedaz = sprzedaz
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresKontrahenta(self):
        """Adres kontrahenta

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getAdresKontrahenta}
        # TODO: Fill in the actual data
        return u'%s' % self.sprzedaz.AdresKontrahenta
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {854341f4}

    def getDataSprzedazy(self):
        """Data sprzedaży, o ile jest określona i różni się od daty wystawienia
        dowodu sprzedaży. W przeciwnym przypadku - pole puste

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getDataSprzedazy}
        # TODO: Fill in the actual data
#        return datetime.datetime.strptime('2006-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        return self.sprzedaz.DataSprzedazy if self.sprzedaz.DataSprzedazy else None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b5511aea}

    def getDataWystawienia(self):
        """Data wystawienia dowodu sprzedaży

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getDataWystawienia}
        # TODO: Fill in the actual data
#        return datetime.datetime.strptime('2006-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        return self.sprzedaz.DataWystawienia if self.sprzedaz.DataWystawienia else None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b5511aea}

    def getDowodSprzedazy(self):
        """Numer dowodu sprzedaży

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getDowodSprzedazy}
        # TODO: Fill in the actual data
        return self.sprzedaz.DowodSprzedazy
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e684b2ed}

    def getK_10(self):
        """Kwota netto - Dostawa towarów oraz świadczenie usług na terytorium
        kraju, zwolnione od podatku

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_10}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_10
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_11(self):
        """Kwota netto - Dostawa towarów oraz świadczenie usług poza terytorium
        kraju

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_11}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_11
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_12(self):
        """Kwota netto - w tym świadczenie usług, o których mowa w art. 100 ust.
        1 pkt 4 ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_12}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_12
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_13(self):
        """Kwota netto - Dostawa towarów oraz świadczenie usług na terytorium
        kraju, opodatkowane stawką 0%

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_13}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_13
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_14(self):
        """Kwota netto - w tym dostawa towarów, o której mowa w art. 129 ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_14}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_14
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_15(self):
        """Kwota netto - Dostawa towarów oraz świadczenie usług na terytorium
        kraju, opodatkowane stawką 5%

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_15}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_15
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_16(self):
        """Kwota podatku należnego - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 5%

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_16}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_16
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_17(self):
        """Kwota netto - Dostawa towarów oraz świadczenie usług na terytorium
        kraju, opodatkowane stawką 7% albo 8%

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_17}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_17
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_18(self):
        """Kwota podatku należnego - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 7% albo 8%

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_18}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_18
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_19(self):
        """Kwota netto - Dostawa towarów oraz świadczenie usług na terytorium
        kraju, opodatkowane stawką 22% albo 23%

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_19}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_19
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_20(self):
        """Kwota podatku należnego - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 22% albo 23%

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_20}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_20
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_21(self):
        """Kwota netto - Wewnątrzwspólnotowa dostawa towarów

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_21}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_21
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_22(self):
        """Kwota netto - Eksport towarów

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_22}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_22
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_23(self):
        """Kwota netto - Wewnątrzwspólnotowe nabycie towarów

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_23}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_23
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_24(self):
        """Kwota podatku należnego - Wewnątrzwspólnotowe nabycie towarów

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_24}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_24
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_25(self):
        """Kwota netto - Import towarów podlegający rozliczeniu zgodnie z art.
        33a ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_25}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_25
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_26(self):
        """Kwota podatku należnego - Import towarów podlegający rozliczeniu
        zgodnie z art. 33a ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_26}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_26
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_27(self):
        """Kwota netto - Import usług z wyłączeniem usług nabywanych od
        podatników podatku od wartości dodanej, do których stosuje się art. 28b
        ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_27}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_27
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_28(self):
        """Kwota podatku należnego - Import usług z wyłączeniem usług nabywanych
        od podatników podatku od wartości dodanej, do których stosuje się art.
        28b ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_28}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_28
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_29(self):
        """Kwota netto - Import usług nabywanych od podatników podatku od
        wartości dodanej, do których stosuje się art. 28b ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_29}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_29
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_30(self):
        """Kwota podatku należnego - Import usług nabywanych od podatników
        podatku od wartości dodanej, do których stosuje się art. 28b ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_30}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_30
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_31(self):
        """Kwota netto - Dostawa towarów oraz świadczenie usług, dla których
        podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy
        (wypełnia dostawca)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_31}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_31
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_32(self):
        """Kwota netto - Dostawa towarów, dla których podatnikiem jest nabywca
        zgodnie z art. 17 ust. 1 pkt 5 ustawy (wypełnia nabywca)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_32}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_32
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_33(self):
        """Kwota podatku należnego - Dostawa towarów, dla których podatnikiem
        jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wypełnia nabywca)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_33}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_33
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_34(self):
        """Kwota netto - Dostawa towarów oraz świadczenie usług, dla których
        podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy
        (wypełnia nabywca)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_34}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_34
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_35(self):
        """Kwota podatku należnego - Dostawa towarów oraz świadczenie usług, dla
        których podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8
        ustawy (wypełnia nabywca)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_35}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_35
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_36(self):
        """Kwota podatku należnego od towarów i usług objętych spisem z natury,
        o którym mowa w art. 14 ust. 5 ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_36}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_36
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_37(self):
        """Zwrot odliczonej lub zwróconej kwoty wydatkowanej na zakup kas
        rejestrujących, o którym mowa w art. 111 ust. 6 ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_37}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_37
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_38(self):
        """Kwota podatku należnego od wewnątrzwspólnotowego nabycia środków
        transportu, wykazanego w elemencie K_24, podlegająca wpłacie w terminie,
        o którym mowa w art. 103 ust. 3, w związku z ust. 4 ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_38}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_38
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_39(self):
        """Kwota podatku od wewnątrzwspólnotowego nabycia paliw silnikowych,
        podlegająca wpłacie w terminach,
        o których mowa w art. 103 ust. 5a i 5b ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getK_39}
        # TODO: Fill in the actual data
        return self.sprzedaz.K_39
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getLpSprzedazy(self):
        """Lp. wiersza ewidencji sprzedaży VAT

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getLpSprzedazy}
        # TODO: Fill in the actual data
        return self.sprzedaz.LpSprzedazy
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getNazwaKontrahenta(self):
        """Imię i nazwisko lub nazwa kontrahenta

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getNazwaKontrahenta}
        # TODO: Fill in the actual data
        return u'%s' % self.sprzedaz.NazwaKontrahenta
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e64d5f60}

    def getNrKontrahenta(self):
        """Numer, za pomocą którego kontrahent jest zidentyfikowany na potrzeby
        podatku lub podatku od wartości dodanej

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazWiersz:getNrKontrahenta}
        # TODO: Fill in the actual data
        return self.sprzedaz.NrKontrahenta
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {02ea9113}


class Element_JPK_SprzedazCtrl(object):
    """Sumy kontrolne dla ewidencji sprzedaży VAT"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazCtrl}
    def __init__(self, scount, ssum):
        self.scount=scount
        self.ssum=ssum
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaWierszySprzedazy(self):
        """Liczba wierszy ewidencji sprzedaży, w okresie którego dotyczy JPK

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazCtrl:getLiczbaWierszySprzedazy}
        # TODO: Fill in the actual data
        return self.scount #if self.scount>0 else None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getPodatekNalezny(self):
        """Podatek należny wg ewidencji sprzedaży w okresie, którego dotyczy JPK
        - suma kwot z elementów K_16, K_18, K_20, K_24, K_26, K_28, K_30, K_33,
        K_35, K_36 i K_37 pomniejszona o kwotę z elementów K_38 i K_39

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_SprzedazCtrl:getPodatekNalezny}
        # TODO: Fill in the actual data
        return self.ssum
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_Podmiot1(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1}
    def __init__(self, data):
        self.data=data
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getEmail(self):
        """@returns string"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1:getEmail}
        # TODO: Fill in the actual data
        return self.data.email if self.data.email else 'nn@example.com'
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b273e17e}

    def getNIP(self):
        """Identyfikator podatkowy NIP

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1:getNIP}
        # TODO: Fill in the actual data
        if not self.data.NIP:
          return '0000000000'
        else:
          nip=self.data.NIP
          if nip[:2]=='PL':
            return nip[2:]
          else:
            return nip
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getPelnaNazwa(self):
        """Pełna nazwa

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1:getPelnaNazwa}
        # TODO: Fill in the actual data
        if self.data.PelnaNazwa:
            return u'%s' % self.data.PelnaNazwa
        else:
            return u'[uzupełnić]'

        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {bdbaf47e}
