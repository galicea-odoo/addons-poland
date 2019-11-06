# Signature <<<9763e664>>>
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
    """Nagłówek JPK_FA"""
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
        """Data końcowa okresu, którego dotyczy JPK_FA

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataDo}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataOd(self):
        """Data początkowa okresu, którego dotyczy JPK_FA

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataOd}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataWytworzeniaJPK(self):
        """Data i czas wytworzenia JPK_FA

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataWytworzeniaJPK}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {df3a3662}

    def getDomyslnyKodWaluty(self):
        """Trzyliterowy kod lokalnej waluty (ISO-4217), domyślny dla
        wytworzonego JPK_FA

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
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}


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
        return "JPK_FA"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c6520963}

    def getkodSystemowy(self):
        """@returns string"""
        return "JPK_FA (1)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "1-0"


class Element_JPK(object):
    """Jednolity plik kontrolny dla faktur VAT"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK}
    def __init__(self, document):
        """@param document odoo.addons.gal_jpk.models.Document"""
        self.document = document
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getFaktura(self):
        """Na podstawie art.106 a-q ustawy z 11 marca 2004 r. o podatku od
        towarów i usług /Dz.U. z 2011 r. Nr 177, poz. 1054, z późn. zm./

        @returns Element_JPK_Faktura[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getFaktura}
        # TODO: Fill in the actual data
        return [Element_JPK_Faktura(), Element_JPK_Faktura()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {933b5b94}

    def getFakturaCtrl(self):
        """Sumy kontrolne dla faktur

        @returns Element_JPK_FakturaCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getFakturaCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_FakturaCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {89629876}

    def getFakturaWiersz(self):
        """Szczegółowe pozycje faktur

        @returns Element_JPK_FakturaWiersz[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getFakturaWiersz}
        # TODO: Fill in the actual data
        return [Element_JPK_FakturaWiersz(), Element_JPK_FakturaWiersz()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {857eea28}

    def getFakturaWierszCtrl(self):
        """Sumy kontrolne dla wierszy faktur

        @returns Element_JPK_FakturaWierszCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getFakturaWierszCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_FakturaWierszCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {26ca0eac}

    def getNaglowek(self):
        """Nagłówek JPK_FA

        @returns Element_JPK_Naglowek
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getNaglowek}
        # TODO: Fill in the actual data
        return Element_JPK_Naglowek()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {712806d4}

    def getPodmiot1(self):
        """@returns Element_JPK_Podmiot1"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPodmiot1}
        # TODO: Fill in the actual data
        return Element_JPK_Podmiot1()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1be705e0}

    def getStawkiPodatku(self):
        """Zestawienie stawek podatku, w okresie którego dotyczy JPK_FA

        @returns Element_JPK_StawkiPodatku
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getStawkiPodatku}
        # TODO: Fill in the actual data
        return Element_JPK_StawkiPodatku()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {266e6057}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['JPK'], self).toxml()


class Element_JPK_StawkiPodatku(object):
    """Zestawienie stawek podatku, w okresie którego dotyczy JPK_FA"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_StawkiPodatku}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getStawka1(self):
        """Wartość stawki podstawowej

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_StawkiPodatku:getStawka1}
        # TODO: Fill in the actual data
        return 0.23
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {5bd593e9}

    def getStawka2(self):
        """Wartość stawki obniżonej pierwszej

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_StawkiPodatku:getStawka2}
        # TODO: Fill in the actual data
        return 0.08
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fe932262}

    def getStawka3(self):
        """Wartość stawki obniżonej drugiej

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_StawkiPodatku:getStawka3}
        # TODO: Fill in the actual data
        return 0.05
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {4b538ca9}

    def getStawka4(self):
        """Wartość stawki obniżonej trzeciej - pole rezerwowe

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_StawkiPodatku:getStawka4}
        # TODO: Fill in the actual data
        return 0.00
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {cc6cb779}

    def getStawka5(self):
        """Wartość stawki obniżonej czwartej - pole rezerwowe

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_StawkiPodatku:getStawka5}
        # TODO: Fill in the actual data
        return 0.00
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {cc6cb779}


