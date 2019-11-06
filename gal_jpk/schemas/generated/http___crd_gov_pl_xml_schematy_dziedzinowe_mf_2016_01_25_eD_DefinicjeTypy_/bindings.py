# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:23b1b549e4f2cf041fd6dce67b996e1d09162b97
# Generated 2018-03-08 13:30:04.720595 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ [xmlns:etd]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6998c690-22cc-11e8-9d15-8c705ac2b4bc')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TZnakowy
class TZnakowy (pyxb.binding.datatypes.token):

    """Typ znakowy ograniczony do jednej linii"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TZnakowy')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 8, 1)
    _Documentation = 'Typ znakowy ograniczony do jednej linii'
TZnakowy._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TZnakowy._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(240))
TZnakowy._InitializeFacetMap(TZnakowy._CF_minLength,
   TZnakowy._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TZnakowy', TZnakowy)
_module_typeBindings.TZnakowy = TZnakowy

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TTekstowy
class TTekstowy (pyxb.binding.datatypes.string):

    """Typ znakowy ograniczony do 3500 znaków"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TTekstowy')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 17, 1)
    _Documentation = 'Typ znakowy ograniczony do 3500 znak\xf3w'
TTekstowy._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TTekstowy._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3500))
TTekstowy._InitializeFacetMap(TTekstowy._CF_minLength,
   TTekstowy._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TTekstowy', TTekstowy)
_module_typeBindings.TTekstowy = TTekstowy

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TProcentowy
class TProcentowy (pyxb.binding.datatypes.decimal):

    """Wartość procentowa z dokładnością do 2 miejsc po przecinku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TProcentowy')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 26, 1)
    _Documentation = 'Warto\u015b\u0107 procentowa z dok\u0142adno\u015bci\u0105 do 2 miejsc po przecinku'
TProcentowy._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
TProcentowy._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TProcentowy._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TProcentowy, value=pyxb.binding.datatypes.decimal('0.0'))
TProcentowy._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5))
TProcentowy._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=TProcentowy, value=pyxb.binding.datatypes.decimal('100.0'))
TProcentowy._InitializeFacetMap(TProcentowy._CF_whiteSpace,
   TProcentowy._CF_fractionDigits,
   TProcentowy._CF_minInclusive,
   TProcentowy._CF_totalDigits,
   TProcentowy._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'TProcentowy', TProcentowy)
_module_typeBindings.TProcentowy = TProcentowy

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TCalkowity
class TCalkowity (pyxb.binding.datatypes.int):

    """Liczby naturalne"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCalkowity')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 38, 1)
    _Documentation = 'Liczby naturalne'
TCalkowity._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
TCalkowity._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14))
TCalkowity._InitializeFacetMap(TCalkowity._CF_whiteSpace,
   TCalkowity._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TCalkowity', TCalkowity)
_module_typeBindings.TCalkowity = TCalkowity

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNaturalny
class TNaturalny (pyxb.binding.datatypes.nonNegativeInteger):

    """Liczby naturalne"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaturalny')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 47, 1)
    _Documentation = 'Liczby naturalne'
TNaturalny._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
TNaturalny._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14))
TNaturalny._InitializeFacetMap(TNaturalny._CF_whiteSpace,
   TNaturalny._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TNaturalny', TNaturalny)
_module_typeBindings.TNaturalny = TNaturalny

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKwota2
class TKwota2 (pyxb.binding.datatypes.decimal):

    """Wartość kwotowa wykazana w zł i gr"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwota2')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 64, 1)
    _Documentation = 'Warto\u015b\u0107 kwotowa wykazana w z\u0142 i gr'
TKwota2._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
TKwota2._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TKwota2._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(16))
TKwota2._InitializeFacetMap(TKwota2._CF_whiteSpace,
   TKwota2._CF_fractionDigits,
   TKwota2._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TKwota2', TKwota2)
_module_typeBindings.TKwota2 = TKwota2

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKwotaC
class TKwotaC (pyxb.binding.datatypes.integer):

    """Wartość kwotowa wykazana w zł"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwotaC')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 74, 1)
    _Documentation = 'Warto\u015b\u0107 kwotowa wykazana w z\u0142'
TKwotaC._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14))
TKwotaC._InitializeFacetMap(TKwotaC._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TKwotaC', TKwotaC)
_module_typeBindings.TKwotaC = TKwotaC

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TData
class TData (pyxb.binding.datatypes.date):

    """Typ daty"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TData')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 98, 1)
    _Documentation = 'Typ daty'
TData._CF_pattern = pyxb.binding.facets.CF_pattern()
TData._CF_pattern.addPattern(pattern='((\\d{4})-(\\d{2})-(\\d{2}))')
TData._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TData, value=pyxb.binding.datatypes.date('1900-01-01'))
TData._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=TData, value=pyxb.binding.datatypes.date('2030-12-31'))
TData._InitializeFacetMap(TData._CF_pattern,
   TData._CF_minInclusive,
   TData._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'TData', TData)
_module_typeBindings.TData = TData

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TDataCzas
class TDataCzas (pyxb.binding.datatypes.dateTime):

    """Typ daty i godziny"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TDataCzas')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 108, 1)
    _Documentation = 'Typ daty i godziny'
TDataCzas._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
TDataCzas._InitializeFacetMap(TDataCzas._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TDataCzas', TDataCzas)
_module_typeBindings.TDataCzas = TDataCzas

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TRok
class TRok (pyxb.binding.datatypes.gYear):

    """Oznaczenie roku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TRok')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 116, 1)
    _Documentation = 'Oznaczenie roku'
TRok._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TRok, value=pyxb.binding.datatypes.gYear('1900'))
TRok._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=TRok, value=pyxb.binding.datatypes.gYear('2030'))
TRok._InitializeFacetMap(TRok._CF_minInclusive,
   TRok._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'TRok', TRok)
_module_typeBindings.TRok = TRok

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TMiesiac
class TMiesiac (pyxb.binding.datatypes.byte):

    """Element będący numerem miesiąca"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TMiesiac')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 125, 1)
    _Documentation = 'Element b\u0119d\u0105cy numerem miesi\u0105ca'
TMiesiac._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TMiesiac, value=pyxb.binding.datatypes.byte(1))
TMiesiac._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=TMiesiac, value=pyxb.binding.datatypes.byte(12))
TMiesiac._InitializeFacetMap(TMiesiac._CF_minInclusive,
   TMiesiac._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'TMiesiac', TMiesiac)
_module_typeBindings.TMiesiac = TMiesiac

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKwartal
class TKwartal (pyxb.binding.datatypes.byte):

    """Element będący numerem kwartału"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwartal')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 134, 1)
    _Documentation = 'Element b\u0119d\u0105cy numerem kwarta\u0142u'
TKwartal._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TKwartal, value=pyxb.binding.datatypes.byte(1))
TKwartal._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=TKwartal, value=pyxb.binding.datatypes.byte(4))
TKwartal._InitializeFacetMap(TKwartal._CF_minInclusive,
   TKwartal._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'TKwartal', TKwartal)
_module_typeBindings.TKwartal = TKwartal

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrNIP
class TNrNIP (pyxb.binding.datatypes.string):

    """Identyfikator podatkowy NIP"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrNIP')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 152, 1)
    _Documentation = 'Identyfikator podatkowy NIP'
TNrNIP._CF_pattern = pyxb.binding.facets.CF_pattern()
TNrNIP._CF_pattern.addPattern(pattern='[1-9]((\\d[1-9])|([1-9]\\d))\\d{7}')
TNrNIP._InitializeFacetMap(TNrNIP._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TNrNIP', TNrNIP)
_module_typeBindings.TNrNIP = TNrNIP

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrPESEL
class TNrPESEL (pyxb.binding.datatypes.string):

    """Identyfikator podatkowy numer PESEL"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrPESEL')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 160, 1)
    _Documentation = 'Identyfikator podatkowy numer PESEL'
TNrPESEL._CF_pattern = pyxb.binding.facets.CF_pattern()
TNrPESEL._CF_pattern.addPattern(pattern='\\d{11}')
TNrPESEL._InitializeFacetMap(TNrPESEL._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TNrPESEL', TNrPESEL)
_module_typeBindings.TNrPESEL = TNrPESEL

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 173, 3)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='\\d{9}')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 178, 3)
    _Documentation = None
STD_ANON_._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_._CF_pattern.addPattern(pattern='\\d{14}')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_pattern)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrAKC
class TNrAKC (pyxb.binding.datatypes.string):

    """Numer akcyzowy"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrAKC')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 185, 1)
    _Documentation = 'Numer akcyzowy'
TNrAKC._CF_pattern = pyxb.binding.facets.CF_pattern()
TNrAKC._CF_pattern.addPattern(pattern='[A-Z]{2}\\d{11}')
TNrAKC._InitializeFacetMap(TNrAKC._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TNrAKC', TNrAKC)
_module_typeBindings.TNrAKC = TNrAKC

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrKRS
class TNrKRS (pyxb.binding.datatypes.string):

    """Numer Krajowego Rejestru Sądowego"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrKRS')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 193, 1)
    _Documentation = 'Numer Krajowego Rejestru S\u0105dowego'
