# Signature <<<efa40bcd>>>
# -*- coding: utf-8 -*-

import decimal
import datetime
from .bindings import Namespace
from xsd2xml import xmlgen
# vvv ONLY EDIT CODE BELOW THIS LINE vvv {imports}
# ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ecf8427e}

class TIdentyfikatorOsobyNiefizycznejPelny(object):
    """Pełny zestaw danych identyfikacyjnych o osobie niefizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznejPelny}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNIP(self):
        """Identyfikator podatkowy NIP

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznejPelny:getNIP}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getPelnaNazwa(self):
        """Pełna nazwa

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznejPelny:getPelnaNazwa}
        # TODO: Fill in the actual data
        return "PelnaNazwa"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {bdbaf47e}

    def getREGON(self):
        """Numer REGON

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznejPelny:getREGON}
        # TODO: Fill in the actual data
        return "742547345"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {0d00ae40}

    def getSkroconaNazwa(self):
        """Skrócona nazwa

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznejPelny:getSkroconaNazwa}
        # TODO: Fill in the actual data
        return "SkroconaNazwa"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {5e0b9872}


class TOsobaFizycznaPelna(object):
    """Pełny zestaw danych o osobie fizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizycznaPelna}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresZamieszkania(self):
        """@returns TOsobaFizycznaPelna_AdresZamieszkania"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizycznaPelna:getAdresZamieszkania}
        # TODO: Fill in the actual data
        return TOsobaFizycznaPelna_AdresZamieszkania()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b50dd2a4}

    def getOsobaFizyczna(self):
        """@returns TIdentyfikatorOsobyFizycznejPelny"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizycznaPelna:getOsobaFizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyFizycznejPelny()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6a08c99c}


class TOsobaNiefizycznaPelna(object):
    """Pełny zestaw danych o osobie fizycznej lub niefizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaNiefizycznaPelna}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresSiedziby(self):
        """@returns TOsobaNiefizycznaPelna_AdresSiedziby"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaNiefizycznaPelna:getAdresSiedziby}
        # TODO: Fill in the actual data
        return TOsobaNiefizycznaPelna_AdresSiedziby()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {791cd1a9}

    def getOsobaNiefizyczna(self):
        """@returns TIdentyfikatorOsobyNiefizycznejPelny"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaNiefizycznaPelna:getOsobaNiefizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyNiefizycznejPelny()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {d581c57b}


class TIdentyfikatorOsobyNiefizycznejZagranicznej(object):
    """Zestaw danych identyfikacyjnych dla osoby niefizycznej zagranicznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznejZagranicznej}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNIP(self):
        """Identyfikator podatkowy NIP [Tax Identification Number (NIP)]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznejZagranicznej:getNIP}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getPelnaNazwa(self):
        """Pełna nazwa [Name]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznejZagranicznej:getPelnaNazwa}
        # TODO: Fill in the actual data
        return "PelnaNazwa"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {bdbaf47e}

    def getSkroconaNazwa(self):
        """Nazwa skrócona [Short Name]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznejZagranicznej:getSkroconaNazwa}
        # TODO: Fill in the actual data
        return "SkroconaNazwa"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {5e0b9872}


class TPodmiotDowolnyBezAdresu(object):
    """Skrócony zestaw danych o osobie fizycznej lub niefizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyBezAdresu}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getOsobaFizyczna(self):
        """@returns TIdentyfikatorOsobyFizycznej"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyBezAdresu:getOsobaFizyczna}
        # TODO: Fill in the actual data
        return None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b5ba4e3f}

    def getOsobaNiefizyczna(self):
        """@returns TIdentyfikatorOsobyNiefizycznej"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyBezAdresu:getOsobaNiefizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyNiefizycznej()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8b6f02d1}


