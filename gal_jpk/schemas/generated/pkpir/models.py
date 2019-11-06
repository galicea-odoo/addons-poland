# Signature <<<76cd7d97>>>
# -*- coding: utf-8 -*-

import decimal
import datetime
from .bindings import Namespace
from xsd2xml import xmlgen
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import models as etd
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW_ import models as kck
# vvv ONLY EDIT CODE BELOW THIS LINE vvv {imports}
# ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ecf8427e}

class TNaglowek(object):
    """Nagłówek JPK_PKPIR"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getCelZlozenia(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getCelZlozenia}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getDataDo(self):
        """Data końcowa okresu, którego dotyczy JPK_PKPIR

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataDo}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataOd(self):
        """Data początkowa okresu, którego dotyczy JPK_PKPIR

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataOd}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataWytworzeniaJPK(self):
        """Data i czas wytworzenia JPK_PKPIR

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataWytworzeniaJPK}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {df3a3662}

    def getDomyslnyKodWaluty(self):
        """Trzyliterowy kod lokalnej waluty (ISO-4217), domyślny dla
        wytworzonego JPK_PKPIR

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDomyslnyKodWaluty}
        # TODO: Fill in the actual data
        return "AED"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {38f462e0}

    def getKodFormularza(self):
        """@returns TNaglowek_KodFormularza"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getKodFormularza}
        # TODO: Fill in the actual data
        return TNaglowek_KodFormularza()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {840267e6}

    def getKodUrzedu(self):
        """@returns string"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getKodUrzedu}
        # TODO: Fill in the actual data
        return "0202"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f770400d}

    def getWariantFormularza(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getWariantFormularza}
        # TODO: Fill in the actual data
        return 2
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {d8670d52}


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
        return "JPK_PKPIR"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e470aa9a}

    def getkodSystemowy(self):
        """@returns string"""
        return "JPK_PKPIR (2)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "1-0"


class TAdresJPK(object):
    """Informacje opisujące adres"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getGmina(self):
        """Gmina

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getGmina}
        # TODO: Fill in the actual data
        return "Gmina"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {db051a86}

    def getKodKraju(self):
        """Kraj

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getKodKraju}
        # TODO: Fill in the actual data
        return "AD"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2c2fc413}

    def getKodPocztowy(self):
        """Kod pocztowy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getKodPocztowy}
        # TODO: Fill in the actual data
        return "KodPoczt"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2e4aba9b}

    def getMiejscowosc(self):
        """Nazwa miejscowości

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getMiejscowosc}
        # TODO: Fill in the actual data
        return "Miejscowosc"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {48f8d7b1}

    def getNrDomu(self):
        """Numer budynku

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getNrDomu}
        # TODO: Fill in the actual data
        return "NrDomu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f2d99da1}

    def getNrLokalu(self):
        """Numer lokalu

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getNrLokalu}
        # TODO: Fill in the actual data
        return "NrLokalu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {9231d8ec}

    def getPoczta(self):
        """Nazwa urzędu pocztowego

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getPoczta}
        # TODO: Fill in the actual data
        return "Poczta"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a3cc6d62}

    def getPowiat(self):
        """Powiat

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getPowiat}
        # TODO: Fill in the actual data
        return "Powiat"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {871f1b15}

    def getUlica(self):
        """Nazwa ulicy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getUlica}
        # TODO: Fill in the actual data
        return "Ulica"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {42dc0012}

    def getWojewodztwo(self):
        """Województwo

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresJPK:getWojewodztwo}
        # TODO: Fill in the actual data
        return "Wojewodztwo"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e0f65118}