TNrKRS._CF_pattern = pyxb.binding.facets.CF_pattern()
TNrKRS._CF_pattern.addPattern(pattern='\\d{10}')
TNrKRS._InitializeFacetMap(TNrKRS._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TNrKRS', TNrKRS)
_module_typeBindings.TNrKRS = TNrKRS

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrIdentyfikacjiPodatkowej
class TNrIdentyfikacjiPodatkowej (pyxb.binding.datatypes.string):

    """Numer służący identyfikacji dla celów podatkowych"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrIdentyfikacjiPodatkowej')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 201, 1)
    _Documentation = 'Numer s\u0142u\u017c\u0105cy identyfikacji dla cel\xf3w podatkowych'
TNrIdentyfikacjiPodatkowej._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.replace)
TNrIdentyfikacjiPodatkowej._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TNrIdentyfikacjiPodatkowej._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
TNrIdentyfikacjiPodatkowej._InitializeFacetMap(TNrIdentyfikacjiPodatkowej._CF_whiteSpace,
   TNrIdentyfikacjiPodatkowej._CF_minLength,
   TNrIdentyfikacjiPodatkowej._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TNrIdentyfikacjiPodatkowej', TNrIdentyfikacjiPodatkowej)
_module_typeBindings.TNrIdentyfikacjiPodatkowej = TNrIdentyfikacjiPodatkowej

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrDokumentuStwierdzajacegoTozsamosc
class TNrDokumentuStwierdzajacegoTozsamosc (pyxb.binding.datatypes.string):

    """Numer dokumentu stwierdzającego tożsamość"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrDokumentuStwierdzajacegoTozsamosc')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 211, 1)
    _Documentation = 'Numer dokumentu stwierdzaj\u0105cego to\u017csamo\u015b\u0107'
TNrDokumentuStwierdzajacegoTozsamosc._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.replace)
TNrDokumentuStwierdzajacegoTozsamosc._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TNrDokumentuStwierdzajacegoTozsamosc._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
TNrDokumentuStwierdzajacegoTozsamosc._InitializeFacetMap(TNrDokumentuStwierdzajacegoTozsamosc._CF_whiteSpace,
   TNrDokumentuStwierdzajacegoTozsamosc._CF_minLength,
   TNrDokumentuStwierdzajacegoTozsamosc._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TNrDokumentuStwierdzajacegoTozsamosc', TNrDokumentuStwierdzajacegoTozsamosc)
_module_typeBindings.TNrDokumentuStwierdzajacegoTozsamosc = TNrDokumentuStwierdzajacegoTozsamosc

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TImie
class TImie (pyxb.binding.datatypes.token):

    """Pierwsze imię"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TImie')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 221, 1)
    _Documentation = 'Pierwsze imi\u0119'
TImie._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TImie._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
TImie._InitializeFacetMap(TImie._CF_minLength,
   TImie._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TImie', TImie)
_module_typeBindings.TImie = TImie

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TMiejscowosc
class TMiejscowosc (pyxb.binding.datatypes.token):

    """Typ określający nazwę miejscowości"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TMiejscowosc')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 230, 1)
    _Documentation = 'Typ okre\u015blaj\u0105cy nazw\u0119 miejscowo\u015bci'
TMiejscowosc._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TMiejscowosc._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(56))
TMiejscowosc._InitializeFacetMap(TMiejscowosc._CF_minLength,
   TMiejscowosc._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TMiejscowosc', TMiejscowosc)
_module_typeBindings.TMiejscowosc = TMiejscowosc

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNazwisko
class TNazwisko (pyxb.binding.datatypes.token):

    """Nazwisko"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNazwisko')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 239, 1)
    _Documentation = 'Nazwisko'
TNazwisko._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TNazwisko._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(81))
TNazwisko._InitializeFacetMap(TNazwisko._CF_minLength,
   TNazwisko._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TNazwisko', TNazwisko)
_module_typeBindings.TNazwisko = TNazwisko

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TJednAdmin
class TJednAdmin (pyxb.binding.datatypes.token):

    """Typ określający nazwę województwa, nazwę powiatu lub nazwę gminy"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TJednAdmin')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 248, 1)
    _Documentation = 'Typ okre\u015blaj\u0105cy nazw\u0119 wojew\xf3dztwa, nazw\u0119 powiatu lub nazw\u0119 gminy'
TJednAdmin._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TJednAdmin._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(36))
TJednAdmin._InitializeFacetMap(TJednAdmin._CF_minLength,
   TJednAdmin._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TJednAdmin', TJednAdmin)
_module_typeBindings.TJednAdmin = TJednAdmin

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKodKrajuUrodzenia
class TKodKrajuUrodzenia (pyxb.binding.datatypes.string):

    """Kod kraju urodzenia"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodKrajuUrodzenia')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 289, 1)
    _Documentation = 'Kod kraju urodzenia'
TKodKrajuUrodzenia._CF_pattern = pyxb.binding.facets.CF_pattern()
TKodKrajuUrodzenia._CF_pattern.addPattern(pattern='[A-Z]{2}')
TKodKrajuUrodzenia._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TKodKrajuUrodzenia._InitializeFacetMap(TKodKrajuUrodzenia._CF_pattern,
   TKodKrajuUrodzenia._CF_length)
Namespace.addCategoryObject('typeBinding', 'TKodKrajuUrodzenia', TKodKrajuUrodzenia)
_module_typeBindings.TKodKrajuUrodzenia = TKodKrajuUrodzenia

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TCelZlozenia
class TCelZlozenia (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Określa, czy to jest złożenie, czy korekta dokumentu"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCelZlozenia')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 307, 1)
    _Documentation = 'Okre\u015bla, czy to jest z\u0142o\u017cenie, czy korekta dokumentu'
TCelZlozenia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TCelZlozenia, enum_prefix=None)
TCelZlozenia._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
TCelZlozenia._CF_enumeration.addEnumeration(unicode_value='2', tag=None)
TCelZlozenia._InitializeFacetMap(TCelZlozenia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TCelZlozenia', TCelZlozenia)
_module_typeBindings.TCelZlozenia = TCelZlozenia

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TWybor1
class TWybor1 (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Pojedyncze pole wyboru"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TWybor1')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 333, 1)
    _Documentation = 'Pojedyncze pole wyboru'
TWybor1._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TWybor1, enum_prefix=None)
TWybor1._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
TWybor1._InitializeFacetMap(TWybor1._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TWybor1', TWybor1)
_module_typeBindings.TWybor1 = TWybor1

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TWybor1_2
class TWybor1_2 (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Podwójne pole wyboru"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TWybor1_2')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 341, 1)
    _Documentation = 'Podw\xf3jne pole wyboru'
TWybor1_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TWybor1_2, enum_prefix=None)
TWybor1_2._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
TWybor1_2._CF_enumeration.addEnumeration(unicode_value='2', tag=None)
TWybor1_2._InitializeFacetMap(TWybor1_2._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TWybor1_2', TWybor1_2)
_module_typeBindings.TWybor1_2 = TWybor1_2

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TWybor1_3
class TWybor1_3 (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Potrójne pole wyboru"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TWybor1_3')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 350, 1)
    _Documentation = 'Potr\xf3jne pole wyboru'
TWybor1_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TWybor1_3, enum_prefix=None)
TWybor1_3._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
TWybor1_3._CF_enumeration.addEnumeration(unicode_value='2', tag=None)
TWybor1_3._CF_enumeration.addEnumeration(unicode_value='3', tag=None)
TWybor1_3._InitializeFacetMap(TWybor1_3._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TWybor1_3', TWybor1_3)
_module_typeBindings.TWybor1_3 = TWybor1_3

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKodKraju
class TKodKraju (pyxb.binding.datatypes.normalizedString, pyxb.binding.basis.enumeration_mixin):

    """Słownik kodów krajów"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodKraju')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/KodyKrajow_v4-1E.xsd', 6, 1)
    _Documentation = 'S\u0142ownik kod\xf3w kraj\xf3w'
TKodKraju._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodKraju, enum_prefix=None)
TKodKraju.AF = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AF', tag='AF')
TKodKraju.AX = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AX', tag='AX')
TKodKraju.AL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
TKodKraju.DZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='DZ', tag='DZ')
TKodKraju.AD = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AD', tag='AD')
TKodKraju.AO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AO', tag='AO')
TKodKraju.AI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AI', tag='AI')
TKodKraju.AQ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AQ', tag='AQ')
TKodKraju.AG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AG', tag='AG')
TKodKraju.AN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AN', tag='AN')
TKodKraju.SA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SA', tag='SA')
TKodKraju.AR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AR', tag='AR')
TKodKraju.AM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AM', tag='AM')
TKodKraju.AW = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AW', tag='AW')
TKodKraju.AU = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AU', tag='AU')
TKodKraju.AT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AT', tag='AT')
TKodKraju.AZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AZ', tag='AZ')
TKodKraju.BS = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BS', tag='BS')
TKodKraju.BH = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BH', tag='BH')
TKodKraju.BD = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BD', tag='BD')
TKodKraju.BB = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BB', tag='BB')
TKodKraju.BE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BE', tag='BE')
TKodKraju.BZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BZ', tag='BZ')
TKodKraju.BJ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BJ', tag='BJ')
TKodKraju.BM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BM', tag='BM')
TKodKraju.BT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BT', tag='BT')
TKodKraju.BY = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BY', tag='BY')
TKodKraju.BO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BO', tag='BO')
TKodKraju.BA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BA', tag='BA')
TKodKraju.BW = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BW', tag='BW')
TKodKraju.BR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BR', tag='BR')
TKodKraju.BN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BN', tag='BN')
TKodKraju.IO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='IO', tag='IO')
TKodKraju.BG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BG', tag='BG')
TKodKraju.BF = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BF', tag='BF')
TKodKraju.BI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BI', tag='BI')
TKodKraju.XC = TKodKraju._CF_enumeration.addEnumeration(unicode_value='XC', tag='XC')
TKodKraju.CL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CL', tag='CL')
TKodKraju.CN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CN', tag='CN')
TKodKraju.HR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='HR', tag='HR')
TKodKraju.CY = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CY', tag='CY')
TKodKraju.TD = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TD', tag='TD')
TKodKraju.ME = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ME', tag='ME')
TKodKraju.DK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='DK', tag='DK')
TKodKraju.DM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='DM', tag='DM')
TKodKraju.DO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='DO', tag='DO')
TKodKraju.DJ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='DJ', tag='DJ')
TKodKraju.EG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='EG', tag='EG')
TKodKraju.EC = TKodKraju._CF_enumeration.addEnumeration(unicode_value='EC', tag='EC')
TKodKraju.ER = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
TKodKraju.EE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='EE', tag='EE')
TKodKraju.ET = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ET', tag='ET')
TKodKraju.FK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='FK', tag='FK')
TKodKraju.FJ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='FJ', tag='FJ')
TKodKraju.PH = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PH', tag='PH')
TKodKraju.FI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='FI', tag='FI')
TKodKraju.FR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='FR', tag='FR')
TKodKraju.TF = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TF', tag='TF')
TKodKraju.GA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GA', tag='GA')
TKodKraju.GM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GM', tag='GM')
TKodKraju.GH = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GH', tag='GH')
TKodKraju.GI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GI', tag='GI')
TKodKraju.GR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GR', tag='GR')
TKodKraju.GD = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GD', tag='GD')
TKodKraju.GL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GL', tag='GL')
TKodKraju.GE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GE', tag='GE')
TKodKraju.GU = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GU', tag='GU')
TKodKraju.GG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GG', tag='GG')
TKodKraju.GY = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GY', tag='GY')
TKodKraju.GF = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GF', tag='GF')
TKodKraju.GP = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GP', tag='GP')
TKodKraju.GT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
TKodKraju.GN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GN', tag='GN')
TKodKraju.GQ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GQ', tag='GQ')
TKodKraju.GW = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
TKodKraju.HT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='HT', tag='HT')
TKodKraju.ES = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ES', tag='ES')
TKodKraju.HN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='HN', tag='HN')
TKodKraju.HK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='HK', tag='HK')
TKodKraju.IN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='IN', tag='IN')
TKodKraju.ID = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ID', tag='ID')
TKodKraju.IQ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='IQ', tag='IQ')
TKodKraju.IR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='IR', tag='IR')
TKodKraju.IE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='IE', tag='IE')
TKodKraju.IS = TKodKraju._CF_enumeration.addEnumeration(unicode_value='IS', tag='IS')
TKodKraju.IL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='IL', tag='IL')
TKodKraju.JM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='JM', tag='JM')
TKodKraju.JP = TKodKraju._CF_enumeration.addEnumeration(unicode_value='JP', tag='JP')
TKodKraju.YE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='YE', tag='YE')
TKodKraju.JE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='JE', tag='JE')
TKodKraju.JO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='JO', tag='JO')
TKodKraju.KY = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KY', tag='KY')
TKodKraju.KH = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KH', tag='KH')
TKodKraju.CM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CM', tag='CM')
TKodKraju.CA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CA', tag='CA')
TKodKraju.QA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='QA', tag='QA')
TKodKraju.KZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KZ', tag='KZ')
TKodKraju.KE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KE', tag='KE')
TKodKraju.KG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KG', tag='KG')
TKodKraju.KI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KI', tag='KI')
TKodKraju.CO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CO', tag='CO')
TKodKraju.KM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KM', tag='KM')
TKodKraju.CG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CG', tag='CG')
TKodKraju.CD = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CD', tag='CD')
TKodKraju.KP = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KP', tag='KP')
TKodKraju.XK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='XK', tag='XK')
TKodKraju.CR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CR', tag='CR')
TKodKraju.CU = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CU', tag='CU')
TKodKraju.KW = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KW', tag='KW')
TKodKraju.LA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LA', tag='LA')
TKodKraju.LS = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LS', tag='LS')
TKodKraju.LB = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LB', tag='LB')
TKodKraju.LR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LR', tag='LR')
TKodKraju.LY = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LY', tag='LY')
TKodKraju.LI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LI', tag='LI')
TKodKraju.LT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
TKodKraju.LV = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LV', tag='LV')
TKodKraju.LU = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LU', tag='LU')
TKodKraju.MK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MK', tag='MK')
TKodKraju.MG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MG', tag='MG')
TKodKraju.YT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='YT', tag='YT')
TKodKraju.MO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MO', tag='MO')
TKodKraju.MW = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
TKodKraju.MV = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
TKodKraju.MY = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MY', tag='MY')
TKodKraju.ML = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ML', tag='ML')
TKodKraju.MT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MT', tag='MT')
TKodKraju.MP = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MP', tag='MP')
TKodKraju.MA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
TKodKraju.MQ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MQ', tag='MQ')
TKodKraju.MR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MR', tag='MR')
TKodKraju.MU = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MU', tag='MU')
TKodKraju.MX = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MX', tag='MX')
TKodKraju.XL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='XL', tag='XL')
TKodKraju.FM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='FM', tag='FM')
TKodKraju.UM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='UM', tag='UM')
TKodKraju.MD = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MD', tag='MD')
TKodKraju.MC = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MC', tag='MC')
TKodKraju.MN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
TKodKraju.MS = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
TKodKraju.MZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MZ', tag='MZ')
TKodKraju.MM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MM', tag='MM')
TKodKraju.NA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NA', tag='NA')
TKodKraju.NR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NR', tag='NR')
TKodKraju.NP = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NP', tag='NP')
TKodKraju.NL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NL', tag='NL')
TKodKraju.DE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
TKodKraju.NE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NE', tag='NE')
TKodKraju.NG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NG', tag='NG')
TKodKraju.NI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NI', tag='NI')
TKodKraju.NU = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NU', tag='NU')
TKodKraju.NF = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NF', tag='NF')
TKodKraju.NO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NO', tag='NO')
TKodKraju.NC = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NC', tag='NC')
TKodKraju.NZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='NZ', tag='NZ')
TKodKraju.PS = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PS', tag='PS')
TKodKraju.OM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='OM', tag='OM')
TKodKraju.PK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PK', tag='PK')
TKodKraju.PW = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PW', tag='PW')
TKodKraju.PA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PA', tag='PA')
TKodKraju.PG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PG', tag='PG')
TKodKraju.PY = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PY', tag='PY')
TKodKraju.PE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PE', tag='PE')
TKodKraju.PN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PN', tag='PN')
TKodKraju.PF = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PF', tag='PF')
TKodKraju.PL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PL', tag='PL')
TKodKraju.GS = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GS', tag='GS')
TKodKraju.PT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PT', tag='PT')
TKodKraju.PR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
TKodKraju.CF = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CF', tag='CF')
TKodKraju.CZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CZ', tag='CZ')
TKodKraju.KR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KR', tag='KR')
TKodKraju.ZA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ZA', tag='ZA')
TKodKraju.RE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='RE', tag='RE')
TKodKraju.RU = TKodKraju._CF_enumeration.addEnumeration(unicode_value='RU', tag='RU')
TKodKraju.RO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='RO', tag='RO')
TKodKraju.RW = TKodKraju._CF_enumeration.addEnumeration(unicode_value='RW', tag='RW')
TKodKraju.EH = TKodKraju._CF_enumeration.addEnumeration(unicode_value='EH', tag='EH')
TKodKraju.BL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BL', tag='BL')
TKodKraju.KN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='KN', tag='KN')
TKodKraju.LC = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LC', tag='LC')
TKodKraju.MF = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MF', tag='MF')
TKodKraju.VC = TKodKraju._CF_enumeration.addEnumeration(unicode_value='VC', tag='VC')
TKodKraju.SV = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SV', tag='SV')
TKodKraju.WS = TKodKraju._CF_enumeration.addEnumeration(unicode_value='WS', tag='WS')
TKodKraju.AS = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AS', tag='AS')
TKodKraju.SM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SM', tag='SM')
TKodKraju.SN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SN', tag='SN')
TKodKraju.RS = TKodKraju._CF_enumeration.addEnumeration(unicode_value='RS', tag='RS')
TKodKraju.SC = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SC', tag='SC')
TKodKraju.SL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SL', tag='SL')
TKodKraju.SG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SG', tag='SG')
TKodKraju.SK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SK', tag='SK')
TKodKraju.SI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
TKodKraju.SO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SO', tag='SO')
TKodKraju.LK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='LK', tag='LK')
TKodKraju.PM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='PM', tag='PM')
TKodKraju.US = TKodKraju._CF_enumeration.addEnumeration(unicode_value='US', tag='US')
TKodKraju.SZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SZ', tag='SZ')
TKodKraju.SD = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SD', tag='SD')
TKodKraju.SR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SR', tag='SR')
TKodKraju.SJ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SJ', tag='SJ')
TKodKraju.SH = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SH', tag='SH')
TKodKraju.SY = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SY', tag='SY')
TKodKraju.CH = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CH', tag='CH')
TKodKraju.SE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SE', tag='SE')
TKodKraju.TJ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TJ', tag='TJ')
TKodKraju.TH = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TH', tag='TH')
TKodKraju.TW = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
TKodKraju.TZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TZ', tag='TZ')
TKodKraju.TG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TG', tag='TG')
TKodKraju.TK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TK', tag='TK')
TKodKraju.TO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TO', tag='TO')
TKodKraju.TT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TT', tag='TT')
TKodKraju.TN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TN', tag='TN')
TKodKraju.TR = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TR', tag='TR')
TKodKraju.TM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TM', tag='TM')
TKodKraju.TV = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TV', tag='TV')
TKodKraju.UG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='UG', tag='UG')
TKodKraju.UA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='UA', tag='UA')
TKodKraju.UY = TKodKraju._CF_enumeration.addEnumeration(unicode_value='UY', tag='UY')
TKodKraju.UZ = TKodKraju._CF_enumeration.addEnumeration(unicode_value='UZ', tag='UZ')
TKodKraju.VU = TKodKraju._CF_enumeration.addEnumeration(unicode_value='VU', tag='VU')
TKodKraju.WF = TKodKraju._CF_enumeration.addEnumeration(unicode_value='WF', tag='WF')
TKodKraju.VA = TKodKraju._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
TKodKraju.HU = TKodKraju._CF_enumeration.addEnumeration(unicode_value='HU', tag='HU')
TKodKraju.VE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='VE', tag='VE')
TKodKraju.GB = TKodKraju._CF_enumeration.addEnumeration(unicode_value='GB', tag='GB')
TKodKraju.VN = TKodKraju._CF_enumeration.addEnumeration(unicode_value='VN', tag='VN')
TKodKraju.IT = TKodKraju._CF_enumeration.addEnumeration(unicode_value='IT', tag='IT')
TKodKraju.TL = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TL', tag='TL')
TKodKraju.CI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CI', tag='CI')
TKodKraju.BV = TKodKraju._CF_enumeration.addEnumeration(unicode_value='BV', tag='BV')
TKodKraju.CX = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CX', tag='CX')
TKodKraju.IM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='IM', tag='IM')
TKodKraju.CK = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CK', tag='CK')
TKodKraju.VI = TKodKraju._CF_enumeration.addEnumeration(unicode_value='VI', tag='VI')
TKodKraju.VG = TKodKraju._CF_enumeration.addEnumeration(unicode_value='VG', tag='VG')
TKodKraju.HM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='HM', tag='HM')
TKodKraju.CC = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
TKodKraju.MH = TKodKraju._CF_enumeration.addEnumeration(unicode_value='MH', tag='MH')
TKodKraju.FO = TKodKraju._CF_enumeration.addEnumeration(unicode_value='FO', tag='FO')
TKodKraju.SB = TKodKraju._CF_enumeration.addEnumeration(unicode_value='SB', tag='SB')
TKodKraju.ST = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ST', tag='ST')
TKodKraju.TC = TKodKraju._CF_enumeration.addEnumeration(unicode_value='TC', tag='TC')
TKodKraju.ZM = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ZM', tag='ZM')
TKodKraju.CV = TKodKraju._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
TKodKraju.ZW = TKodKraju._CF_enumeration.addEnumeration(unicode_value='ZW', tag='ZW')
TKodKraju.AE = TKodKraju._CF_enumeration.addEnumeration(unicode_value='AE', tag='AE')
TKodKraju._InitializeFacetMap(TKodKraju._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodKraju', TKodKraju)
_module_typeBindings.TKodKraju = TKodKraju

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKodUS
class TKodUS (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodUS')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/KodyUrzedowSkarbowych_v4-0E.xsd', 6, 1)
    _Documentation = None
TKodUS._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodUS, enum_prefix=None)
TKodUS.n0202 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0202', tag='n0202')
TKodUS.n0203 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0203', tag='n0203')
TKodUS.n0204 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0204', tag='n0204')
TKodUS.n0205 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0205', tag='n0205')
TKodUS.n0206 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0206', tag='n0206')
TKodUS.n0207 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0207', tag='n0207')
TKodUS.n0208 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0208', tag='n0208')
TKodUS.n0209 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0209', tag='n0209')
TKodUS.n0210 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0210', tag='n0210')
TKodUS.n0211 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0211', tag='n0211')
TKodUS.n0212 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0212', tag='n0212')
TKodUS.n0213 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0213', tag='n0213')
TKodUS.n0214 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0214', tag='n0214')
TKodUS.n0215 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0215', tag='n0215')
TKodUS.n0216 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0216', tag='n0216')
TKodUS.n0217 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0217', tag='n0217')
TKodUS.n0218 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0218', tag='n0218')
TKodUS.n0219 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0219', tag='n0219')
TKodUS.n0220 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0220', tag='n0220')
TKodUS.n0221 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0221', tag='n0221')
TKodUS.n0222 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0222', tag='n0222')
TKodUS.n0223 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0223', tag='n0223')
TKodUS.n0224 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0224', tag='n0224')
TKodUS.n0225 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0225', tag='n0225')
TKodUS.n0226 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0226', tag='n0226')
TKodUS.n0227 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0227', tag='n0227')
TKodUS.n0228 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0228', tag='n0228')
TKodUS.n0229 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0229', tag='n0229')
TKodUS.n0230 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0230', tag='n0230')
TKodUS.n0231 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0231', tag='n0231')
TKodUS.n0232 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0232', tag='n0232')
TKodUS.n0233 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0233', tag='n0233')
TKodUS.n0234 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0234', tag='n0234')
TKodUS.n0271 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0271', tag='n0271')
TKodUS.n0402 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0402', tag='n0402')
TKodUS.n0403 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0403', tag='n0403')
TKodUS.n0404 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0404', tag='n0404')
TKodUS.n0405 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0405', tag='n0405')
TKodUS.n0406 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0406', tag='n0406')
TKodUS.n0407 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0407', tag='n0407')
TKodUS.n0408 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0408', tag='n0408')
TKodUS.n0409 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0409', tag='n0409')
TKodUS.n0410 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0410', tag='n0410')
TKodUS.n0411 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0411', tag='n0411')
TKodUS.n0412 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0412', tag='n0412')
TKodUS.n0413 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0413', tag='n0413')
TKodUS.n0414 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0414', tag='n0414')
TKodUS.n0415 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0415', tag='n0415')
TKodUS.n0416 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0416', tag='n0416')
TKodUS.n0417 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0417', tag='n0417')
TKodUS.n0418 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0418', tag='n0418')
TKodUS.n0419 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0419', tag='n0419')
TKodUS.n0420 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0420', tag='n0420')
TKodUS.n0421 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0421', tag='n0421')
TKodUS.n0422 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0422', tag='n0422')
TKodUS.n0423 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0423', tag='n0423')
TKodUS.n0471 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0471', tag='n0471')
TKodUS.n0602 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0602', tag='n0602')
TKodUS.n0603 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0603', tag='n0603')
TKodUS.n0604 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0604', tag='n0604')
TKodUS.n0605 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0605', tag='n0605')
TKodUS.n0606 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0606', tag='n0606')
TKodUS.n0607 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0607', tag='n0607')
TKodUS.n0608 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0608', tag='n0608')
TKodUS.n0609 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0609', tag='n0609')
TKodUS.n0610 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0610', tag='n0610')
TKodUS.n0611 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0611', tag='n0611')
TKodUS.n0612 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0612', tag='n0612')
TKodUS.n0613 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0613', tag='n0613')
TKodUS.n0614 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0614', tag='n0614')
TKodUS.n0615 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0615', tag='n0615')
TKodUS.n0616 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0616', tag='n0616')
TKodUS.n0617 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0617', tag='n0617')
TKodUS.n0618 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0618', tag='n0618')
TKodUS.n0619 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0619', tag='n0619')
TKodUS.n0620 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0620', tag='n0620')
TKodUS.n0621 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0621', tag='n0621')
TKodUS.n0622 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0622', tag='n0622')
TKodUS.n0671 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0671', tag='n0671')
TKodUS.n0802 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0802', tag='n0802')
TKodUS.n0803 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0803', tag='n0803')
TKodUS.n0804 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0804', tag='n0804')
TKodUS.n0805 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0805', tag='n0805')
TKodUS.n0806 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0806', tag='n0806')
TKodUS.n0807 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0807', tag='n0807')
TKodUS.n0808 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0808', tag='n0808')
TKodUS.n0809 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0809', tag='n0809')
TKodUS.n0810 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0810', tag='n0810')
TKodUS.n0811 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0811', tag='n0811')
TKodUS.n0812 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0812', tag='n0812')
TKodUS.n0813 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0813', tag='n0813')
TKodUS.n0814 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0814', tag='n0814')
TKodUS.n0871 = TKodUS._CF_enumeration.addEnumeration(unicode_value='0871', tag='n0871')
TKodUS.n1002 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1002', tag='n1002')
TKodUS.n1003 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1003', tag='n1003')
TKodUS.n1004 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1004', tag='n1004')
TKodUS.n1005 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1005', tag='n1005')
TKodUS.n1006 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1006', tag='n1006')
TKodUS.n1007 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1007', tag='n1007')
TKodUS.n1008 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1008', tag='n1008')
TKodUS.n1009 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1009', tag='n1009')
TKodUS.n1010 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1010', tag='n1010')
TKodUS.n1011 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1011', tag='n1011')
TKodUS.n1012 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1012', tag='n1012')
TKodUS.n1013 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1013', tag='n1013')
TKodUS.n1014 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1014', tag='n1014')
TKodUS.n1015 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1015', tag='n1015')
TKodUS.n1016 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1016', tag='n1016')
TKodUS.n1017 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1017', tag='n1017')
TKodUS.n1018 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1018', tag='n1018')
TKodUS.n1019 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1019', tag='n1019')
TKodUS.n1020 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1020', tag='n1020')
TKodUS.n1021 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1021', tag='n1021')
TKodUS.n1022 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1022', tag='n1022')
TKodUS.n1023 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1023', tag='n1023')
TKodUS.n1024 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1024', tag='n1024')
TKodUS.n1025 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1025', tag='n1025')
TKodUS.n1026 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1026', tag='n1026')
TKodUS.n1027 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1027', tag='n1027')
TKodUS.n1028 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1028', tag='n1028')
TKodUS.n1029 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1029', tag='n1029')
TKodUS.n1071 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1071', tag='n1071')
TKodUS.n1202 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1202', tag='n1202')
TKodUS.n1203 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1203', tag='n1203')
TKodUS.n1204 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1204', tag='n1204')
TKodUS.n1205 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1205', tag='n1205')
TKodUS.n1206 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1206', tag='n1206')
TKodUS.n1207 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1207', tag='n1207')
TKodUS.n1208 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1208', tag='n1208')
TKodUS.n1209 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1209', tag='n1209')
TKodUS.n1210 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1210', tag='n1210')
TKodUS.n1211 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1211', tag='n1211')
TKodUS.n1212 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1212', tag='n1212')
TKodUS.n1213 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1213', tag='n1213')
TKodUS.n1214 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1214', tag='n1214')
TKodUS.n1215 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1215', tag='n1215')
TKodUS.n1216 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1216', tag='n1216')
TKodUS.n1217 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1217', tag='n1217')
TKodUS.n1218 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1218', tag='n1218')
TKodUS.n1219 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1219', tag='n1219')
TKodUS.n1220 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1220', tag='n1220')
TKodUS.n1221 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1221', tag='n1221')
TKodUS.n1222 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1222', tag='n1222')
TKodUS.n1223 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1223', tag='n1223')
TKodUS.n1224 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1224', tag='n1224')
TKodUS.n1225 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1225', tag='n1225')
TKodUS.n1226 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1226', tag='n1226')
TKodUS.n1227 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1227', tag='n1227')
TKodUS.n1228 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1228', tag='n1228')
TKodUS.n1271 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1271', tag='n1271')
TKodUS.n1402 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1402', tag='n1402')
TKodUS.n1403 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1403', tag='n1403')
TKodUS.n1404 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1404', tag='n1404')
TKodUS.n1405 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1405', tag='n1405')
TKodUS.n1406 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1406', tag='n1406')
TKodUS.n1407 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1407', tag='n1407')
TKodUS.n1408 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1408', tag='n1408')
TKodUS.n1409 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1409', tag='n1409')
TKodUS.n1410 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1410', tag='n1410')
TKodUS.n1411 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1411', tag='n1411')
TKodUS.n1412 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1412', tag='n1412')
TKodUS.n1413 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1413', tag='n1413')
TKodUS.n1414 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1414', tag='n1414')
TKodUS.n1415 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1415', tag='n1415')
TKodUS.n1416 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1416', tag='n1416')
TKodUS.n1417 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1417', tag='n1417')
TKodUS.n1418 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1418', tag='n1418')
TKodUS.n1419 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1419', tag='n1419')
TKodUS.n1420 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1420', tag='n1420')
TKodUS.n1421 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1421', tag='n1421')
TKodUS.n1422 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1422', tag='n1422')
TKodUS.n1423 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1423', tag='n1423')
TKodUS.n1424 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1424', tag='n1424')
TKodUS.n1425 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1425', tag='n1425')
TKodUS.n1426 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1426', tag='n1426')
TKodUS.n1427 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1427', tag='n1427')
TKodUS.n1428 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1428', tag='n1428')
TKodUS.n1429 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1429', tag='n1429')
TKodUS.n1430 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1430', tag='n1430')
TKodUS.n1431 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1431', tag='n1431')
TKodUS.n1432 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1432', tag='n1432')
TKodUS.n1433 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1433', tag='n1433')
TKodUS.n1434 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1434', tag='n1434')
TKodUS.n1435 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1435', tag='n1435')
TKodUS.n1436 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1436', tag='n1436')
TKodUS.n1437 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1437', tag='n1437')
TKodUS.n1438 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1438', tag='n1438')
TKodUS.n1439 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1439', tag='n1439')
TKodUS.n1440 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1440', tag='n1440')
TKodUS.n1441 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1441', tag='n1441')
TKodUS.n1442 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1442', tag='n1442')
TKodUS.n1443 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1443', tag='n1443')
TKodUS.n1444 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1444', tag='n1444')
TKodUS.n1445 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1445', tag='n1445')
TKodUS.n1446 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1446', tag='n1446')
TKodUS.n1447 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1447', tag='n1447')
TKodUS.n1448 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1448', tag='n1448')
TKodUS.n1449 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1449', tag='n1449')
TKodUS.n1471 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1471', tag='n1471')
TKodUS.n1472 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1472', tag='n1472')
TKodUS.n1473 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1473', tag='n1473')
TKodUS.n1602 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1602', tag='n1602')
TKodUS.n1603 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1603', tag='n1603')
TKodUS.n1604 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1604', tag='n1604')
TKodUS.n1605 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1605', tag='n1605')
TKodUS.n1606 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1606', tag='n1606')
TKodUS.n1607 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1607', tag='n1607')
TKodUS.n1608 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1608', tag='n1608')
TKodUS.n1609 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1609', tag='n1609')
TKodUS.n1610 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1610', tag='n1610')
TKodUS.n1611 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1611', tag='n1611')
TKodUS.n1612 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1612', tag='n1612')
TKodUS.n1613 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1613', tag='n1613')
TKodUS.n1671 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1671', tag='n1671')
TKodUS.n1802 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1802', tag='n1802')
TKodUS.n1803 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1803', tag='n1803')
TKodUS.n1804 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1804', tag='n1804')
TKodUS.n1805 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1805', tag='n1805')
TKodUS.n1806 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1806', tag='n1806')
TKodUS.n1807 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1807', tag='n1807')
TKodUS.n1808 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1808', tag='n1808')
TKodUS.n1809 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1809', tag='n1809')
TKodUS.n1810 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1810', tag='n1810')
TKodUS.n1811 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1811', tag='n1811')
TKodUS.n1812 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1812', tag='n1812')
TKodUS.n1813 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1813', tag='n1813')
TKodUS.n1814 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1814', tag='n1814')
TKodUS.n1815 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1815', tag='n1815')
TKodUS.n1816 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1816', tag='n1816')
TKodUS.n1817 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1817', tag='n1817')
TKodUS.n1818 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1818', tag='n1818')
TKodUS.n1819 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1819', tag='n1819')
TKodUS.n1820 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1820', tag='n1820')
TKodUS.n1821 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1821', tag='n1821')
TKodUS.n1822 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1822', tag='n1822')
TKodUS.n1823 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1823', tag='n1823')
TKodUS.n1871 = TKodUS._CF_enumeration.addEnumeration(unicode_value='1871', tag='n1871')
TKodUS.n2002 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2002', tag='n2002')
TKodUS.n2003 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2003', tag='n2003')
TKodUS.n2004 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2004', tag='n2004')
TKodUS.n2005 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2005', tag='n2005')
TKodUS.n2006 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2006', tag='n2006')
TKodUS.n2007 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2007', tag='n2007')
TKodUS.n2008 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2008', tag='n2008')
TKodUS.n2009 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2009', tag='n2009')
TKodUS.n2010 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2010', tag='n2010')
TKodUS.n2011 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2011', tag='n2011')
TKodUS.n2012 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2012', tag='n2012')
TKodUS.n2013 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2013', tag='n2013')
TKodUS.n2014 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2014', tag='n2014')
TKodUS.n2015 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2015', tag='n2015')
TKodUS.n2071 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2071', tag='n2071')
TKodUS.n2202 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2202', tag='n2202')
TKodUS.n2203 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2203', tag='n2203')
TKodUS.n2204 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2204', tag='n2204')
TKodUS.n2205 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2205', tag='n2205')
TKodUS.n2206 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2206', tag='n2206')
TKodUS.n2207 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2207', tag='n2207')
TKodUS.n2208 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2208', tag='n2208')
TKodUS.n2209 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2209', tag='n2209')
TKodUS.n2210 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2210', tag='n2210')
TKodUS.n2211 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2211', tag='n2211')
TKodUS.n2212 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2212', tag='n2212')
TKodUS.n2213 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2213', tag='n2213')
TKodUS.n2214 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2214', tag='n2214')
TKodUS.n2215 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2215', tag='n2215')
TKodUS.n2216 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2216', tag='n2216')
TKodUS.n2217 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2217', tag='n2217')
TKodUS.n2218 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2218', tag='n2218')
TKodUS.n2219 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2219', tag='n2219')
TKodUS.n2220 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2220', tag='n2220')
TKodUS.n2221 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2221', tag='n2221')
TKodUS.n2271 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2271', tag='n2271')
TKodUS.n2402 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2402', tag='n2402')
TKodUS.n2403 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2403', tag='n2403')
TKodUS.n2404 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2404', tag='n2404')
TKodUS.n2405 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2405', tag='n2405')
TKodUS.n2406 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2406', tag='n2406')
TKodUS.n2407 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2407', tag='n2407')
TKodUS.n2408 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2408', tag='n2408')
TKodUS.n2409 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2409', tag='n2409')
TKodUS.n2410 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2410', tag='n2410')
TKodUS.n2411 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2411', tag='n2411')
TKodUS.n2412 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2412', tag='n2412')
TKodUS.n2413 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2413', tag='n2413')
TKodUS.n2414 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2414', tag='n2414')
TKodUS.n2415 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2415', tag='n2415')
TKodUS.n2416 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2416', tag='n2416')
TKodUS.n2417 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2417', tag='n2417')
TKodUS.n2418 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2418', tag='n2418')
TKodUS.n2419 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2419', tag='n2419')
TKodUS.n2420 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2420', tag='n2420')
TKodUS.n2421 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2421', tag='n2421')
TKodUS.n2422 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2422', tag='n2422')
TKodUS.n2423 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2423', tag='n2423')
TKodUS.n2424 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2424', tag='n2424')
TKodUS.n2425 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2425', tag='n2425')
TKodUS.n2426 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2426', tag='n2426')
TKodUS.n2427 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2427', tag='n2427')
TKodUS.n2428 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2428', tag='n2428')
TKodUS.n2429 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2429', tag='n2429')
TKodUS.n2430 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2430', tag='n2430')
TKodUS.n2431 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2431', tag='n2431')
TKodUS.n2432 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2432', tag='n2432')
TKodUS.n2433 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2433', tag='n2433')
TKodUS.n2434 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2434', tag='n2434')
TKodUS.n2435 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2435', tag='n2435')
TKodUS.n2436 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2436', tag='n2436')
TKodUS.n2471 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2471', tag='n2471')
TKodUS.n2472 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2472', tag='n2472')
TKodUS.n2602 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2602', tag='n2602')
TKodUS.n2603 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2603', tag='n2603')
TKodUS.n2604 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2604', tag='n2604')
TKodUS.n2605 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2605', tag='n2605')
TKodUS.n2606 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2606', tag='n2606')
TKodUS.n2607 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2607', tag='n2607')
TKodUS.n2608 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2608', tag='n2608')
TKodUS.n2609 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2609', tag='n2609')
TKodUS.n2610 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2610', tag='n2610')
TKodUS.n2611 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2611', tag='n2611')
TKodUS.n2612 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2612', tag='n2612')
TKodUS.n2613 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2613', tag='n2613')
TKodUS.n2614 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2614', tag='n2614')
TKodUS.n2615 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2615', tag='n2615')
TKodUS.n2671 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2671', tag='n2671')
TKodUS.n2802 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2802', tag='n2802')
TKodUS.n2803 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2803', tag='n2803')
TKodUS.n2804 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2804', tag='n2804')
TKodUS.n2805 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2805', tag='n2805')
TKodUS.n2806 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2806', tag='n2806')
TKodUS.n2807 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2807', tag='n2807')
TKodUS.n2808 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2808', tag='n2808')
TKodUS.n2809 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2809', tag='n2809')
TKodUS.n2810 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2810', tag='n2810')
TKodUS.n2811 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2811', tag='n2811')
TKodUS.n2812 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2812', tag='n2812')
TKodUS.n2813 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2813', tag='n2813')
TKodUS.n2814 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2814', tag='n2814')
TKodUS.n2815 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2815', tag='n2815')
TKodUS.n2816 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2816', tag='n2816')
TKodUS.n2871 = TKodUS._CF_enumeration.addEnumeration(unicode_value='2871', tag='n2871')
TKodUS.n3002 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3002', tag='n3002')
TKodUS.n3003 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3003', tag='n3003')
TKodUS.n3004 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3004', tag='n3004')
TKodUS.n3005 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3005', tag='n3005')
TKodUS.n3006 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3006', tag='n3006')
TKodUS.n3007 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3007', tag='n3007')
TKodUS.n3008 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3008', tag='n3008')
TKodUS.n3009 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3009', tag='n3009')
TKodUS.n3010 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3010', tag='n3010')
TKodUS.n3011 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3011', tag='n3011')
TKodUS.n3012 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3012', tag='n3012')
TKodUS.n3013 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3013', tag='n3013')
TKodUS.n3014 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3014', tag='n3014')
TKodUS.n3015 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3015', tag='n3015')
TKodUS.n3016 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3016', tag='n3016')
TKodUS.n3017 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3017', tag='n3017')
TKodUS.n3018 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3018', tag='n3018')
TKodUS.n3019 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3019', tag='n3019')
TKodUS.n3020 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3020', tag='n3020')
TKodUS.n3021 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3021', tag='n3021')
TKodUS.n3022 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3022', tag='n3022')
TKodUS.n3023 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3023', tag='n3023')
TKodUS.n3025 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3025', tag='n3025')
TKodUS.n3026 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3026', tag='n3026')
TKodUS.n3027 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3027', tag='n3027')
TKodUS.n3028 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3028', tag='n3028')
TKodUS.n3029 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3029', tag='n3029')
TKodUS.n3030 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3030', tag='n3030')
TKodUS.n3031 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3031', tag='n3031')
TKodUS.n3032 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3032', tag='n3032')
TKodUS.n3033 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3033', tag='n3033')
TKodUS.n3034 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3034', tag='n3034')
TKodUS.n3035 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3035', tag='n3035')
TKodUS.n3036 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3036', tag='n3036')
TKodUS.n3037 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3037', tag='n3037')
TKodUS.n3038 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3038', tag='n3038')
TKodUS.n3039 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3039', tag='n3039')
TKodUS.n3071 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3071', tag='n3071')
TKodUS.n3072 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3072', tag='n3072')
TKodUS.n3202 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3202', tag='n3202')
TKodUS.n3203 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3203', tag='n3203')
TKodUS.n3204 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3204', tag='n3204')
TKodUS.n3205 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3205', tag='n3205')
TKodUS.n3206 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3206', tag='n3206')
TKodUS.n3207 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3207', tag='n3207')
TKodUS.n3208 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3208', tag='n3208')
TKodUS.n3209 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3209', tag='n3209')
TKodUS.n3210 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3210', tag='n3210')
TKodUS.n3211 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3211', tag='n3211')
TKodUS.n3212 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3212', tag='n3212')
TKodUS.n3213 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3213', tag='n3213')
TKodUS.n3214 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3214', tag='n3214')
TKodUS.n3215 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3215', tag='n3215')
TKodUS.n3216 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3216', tag='n3216')
TKodUS.n3217 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3217', tag='n3217')
TKodUS.n3218 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3218', tag='n3218')
TKodUS.n3219 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3219', tag='n3219')
TKodUS.n3220 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3220', tag='n3220')
TKodUS.n3271 = TKodUS._CF_enumeration.addEnumeration(unicode_value='3271', tag='n3271')
TKodUS._InitializeFacetMap(TKodUS._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodUS', TKodUS)
_module_typeBindings.TKodUS = TKodUS

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 310, 4)
    _Documentation = None