class TOsobaNiefizyczna(object):
    """Podstawowy zestaw danych o osobie niefizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaNiefizyczna}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresSiedziby(self):
        """@returns TOsobaNiefizyczna_AdresSiedziby"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaNiefizyczna:getAdresSiedziby}
        # TODO: Fill in the actual data
        return TOsobaNiefizyczna_AdresSiedziby()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {cfcd3b47}

    def getOsobaNiefizyczna(self):
        """@returns TIdentyfikatorOsobyNiefizycznej"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaNiefizyczna:getOsobaNiefizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyNiefizycznej()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8b6f02d1}


class TIdentyfikatorOsobyFizycznej1(object):
    """Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej z
    identyfikatorem NIP albo PESEL
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej1}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataUrodzenia(self):
        """Data urodzenia

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej1:getDataUrodzenia}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getImiePierwsze(self):
        """Pierwsze imię

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej1:getImiePierwsze}
        # TODO: Fill in the actual data
        return "ImiePierwsze"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {80eb5b24}

    def getNIP(self):
        """Identyfikator podatkowy NIP

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej1:getNIP}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getNazwisko(self):
        """Nazwisko

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej1:getNazwisko}
        # TODO: Fill in the actual data
        return "Nazwisko"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {959e55ca}

    def getPESEL(self):
        """Identyfikator podatkowy numer PESEL

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej1:getPESEL}
        # TODO: Fill in the actual data
        return None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ee342474}


class TIdentyfikatorOsobyFizycznej2(object):
    """Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej z
    identyfikatorem NIP
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej2}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataUrodzenia(self):
        """Data urodzenia

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej2:getDataUrodzenia}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getImiePierwsze(self):
        """Pierwsze imię

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej2:getImiePierwsze}
        # TODO: Fill in the actual data
        return "ImiePierwsze"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {80eb5b24}

    def getNIP(self):
        """Identyfikator podatkowy NIP

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej2:getNIP}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getNazwisko(self):
        """Nazwisko

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej2:getNazwisko}
        # TODO: Fill in the actual data
        return "Nazwisko"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {959e55ca}


class TPodmiotDowolnyBezAdresu2(object):
    """Skrócony zestaw danych o osobie fizycznej lub niefizycznej z
    identyfikatorem NIP
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyBezAdresu2}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getOsobaFizyczna(self):
        """@returns TIdentyfikatorOsobyFizycznej2"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyBezAdresu2:getOsobaFizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyFizycznej2()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b2a61957}

    def getOsobaNiefizyczna(self):
        """@returns TIdentyfikatorOsobyNiefizycznej"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyBezAdresu2:getOsobaNiefizyczna}
        # TODO: Fill in the actual data
        return None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8b6f02d1}


class TPodmiotDowolnyBezAdresu1(object):
    """Skrócony zestaw danych o osobie fizycznej lub niefizycznej z
    identyfikatorem NIP albo PESEL
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyBezAdresu1}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getOsobaFizyczna(self):
        """@returns TIdentyfikatorOsobyFizycznej1"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyBezAdresu1:getOsobaFizyczna}
        # TODO: Fill in the actual data
        return None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {050d7d47}

    def getOsobaNiefizyczna(self):
        """@returns TIdentyfikatorOsobyNiefizycznej"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyBezAdresu1:getOsobaNiefizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyNiefizycznej()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8b6f02d1}


class TOsobaFizyczna1(object):
    """Podstawowy zestaw danych o osobie fizycznej z identyfikatorem NIP albo
    PESEL
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna1}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresZamieszkania(self):
        """@returns TOsobaFizyczna1_AdresZamieszkania"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna1:getAdresZamieszkania}
        # TODO: Fill in the actual data
        return TOsobaFizyczna1_AdresZamieszkania()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {06693f97}

    def getOsobaFizyczna(self):
        """@returns TIdentyfikatorOsobyFizycznej1"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna1:getOsobaFizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyFizycznej1()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {050d7d47}


class TOsobaFizyczna2(object):
    """Podstawowy zestaw danych o osobie fizycznej z identyfikatorem NIP"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna2}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresZamieszkania(self):
        """@returns TOsobaFizyczna2_AdresZamieszkania"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna2:getAdresZamieszkania}
        # TODO: Fill in the actual data
        return TOsobaFizyczna2_AdresZamieszkania()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {49a9a6fa}

    def getOsobaFizyczna(self):
        """@returns TIdentyfikatorOsobyFizycznej2"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna2:getOsobaFizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyFizycznej2()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b2a61957}