class Element_JPK(object):
    """Jednolity plik kontrolny dla podatkowej księgi przychodów i rozchodów"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK}
    def __init__(self, document):
        """@param document odoo.addons.gal_jpk.models.Document"""
        self.document = document
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """Nagłówek JPK_PKPIR

        @returns TNaglowek
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {98f6a537}

    def getPKPIRCtrl(self):
        """Sumy kontrolne dla tabeli PKPIRWiersz

        @returns Element_JPK_PKPIRCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPKPIRCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_PKPIRCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3b2e0d9f}

    def getPKPIRInfo(self):
        """Dane dotyczące ustalenia dochodu w roku podatkowym

        @returns Element_JPK_PKPIRInfo
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPKPIRInfo}
        # TODO: Fill in the actual data
        return Element_JPK_PKPIRInfo()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {d403879d}

    def getPKPIRSpis(self):
        """Spisy z natury sporządzone w ciągu roku podatkowego

        @returns Element_JPK_PKPIRSpis[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPKPIRSpis}
        # TODO: Fill in the actual data
        return [Element_JPK_PKPIRSpis(), Element_JPK_PKPIRSpis()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {bb91c72a}

    def getPKPIRWiersz(self):
        """Na podstawie załącznika do rozporządzenia Ministra Finansów z dnia 26
        sierpnia 2003 r. w sprawie prowadzenia podatkowej księgi przychodów i
        rozchodów (Dz. U. z 2014 r. poz. 1037, z późn. zm.)

        @returns Element_JPK_PKPIRWiersz[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPKPIRWiersz}
        # TODO: Fill in the actual data
        return [Element_JPK_PKPIRWiersz(), Element_JPK_PKPIRWiersz()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {bc1599c3}

    def getPodmiot1(self):
        """@returns Element_JPK_Podmiot1"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPodmiot1}
        # TODO: Fill in the actual data
        return Element_JPK_Podmiot1()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1be705e0}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['JPK'], self).toxml()


class Element_JPK_Podmiot1(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresPodmiotu(self):
        """Adres podmiotu

        @returns TAdresJPK
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1:getAdresPodmiotu}
        # TODO: Fill in the actual data
        return TAdresJPK()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3bacac0e}

    def getIdentyfikatorPodmiotu(self):
        """Dane identyfikujące podmiot

        @returns etd.TIdentyfikatorOsobyNiefizycznej
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1:getIdentyfikatorPodmiotu}
        # TODO: Fill in the actual data
        return etd.TIdentyfikatorOsobyNiefizycznej()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {429b9b00}


class Element_JPK_PKPIRWiersz(object):
    """Na podstawie załącznika do rozporządzenia Ministra Finansów z dnia 26
    sierpnia 2003 r. w sprawie prowadzenia podatkowej księgi przychodów i
    rozchodów (Dz. U. z 2014 r. poz. 1037, z późn. zm.)
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getK_1(self):
        """Lp.

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_1}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getK_10(self):
        """Zakup towarów handlowych i materiałów wg cen zakupu

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_10}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_11(self):
        """Koszty uboczne zakupu

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_11}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_12(self):
        """Wydatki (koszty) - wynagrodzenia w gotówce i w naturze

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_12}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_13(self):
        """Wydatki (koszty) - pozostałe wydatki

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_13}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_14(self):
        """Wydatki (koszty) - razem wydatki (12+13)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_14}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_15(self):
        """Wydatki (koszty) - pole wolne

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_15}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_16A(self):
        """Koszty działalności badawczo
        -rozwojowej, o których mowa w art. 26e ustawy o podatku dochodowym -
        opis kosztu

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_16A}
        # TODO: Fill in the actual data
        return "K_16A"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a55e3a0c}

    def getK_16B(self):
        """Koszty działalności badawczo-rozwojowej, o których mowa w art. 26e
        ustawy o podatku dochodowym - wartość

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_16B}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_17(self):
        """Uwagi

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_17}
        # TODO: Fill in the actual data
        return "K_17"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {698f4cfa}

    def getK_2(self):
        """Data zdarzenia gospodarczego

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_2}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getK_3(self):
        """Nr dowodu księgowego

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_3}
        # TODO: Fill in the actual data
        return "K_3"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {36e2dd1e}

    def getK_4(self):
        """Kontrahent - imię i nazwisko (firma)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_4}
        # TODO: Fill in the actual data
        return "K_4"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7173a3c1}

    def getK_5(self):
        """Kontrahent- adres

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_5}
        # TODO: Fill in the actual data
        return "K_5"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {deabd288}

    def getK_6(self):
        """Opis zdarzenia gospodarczego

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_6}
        # TODO: Fill in the actual data
        return "K_6"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f845d36b}

    def getK_7(self):
        """Przychód - wartość sprzedanych towarów i usług

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_7}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_8(self):
        """Przychód - pozostałe przychody

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_8}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getK_9(self):
        """Przychód - razem przychód (7+8)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRWiersz:getK_9}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def gettyp(self):
        """@returns string"""
        return "G"


class Element_JPK_PKPIRSpis(object):
    """Spisy z natury sporządzone w ciągu roku podatkowego"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRSpis}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_5A(self):
        """Data spisu z natury sporządzonego w ciągu roku podatkowego

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRSpis:getP_5A}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getP_5B(self):
        """Wartość spisu z natury sporządzonego w ciągu roku podatkowego

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRSpis:getP_5B}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def gettyp(self):
        """@returns string"""
        return "G"


class Element_JPK_PKPIRInfo(object):
    """Dane dotyczące ustalenia dochodu w roku podatkowym"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRInfo}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_1(self):
        """Wartość spisu z natury na początek roku podatkowego

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRInfo:getP_1}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_2(self):
        """Wartość spisu z natury na koniec roku podatkowego

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRInfo:getP_2}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_3(self):
        """Razem koszty uzyskania przychodu, wg objaśnień do podatkowej księgi
        przychodów i rozchodów

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRInfo:getP_3}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_4(self):
        """Dochód osiągnięty w roku podatkowym, wg objaśnień do podatkowej
        księgi przychodów i rozchodów

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRInfo:getP_4}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_PKPIRCtrl(object):
    """Sumy kontrolne dla tabeli PKPIRWiersz"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaWierszy(self):
        """Liczba wierszy (zapisów) PKPIR, w okresie którego dotyczy JPK_PKPIR

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRCtrl:getLiczbaWierszy}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getSumaPrzychodow(self):
        """Łączna wartość przychodów razem (kol. 9) w PKPIR w okresie, którego
        dotyczy JPK_PKPIR

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PKPIRCtrl:getSumaPrzychodow}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}