STD_ANON_2._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(240))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_minLength,
   STD_ANON_2._CF_maxLength)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 338, 4)
    _Documentation = None
STD_ANON_3._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_3._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(240))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_minLength,
   STD_ANON_3._CF_maxLength)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 349, 4)
    _Documentation = None
STD_ANON_4._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(70))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_minLength,
   STD_ANON_4._CF_maxLength)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 372, 4)
    _Documentation = None
STD_ANON_5._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_5._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(240))
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_minLength,
   STD_ANON_5._CF_maxLength)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 383, 4)
    _Documentation = None
STD_ANON_6._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_6._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(70))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_minLength,
   STD_ANON_6._CF_maxLength)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TRzeczywisty
class TRzeczywisty (TKwota2):

    """Liczby wykazywane z dokładnością do dwóch miejsc po przecinku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TRzeczywisty')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 56, 1)
    _Documentation = 'Liczby wykazywane z dok\u0142adno\u015bci\u0105 do dw\xf3ch miejsc po przecinku'
TRzeczywisty._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TRzeczywisty, value=pyxb.binding.datatypes.decimal('0.0'))
TRzeczywisty._InitializeFacetMap(TRzeczywisty._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'TRzeczywisty', TRzeczywisty)
_module_typeBindings.TRzeczywisty = TRzeczywisty

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKwota2Nieujemna
class TKwota2Nieujemna (TKwota2):

    """Wartość kwotowa nieujemna wykazana w zł i gr"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwota2Nieujemna')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 82, 1)
    _Documentation = 'Warto\u015b\u0107 kwotowa nieujemna wykazana w z\u0142 i gr'