class TAdresZagraniczny(object):
    """Informacje opisujące adres zagraniczny"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresZagraniczny}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getKodKraju(self):
        """Kod Kraju [Country Code]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresZagraniczny:getKodKraju}
        # TODO: Fill in the actual data
        return "AD"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2c2fc413}

    def getKodPocztowy(self):
        """Kod pocztowy [Postal code]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresZagraniczny:getKodPocztowy}
        # TODO: Fill in the actual data
        return "KodPoczt"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2e4aba9b}

    def getMiejscowosc(self):
        """Nazwa miejscowości [City]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresZagraniczny:getMiejscowosc}
        # TODO: Fill in the actual data
        return "Miejscowosc"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {48f8d7b1}

    def getNrDomu(self):
        """Numer budynku [Building number]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresZagraniczny:getNrDomu}
        # TODO: Fill in the actual data
        return "NrDomu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f2d99da1}

    def getNrLokalu(self):
        """Numer lokalu [Flat number]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresZagraniczny:getNrLokalu}
        # TODO: Fill in the actual data
        return "NrLokalu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {9231d8ec}

    def getUlica(self):
        """Nazwa ulicy [Street]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresZagraniczny:getUlica}
        # TODO: Fill in the actual data
        return "Ulica"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {42dc0012}


class TIdentyfikatorOsobyFizycznejZagranicznej(object):
    """Zestaw danych identyfikacyjnych dla osoby fizycznej zagranicznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejZagranicznej}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataUrodzenia(self):
        """Data urodzenia [Date of Birth]

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejZagranicznej:getDataUrodzenia}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getImieMatki(self):
        """Imię matki [Mother’s name]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejZagranicznej:getImieMatki}
        # TODO: Fill in the actual data
        return "ImieMatki"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {948ea119}

    def getImieOjca(self):
        """Imię ojca [Father’s name]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejZagranicznej:getImieOjca}
        # TODO: Fill in the actual data
        return "ImieOjca"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e0e5d121}

    def getImiePierwsze(self):
        """Imię pierwsze [First name]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejZagranicznej:getImiePierwsze}
        # TODO: Fill in the actual data
        return "ImiePierwsze"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {80eb5b24}

    def getMiejsceUrodzenia(self):
        """Miejsce urodzenia [Place of Birth]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejZagranicznej:getMiejsceUrodzenia}
        # TODO: Fill in the actual data
        return "MiejsceUrodzenia"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1c38bfd3}

    def getNIP(self):
        """Identyfikator podatkowy NIP [Tax Identification Number (NIP)]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejZagranicznej:getNIP}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getNazwisko(self):
        """Nazwisko [Family name]

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejZagranicznej:getNazwisko}
        # TODO: Fill in the actual data
        return "Nazwisko"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {959e55ca}


class TIdentyfikatorOsobyFizycznejPelny(object):
    """Pełny zestaw danych identyfikacyjnych o osobie fizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejPelny}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataUrodzenia(self):
        """Data urodzenia

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejPelny:getDataUrodzenia}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getImieMatki(self):
        """Imię matki

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejPelny:getImieMatki}
        # TODO: Fill in the actual data
        return "ImieMatki"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {948ea119}

    def getImieOjca(self):
        """Imię ojca

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejPelny:getImieOjca}
        # TODO: Fill in the actual data
        return "ImieOjca"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e0e5d121}

    def getImiePierwsze(self):
        """Pierwsze imię

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejPelny:getImiePierwsze}
        # TODO: Fill in the actual data
        return "ImiePierwsze"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {80eb5b24}

    def getNIP(self):
        """Identyfikator podatkowy NIP

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejPelny:getNIP}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getNazwisko(self):
        """Nazwisko

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejPelny:getNazwisko}
        # TODO: Fill in the actual data
        return "Nazwisko"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {959e55ca}

    def getPESEL(self):
        """Identyfikator podatkowy numer PESEL

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznejPelny:getPESEL}
        # TODO: Fill in the actual data
        return "74254734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ee342474}


class TPodmiotDowolnyPelny(object):
    """Pełny zestaw danych o osobie fizycznej lub niefizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyPelny}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresZamieszkaniaSiedziby(self):
        """@returns TPodmiotDowolnyPelny_AdresZamieszkaniaSiedziby"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyPelny:getAdresZamieszkaniaSiedziby}
        # TODO: Fill in the actual data
        return TPodmiotDowolnyPelny_AdresZamieszkaniaSiedziby()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b6cfb5ab}

    def getOsobaFizyczna(self):
        """@returns TIdentyfikatorOsobyFizycznejPelny"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyPelny:getOsobaFizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyFizycznejPelny()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6a08c99c}

    def getOsobaNiefizyczna(self):
        """@returns TIdentyfikatorOsobyNiefizycznejPelny"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyPelny:getOsobaNiefizyczna}
        # TODO: Fill in the actual data
        return None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {d581c57b}


class TIdentyfikatorOsobyNiefizycznej(object):
    """Podstawowy zestaw danych identyfikacyjnych o osobie niefizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznej}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNIP(self):
        """Identyfikator podatkowy NIP

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznej:getNIP}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getPelnaNazwa(self):
        """Pełna nazwa

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznej:getPelnaNazwa}
        # TODO: Fill in the actual data
        return "PelnaNazwa"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {bdbaf47e}

    def getREGON(self):
        """Numer REGON

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyNiefizycznej:getREGON}
        # TODO: Fill in the actual data
        return "742547345"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {0d00ae40}


class TOsobaFizyczna(object):
    """Podstawowy zestaw danych o osobie fizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresZamieszkania(self):
        """@returns TOsobaFizyczna_AdresZamieszkania"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna:getAdresZamieszkania}
        # TODO: Fill in the actual data
        return TOsobaFizyczna_AdresZamieszkania()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {0f98dfef}

    def getOsobaFizyczna(self):
        """@returns TIdentyfikatorOsobyFizycznej"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna:getOsobaFizyczna}
        # TODO: Fill in the actual data
        return TIdentyfikatorOsobyFizycznej()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b5ba4e3f}