class Element_JPK_Podmiot1(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresPodmiotu(self):
        """Adres podmiotu

        @returns etd.TAdresPolski
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1:getAdresPodmiotu}
        # TODO: Fill in the actual data
        return etd.TAdresPolski()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e38984d4}

    def getIdentyfikatorPodmiotu(self):
        """Dane identyfikujące podmiot

        @returns etd.TIdentyfikatorOsobyNiefizycznej
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1:getIdentyfikatorPodmiotu}
        # TODO: Fill in the actual data
        return etd.TIdentyfikatorOsobyNiefizycznej()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {429b9b00}


class Element_JPK_Naglowek(TNaglowek):
    """Nagłówek JPK_FA"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Naglowek}
    def __init__(self, *args, **kwargs):
        super(Element_JPK_Naglowek, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {5eba9267}


class Element_JPK_FakturaWierszCtrl(object):
    """Sumy kontrolne dla wierszy faktur"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWierszCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaWierszyFaktur(self):
        """Liczba wierszy faktur, w okresie którego dotyczy JPK_FA

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWierszCtrl:getLiczbaWierszyFaktur}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getWartoscWierszyFaktur(self):
        """Łączna wartość kolumny P_11 tabeli FakturaWiersz w okresie, którego
        dotyczy JPK_FA

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWierszCtrl:getWartoscWierszyFaktur}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_FakturaWiersz(object):
    """Szczegółowe pozycje faktur"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_10(self):
        """Kwoty wszelkich opustów lub obniżek cen, w tym w formie rabatu z
        tytułu wcześniejszej zapłaty, o ile nie zostały one uwzględnione w cenie
        jednostkowej netto. Pole opcjonalne dla przypadków określonych w art.
        106e ust.2 i 3 ustawy (gdy przynajmniej jedno z pól P_106E_2 i P_106E_3
        przyjmuje wartość "true") oraz dla przypadku określonego w art. 106e
        ust. 5 pkt 1 ustawy.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_10}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_11(self):
        """Wartość dostarczonych towarów lub wykonanych usług, objętych
        transakcją, bez kwoty podatku (wartość sprzedaży netto). Pole opcjonalne
        dla przypadków określonych w art. 106e ust.2 i 3 ustawy (gdy
        przynajmniej jedno z pól P_106E_2 i P_106E_3 przyjmuje wartość "true")
        oraz dla przypadku określonego w art. 106e ust. 5 pkt 3 ustawy.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_11}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_11A(self):
        """W przypadku zastosowania art. 106e ust.7 i 8 ustawy, wartość
        sprzedaży brutto

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_11A}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_12(self):
        """Stawka podatku. Pole opcjonalne dla przypadków określonych w art.
        106e ust.2 i 3 ustawy (gdy przynajmniej jedno z pól P_106E_2 i P_106E_3
        przyjmuje wartość "true"), a także art. 106e ust.4 pkt 3 i ust. 5 pkt
        1-3 ustawy.

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_12}
        # TODO: Fill in the actual data
        return "0"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {01d75843}

    def getP_2B(self):
        """Kolejny numer faktury, nadany w ramach jednej lub więcej serii, który
        w sposób jednoznaczny indentyfikuje fakturę

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_2B}
        # TODO: Fill in the actual data
        return "P_2B"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {294abda3}

    def getP_7(self):
        """Nazwa (rodzaj) towaru lub usługi. Pole opcjonalne wyłącznie dla
        przypadku określonego w art 106j ust.3 pkt 2 ustawy (faktura korekta)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_7}
        # TODO: Fill in the actual data
        return "P_7"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {79362f30}

    def getP_8A(self):
        """Miara dostarczonych towarów lub zakres wykonanych usług. Pole
        opcjonalne dla przypadku określonego w art 106e ust. 5 pkt 3 ustawy.

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_8A}
        # TODO: Fill in the actual data
        return "P_8A"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {991b5e48}

    def getP_8B(self):
        """Ilość (liczba) dostarczonych towarów lub zakres wykonanych usług.
        Pole opcjonalne dla przypadku określonego w art 106e ust. 5 pkt 3
        ustawy.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_8B}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_9A(self):
        """Cena jednostkowa towaru lub usługi bez kwoty podatku (cena
        jednostkowa netto). Pole opcjonalne dla przypadków określonych w art.
        106e ust.2 i 3 ustawy (gdy przynajmniej jedno z pól P_106E_2 i P_106E_3
        przyjmuje wartość "true") oraz dla przypadku określonego w art 106e ust.
        5 pkt 3 ustawy.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_9A}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_9B(self):
        """W przypadku zastosowania art.106e ustawy, cena wraz z kwotą podatku
        (cena jednostkowa brutto)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaWiersz:getP_9B}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def gettyp(self):
        """@returns string"""
        return "G"


class Element_JPK_FakturaCtrl(object):
    """Sumy kontrolne dla faktur"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaFaktur(self):
        """Liczba faktur, w okresie którego dotyczy JPK_FA

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaCtrl:getLiczbaFaktur}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getWartoscFaktur(self):
        """Łączna wartość kwot brutto faktur w okresie, którego dotyczy JPK_FA

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_FakturaCtrl:getWartoscFaktur}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_Faktura(object):
    """Na podstawie art.106 a-q ustawy z 11 marca 2004 r. o podatku od towarów i
    usług /Dz.U. z 2011 r. Nr 177, poz. 1054, z późn. zm./
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNrFaKorygowanej(self):
        """Numer faktury korygowanej

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getNrFaKorygowanej}
        # TODO: Fill in the actual data
        return "NrFaKorygowanej"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ca72bd17}

    def getOkresFaKorygowanej(self):
        """Dla faktury korygującej - okres, do którego odnosi się udzielany
        opust lub obniżka, w przypadku gdy podatnik udziela opustu lub obniżki
        ceny w odniesieniu do wszystkich dostaw towarów lub usług dokonanych lub
        świadczonych na rzecz jednego odbiorcy w danym okresie

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getOkresFaKorygowanej}
        # TODO: Fill in the actual data
        return "OkresFaKorygowanej"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3385616f}

    def getP_1(self):
        """Data wystawienia

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_1}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getP_106E_2(self):
        """W przypadku świadczenia usług turystyki, dla których podstawę
        opodatkowania stanowi zgodnie z art. 119 ust. 1 kwota marży, faktura - w
        zakresie danych określonych w ust. 1 pkt 1-17 - powinna zawierać
        wyłącznie dane określone w ust. 1 pkt 1-8 i 15-17, a także wyrazy
        "procedura marży dla biur podróży", należy podać wartość "true"; w
        przeciwnym przypadku - wartość - "false"


        @returns bool
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_106E_2}
        # TODO: Fill in the actual data
        return False
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c5251bcb}

    def getP_106E_3(self):
        """W przypadku dostawy towarów używanych, dzieł sztuki, przedmiotów
        kolekcjonerskich i antyków, dla których podstawę opodatkowania stanowi
        zgodnie z art. 120 ust. 4 i 5 marża, należy podać wartość "true"; w
        przeciwnym przypadku - wartość - "false"

        @returns bool
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_106E_3}
        # TODO: Fill in the actual data
        return False
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c5251bcb}

    def getP_106E_3A(self):
        """Jeżeli pole P_106E_3 równa się wartości "true", należy podać wyrazy:
        "procedura marży - towary używane" lub "procedura marży - dzieła sztuki"
        lub "procedura marży - przedmioty kolekcjonerskie i antyki"

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_106E_3A}
        # TODO: Fill in the actual data
        return "false"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a2e98aaa}

    def getP_13_1(self):
        """Suma wartości sprzedaży netto ze stawką podstawową - aktualnie 23%
        albo 22%.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_13_1}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_13_2(self):
        """Suma wartości sprzedaży netto ze stawką obniżoną pierwszą - aktualnie
        8 % albo 7%.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_13_2}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_13_3(self):
        """Suma wartości sprzedaży netto ze stawką obniżoną drugą - aktualnie
        5%.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_13_3}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_13_4(self):
        """Suma wartości sprzedaży netto ze stawką obniżoną trzecią - pole
        rezerwowe.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_13_4}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_13_5(self):
        """Suma wartości sprzedaży netto ze stawką obniżoną czwartą - pole
        rezerwowe.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_13_5}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_13_6(self):
        """Suma wartości sprzedaży netto ze stawką 0%. Pole opcjonalne dla
        przypadków określonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej
        jedno z pól P_106E_2 i P_106E_3 przyjmuje wartość "true"), a także art.
        106e ust. 4 pkt 3 i ust. 5 pkt 1-3 ustawy.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_13_6}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_13_7(self):
        """Suma wartości sprzedaży zwolnionej. Pole opcjonalne dla przypadków
        określonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z pól
        P_106E_2 i P_106E_3 przyjmuje wartość "true"), a także art. 106e ust. 4
        pkt 3 i ust. 5 pkt 1-3 ustawy.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_13_7}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_14_1(self):
        """Kwota podatku od sumy wartości sprzedaży netto ze stawką podstawową -
        aktualnie 23% albo 22%.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_14_1}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_14_2(self):
        """Kwota podatku od sumy wartości sprzedaży netto ze stawką obniżoną -
        aktualnie 8% albo 7%.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_14_2}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_14_3(self):
        """Kwota podatku od sumy wartości sprzedaży netto ze stawką obniżoną
        drugą - aktualnie 5%.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_14_3}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_14_4(self):
        """Kwota podatku od sumy wartości sprzedaży netto ze stawką obniżoną
        trzecią - pole rezerwowe.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_14_4}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_14_5(self):
        """Kwota podatku od sumy wartości sprzedaży netto ze stawką obniżoną
        czwartą - pole rezerwowe.

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_14_5}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_15(self):
        """Kwota należności ogółem

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_15}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_16(self):
        """W przypadku dostawy towarów lub świadczenia usług, w odniesieniu do
        których obowiązek podatkowy powstaje zgodnie z art. 19a ust. 5 pkt 1 lub
        art. 21 ust. 1 - wyrazy "metoda kasowa", należy podać wartość "true"; w
        przeciwnym przypadku - wartość - "false"

        @returns bool
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_16}
        # TODO: Fill in the actual data
        return False
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c5251bcb}

    def getP_17(self):
        """W przypadku faktur, o których mowa w art. 106d ust. 1 - wyraz
        "samofakturowanie", należy podać wartość "true"; w przeciwnym przypadku
        - wartość - "false"

        @returns bool
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_17}
        # TODO: Fill in the actual data
        return False
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c5251bcb}

    def getP_18(self):
        """W przypadku dostawy towarów lub wykonania usługi, dla których
        obowiązanym do rozliczenia podatku, podatku od wartości dodanej lub
        podatku o podobnym charakterze jest nabywca towaru lub usługi - wyrazy
        "odwrotne obciążenie", należy podać wartość "true"; w przeciwnym
        przypadku - wartość - "false"

        @returns bool
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_18}
        # TODO: Fill in the actual data
        return False
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c5251bcb}

    def getP_19(self):
        """W przypadku dostawy towarów lub świadczenia usług zwolnionych od
        podatku na podstawie art. 43 ust. 1, art. 113 ust. 1 i 9 albo przepisów
        wydanych na podstawie art. 82 ust. 3 należy podać wartość "true"; w
        przeciwnym przypadku - wartość - "false"

        @returns bool
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_19}
        # TODO: Fill in the actual data
        return False
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c5251bcb}

    def getP_19A(self):
        """Jeśli pole P_19 równa się "true" - należy wskazać przepis ustawy albo
        aktu wydanego na podstawie ustawy, na podstawie którego podatnik stosuje
        zwolnienie od podatku

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_19A}
        # TODO: Fill in the actual data
        return "false"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a2e98aaa}

    def getP_19B(self):
        """Jeśli pole P_19 równa się "true" - należy wskazać przepis dyrektywy
        2006/112/WE, który zwalnia od podatku taką dostawę towarów lub takie
        świadczenie usług

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_19B}
        # TODO: Fill in the actual data
        return "false"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a2e98aaa}

    def getP_19C(self):
        """Jeśli pole P_19 równa się "true" - należy wskazać inną podstawę
        prawną wskazującą na to, że dostawa towarów lub świadczenie usług
        korzysta ze zwolnienia


        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_19C}
        # TODO: Fill in the actual data
        return "false"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a2e98aaa}

    def getP_20(self):
        """W przypadku, o którym mowa w art. 106c ustawy należy podać wartość
        "true"; w przeciwnym przypadku - wartość - "false"

        @returns bool
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_20}
        # TODO: Fill in the actual data
        return False
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c5251bcb}

    def getP_20A(self):
        """Jeśli pole P_20 równa się "true" - należy podać nazwę organu
        egzekucyjnego lub imię i nazwisko komornika sądowego

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_20A}
        # TODO: Fill in the actual data
        return "P_20A"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6cac744f}

    def getP_20B(self):
        """Jeśli pole P_20 równa się "true" - należy podać adres organu
        egzekucyjnego lub komornika sądowego

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_20B}
        # TODO: Fill in the actual data
        return "P_20B"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {4190a869}

    def getP_21(self):
        """W przypadku faktur wystawianych w imieniu i na rzecz podatnika przez
        jego przedstawiciela podatkowego należy podać wartość "true"; w
        przeciwnym przypadku - wartość - "false"

        @returns bool
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_21}
        # TODO: Fill in the actual data
        return False
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c5251bcb}

    def getP_21A(self):
        """Jeśli pole P_21 równa się "true" - należy podać nazwę lub imię i
        nazwisko przedstawiciela podatkowego

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_21A}
        # TODO: Fill in the actual data
        return "false"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a2e98aaa}

    def getP_21B(self):
        """Jeśli pole P_21 równa się "true" - należy podać adres przedstawiciela
        podatkowego

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_21B}
        # TODO: Fill in the actual data
        return "false"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a2e98aaa}

    def getP_21C(self):
        """Jeśli pole P_21 równa się "true" - należy podać numer przedstawiciela
        podatkowego, za pomocą którego jest on zidentyfikowany na potrzeby
        podatku

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_21C}
        # TODO: Fill in the actual data
        return "false"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a2e98aaa}

    def getP_22A(self):
        """Data dopuszczenia nowego środka transportu do użytku

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_22A}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getP_22B(self):
        """Przebieg pojazdu - w przypadku pojazdów lądowych, o których mowa w
        art. 2 pkt 10 lit. a ustawy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_22B}
        # TODO: Fill in the actual data
        return "P_22B"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1721472d}

    def getP_22C(self):
        """Liczba godzin roboczych używania nowego środka transportu - w
        przypadku jednostek pływających, o których mowa w art. 2 pkt 10 lit. b,
        oraz statków powietrznych, o których mowa w art. 2 pkt 10 lit. c ustawy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_22C}
        # TODO: Fill in the actual data
        return "P_22C"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {4a27a9cc}

    def getP_23(self):
        """W przypadku faktur wystawianych przez drugiego w kolejności
        podatnika, o którym mowa w art. 135 ust. 1 pkt 4 lit. b i c, w
        wewnątrzwspólnotowej transakcji trójstronnej (procedurze uproszczonej) -
        dane określone w art. 136, należy podać wartość "true"; w przeciwnym
        przypadku - wartość - "false"

        @returns bool
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_23}
        # TODO: Fill in the actual data
        return False
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c5251bcb}

    def getP_2A(self):
        """Kolejny numer faktury, nadany w ramach jednej lub więcej serii, który
        w sposób jednoznaczny indentyfikuje fakturę

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_2A}
        # TODO: Fill in the actual data
        return "P_2A"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {13499a64}

    def getP_3A(self):
        """Imię i nazwisko lub nazwa nabywcy towarów lub usług. Pole opcjonalne
        dla przypadku określonego w art. 106e ust. 5 pkt 3 ustawy.

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_3A}
        # TODO: Fill in the actual data
        return "P_3A"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {26e6c6f2}

    def getP_3B(self):
        """Adres nabywcy. Pole opcjonalne dla przypadku określonego w art. 106e
        ust. 5 pkt 3 ustawy.

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_3B}
        # TODO: Fill in the actual data
        return "P_3B"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e136568f}

    def getP_3C(self):
        """Imię i nazwisko lub nazwa sprzedawcy towarów lub usług

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_3C}
        # TODO: Fill in the actual data
        return "P_3C"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1d57ad01}

    def getP_3D(self):
        """Adres sprzedawcy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_3D}
        # TODO: Fill in the actual data
        return "P_3D"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2e7d2a2b}

    def getP_4A(self):
        """Kod (prefiks) podatnika VAT UE dla przypadków określonych w art. 97
        ust. 10 ustawy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_4A}
        # TODO: Fill in the actual data
        return "AT"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {581958c5}

    def getP_4B(self):
        """Numer, za pomocą którego podatnik jest zidentyfikowany na potrzeby
        podatku, z zastrzeżeniem pkt 24 lit. a ustawy. Pole opcjonalne dla
        przypadku określonego w art. 106e ust. 4 pkt 2 ustawy.

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_4B}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getP_5A(self):
        """Kod (prefiks) nabywcy - podatnika VAT UE dla przypadków określonych w
        art. 97 ust. 10 ustawy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_5A}
        # TODO: Fill in the actual data
        return "AT"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {581958c5}

    def getP_5B(self):
        """Numer, za pomocą którego nabywca towarów lub usług jest
        identyfikowany dla podatku lub podatku od wartości dodanej, pod którym
        otrzymał on towary lub usługi, z zastrzeżeniem pkt 24 lit. b ustawy.
        Pole opcjonalne dla przypadku określonego w art. 106e ust. 5 pkt 2
        ustawy.

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_5B}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getP_6(self):
        """Data dokonania lub zakończenia dostawy towarów lub wykonania usługi
        lub data otrzymania zapłaty, o której mowa w art. 106b ust. 1 pkt 4, o
        ile taka data jest określona i różni się od daty wystawienia faktury

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getP_6}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getPrzyczynaKorekty(self):
        """Przyczyna korekty dla faktur korygujących

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getPrzyczynaKorekty}
        # TODO: Fill in the actual data
        return "PrzyczynaKorekty"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {831e0fa7}

    def getRodzajFaktury(self):
        """Rodzaj faktury: VAT - podstawowa; KOREKTA - korygująca; ZAL - faktura
        dokumentująca otrzymanie zapłaty lub jej części przed dokonaniem
        czynności (art.106b ust. 1 pkt 4 ustawy); POZ - pozostałe

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getRodzajFaktury}
        # TODO: Fill in the actual data
        return "KOREKTA"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6e3afe76}

    def getZALPodatek(self):
        """Dla faktury zaliczkowej - kwota podatku wyliczona według wzoru z
        art.106f ust. 1 pkt 3 ustawy

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getZALPodatek}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getZALZaplata(self):
        """Dla faktury zaliczkowej - otrzymana kwota zapłaty

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Faktura:getZALZaplata}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def gettyp(self):
        """@returns string"""
        return "G"