TKwota2Nieujemna._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TKwota2Nieujemna, value=pyxb.binding.datatypes.decimal('0.0'))
TKwota2Nieujemna._InitializeFacetMap(TKwota2Nieujemna._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'TKwota2Nieujemna', TKwota2Nieujemna)
_module_typeBindings.TKwota2Nieujemna = TKwota2Nieujemna

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKwotaCNieujemna
class TKwotaCNieujemna (TKwotaC):

    """Wartość kwotowa nieujemna wykazana w zł"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwotaCNieujemna')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 90, 1)
    _Documentation = 'Warto\u015b\u0107 kwotowa nieujemna wykazana w z\u0142'
TKwotaCNieujemna._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TKwotaCNieujemna, value=pyxb.binding.datatypes.integer(0))
TKwotaCNieujemna._InitializeFacetMap(TKwotaCNieujemna._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'TKwotaCNieujemna', TKwotaCNieujemna)
_module_typeBindings.TKwotaCNieujemna = TKwotaCNieujemna

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdresEmail
class TAdresEmail (TZnakowy):

    """Element będący adresem e-mail"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TAdresEmail')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 143, 1)
    _Documentation = 'Element b\u0119d\u0105cy adresem e-mail'
TAdresEmail._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
TAdresEmail._CF_pattern = pyxb.binding.facets.CF_pattern()
TAdresEmail._CF_pattern.addPattern(pattern="[0-9\\p{L}'\\.\\-_]{1,127}@[0-9\\p{L}'\\.\\-_]{1,127}")
TAdresEmail._InitializeFacetMap(TAdresEmail._CF_whiteSpace,
   TAdresEmail._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TAdresEmail', TAdresEmail)
_module_typeBindings.TAdresEmail = TAdresEmail

# Union simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrREGON
# superclasses pyxb.binding.datatypes.anySimpleType
class TNrREGON (pyxb.binding.basis.STD_union):

    """Numer REGON"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrREGON')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 168, 1)
    _Documentation = 'Numer REGON'

    _MemberTypes = ( STD_ANON, STD_ANON_, )
TNrREGON._CF_pattern = pyxb.binding.facets.CF_pattern()
TNrREGON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TNrREGON)
TNrREGON._InitializeFacetMap(TNrREGON._CF_pattern,
   TNrREGON._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TNrREGON', TNrREGON)
_module_typeBindings.TNrREGON = TNrREGON

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TUlica
class TUlica (TZnakowy):

    """Nazwa ulicy"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TUlica')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 257, 1)
    _Documentation = 'Nazwa ulicy'
TUlica._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(65))
TUlica._InitializeFacetMap(TUlica._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TUlica', TUlica)
_module_typeBindings.TUlica = TUlica

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrBudynku
class TNrBudynku (TZnakowy):

    """Numer budynku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrBudynku')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 265, 1)
    _Documentation = 'Numer budynku'
TNrBudynku._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
TNrBudynku._InitializeFacetMap(TNrBudynku._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TNrBudynku', TNrBudynku)
_module_typeBindings.TNrBudynku = TNrBudynku

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrLokalu
class TNrLokalu (TZnakowy):

    """Numer lokalu"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrLokalu')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 273, 1)
    _Documentation = 'Numer lokalu'
TNrLokalu._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
TNrLokalu._InitializeFacetMap(TNrLokalu._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TNrLokalu', TNrLokalu)
_module_typeBindings.TNrLokalu = TNrLokalu

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKodPocztowy
class TKodPocztowy (TZnakowy):

    """Kod pocztowy"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodPocztowy')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 281, 1)
    _Documentation = 'Kod pocztowy'
TKodPocztowy._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
TKodPocztowy._InitializeFacetMap(TKodPocztowy._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TKodPocztowy', TKodPocztowy)
_module_typeBindings.TKodPocztowy = TKodPocztowy

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TKodKrajuWydania
class TKodKrajuWydania (TKodKraju):

    """Kod kraju wydania numeru identyfikacyjnego"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodKrajuWydania')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 298, 1)
    _Documentation = 'Kod kraju wydania numeru identyfikacyjnego'
TKodKrajuWydania._CF_pattern = pyxb.binding.facets.CF_pattern()
TKodKrajuWydania._CF_pattern.addPattern(pattern='P[A-KM-Z]')
TKodKrajuWydania._CF_pattern.addPattern(pattern='[A-OQ-Z][A-Z]')
TKodKrajuWydania._InitializeFacetMap(TKodKrajuWydania._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TKodKrajuWydania', TKodKrajuWydania)
_module_typeBindings.TKodKrajuWydania = TKodKrajuWydania

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TNrDokumentu
class TNrDokumentu (TZnakowy):

    """Numer dokumentu"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNrDokumentu')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/ElementarneTypyDanych_v4-0E.xsd', 324, 1)
    _Documentation = 'Numer dokumentu'
TNrDokumentu._CF_pattern = pyxb.binding.facets.CF_pattern()
TNrDokumentu._CF_pattern.addPattern(pattern='\\d{2}/\\d{2}')
TNrDokumentu._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(5))
TNrDokumentu._InitializeFacetMap(TNrDokumentu._CF_pattern,
   TNrDokumentu._CF_length)
Namespace.addCategoryObject('typeBinding', 'TNrDokumentu', TNrDokumentu)
_module_typeBindings.TNrDokumentu = TNrDokumentu

# Atomic simple type: [anonymous]
class STD_ANON_7 (TKodKraju):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 84, 4)
    _Documentation = None
STD_ANON_7._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_7._CF_pattern.addPattern(pattern='P[A-KM-Z]')
STD_ANON_7._CF_pattern.addPattern(pattern='[A-OQ-Z][A-Z]')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_pattern)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres with content type ELEMENT_ONLY
class TAdres (pyxb.binding.basis.complexTypeDefinition):
    """Dane określające adres"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TAdres')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 5, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresPol uses Python identifier AdresPol
    __AdresPol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresPol'), 'AdresPol', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdres_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresPol', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4), )

    
    AdresPol = property(__AdresPol.value, __AdresPol.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZagr uses Python identifier AdresZagr
    __AdresZagr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr'), 'AdresZagr', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdres_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresZagr', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4), )

    
    AdresZagr = property(__AdresZagr.value, __AdresZagr.set, None, None)

    _ElementMap.update({
        __AdresPol.name() : __AdresPol,
        __AdresZagr.name() : __AdresZagr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TAdres = TAdres
Namespace.addCategoryObject('typeBinding', 'TAdres', TAdres)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdresPolski with content type ELEMENT_ONLY
class TAdresPolski (pyxb.binding.basis.complexTypeDefinition):
    """Informacje opisujące adres polski"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TAdresPolski')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 18, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}KodKraju uses Python identifier KodKraju
    __KodKraju = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodKraju'), 'KodKraju', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyKodKraju', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 23, 3), )

    
    KodKraju = property(__KodKraju.value, __KodKraju.set, None, 'Kraj')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Wojewodztwo uses Python identifier Wojewodztwo
    __Wojewodztwo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Wojewodztwo'), 'Wojewodztwo', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyWojewodztwo', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 28, 3), )

    
    Wojewodztwo = property(__Wojewodztwo.value, __Wojewodztwo.set, None, 'Wojew\xf3dztwo')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Powiat uses Python identifier Powiat
    __Powiat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Powiat'), 'Powiat', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyPowiat', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 33, 3), )

    
    Powiat = property(__Powiat.value, __Powiat.set, None, 'Powiat')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Gmina uses Python identifier Gmina
    __Gmina = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Gmina'), 'Gmina', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyGmina', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 38, 3), )

    
    Gmina = property(__Gmina.value, __Gmina.set, None, 'Gmina')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Ulica uses Python identifier Ulica
    __Ulica = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ulica'), 'Ulica', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyUlica', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 43, 3), )

    
    Ulica = property(__Ulica.value, __Ulica.set, None, 'Nazwa ulicy')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NrDomu uses Python identifier NrDomu
    __NrDomu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrDomu'), 'NrDomu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNrDomu', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 48, 3), )

    
    NrDomu = property(__NrDomu.value, __NrDomu.set, None, 'Numer budynku')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NrLokalu uses Python identifier NrLokalu
    __NrLokalu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrLokalu'), 'NrLokalu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNrLokalu', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 53, 3), )

    
    NrLokalu = property(__NrLokalu.value, __NrLokalu.set, None, 'Numer lokalu')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Miejscowosc uses Python identifier Miejscowosc
    __Miejscowosc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Miejscowosc'), 'Miejscowosc', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyMiejscowosc', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 58, 3), )

    
    Miejscowosc = property(__Miejscowosc.value, __Miejscowosc.set, None, 'Nazwa miejscowo\u015bci')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}KodPocztowy uses Python identifier KodPocztowy
    __KodPocztowy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodPocztowy'), 'KodPocztowy', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyKodPocztowy', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 63, 3), )

    
    KodPocztowy = property(__KodPocztowy.value, __KodPocztowy.set, None, 'Kod pocztowy')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Poczta uses Python identifier Poczta
    __Poczta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Poczta'), 'Poczta', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresPolski_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyPoczta', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 68, 3), )

    
    Poczta = property(__Poczta.value, __Poczta.set, None, 'Nazwa urz\u0119du pocztowego')

    _ElementMap.update({
        __KodKraju.name() : __KodKraju,
        __Wojewodztwo.name() : __Wojewodztwo,
        __Powiat.name() : __Powiat,
        __Gmina.name() : __Gmina,
        __Ulica.name() : __Ulica,
        __NrDomu.name() : __NrDomu,
        __NrLokalu.name() : __NrLokalu,
        __Miejscowosc.name() : __Miejscowosc,
        __KodPocztowy.name() : __KodPocztowy,
        __Poczta.name() : __Poczta
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TAdresPolski = TAdresPolski
Namespace.addCategoryObject('typeBinding', 'TAdresPolski', TAdresPolski)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdresZagraniczny with content type ELEMENT_ONLY
class TAdresZagraniczny (pyxb.binding.basis.complexTypeDefinition):
    """Informacje opisujące adres zagraniczny"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TAdresZagraniczny')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 75, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}KodKraju uses Python identifier KodKraju
    __KodKraju = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodKraju'), 'KodKraju', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresZagraniczny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyKodKraju', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 80, 3), )

    
    KodKraju = property(__KodKraju.value, __KodKraju.set, None, 'Kod Kraju [Country Code]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}KodPocztowy uses Python identifier KodPocztowy
    __KodPocztowy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodPocztowy'), 'KodPocztowy', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresZagraniczny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyKodPocztowy', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 91, 3), )

    
    KodPocztowy = property(__KodPocztowy.value, __KodPocztowy.set, None, 'Kod pocztowy [Postal code]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Miejscowosc uses Python identifier Miejscowosc
    __Miejscowosc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Miejscowosc'), 'Miejscowosc', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresZagraniczny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyMiejscowosc', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 96, 3), )

    
    Miejscowosc = property(__Miejscowosc.value, __Miejscowosc.set, None, 'Nazwa miejscowo\u015bci [City]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Ulica uses Python identifier Ulica
    __Ulica = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ulica'), 'Ulica', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresZagraniczny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyUlica', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 101, 3), )

    
    Ulica = property(__Ulica.value, __Ulica.set, None, 'Nazwa ulicy [Street]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NrDomu uses Python identifier NrDomu
    __NrDomu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrDomu'), 'NrDomu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresZagraniczny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNrDomu', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 106, 3), )

    
    NrDomu = property(__NrDomu.value, __NrDomu.set, None, 'Numer budynku [Building number]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NrLokalu uses Python identifier NrLokalu
    __NrLokalu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrLokalu'), 'NrLokalu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TAdresZagraniczny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNrLokalu', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 111, 3), )

    
    NrLokalu = property(__NrLokalu.value, __NrLokalu.set, None, 'Numer lokalu [Flat number]')

    _ElementMap.update({
        __KodKraju.name() : __KodKraju,
        __KodPocztowy.name() : __KodPocztowy,
        __Miejscowosc.name() : __Miejscowosc,
        __Ulica.name() : __Ulica,
        __NrDomu.name() : __NrDomu,
        __NrLokalu.name() : __NrLokalu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TAdresZagraniczny = TAdresZagraniczny
Namespace.addCategoryObject('typeBinding', 'TAdresZagraniczny', TAdresZagraniczny)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TIdentyfikatorOsobyFizycznej with content type ELEMENT_ONLY
class TIdentyfikatorOsobyFizycznej (pyxb.binding.basis.complexTypeDefinition):
    """Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIdentyfikatorOsobyFizycznej')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 119, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NIP uses Python identifier NIP
    __NIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIP'), 'NIP', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNIP', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 124, 3), )

    
    NIP = property(__NIP.value, __NIP.set, None, 'Identyfikator podatkowy NIP')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}ImiePierwsze uses Python identifier ImiePierwsze
    __ImiePierwsze = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), 'ImiePierwsze', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyImiePierwsze', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 129, 3), )

    
    ImiePierwsze = property(__ImiePierwsze.value, __ImiePierwsze.set, None, 'Pierwsze imi\u0119')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Nazwisko uses Python identifier Nazwisko
    __Nazwisko = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), 'Nazwisko', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNazwisko', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 134, 3), )

    
    Nazwisko = property(__Nazwisko.value, __Nazwisko.set, None, 'Nazwisko')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}DataUrodzenia uses Python identifier DataUrodzenia
    __DataUrodzenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), 'DataUrodzenia', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyDataUrodzenia', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 139, 3), )

    
    DataUrodzenia = property(__DataUrodzenia.value, __DataUrodzenia.set, None, 'Data urodzenia')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}PESEL uses Python identifier PESEL
    __PESEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PESEL'), 'PESEL', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyPESEL', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 144, 3), )

    
    PESEL = property(__PESEL.value, __PESEL.set, None, 'Identyfikator podatkowy numer PESEL')

    _ElementMap.update({
        __NIP.name() : __NIP,
        __ImiePierwsze.name() : __ImiePierwsze,
        __Nazwisko.name() : __Nazwisko,
        __DataUrodzenia.name() : __DataUrodzenia,
        __PESEL.name() : __PESEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TIdentyfikatorOsobyFizycznej = TIdentyfikatorOsobyFizycznej
Namespace.addCategoryObject('typeBinding', 'TIdentyfikatorOsobyFizycznej', TIdentyfikatorOsobyFizycznej)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TIdentyfikatorOsobyFizycznej1 with content type ELEMENT_ONLY
class TIdentyfikatorOsobyFizycznej1 (pyxb.binding.basis.complexTypeDefinition):
    """Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej z identyfikatorem NIP albo PESEL"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIdentyfikatorOsobyFizycznej1')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 151, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NIP uses Python identifier NIP
    __NIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIP'), 'NIP', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej1_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNIP', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 157, 4), )

    
    NIP = property(__NIP.value, __NIP.set, None, 'Identyfikator podatkowy NIP')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}PESEL uses Python identifier PESEL
    __PESEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PESEL'), 'PESEL', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej1_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyPESEL', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 162, 4), )

    
    PESEL = property(__PESEL.value, __PESEL.set, None, 'Identyfikator podatkowy numer PESEL')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}ImiePierwsze uses Python identifier ImiePierwsze
    __ImiePierwsze = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), 'ImiePierwsze', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej1_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyImiePierwsze', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 168, 3), )

    
    ImiePierwsze = property(__ImiePierwsze.value, __ImiePierwsze.set, None, 'Pierwsze imi\u0119')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Nazwisko uses Python identifier Nazwisko
    __Nazwisko = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), 'Nazwisko', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej1_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNazwisko', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 173, 3), )

    
    Nazwisko = property(__Nazwisko.value, __Nazwisko.set, None, 'Nazwisko')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}DataUrodzenia uses Python identifier DataUrodzenia
    __DataUrodzenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), 'DataUrodzenia', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej1_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyDataUrodzenia', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 178, 3), )

    
    DataUrodzenia = property(__DataUrodzenia.value, __DataUrodzenia.set, None, 'Data urodzenia')

    _ElementMap.update({
        __NIP.name() : __NIP,
        __PESEL.name() : __PESEL,
        __ImiePierwsze.name() : __ImiePierwsze,
        __Nazwisko.name() : __Nazwisko,
        __DataUrodzenia.name() : __DataUrodzenia
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TIdentyfikatorOsobyFizycznej1 = TIdentyfikatorOsobyFizycznej1
Namespace.addCategoryObject('typeBinding', 'TIdentyfikatorOsobyFizycznej1', TIdentyfikatorOsobyFizycznej1)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TIdentyfikatorOsobyFizycznej2 with content type ELEMENT_ONLY
class TIdentyfikatorOsobyFizycznej2 (pyxb.binding.basis.complexTypeDefinition):
    """Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej z identyfikatorem NIP"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIdentyfikatorOsobyFizycznej2')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 185, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NIP uses Python identifier NIP
    __NIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIP'), 'NIP', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej2_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNIP', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 190, 3), )

    
    NIP = property(__NIP.value, __NIP.set, None, 'Identyfikator podatkowy NIP')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}ImiePierwsze uses Python identifier ImiePierwsze
    __ImiePierwsze = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), 'ImiePierwsze', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej2_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyImiePierwsze', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 195, 3), )

    
    ImiePierwsze = property(__ImiePierwsze.value, __ImiePierwsze.set, None, 'Pierwsze imi\u0119')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Nazwisko uses Python identifier Nazwisko
    __Nazwisko = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), 'Nazwisko', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej2_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNazwisko', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 200, 3), )

    
    Nazwisko = property(__Nazwisko.value, __Nazwisko.set, None, 'Nazwisko')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}DataUrodzenia uses Python identifier DataUrodzenia
    __DataUrodzenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), 'DataUrodzenia', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznej2_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyDataUrodzenia', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 205, 3), )

    
    DataUrodzenia = property(__DataUrodzenia.value, __DataUrodzenia.set, None, 'Data urodzenia')

    _ElementMap.update({
        __NIP.name() : __NIP,
        __ImiePierwsze.name() : __ImiePierwsze,
        __Nazwisko.name() : __Nazwisko,
        __DataUrodzenia.name() : __DataUrodzenia
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TIdentyfikatorOsobyFizycznej2 = TIdentyfikatorOsobyFizycznej2
Namespace.addCategoryObject('typeBinding', 'TIdentyfikatorOsobyFizycznej2', TIdentyfikatorOsobyFizycznej2)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TIdentyfikatorOsobyFizycznejPelny with content type ELEMENT_ONLY
class TIdentyfikatorOsobyFizycznejPelny (pyxb.binding.basis.complexTypeDefinition):
    """Pełny zestaw danych identyfikacyjnych o osobie fizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIdentyfikatorOsobyFizycznejPelny')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 212, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NIP uses Python identifier NIP
    __NIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIP'), 'NIP', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNIP', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 217, 3), )

    
    NIP = property(__NIP.value, __NIP.set, None, 'Identyfikator podatkowy NIP')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}ImiePierwsze uses Python identifier ImiePierwsze
    __ImiePierwsze = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), 'ImiePierwsze', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyImiePierwsze', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 222, 3), )

    
    ImiePierwsze = property(__ImiePierwsze.value, __ImiePierwsze.set, None, 'Pierwsze imi\u0119')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Nazwisko uses Python identifier Nazwisko
    __Nazwisko = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), 'Nazwisko', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNazwisko', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 227, 3), )

    
    Nazwisko = property(__Nazwisko.value, __Nazwisko.set, None, 'Nazwisko')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}DataUrodzenia uses Python identifier DataUrodzenia
    __DataUrodzenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), 'DataUrodzenia', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyDataUrodzenia', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 232, 3), )

    
    DataUrodzenia = property(__DataUrodzenia.value, __DataUrodzenia.set, None, 'Data urodzenia')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}ImieOjca uses Python identifier ImieOjca
    __ImieOjca = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImieOjca'), 'ImieOjca', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyImieOjca', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 237, 3), )

    
    ImieOjca = property(__ImieOjca.value, __ImieOjca.set, None, 'Imi\u0119 ojca')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}ImieMatki uses Python identifier ImieMatki
    __ImieMatki = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImieMatki'), 'ImieMatki', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyImieMatki', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 242, 3), )

    
    ImieMatki = property(__ImieMatki.value, __ImieMatki.set, None, 'Imi\u0119 matki')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}PESEL uses Python identifier PESEL
    __PESEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PESEL'), 'PESEL', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyPESEL', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 247, 3), )

    
    PESEL = property(__PESEL.value, __PESEL.set, None, 'Identyfikator podatkowy numer PESEL')

    _ElementMap.update({
        __NIP.name() : __NIP,
        __ImiePierwsze.name() : __ImiePierwsze,
        __Nazwisko.name() : __Nazwisko,
        __DataUrodzenia.name() : __DataUrodzenia,
        __ImieOjca.name() : __ImieOjca,
        __ImieMatki.name() : __ImieMatki,
        __PESEL.name() : __PESEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TIdentyfikatorOsobyFizycznejPelny = TIdentyfikatorOsobyFizycznejPelny
Namespace.addCategoryObject('typeBinding', 'TIdentyfikatorOsobyFizycznejPelny', TIdentyfikatorOsobyFizycznejPelny)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TIdentyfikatorOsobyFizycznejZagranicznej with content type ELEMENT_ONLY
class TIdentyfikatorOsobyFizycznejZagranicznej (pyxb.binding.basis.complexTypeDefinition):
    """Zestaw danych identyfikacyjnych dla osoby fizycznej zagranicznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIdentyfikatorOsobyFizycznejZagranicznej')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 254, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}ImiePierwsze uses Python identifier ImiePierwsze
    __ImiePierwsze = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), 'ImiePierwsze', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyImiePierwsze', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 259, 3), )

    
    ImiePierwsze = property(__ImiePierwsze.value, __ImiePierwsze.set, None, 'Imi\u0119 pierwsze [First name]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}Nazwisko uses Python identifier Nazwisko
    __Nazwisko = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), 'Nazwisko', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNazwisko', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 264, 3), )

    
    Nazwisko = property(__Nazwisko.value, __Nazwisko.set, None, 'Nazwisko [Family name]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}DataUrodzenia uses Python identifier DataUrodzenia
    __DataUrodzenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), 'DataUrodzenia', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyDataUrodzenia', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 269, 3), )

    
    DataUrodzenia = property(__DataUrodzenia.value, __DataUrodzenia.set, None, 'Data urodzenia [Date of Birth]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}MiejsceUrodzenia uses Python identifier MiejsceUrodzenia
    __MiejsceUrodzenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MiejsceUrodzenia'), 'MiejsceUrodzenia', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyMiejsceUrodzenia', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 274, 3), )

    
    MiejsceUrodzenia = property(__MiejsceUrodzenia.value, __MiejsceUrodzenia.set, None, 'Miejsce urodzenia [Place of Birth]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}ImieOjca uses Python identifier ImieOjca
    __ImieOjca = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImieOjca'), 'ImieOjca', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyImieOjca', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 279, 3), )

    
    ImieOjca = property(__ImieOjca.value, __ImieOjca.set, None, 'Imi\u0119 ojca [Father\u2019s name]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}ImieMatki uses Python identifier ImieMatki
    __ImieMatki = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImieMatki'), 'ImieMatki', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyImieMatki', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 284, 3), )

    
    ImieMatki = property(__ImieMatki.value, __ImieMatki.set, None, 'Imi\u0119 matki [Mother\u2019s name]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NIP uses Python identifier NIP
    __NIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIP'), 'NIP', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyFizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNIP', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 289, 3), )

    
    NIP = property(__NIP.value, __NIP.set, None, 'Identyfikator podatkowy NIP [Tax Identification Number (NIP)]')

    _ElementMap.update({
        __ImiePierwsze.name() : __ImiePierwsze,
        __Nazwisko.name() : __Nazwisko,
        __DataUrodzenia.name() : __DataUrodzenia,
        __MiejsceUrodzenia.name() : __MiejsceUrodzenia,
        __ImieOjca.name() : __ImieOjca,
        __ImieMatki.name() : __ImieMatki,
        __NIP.name() : __NIP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TIdentyfikatorOsobyFizycznejZagranicznej = TIdentyfikatorOsobyFizycznejZagranicznej
Namespace.addCategoryObject('typeBinding', 'TIdentyfikatorOsobyFizycznejZagranicznej', TIdentyfikatorOsobyFizycznejZagranicznej)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TIdentyfikatorOsobyNiefizycznej with content type ELEMENT_ONLY
class TIdentyfikatorOsobyNiefizycznej (pyxb.binding.basis.complexTypeDefinition):
    """Podstawowy zestaw danych identyfikacyjnych o osobie niefizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIdentyfikatorOsobyNiefizycznej')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 296, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NIP uses Python identifier NIP
    __NIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIP'), 'NIP', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNIP', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 301, 3), )

    
    NIP = property(__NIP.value, __NIP.set, None, 'Identyfikator podatkowy NIP')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}PelnaNazwa uses Python identifier PelnaNazwa
    __PelnaNazwa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa'), 'PelnaNazwa', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyPelnaNazwa', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 306, 3), )

    
    PelnaNazwa = property(__PelnaNazwa.value, __PelnaNazwa.set, None, 'Pe\u0142na nazwa')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}REGON uses Python identifier REGON
    __REGON = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'REGON'), 'REGON', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyREGON', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 317, 3), )

    
    REGON = property(__REGON.value, __REGON.set, None, 'Numer REGON')

    _ElementMap.update({
        __NIP.name() : __NIP,
        __PelnaNazwa.name() : __PelnaNazwa,
        __REGON.name() : __REGON
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TIdentyfikatorOsobyNiefizycznej = TIdentyfikatorOsobyNiefizycznej
Namespace.addCategoryObject('typeBinding', 'TIdentyfikatorOsobyNiefizycznej', TIdentyfikatorOsobyNiefizycznej)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TIdentyfikatorOsobyNiefizycznejPelny with content type ELEMENT_ONLY
class TIdentyfikatorOsobyNiefizycznejPelny (pyxb.binding.basis.complexTypeDefinition):
    """Pełny zestaw danych identyfikacyjnych o osobie niefizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIdentyfikatorOsobyNiefizycznejPelny')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 324, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NIP uses Python identifier NIP
    __NIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIP'), 'NIP', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNIP', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 329, 3), )

    
    NIP = property(__NIP.value, __NIP.set, None, 'Identyfikator podatkowy NIP')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}PelnaNazwa uses Python identifier PelnaNazwa
    __PelnaNazwa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa'), 'PelnaNazwa', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyPelnaNazwa', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 334, 3), )

    
    PelnaNazwa = property(__PelnaNazwa.value, __PelnaNazwa.set, None, 'Pe\u0142na nazwa')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}SkroconaNazwa uses Python identifier SkroconaNazwa
    __SkroconaNazwa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SkroconaNazwa'), 'SkroconaNazwa', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypySkroconaNazwa', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 345, 3), )

    
    SkroconaNazwa = property(__SkroconaNazwa.value, __SkroconaNazwa.set, None, 'Skr\xf3cona nazwa')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}REGON uses Python identifier REGON
    __REGON = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'REGON'), 'REGON', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznejPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyREGON', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 356, 3), )

    
    REGON = property(__REGON.value, __REGON.set, None, 'Numer REGON')

    _ElementMap.update({
        __NIP.name() : __NIP,
        __PelnaNazwa.name() : __PelnaNazwa,
        __SkroconaNazwa.name() : __SkroconaNazwa,
        __REGON.name() : __REGON
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TIdentyfikatorOsobyNiefizycznejPelny = TIdentyfikatorOsobyNiefizycznejPelny
Namespace.addCategoryObject('typeBinding', 'TIdentyfikatorOsobyNiefizycznejPelny', TIdentyfikatorOsobyNiefizycznejPelny)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TIdentyfikatorOsobyNiefizycznejZagranicznej with content type ELEMENT_ONLY
class TIdentyfikatorOsobyNiefizycznejZagranicznej (pyxb.binding.basis.complexTypeDefinition):
    """Zestaw danych identyfikacyjnych dla osoby niefizycznej zagranicznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIdentyfikatorOsobyNiefizycznejZagranicznej')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 363, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}PelnaNazwa uses Python identifier PelnaNazwa
    __PelnaNazwa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa'), 'PelnaNazwa', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyPelnaNazwa', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 368, 3), )

    
    PelnaNazwa = property(__PelnaNazwa.value, __PelnaNazwa.set, None, 'Pe\u0142na nazwa [Name]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}SkroconaNazwa uses Python identifier SkroconaNazwa
    __SkroconaNazwa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SkroconaNazwa'), 'SkroconaNazwa', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypySkroconaNazwa', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 379, 3), )

    
    SkroconaNazwa = property(__SkroconaNazwa.value, __SkroconaNazwa.set, None, 'Nazwa skr\xf3cona [Short Name]')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}NIP uses Python identifier NIP
    __NIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIP'), 'NIP', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TIdentyfikatorOsobyNiefizycznejZagranicznej_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyNIP', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 390, 3), )

    
    NIP = property(__NIP.value, __NIP.set, None, 'Identyfikator podatkowy NIP [Tax Identification Number (NIP)]')

    _ElementMap.update({
        __PelnaNazwa.name() : __PelnaNazwa,
        __SkroconaNazwa.name() : __SkroconaNazwa,
        __NIP.name() : __NIP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TIdentyfikatorOsobyNiefizycznejZagranicznej = TIdentyfikatorOsobyNiefizycznejZagranicznej
Namespace.addCategoryObject('typeBinding', 'TIdentyfikatorOsobyNiefizycznejZagranicznej', TIdentyfikatorOsobyNiefizycznejZagranicznej)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TPodmiotDowolnyBezAdresu with content type ELEMENT_ONLY
class TPodmiotDowolnyBezAdresu (pyxb.binding.basis.complexTypeDefinition):
    """Skrócony zestaw danych o osobie fizycznej lub niefizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TPodmiotDowolnyBezAdresu')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 398, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna uses Python identifier OsobaFizyczna
    __OsobaFizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), 'OsobaFizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolnyBezAdresu_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaFizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 403, 3), )

    
    OsobaFizyczna = property(__OsobaFizyczna.value, __OsobaFizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaNiefizyczna uses Python identifier OsobaNiefizyczna
    __OsobaNiefizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), 'OsobaNiefizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolnyBezAdresu_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaNiefizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 404, 3), )

    
    OsobaNiefizyczna = property(__OsobaNiefizyczna.value, __OsobaNiefizyczna.set, None, None)

    _ElementMap.update({
        __OsobaFizyczna.name() : __OsobaFizyczna,
        __OsobaNiefizyczna.name() : __OsobaNiefizyczna
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TPodmiotDowolnyBezAdresu = TPodmiotDowolnyBezAdresu
Namespace.addCategoryObject('typeBinding', 'TPodmiotDowolnyBezAdresu', TPodmiotDowolnyBezAdresu)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TPodmiotDowolnyBezAdresu1 with content type ELEMENT_ONLY
class TPodmiotDowolnyBezAdresu1 (pyxb.binding.basis.complexTypeDefinition):
    """Skrócony zestaw danych o osobie fizycznej lub niefizycznej z identyfikatorem NIP albo PESEL"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TPodmiotDowolnyBezAdresu1')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 407, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna uses Python identifier OsobaFizyczna
    __OsobaFizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), 'OsobaFizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolnyBezAdresu1_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaFizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 412, 3), )

    
    OsobaFizyczna = property(__OsobaFizyczna.value, __OsobaFizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaNiefizyczna uses Python identifier OsobaNiefizyczna
    __OsobaNiefizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), 'OsobaNiefizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolnyBezAdresu1_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaNiefizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 413, 3), )

    
    OsobaNiefizyczna = property(__OsobaNiefizyczna.value, __OsobaNiefizyczna.set, None, None)

    _ElementMap.update({
        __OsobaFizyczna.name() : __OsobaFizyczna,
        __OsobaNiefizyczna.name() : __OsobaNiefizyczna
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TPodmiotDowolnyBezAdresu1 = TPodmiotDowolnyBezAdresu1
Namespace.addCategoryObject('typeBinding', 'TPodmiotDowolnyBezAdresu1', TPodmiotDowolnyBezAdresu1)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TPodmiotDowolnyBezAdresu2 with content type ELEMENT_ONLY
class TPodmiotDowolnyBezAdresu2 (pyxb.binding.basis.complexTypeDefinition):
    """Skrócony zestaw danych o osobie fizycznej lub niefizycznej z identyfikatorem NIP"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TPodmiotDowolnyBezAdresu2')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 416, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna uses Python identifier OsobaFizyczna
    __OsobaFizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), 'OsobaFizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolnyBezAdresu2_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaFizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 421, 3), )

    
    OsobaFizyczna = property(__OsobaFizyczna.value, __OsobaFizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaNiefizyczna uses Python identifier OsobaNiefizyczna
    __OsobaNiefizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), 'OsobaNiefizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolnyBezAdresu2_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaNiefizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 422, 3), )

    
    OsobaNiefizyczna = property(__OsobaNiefizyczna.value, __OsobaNiefizyczna.set, None, None)

    _ElementMap.update({
        __OsobaFizyczna.name() : __OsobaFizyczna,
        __OsobaNiefizyczna.name() : __OsobaNiefizyczna
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TPodmiotDowolnyBezAdresu2 = TPodmiotDowolnyBezAdresu2
Namespace.addCategoryObject('typeBinding', 'TPodmiotDowolnyBezAdresu2', TPodmiotDowolnyBezAdresu2)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TOsobaFizyczna with content type ELEMENT_ONLY
class TOsobaFizyczna (pyxb.binding.basis.complexTypeDefinition):
    """Podstawowy zestaw danych o osobie fizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TOsobaFizyczna')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 426, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna uses Python identifier OsobaFizyczna
    __OsobaFizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), 'OsobaFizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaFizyczna_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaFizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 431, 3), )

    
    OsobaFizyczna = property(__OsobaFizyczna.value, __OsobaFizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZamieszkania uses Python identifier AdresZamieszkania
    __AdresZamieszkania = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania'), 'AdresZamieszkania', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaFizyczna_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresZamieszkania', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 432, 3), )

    
    AdresZamieszkania = property(__AdresZamieszkania.value, __AdresZamieszkania.set, None, None)

    _ElementMap.update({
        __OsobaFizyczna.name() : __OsobaFizyczna,
        __AdresZamieszkania.name() : __AdresZamieszkania
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TOsobaFizyczna = TOsobaFizyczna
Namespace.addCategoryObject('typeBinding', 'TOsobaFizyczna', TOsobaFizyczna)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TOsobaFizyczna1 with content type ELEMENT_ONLY
class TOsobaFizyczna1 (pyxb.binding.basis.complexTypeDefinition):
    """Podstawowy zestaw danych o osobie fizycznej z identyfikatorem NIP albo PESEL"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TOsobaFizyczna1')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 443, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna uses Python identifier OsobaFizyczna
    __OsobaFizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), 'OsobaFizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaFizyczna1_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaFizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 448, 3), )

    
    OsobaFizyczna = property(__OsobaFizyczna.value, __OsobaFizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZamieszkania uses Python identifier AdresZamieszkania
    __AdresZamieszkania = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania'), 'AdresZamieszkania', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaFizyczna1_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresZamieszkania', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 449, 3), )

    
    AdresZamieszkania = property(__AdresZamieszkania.value, __AdresZamieszkania.set, None, None)

    _ElementMap.update({
        __OsobaFizyczna.name() : __OsobaFizyczna,
        __AdresZamieszkania.name() : __AdresZamieszkania
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TOsobaFizyczna1 = TOsobaFizyczna1
Namespace.addCategoryObject('typeBinding', 'TOsobaFizyczna1', TOsobaFizyczna1)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TOsobaFizyczna2 with content type ELEMENT_ONLY
class TOsobaFizyczna2 (pyxb.binding.basis.complexTypeDefinition):
    """Podstawowy zestaw danych o osobie fizycznej z identyfikatorem NIP"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TOsobaFizyczna2')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 460, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna uses Python identifier OsobaFizyczna
    __OsobaFizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), 'OsobaFizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaFizyczna2_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaFizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 465, 3), )

    
    OsobaFizyczna = property(__OsobaFizyczna.value, __OsobaFizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZamieszkania uses Python identifier AdresZamieszkania
    __AdresZamieszkania = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania'), 'AdresZamieszkania', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaFizyczna2_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresZamieszkania', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 466, 3), )

    
    AdresZamieszkania = property(__AdresZamieszkania.value, __AdresZamieszkania.set, None, None)

    _ElementMap.update({
        __OsobaFizyczna.name() : __OsobaFizyczna,
        __AdresZamieszkania.name() : __AdresZamieszkania
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TOsobaFizyczna2 = TOsobaFizyczna2
Namespace.addCategoryObject('typeBinding', 'TOsobaFizyczna2', TOsobaFizyczna2)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TOsobaNiefizyczna with content type ELEMENT_ONLY
class TOsobaNiefizyczna (pyxb.binding.basis.complexTypeDefinition):
    """Podstawowy zestaw danych o osobie niefizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TOsobaNiefizyczna')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 477, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaNiefizyczna uses Python identifier OsobaNiefizyczna
    __OsobaNiefizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), 'OsobaNiefizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaNiefizyczna_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaNiefizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 482, 3), )

    
    OsobaNiefizyczna = property(__OsobaNiefizyczna.value, __OsobaNiefizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresSiedziby uses Python identifier AdresSiedziby
    __AdresSiedziby = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresSiedziby'), 'AdresSiedziby', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaNiefizyczna_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresSiedziby', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 483, 3), )

    
    AdresSiedziby = property(__AdresSiedziby.value, __AdresSiedziby.set, None, None)

    _ElementMap.update({
        __OsobaNiefizyczna.name() : __OsobaNiefizyczna,
        __AdresSiedziby.name() : __AdresSiedziby
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TOsobaNiefizyczna = TOsobaNiefizyczna
Namespace.addCategoryObject('typeBinding', 'TOsobaNiefizyczna', TOsobaNiefizyczna)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TOsobaFizycznaPelna with content type ELEMENT_ONLY
class TOsobaFizycznaPelna (pyxb.binding.basis.complexTypeDefinition):
    """Pełny zestaw danych o osobie fizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TOsobaFizycznaPelna')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 515, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna uses Python identifier OsobaFizyczna
    __OsobaFizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), 'OsobaFizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaFizycznaPelna_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaFizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 520, 3), )

    
    OsobaFizyczna = property(__OsobaFizyczna.value, __OsobaFizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZamieszkania uses Python identifier AdresZamieszkania
    __AdresZamieszkania = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania'), 'AdresZamieszkania', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaFizycznaPelna_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresZamieszkania', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 521, 3), )

    
    AdresZamieszkania = property(__AdresZamieszkania.value, __AdresZamieszkania.set, None, None)

    _ElementMap.update({
        __OsobaFizyczna.name() : __OsobaFizyczna,
        __AdresZamieszkania.name() : __AdresZamieszkania
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TOsobaFizycznaPelna = TOsobaFizycznaPelna
Namespace.addCategoryObject('typeBinding', 'TOsobaFizycznaPelna', TOsobaFizycznaPelna)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TOsobaNiefizycznaPelna with content type ELEMENT_ONLY
class TOsobaNiefizycznaPelna (pyxb.binding.basis.complexTypeDefinition):
    """Pełny zestaw danych o osobie fizycznej lub niefizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TOsobaNiefizycznaPelna')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 532, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaNiefizyczna uses Python identifier OsobaNiefizyczna
    __OsobaNiefizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), 'OsobaNiefizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaNiefizycznaPelna_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaNiefizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 537, 3), )

    
    OsobaNiefizyczna = property(__OsobaNiefizyczna.value, __OsobaNiefizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresSiedziby uses Python identifier AdresSiedziby
    __AdresSiedziby = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresSiedziby'), 'AdresSiedziby', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TOsobaNiefizycznaPelna_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresSiedziby', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 538, 3), )

    
    AdresSiedziby = property(__AdresSiedziby.value, __AdresSiedziby.set, None, None)

    _ElementMap.update({
        __OsobaNiefizyczna.name() : __OsobaNiefizyczna,
        __AdresSiedziby.name() : __AdresSiedziby
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TOsobaNiefizycznaPelna = TOsobaNiefizycznaPelna
Namespace.addCategoryObject('typeBinding', 'TOsobaNiefizycznaPelna', TOsobaNiefizycznaPelna)


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TPodmiotDowolnyPelny with content type ELEMENT_ONLY
class TPodmiotDowolnyPelny (pyxb.binding.basis.complexTypeDefinition):
    """Pełny zestaw danych o osobie fizycznej lub niefizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TPodmiotDowolnyPelny')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 549, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna uses Python identifier OsobaFizyczna
    __OsobaFizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), 'OsobaFizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolnyPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaFizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 555, 4), )

    
    OsobaFizyczna = property(__OsobaFizyczna.value, __OsobaFizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaNiefizyczna uses Python identifier OsobaNiefizyczna
    __OsobaNiefizyczna = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), 'OsobaNiefizyczna', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolnyPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyOsobaNiefizyczna', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 556, 4), )

    
    OsobaNiefizyczna = property(__OsobaNiefizyczna.value, __OsobaNiefizyczna.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZamieszkaniaSiedziby uses Python identifier AdresZamieszkaniaSiedziby
    __AdresZamieszkaniaSiedziby = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkaniaSiedziby'), 'AdresZamieszkaniaSiedziby', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolnyPelny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresZamieszkaniaSiedziby', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 558, 3), )

    
    AdresZamieszkaniaSiedziby = property(__AdresZamieszkaniaSiedziby.value, __AdresZamieszkaniaSiedziby.set, None, None)

    _ElementMap.update({
        __OsobaFizyczna.name() : __OsobaFizyczna,
        __OsobaNiefizyczna.name() : __OsobaNiefizyczna,
        __AdresZamieszkaniaSiedziby.name() : __AdresZamieszkaniaSiedziby
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TPodmiotDowolnyPelny = TPodmiotDowolnyPelny
Namespace.addCategoryObject('typeBinding', 'TPodmiotDowolnyPelny', TPodmiotDowolnyPelny)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (TAdres):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 433, 4)
    _ElementMap = TAdres._ElementMap.copy()
    _AttributeMap = TAdres._AttributeMap.copy()
    # Base type is TAdres
    
    # Element AdresPol ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresPol) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Element AdresZagr ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZagr) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Attribute rodzajAdresu uses Python identifier rodzajAdresu
    __rodzajAdresu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rodzajAdresu'), 'rodzajAdresu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_CTD_ANON_rodzajAdresu', pyxb.binding.datatypes.string, fixed=True, unicode_default='RAD', required=True)
    __rodzajAdresu._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 436, 7)
    __rodzajAdresu._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 436, 7)
    
    rodzajAdresu = property(__rodzajAdresu.value, __rodzajAdresu.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rodzajAdresu.name() : __rodzajAdresu
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (TAdres):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 450, 4)
    _ElementMap = TAdres._ElementMap.copy()
    _AttributeMap = TAdres._AttributeMap.copy()
    # Base type is TAdres
    
    # Element AdresPol ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresPol) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Element AdresZagr ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZagr) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Attribute rodzajAdresu uses Python identifier rodzajAdresu
    __rodzajAdresu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rodzajAdresu'), 'rodzajAdresu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_CTD_ANON__rodzajAdresu', pyxb.binding.datatypes.string, fixed=True, unicode_default='RAD', required=True)
    __rodzajAdresu._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 453, 7)
    __rodzajAdresu._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 453, 7)
    
    rodzajAdresu = property(__rodzajAdresu.value, __rodzajAdresu.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rodzajAdresu.name() : __rodzajAdresu
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (TAdres):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 467, 4)
    _ElementMap = TAdres._ElementMap.copy()
    _AttributeMap = TAdres._AttributeMap.copy()
    # Base type is TAdres
    
    # Element AdresPol ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresPol) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Element AdresZagr ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZagr) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Attribute rodzajAdresu uses Python identifier rodzajAdresu
    __rodzajAdresu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rodzajAdresu'), 'rodzajAdresu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_CTD_ANON_2_rodzajAdresu', pyxb.binding.datatypes.string, fixed=True, unicode_default='RAD', required=True)
    __rodzajAdresu._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 470, 7)
    __rodzajAdresu._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 470, 7)
    
    rodzajAdresu = property(__rodzajAdresu.value, __rodzajAdresu.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rodzajAdresu.name() : __rodzajAdresu
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (TAdres):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 484, 4)
    _ElementMap = TAdres._ElementMap.copy()
    _AttributeMap = TAdres._AttributeMap.copy()
    # Base type is TAdres
    
    # Element AdresPol ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresPol) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Element AdresZagr ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZagr) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Attribute rodzajAdresu uses Python identifier rodzajAdresu
    __rodzajAdresu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rodzajAdresu'), 'rodzajAdresu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_CTD_ANON_3_rodzajAdresu', pyxb.binding.datatypes.string, fixed=True, unicode_default='RAD', required=True)
    __rodzajAdresu._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 487, 7)
    __rodzajAdresu._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 487, 7)
    
    rodzajAdresu = property(__rodzajAdresu.value, __rodzajAdresu.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rodzajAdresu.name() : __rodzajAdresu
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TPodmiotDowolny with content type ELEMENT_ONLY
class TPodmiotDowolny (TPodmiotDowolnyBezAdresu):
    """Podstawowy zestaw danych o osobie fizycznej lub niefizycznej"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TPodmiotDowolny')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 494, 1)
    _ElementMap = TPodmiotDowolnyBezAdresu._ElementMap.copy()
    _AttributeMap = TPodmiotDowolnyBezAdresu._AttributeMap.copy()
    # Base type is TPodmiotDowolnyBezAdresu
    
    # Element OsobaFizyczna ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TPodmiotDowolnyBezAdresu
    
    # Element OsobaNiefizyczna ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaNiefizyczna) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TPodmiotDowolnyBezAdresu
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZamieszkaniaSiedziby uses Python identifier AdresZamieszkaniaSiedziby
    __AdresZamieszkaniaSiedziby = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkaniaSiedziby'), 'AdresZamieszkaniaSiedziby', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_TPodmiotDowolny_httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypyAdresZamieszkaniaSiedziby', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 501, 5), )

    
    AdresZamieszkaniaSiedziby = property(__AdresZamieszkaniaSiedziby.value, __AdresZamieszkaniaSiedziby.set, None, None)

    _ElementMap.update({
        __AdresZamieszkaniaSiedziby.name() : __AdresZamieszkaniaSiedziby
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TPodmiotDowolny = TPodmiotDowolny
Namespace.addCategoryObject('typeBinding', 'TPodmiotDowolny', TPodmiotDowolny)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (TAdres):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 502, 6)
    _ElementMap = TAdres._ElementMap.copy()
    _AttributeMap = TAdres._AttributeMap.copy()
    # Base type is TAdres
    
    # Element AdresPol ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresPol) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Element AdresZagr ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZagr) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Attribute rodzajAdresu uses Python identifier rodzajAdresu
    __rodzajAdresu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rodzajAdresu'), 'rodzajAdresu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_CTD_ANON_4_rodzajAdresu', pyxb.binding.datatypes.string, fixed=True, unicode_default='RAD', required=True)
    __rodzajAdresu._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 505, 9)
    __rodzajAdresu._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 505, 9)
    
    rodzajAdresu = property(__rodzajAdresu.value, __rodzajAdresu.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rodzajAdresu.name() : __rodzajAdresu
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (TAdres):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 522, 4)
    _ElementMap = TAdres._ElementMap.copy()
    _AttributeMap = TAdres._AttributeMap.copy()
    # Base type is TAdres
    
    # Element AdresPol ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresPol) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Element AdresZagr ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZagr) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Attribute rodzajAdresu uses Python identifier rodzajAdresu
    __rodzajAdresu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rodzajAdresu'), 'rodzajAdresu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_CTD_ANON_5_rodzajAdresu', pyxb.binding.datatypes.string, fixed=True, unicode_default='RAD', required=True)
    __rodzajAdresu._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 525, 7)
    __rodzajAdresu._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 525, 7)
    
    rodzajAdresu = property(__rodzajAdresu.value, __rodzajAdresu.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rodzajAdresu.name() : __rodzajAdresu
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (TAdres):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 539, 4)
    _ElementMap = TAdres._ElementMap.copy()
    _AttributeMap = TAdres._AttributeMap.copy()
    # Base type is TAdres
    
    # Element AdresPol ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresPol) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Element AdresZagr ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZagr) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Attribute rodzajAdresu uses Python identifier rodzajAdresu
    __rodzajAdresu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rodzajAdresu'), 'rodzajAdresu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_CTD_ANON_6_rodzajAdresu', pyxb.binding.datatypes.string, fixed=True, unicode_default='RAD', required=True)
    __rodzajAdresu._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 542, 7)
    __rodzajAdresu._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 542, 7)
    
    rodzajAdresu = property(__rodzajAdresu.value, __rodzajAdresu.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rodzajAdresu.name() : __rodzajAdresu
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (TAdres):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 559, 4)
    _ElementMap = TAdres._ElementMap.copy()
    _AttributeMap = TAdres._AttributeMap.copy()
    # Base type is TAdres
    
    # Element AdresPol ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresPol) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Element AdresZagr ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}AdresZagr) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TAdres
    
    # Attribute rodzajAdresu uses Python identifier rodzajAdresu
    __rodzajAdresu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rodzajAdresu'), 'rodzajAdresu', '__httpcrd_gov_plxmlschematydziedzinowemf20160125eDDefinicjeTypy_CTD_ANON_7_rodzajAdresu', pyxb.binding.datatypes.string, fixed=True, unicode_default='RAD', required=True)
    __rodzajAdresu._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 562, 7)
    __rodzajAdresu._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 562, 7)
    
    rodzajAdresu = property(__rodzajAdresu.value, __rodzajAdresu.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rodzajAdresu.name() : __rodzajAdresu
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7




TAdres._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresPol'), TAdresPolski, scope=TAdres, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4)))

TAdres._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr'), TAdresZagraniczny, scope=TAdres, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TAdres._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPol')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TAdres._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TAdres._Automaton = _BuildAutomaton()




TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodKraju'), TKodKraju, scope=TAdresPolski, documentation='Kraj', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 23, 3), fixed=True, unicode_default='PL'))

TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Wojewodztwo'), TJednAdmin, scope=TAdresPolski, documentation='Wojew\xf3dztwo', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 28, 3)))

TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Powiat'), TJednAdmin, scope=TAdresPolski, documentation='Powiat', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 33, 3)))

TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Gmina'), TJednAdmin, scope=TAdresPolski, documentation='Gmina', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 38, 3)))

TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ulica'), TUlica, scope=TAdresPolski, documentation='Nazwa ulicy', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 43, 3)))

TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrDomu'), TNrBudynku, scope=TAdresPolski, documentation='Numer budynku', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 48, 3)))

TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrLokalu'), TNrLokalu, scope=TAdresPolski, documentation='Numer lokalu', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 53, 3)))

TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Miejscowosc'), TMiejscowosc, scope=TAdresPolski, documentation='Nazwa miejscowo\u015bci', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 58, 3)))

TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodPocztowy'), TKodPocztowy, scope=TAdresPolski, documentation='Kod pocztowy', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 63, 3)))

TAdresPolski._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Poczta'), TMiejscowosc, scope=TAdresPolski, documentation='Nazwa urz\u0119du pocztowego', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 68, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 43, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 53, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodKraju')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 23, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Wojewodztwo')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 28, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Powiat')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 33, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Gmina')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 38, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ulica')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrDomu')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 48, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrLokalu')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 53, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Miejscowosc')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 58, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodPocztowy')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 63, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TAdresPolski._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Poczta')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 68, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TAdresPolski._Automaton = _BuildAutomaton_()




TAdresZagraniczny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodKraju'), STD_ANON_7, scope=TAdresZagraniczny, documentation='Kod Kraju [Country Code]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 80, 3)))

TAdresZagraniczny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodPocztowy'), TKodPocztowy, scope=TAdresZagraniczny, documentation='Kod pocztowy [Postal code]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 91, 3)))

TAdresZagraniczny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Miejscowosc'), TMiejscowosc, scope=TAdresZagraniczny, documentation='Nazwa miejscowo\u015bci [City]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 96, 3)))

TAdresZagraniczny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ulica'), TUlica, scope=TAdresZagraniczny, documentation='Nazwa ulicy [Street]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 101, 3)))

TAdresZagraniczny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrDomu'), TNrBudynku, scope=TAdresZagraniczny, documentation='Numer budynku [Building number]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 106, 3)))

TAdresZagraniczny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrLokalu'), TNrLokalu, scope=TAdresZagraniczny, documentation='Numer lokalu [Flat number]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 111, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 91, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 101, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 106, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 111, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresZagraniczny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodKraju')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 80, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresZagraniczny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodPocztowy')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 91, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TAdresZagraniczny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Miejscowosc')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 96, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TAdresZagraniczny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ulica')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 101, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TAdresZagraniczny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrDomu')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 106, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TAdresZagraniczny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrLokalu')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 111, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TAdresZagraniczny._Automaton = _BuildAutomaton_2()




TIdentyfikatorOsobyFizycznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIP'), TNrNIP, scope=TIdentyfikatorOsobyFizycznej, documentation='Identyfikator podatkowy NIP', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 124, 3)))

TIdentyfikatorOsobyFizycznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), TImie, scope=TIdentyfikatorOsobyFizycznej, documentation='Pierwsze imi\u0119', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 129, 3)))

TIdentyfikatorOsobyFizycznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), TNazwisko, scope=TIdentyfikatorOsobyFizycznej, documentation='Nazwisko', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 134, 3)))

TIdentyfikatorOsobyFizycznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), TData, scope=TIdentyfikatorOsobyFizycznej, documentation='Data urodzenia', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 139, 3)))

TIdentyfikatorOsobyFizycznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PESEL'), TNrPESEL, scope=TIdentyfikatorOsobyFizycznej, documentation='Identyfikator podatkowy numer PESEL', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 144, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 144, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIP')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 124, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 129, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 134, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 139, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PESEL')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 144, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TIdentyfikatorOsobyFizycznej._Automaton = _BuildAutomaton_3()




TIdentyfikatorOsobyFizycznej1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIP'), TNrNIP, scope=TIdentyfikatorOsobyFizycznej1, documentation='Identyfikator podatkowy NIP', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 157, 4)))

TIdentyfikatorOsobyFizycznej1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PESEL'), TNrPESEL, scope=TIdentyfikatorOsobyFizycznej1, documentation='Identyfikator podatkowy numer PESEL', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 162, 4)))

TIdentyfikatorOsobyFizycznej1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), TImie, scope=TIdentyfikatorOsobyFizycznej1, documentation='Pierwsze imi\u0119', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 168, 3)))

TIdentyfikatorOsobyFizycznej1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), TNazwisko, scope=TIdentyfikatorOsobyFizycznej1, documentation='Nazwisko', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 173, 3)))

TIdentyfikatorOsobyFizycznej1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), TData, scope=TIdentyfikatorOsobyFizycznej1, documentation='Data urodzenia', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 178, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIP')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 157, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PESEL')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 162, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 168, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 173, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 178, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TIdentyfikatorOsobyFizycznej1._Automaton = _BuildAutomaton_4()




TIdentyfikatorOsobyFizycznej2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIP'), TNrNIP, scope=TIdentyfikatorOsobyFizycznej2, documentation='Identyfikator podatkowy NIP', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 190, 3)))

TIdentyfikatorOsobyFizycznej2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), TImie, scope=TIdentyfikatorOsobyFizycznej2, documentation='Pierwsze imi\u0119', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 195, 3)))

TIdentyfikatorOsobyFizycznej2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), TNazwisko, scope=TIdentyfikatorOsobyFizycznej2, documentation='Nazwisko', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 200, 3)))

TIdentyfikatorOsobyFizycznej2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), TData, scope=TIdentyfikatorOsobyFizycznej2, documentation='Data urodzenia', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 205, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIP')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 190, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 195, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 200, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznej2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 205, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TIdentyfikatorOsobyFizycznej2._Automaton = _BuildAutomaton_5()




TIdentyfikatorOsobyFizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIP'), TNrNIP, scope=TIdentyfikatorOsobyFizycznejPelny, documentation='Identyfikator podatkowy NIP', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 217, 3)))

TIdentyfikatorOsobyFizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), TImie, scope=TIdentyfikatorOsobyFizycznejPelny, documentation='Pierwsze imi\u0119', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 222, 3)))

TIdentyfikatorOsobyFizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), TNazwisko, scope=TIdentyfikatorOsobyFizycznejPelny, documentation='Nazwisko', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 227, 3)))

TIdentyfikatorOsobyFizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), TData, scope=TIdentyfikatorOsobyFizycznejPelny, documentation='Data urodzenia', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 232, 3)))

TIdentyfikatorOsobyFizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImieOjca'), TImie, scope=TIdentyfikatorOsobyFizycznejPelny, documentation='Imi\u0119 ojca', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 237, 3)))

TIdentyfikatorOsobyFizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImieMatki'), TImie, scope=TIdentyfikatorOsobyFizycznejPelny, documentation='Imi\u0119 matki', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 242, 3)))

TIdentyfikatorOsobyFizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PESEL'), TNrPESEL, scope=TIdentyfikatorOsobyFizycznejPelny, documentation='Identyfikator podatkowy numer PESEL', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 247, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 217, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIP')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 217, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 222, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 227, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 232, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImieOjca')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 237, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImieMatki')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 242, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PESEL')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 247, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TIdentyfikatorOsobyFizycznejPelny._Automaton = _BuildAutomaton_6()




TIdentyfikatorOsobyFizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze'), TImie, scope=TIdentyfikatorOsobyFizycznejZagranicznej, documentation='Imi\u0119 pierwsze [First name]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 259, 3)))

TIdentyfikatorOsobyFizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko'), TNazwisko, scope=TIdentyfikatorOsobyFizycznejZagranicznej, documentation='Nazwisko [Family name]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 264, 3)))

TIdentyfikatorOsobyFizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia'), TData, scope=TIdentyfikatorOsobyFizycznejZagranicznej, documentation='Data urodzenia [Date of Birth]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 269, 3)))

TIdentyfikatorOsobyFizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MiejsceUrodzenia'), TMiejscowosc, scope=TIdentyfikatorOsobyFizycznejZagranicznej, documentation='Miejsce urodzenia [Place of Birth]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 274, 3)))

TIdentyfikatorOsobyFizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImieOjca'), TImie, scope=TIdentyfikatorOsobyFizycznejZagranicznej, documentation='Imi\u0119 ojca [Father\u2019s name]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 279, 3)))

TIdentyfikatorOsobyFizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImieMatki'), TImie, scope=TIdentyfikatorOsobyFizycznejZagranicznej, documentation='Imi\u0119 matki [Mother\u2019s name]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 284, 3)))

TIdentyfikatorOsobyFizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIP'), TNrNIP, scope=TIdentyfikatorOsobyFizycznejZagranicznej, documentation='Identyfikator podatkowy NIP [Tax Identification Number (NIP)]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 289, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 279, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 284, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 289, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImiePierwsze')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 259, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nazwisko')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 264, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataUrodzenia')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 269, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MiejsceUrodzenia')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 274, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImieOjca')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 279, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImieMatki')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 284, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyFizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIP')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 289, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TIdentyfikatorOsobyFizycznejZagranicznej._Automaton = _BuildAutomaton_7()




TIdentyfikatorOsobyNiefizycznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIP'), TNrNIP, scope=TIdentyfikatorOsobyNiefizycznej, documentation='Identyfikator podatkowy NIP', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 301, 3)))

TIdentyfikatorOsobyNiefizycznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa'), STD_ANON_2, scope=TIdentyfikatorOsobyNiefizycznej, documentation='Pe\u0142na nazwa', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 306, 3)))

TIdentyfikatorOsobyNiefizycznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'REGON'), TNrREGON, scope=TIdentyfikatorOsobyNiefizycznej, documentation='Numer REGON', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 317, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 317, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIP')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 301, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 306, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'REGON')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 317, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TIdentyfikatorOsobyNiefizycznej._Automaton = _BuildAutomaton_8()




TIdentyfikatorOsobyNiefizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIP'), TNrNIP, scope=TIdentyfikatorOsobyNiefizycznejPelny, documentation='Identyfikator podatkowy NIP', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 329, 3)))

TIdentyfikatorOsobyNiefizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa'), STD_ANON_3, scope=TIdentyfikatorOsobyNiefizycznejPelny, documentation='Pe\u0142na nazwa', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 334, 3)))

TIdentyfikatorOsobyNiefizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SkroconaNazwa'), STD_ANON_4, scope=TIdentyfikatorOsobyNiefizycznejPelny, documentation='Skr\xf3cona nazwa', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 345, 3)))

TIdentyfikatorOsobyNiefizycznejPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'REGON'), TNrREGON, scope=TIdentyfikatorOsobyNiefizycznejPelny, documentation='Numer REGON', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 356, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 329, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIP')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 329, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 334, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SkroconaNazwa')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 345, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznejPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'REGON')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 356, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TIdentyfikatorOsobyNiefizycznejPelny._Automaton = _BuildAutomaton_9()




TIdentyfikatorOsobyNiefizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa'), STD_ANON_5, scope=TIdentyfikatorOsobyNiefizycznejZagranicznej, documentation='Pe\u0142na nazwa [Name]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 368, 3)))

TIdentyfikatorOsobyNiefizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SkroconaNazwa'), STD_ANON_6, scope=TIdentyfikatorOsobyNiefizycznejZagranicznej, documentation='Nazwa skr\xf3cona [Short Name]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 379, 3)))

TIdentyfikatorOsobyNiefizycznejZagranicznej._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIP'), TNrNIP, scope=TIdentyfikatorOsobyNiefizycznejZagranicznej, documentation='Identyfikator podatkowy NIP [Tax Identification Number (NIP)]', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 390, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 379, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 390, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 368, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SkroconaNazwa')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 379, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TIdentyfikatorOsobyNiefizycznejZagranicznej._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIP')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 390, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TIdentyfikatorOsobyNiefizycznejZagranicznej._Automaton = _BuildAutomaton_10()




TPodmiotDowolnyBezAdresu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), TIdentyfikatorOsobyFizycznej, scope=TPodmiotDowolnyBezAdresu, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 403, 3)))

TPodmiotDowolnyBezAdresu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), TIdentyfikatorOsobyNiefizycznej, scope=TPodmiotDowolnyBezAdresu, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 404, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolnyBezAdresu._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 403, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolnyBezAdresu._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 404, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TPodmiotDowolnyBezAdresu._Automaton = _BuildAutomaton_11()




TPodmiotDowolnyBezAdresu1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), TIdentyfikatorOsobyFizycznej1, scope=TPodmiotDowolnyBezAdresu1, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 412, 3)))

TPodmiotDowolnyBezAdresu1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), TIdentyfikatorOsobyNiefizycznej, scope=TPodmiotDowolnyBezAdresu1, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 413, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolnyBezAdresu1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 412, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolnyBezAdresu1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 413, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TPodmiotDowolnyBezAdresu1._Automaton = _BuildAutomaton_12()




TPodmiotDowolnyBezAdresu2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), TIdentyfikatorOsobyFizycznej2, scope=TPodmiotDowolnyBezAdresu2, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 421, 3)))

TPodmiotDowolnyBezAdresu2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), TIdentyfikatorOsobyNiefizycznej, scope=TPodmiotDowolnyBezAdresu2, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 422, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolnyBezAdresu2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 421, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolnyBezAdresu2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 422, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TPodmiotDowolnyBezAdresu2._Automaton = _BuildAutomaton_13()




TOsobaFizyczna._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), TIdentyfikatorOsobyFizycznej, scope=TOsobaFizyczna, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 431, 3)))

TOsobaFizyczna._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania'), CTD_ANON, scope=TOsobaFizyczna, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 432, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TOsobaFizyczna._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 431, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TOsobaFizyczna._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 432, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TOsobaFizyczna._Automaton = _BuildAutomaton_14()




TOsobaFizyczna1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), TIdentyfikatorOsobyFizycznej1, scope=TOsobaFizyczna1, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 448, 3)))

TOsobaFizyczna1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania'), CTD_ANON_, scope=TOsobaFizyczna1, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 449, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TOsobaFizyczna1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 448, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TOsobaFizyczna1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 449, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TOsobaFizyczna1._Automaton = _BuildAutomaton_15()




TOsobaFizyczna2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), TIdentyfikatorOsobyFizycznej2, scope=TOsobaFizyczna2, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 465, 3)))

TOsobaFizyczna2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania'), CTD_ANON_2, scope=TOsobaFizyczna2, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 466, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TOsobaFizyczna2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 465, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TOsobaFizyczna2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 466, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TOsobaFizyczna2._Automaton = _BuildAutomaton_16()




TOsobaNiefizyczna._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), TIdentyfikatorOsobyNiefizycznej, scope=TOsobaNiefizyczna, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 482, 3)))

TOsobaNiefizyczna._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresSiedziby'), CTD_ANON_3, scope=TOsobaNiefizyczna, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 483, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TOsobaNiefizyczna._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 482, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TOsobaNiefizyczna._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresSiedziby')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 483, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TOsobaNiefizyczna._Automaton = _BuildAutomaton_17()




TOsobaFizycznaPelna._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), TIdentyfikatorOsobyFizycznejPelny, scope=TOsobaFizycznaPelna, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 520, 3)))

TOsobaFizycznaPelna._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania'), CTD_ANON_5, scope=TOsobaFizycznaPelna, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 521, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TOsobaFizycznaPelna._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 520, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TOsobaFizycznaPelna._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkania')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 521, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TOsobaFizycznaPelna._Automaton = _BuildAutomaton_18()




TOsobaNiefizycznaPelna._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), TIdentyfikatorOsobyNiefizycznejPelny, scope=TOsobaNiefizycznaPelna, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 537, 3)))

TOsobaNiefizycznaPelna._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresSiedziby'), CTD_ANON_6, scope=TOsobaNiefizycznaPelna, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 538, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TOsobaNiefizycznaPelna._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 537, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TOsobaNiefizycznaPelna._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresSiedziby')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 538, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TOsobaNiefizycznaPelna._Automaton = _BuildAutomaton_19()




TPodmiotDowolnyPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna'), TIdentyfikatorOsobyFizycznejPelny, scope=TPodmiotDowolnyPelny, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 555, 4)))

TPodmiotDowolnyPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna'), TIdentyfikatorOsobyNiefizycznejPelny, scope=TPodmiotDowolnyPelny, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 556, 4)))

TPodmiotDowolnyPelny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkaniaSiedziby'), CTD_ANON_7, scope=TPodmiotDowolnyPelny, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 558, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolnyPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 555, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolnyPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 556, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolnyPelny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkaniaSiedziby')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 558, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TPodmiotDowolnyPelny._Automaton = _BuildAutomaton_20()




def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPol')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_21()




def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPol')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_22()




def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPol')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_23()




def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPol')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_24()




TPodmiotDowolny._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkaniaSiedziby'), CTD_ANON_4, scope=TPodmiotDowolny, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 501, 5)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 403, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OsobaNiefizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 404, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TPodmiotDowolny._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZamieszkaniaSiedziby')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 501, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TPodmiotDowolny._Automaton = _BuildAutomaton_25()




def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPol')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_26()




def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPol')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_27()




def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPol')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_28()




def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPol')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresZagr')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_29()