class TAdresPolski(object):
    """Informacje opisujące adres polski"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getGmina(self):
        """Gmina

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski:getGmina}
        # TODO: Fill in the actual data
        return "Gmina"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {db051a86}

    def getKodKraju(self):
        """Kraj

        @returns string
        """
        return "PL"

    def getKodPocztowy(self):
        """Kod pocztowy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski:getKodPocztowy}
        # TODO: Fill in the actual data
        return "KodPoczt"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2e4aba9b}

    def getMiejscowosc(self):
        """Nazwa miejscowości

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski:getMiejscowosc}
        # TODO: Fill in the actual data
        return "Miejscowosc"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {48f8d7b1}

    def getNrDomu(self):
        """Numer budynku

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski:getNrDomu}
        # TODO: Fill in the actual data
        return "NrDomu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f2d99da1}

    def getNrLokalu(self):
        """Numer lokalu

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski:getNrLokalu}
        # TODO: Fill in the actual data
        return "NrLokalu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {9231d8ec}

    def getPoczta(self):
        """Nazwa urzędu pocztowego

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski:getPoczta}
        # TODO: Fill in the actual data
        return "Poczta"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a3cc6d62}

    def getPowiat(self):
        """Powiat

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski:getPowiat}
        # TODO: Fill in the actual data
        return "Powiat"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {871f1b15}

    def getUlica(self):
        """Nazwa ulicy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski:getUlica}
        # TODO: Fill in the actual data
        return "Ulica"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {42dc0012}

    def getWojewodztwo(self):
        """Województwo

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdresPolski:getWojewodztwo}
        # TODO: Fill in the actual data
        return "Wojewodztwo"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e0f65118}


class TAdres(object):
    """Dane określające adres"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdres}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresPol(self):
        """@returns TAdresPolski"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdres:getAdresPol}
        # TODO: Fill in the actual data
        return TAdresPolski()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7c25ec06}

    def getAdresZagr(self):
        """@returns TAdresZagraniczny"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TAdres:getAdresZagr}
        # TODO: Fill in the actual data
        return None
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {61be35ef}


class TIdentyfikatorOsobyFizycznej(object):
    """Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataUrodzenia(self):
        """Data urodzenia

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej:getDataUrodzenia}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getImiePierwsze(self):
        """Pierwsze imię

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej:getImiePierwsze}
        # TODO: Fill in the actual data
        return "ImiePierwsze"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {80eb5b24}

    def getNIP(self):
        """Identyfikator podatkowy NIP

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej:getNIP}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getNazwisko(self):
        """Nazwisko

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej:getNazwisko}
        # TODO: Fill in the actual data
        return "Nazwisko"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {959e55ca}

    def getPESEL(self):
        """Identyfikator podatkowy numer PESEL

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TIdentyfikatorOsobyFizycznej:getPESEL}
        # TODO: Fill in the actual data
        return "74254734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ee342474}


class TOsobaFizycznaPelna_AdresZamieszkania(TAdres):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizycznaPelna_AdresZamieszkania}
    def __init__(self, *args, **kwargs):
        super(TOsobaFizycznaPelna_AdresZamieszkania, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {af8341ec}

    def getrodzajAdresu(self):
        """@returns string"""
        return "RAD"


class TOsobaNiefizycznaPelna_AdresSiedziby(TAdres):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaNiefizycznaPelna_AdresSiedziby}
    def __init__(self, *args, **kwargs):
        super(TOsobaNiefizycznaPelna_AdresSiedziby, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ef62e60f}

    def getrodzajAdresu(self):
        """@returns string"""
        return "RAD"


class TPodmiotDowolny(TPodmiotDowolnyBezAdresu):
    """Podstawowy zestaw danych o osobie fizycznej lub niefizycznej"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolny}
    def __init__(self, *args, **kwargs):
        super(TPodmiotDowolny, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {241c144e}

    def getAdresZamieszkaniaSiedziby(self):
        """@returns TPodmiotDowolny_AdresZamieszkaniaSiedziby"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolny:getAdresZamieszkaniaSiedziby}
        # TODO: Fill in the actual data
        return TPodmiotDowolny_AdresZamieszkaniaSiedziby()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {76ce3d26}


class TPodmiotDowolny_AdresZamieszkaniaSiedziby(TAdres):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolny_AdresZamieszkaniaSiedziby}
    def __init__(self, *args, **kwargs):
        super(TPodmiotDowolny_AdresZamieszkaniaSiedziby, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {5200d31f}

    def getrodzajAdresu(self):
        """@returns string"""
        return "RAD"


class TOsobaNiefizyczna_AdresSiedziby(TAdres):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaNiefizyczna_AdresSiedziby}
    def __init__(self, *args, **kwargs):
        super(TOsobaNiefizyczna_AdresSiedziby, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c15e037e}

    def getrodzajAdresu(self):
        """@returns string"""
        return "RAD"


class TOsobaFizyczna1_AdresZamieszkania(TAdres):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna1_AdresZamieszkania}
    def __init__(self, *args, **kwargs):
        super(TOsobaFizyczna1_AdresZamieszkania, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1bff32e5}

    def getrodzajAdresu(self):
        """@returns string"""
        return "RAD"


class TOsobaFizyczna2_AdresZamieszkania(TAdres):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna2_AdresZamieszkania}
    def __init__(self, *args, **kwargs):
        super(TOsobaFizyczna2_AdresZamieszkania, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7e32cafa}

    def getrodzajAdresu(self):
        """@returns string"""
        return "RAD"


class TPodmiotDowolnyPelny_AdresZamieszkaniaSiedziby(TAdres):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TPodmiotDowolnyPelny_AdresZamieszkaniaSiedziby}
    def __init__(self, *args, **kwargs):
        super(TPodmiotDowolnyPelny_AdresZamieszkaniaSiedziby, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {209346ea}

    def getrodzajAdresu(self):
        """@returns string"""
        return "RAD"


class TOsobaFizyczna_AdresZamieszkania(TAdres):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TOsobaFizyczna_AdresZamieszkania}
    def __init__(self, *args, **kwargs):
        super(TOsobaFizyczna_AdresZamieszkania, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {80401b09}

    def getrodzajAdresu(self):
        """@returns string"""
        return "RAD"
