# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/vat/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:82ad655d02bcd817cab2a56c283f6d4eac986efc
# Generated 2018-03-08 13:30:04.760884 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://jpk.mf.gov.pl/wzor/2017/11/13/1113/

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
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://jpk.mf.gov.pl/wzor/2017/11/13/1113/', create_if_missing=True)
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


# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}TKodFormularza
class TKodFormularza (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Symbol wzoru formularza"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodFormularza')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 4, 1)
    _Documentation = 'Symbol wzoru formularza'
TKodFormularza._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodFormularza, enum_prefix=None)
TKodFormularza.JPK_VAT = TKodFormularza._CF_enumeration.addEnumeration(unicode_value='JPK_VAT', tag='JPK_VAT')
TKodFormularza._InitializeFacetMap(TKodFormularza._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodFormularza', TKodFormularza)
_module_typeBindings.TKodFormularza = TKodFormularza

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 49, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='3', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 81, 4)
    _Documentation = None
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(240))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minLength,
   STD_ANON_._CF_maxLength)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}TKwotowy
class TKwotowy (pyxb.binding.datatypes.decimal):

    """Wartość numeryczna 18 znaków max, w tym 2 znaki po przecinku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwotowy')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 90, 1)
    _Documentation = 'Warto\u015b\u0107 numeryczna 18 znak\xf3w max, w tym 2 znaki po przecinku'
TKwotowy._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TKwotowy._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
TKwotowy._InitializeFacetMap(TKwotowy._CF_fractionDigits,
   TKwotowy._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TKwotowy', TKwotowy)
_module_typeBindings.TKwotowy = TKwotowy

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}TZnakowyJPK
class TZnakowyJPK (pyxb.binding.datatypes.token):

    """Typ znakowy ograniczony do 256 znaków"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TZnakowyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 107, 1)
    _Documentation = 'Typ znakowy ograniczony do 256 znak\xf3w'
TZnakowyJPK._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TZnakowyJPK._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
TZnakowyJPK._InitializeFacetMap(TZnakowyJPK._CF_minLength,
   TZnakowyJPK._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TZnakowyJPK', TZnakowyJPK)
_module_typeBindings.TZnakowyJPK = TZnakowyJPK

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}TAdresEmail
class TAdresEmail (pyxb.binding.datatypes.token):

    """Adres e-mail"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TAdresEmail')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 116, 1)
    _Documentation = 'Adres e-mail'
TAdresEmail._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
TAdresEmail._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
TAdresEmail._CF_pattern = pyxb.binding.facets.CF_pattern()
TAdresEmail._CF_pattern.addPattern(pattern='([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})')
TAdresEmail._InitializeFacetMap(TAdresEmail._CF_minLength,
   TAdresEmail._CF_maxLength,
   TAdresEmail._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TAdresEmail', TAdresEmail)
_module_typeBindings.TAdresEmail = TAdresEmail

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 149, 8)
    _Documentation = None
STD_ANON_2._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(240))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_minLength,
   STD_ANON_2._CF_maxLength)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}TDataCzas
class TDataCzas (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TDataCzas):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TDataCzas')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 12, 1)
    _Documentation = None
TDataCzas._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TDataCzas, value=pyxb.binding.datatypes.dateTime('2016-07-01T00:00:00Z'))
TDataCzas._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=TDataCzas, value=pyxb.binding.datatypes.dateTime('2030-12-31T23:59:59Z'))
TDataCzas._InitializeFacetMap(TDataCzas._CF_minInclusive,
   TDataCzas._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'TDataCzas', TDataCzas)
_module_typeBindings.TDataCzas = TDataCzas

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}TData
class TData (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TData')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 18, 1)
    _Documentation = None
TData._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TData, value=pyxb.binding.datatypes.date('2016-07-01'))
TData._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=TData, value=pyxb.binding.datatypes.date('2030-01-01'))
TData._InitializeFacetMap(TData._CF_minInclusive,
   TData._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'TData', TData)
_module_typeBindings.TData = TData

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}TDataT
class TDataT (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData):

    """Data transakcji lub zdarzenia"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TDataT')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 24, 1)
    _Documentation = 'Data transakcji lub zdarzenia'
TDataT._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TDataT, value=pyxb.binding.datatypes.date('2006-01-01'))
TDataT._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=TDataT, value=pyxb.binding.datatypes.date('2030-01-01'))
TDataT._InitializeFacetMap(TDataT._CF_minInclusive,
   TDataT._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'TDataT', TDataT)
_module_typeBindings.TDataT = TDataT

# Atomic simple type: [anonymous]
class STD_ANON_3 (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 56, 4)
    _Documentation = None
STD_ANON_3._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_3, value=pyxb.binding.datatypes.nonNegativeInteger(999))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxInclusive)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}TNaturalnyJPK
class TNaturalnyJPK (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny):

    """Liczby naturalne większe od zera"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaturalnyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 99, 1)
    _Documentation = 'Liczby naturalne wi\u0119ksze od zera'
TNaturalnyJPK._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny, value=pyxb.binding.datatypes.integer(0))
TNaturalnyJPK._InitializeFacetMap(TNaturalnyJPK._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'TNaturalnyJPK', TNaturalnyJPK)
_module_typeBindings.TNaturalnyJPK = TNaturalnyJPK

# Complex type {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}TNaglowek with content type ELEMENT_ONLY
class TNaglowek (pyxb.binding.basis.complexTypeDefinition):
    """Nagłówek JPK_VAT"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaglowek')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 33, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}KodFormularza uses Python identifier KodFormularza
    __KodFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), 'KodFormularza', '__httpjpk_mf_gov_plwzor201711131113_TNaglowek_httpjpk_mf_gov_plwzor201711131113KodFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 38, 3), )

    
    KodFormularza = property(__KodFormularza.value, __KodFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}WariantFormularza uses Python identifier WariantFormularza
    __WariantFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), 'WariantFormularza', '__httpjpk_mf_gov_plwzor201711131113_TNaglowek_httpjpk_mf_gov_plwzor201711131113WariantFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 48, 3), )

    
    WariantFormularza = property(__WariantFormularza.value, __WariantFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}CelZlozenia uses Python identifier CelZlozenia
    __CelZlozenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), 'CelZlozenia', '__httpjpk_mf_gov_plwzor201711131113_TNaglowek_httpjpk_mf_gov_plwzor201711131113CelZlozenia', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 55, 3), )

    
    CelZlozenia = property(__CelZlozenia.value, __CelZlozenia.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}DataWytworzeniaJPK uses Python identifier DataWytworzeniaJPK
    __DataWytworzeniaJPK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), 'DataWytworzeniaJPK', '__httpjpk_mf_gov_plwzor201711131113_TNaglowek_httpjpk_mf_gov_plwzor201711131113DataWytworzeniaJPK', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 62, 3), )

    
    DataWytworzeniaJPK = property(__DataWytworzeniaJPK.value, __DataWytworzeniaJPK.set, None, 'Data i czas wytworzenia JPK_VAT')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}DataOd uses Python identifier DataOd
    __DataOd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), 'DataOd', '__httpjpk_mf_gov_plwzor201711131113_TNaglowek_httpjpk_mf_gov_plwzor201711131113DataOd', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 67, 3), )

    
    DataOd = property(__DataOd.value, __DataOd.set, None, 'Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_VAT')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}DataDo uses Python identifier DataDo
    __DataDo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), 'DataDo', '__httpjpk_mf_gov_plwzor201711131113_TNaglowek_httpjpk_mf_gov_plwzor201711131113DataDo', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 72, 3), )

    
    DataDo = property(__DataDo.value, __DataDo.set, None, 'Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_VAT')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}NazwaSystemu uses Python identifier NazwaSystemu
    __NazwaSystemu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NazwaSystemu'), 'NazwaSystemu', '__httpjpk_mf_gov_plwzor201711131113_TNaglowek_httpjpk_mf_gov_plwzor201711131113NazwaSystemu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 77, 3), )

    
    NazwaSystemu = property(__NazwaSystemu.value, __NazwaSystemu.set, None, 'Nazwa systemu, z kt\xf3rego pochodz\u0105 dane')

    _ElementMap.update({
        __KodFormularza.name() : __KodFormularza,
        __WariantFormularza.name() : __WariantFormularza,
        __CelZlozenia.name() : __CelZlozenia,
        __DataWytworzeniaJPK.name() : __DataWytworzeniaJPK,
        __DataOd.name() : __DataOd,
        __DataDo.name() : __DataDo,
        __NazwaSystemu.name() : __NazwaSystemu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TNaglowek = TNaglowek
Namespace.addCategoryObject('typeBinding', 'TNaglowek', TNaglowek)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Jednolity plik kontrolny dla ewidencji zakupu i sprzedaży VAT"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 130, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}Naglowek uses Python identifier Naglowek
    __Naglowek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), 'Naglowek', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_httpjpk_mf_gov_plwzor201711131113Naglowek', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 132, 4), )

    
    Naglowek = property(__Naglowek.value, __Naglowek.set, None, 'Nag\u0142\xf3wek JPK_VAT')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}Podmiot1 uses Python identifier Podmiot1
    __Podmiot1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), 'Podmiot1', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_httpjpk_mf_gov_plwzor201711131113Podmiot1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 137, 4), )

    
    Podmiot1 = property(__Podmiot1.value, __Podmiot1.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}SprzedazWiersz uses Python identifier SprzedazWiersz
    __SprzedazWiersz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SprzedazWiersz'), 'SprzedazWiersz', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_httpjpk_mf_gov_plwzor201711131113SprzedazWiersz', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 161, 5), )

    
    SprzedazWiersz = property(__SprzedazWiersz.value, __SprzedazWiersz.set, None, 'Ewidencja sprzeda\u017cy oraz naby\u0107 towar\xf3w i us\u0142ug dla kt\xf3rych podmiot obowi\u0105zany jest naliczy\u0107 podatek nale\u017cny - tj. wewn\u0105trzwsp\xf3lnotowe nabycia towar\xf3w, import towar\xf3w podlegaj\u0105cych rozliczeniu zgodnie z art. 33 a ustawy, import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28 b ustawy, import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28 b ustawy, dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca), dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}SprzedazCtrl uses Python identifier SprzedazCtrl
    __SprzedazCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SprzedazCtrl'), 'SprzedazCtrl', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_httpjpk_mf_gov_plwzor201711131113SprzedazCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 374, 5), )

    
    SprzedazCtrl = property(__SprzedazCtrl.value, __SprzedazCtrl.set, None, 'Sumy kontrolne dla ewidencji sprzeda\u017cy VAT')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}ZakupWiersz uses Python identifier ZakupWiersz
    __ZakupWiersz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ZakupWiersz'), 'ZakupWiersz', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_httpjpk_mf_gov_plwzor201711131113ZakupWiersz', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 395, 5), )

    
    ZakupWiersz = property(__ZakupWiersz.value, __ZakupWiersz.set, None, 'Ewidencja zakupu VAT')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}ZakupCtrl uses Python identifier ZakupCtrl
    __ZakupCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ZakupCtrl'), 'ZakupCtrl', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_httpjpk_mf_gov_plwzor201711131113ZakupCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 483, 5), )

    
    ZakupCtrl = property(__ZakupCtrl.value, __ZakupCtrl.set, None, 'Sumy kontrolne dla ewidencji zakupu VAT')

    _ElementMap.update({
        __Naglowek.name() : __Naglowek,
        __Podmiot1.name() : __Podmiot1,
        __SprzedazWiersz.name() : __SprzedazWiersz,
        __SprzedazCtrl.name() : __SprzedazCtrl,
        __ZakupWiersz.name() : __ZakupWiersz,
        __ZakupCtrl.name() : __ZakupCtrl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 138, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}NIP uses Python identifier NIP
    __NIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIP'), 'NIP', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON__httpjpk_mf_gov_plwzor201711131113NIP', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 140, 7), )

    
    NIP = property(__NIP.value, __NIP.set, None, 'Identyfikator podatkowy NIP')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}PelnaNazwa uses Python identifier PelnaNazwa
    __PelnaNazwa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa'), 'PelnaNazwa', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON__httpjpk_mf_gov_plwzor201711131113PelnaNazwa', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 145, 7), )

    
    PelnaNazwa = property(__PelnaNazwa.value, __PelnaNazwa.set, None, 'Pe\u0142na nazwa')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}Email uses Python identifier Email
    __Email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Email'), 'Email', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON__httpjpk_mf_gov_plwzor201711131113Email', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 156, 7), )

    
    Email = property(__Email.value, __Email.set, None, None)

    _ElementMap.update({
        __NIP.name() : __NIP,
        __PelnaNazwa.name() : __PelnaNazwa,
        __Email.name() : __Email
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Ewidencja sprzedaży oraz nabyć towarów i usług dla których podmiot obowiązany jest naliczyć podatek należny - tj. wewnątrzwspólnotowe nabycia towarów, import towarów podlegających rozliczeniu zgodnie z art. 33 a ustawy, import usług z wyłączeniem usług nabywanych od podatników podatku od wartości dodanej, do których stosuje się art. 28 b ustawy, import usług nabywanych od podatników podatku od wartości dodanej, do których stosuje się art. 28 b ustawy, dostawa towarów, dla których podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wypełnia nabywca), dostawa towarów, dla których podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wypełnia nabywca)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 165, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}LpSprzedazy uses Python identifier LpSprzedazy
    __LpSprzedazy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LpSprzedazy'), 'LpSprzedazy', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113LpSprzedazy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 167, 8), )

    
    LpSprzedazy = property(__LpSprzedazy.value, __LpSprzedazy.set, None, 'Lp. wiersza ewidencji sprzeda\u017cy VAT')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}NrKontrahenta uses Python identifier NrKontrahenta
    __NrKontrahenta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrKontrahenta'), 'NrKontrahenta', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113NrKontrahenta', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 172, 8), )

    
    NrKontrahenta = property(__NrKontrahenta.value, __NrKontrahenta.set, None, 'Numer, za pomoc\u0105 kt\xf3rego kontrahent jest zidentyfikowany na potrzeby podatku lub podatku od warto\u015bci dodanej')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}NazwaKontrahenta uses Python identifier NazwaKontrahenta
    __NazwaKontrahenta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NazwaKontrahenta'), 'NazwaKontrahenta', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113NazwaKontrahenta', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 177, 8), )

    
    NazwaKontrahenta = property(__NazwaKontrahenta.value, __NazwaKontrahenta.set, None, 'Imi\u0119 i nazwisko lub nazwa kontrahenta')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}AdresKontrahenta uses Python identifier AdresKontrahenta
    __AdresKontrahenta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresKontrahenta'), 'AdresKontrahenta', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113AdresKontrahenta', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 182, 8), )

    
    AdresKontrahenta = property(__AdresKontrahenta.value, __AdresKontrahenta.set, None, 'Adres kontrahenta')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}DowodSprzedazy uses Python identifier DowodSprzedazy
    __DowodSprzedazy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DowodSprzedazy'), 'DowodSprzedazy', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113DowodSprzedazy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 187, 8), )

    
    DowodSprzedazy = property(__DowodSprzedazy.value, __DowodSprzedazy.set, None, 'Numer dowodu sprzeda\u017cy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}DataWystawienia uses Python identifier DataWystawienia
    __DataWystawienia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWystawienia'), 'DataWystawienia', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113DataWystawienia', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 192, 8), )

    
    DataWystawienia = property(__DataWystawienia.value, __DataWystawienia.set, None, 'Data wystawienia dowodu sprzeda\u017cy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}DataSprzedazy uses Python identifier DataSprzedazy
    __DataSprzedazy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSprzedazy'), 'DataSprzedazy', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113DataSprzedazy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 197, 8), )

    
    DataSprzedazy = property(__DataSprzedazy.value, __DataSprzedazy.set, None, 'Data sprzeda\u017cy, o ile jest okre\u015blona i r\xf3\u017cni si\u0119 od daty wystawienia dowodu sprzeda\u017cy. W przeciwnym przypadku - pole puste')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_10 uses Python identifier K_10
    __K_10 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_10'), 'K_10', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_10', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 202, 8), )

    
    K_10 = property(__K_10.value, __K_10.set, None, 'Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, zwolnione od podatku')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_11 uses Python identifier K_11
    __K_11 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_11'), 'K_11', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_11', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 207, 8), )

    
    K_11 = property(__K_11.value, __K_11.set, None, 'Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug poza terytorium kraju')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_12 uses Python identifier K_12
    __K_12 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_12'), 'K_12', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_12', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 212, 8), )

    
    K_12 = property(__K_12.value, __K_12.set, None, 'Kwota netto - w tym \u015bwiadczenie us\u0142ug, o kt\xf3rych mowa w art. 100 ust. 1 pkt 4 ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_13 uses Python identifier K_13
    __K_13 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_13'), 'K_13', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_13', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 217, 8), )

    
    K_13 = property(__K_13.value, __K_13.set, None, 'Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 0%')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_14 uses Python identifier K_14
    __K_14 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_14'), 'K_14', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_14', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 222, 8), )

    
    K_14 = property(__K_14.value, __K_14.set, None, 'Kwota netto - w tym dostawa towar\xf3w, o kt\xf3rej mowa w art. 129 ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_15 uses Python identifier K_15
    __K_15 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_15'), 'K_15', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_15', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 228, 9), )

    
    K_15 = property(__K_15.value, __K_15.set, None, 'Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 5%')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_16 uses Python identifier K_16
    __K_16 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_16'), 'K_16', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_16', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 233, 9), )

    
    K_16 = property(__K_16.value, __K_16.set, None, 'Kwota podatku nale\u017cnego - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 5%')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_17 uses Python identifier K_17
    __K_17 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_17'), 'K_17', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_17', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 240, 9), )

    
    K_17 = property(__K_17.value, __K_17.set, None, 'Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 7% albo 8%')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_18 uses Python identifier K_18
    __K_18 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_18'), 'K_18', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_18', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 245, 9), )

    
    K_18 = property(__K_18.value, __K_18.set, None, 'Kwota podatku nale\u017cnego - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 7% albo 8%')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_19 uses Python identifier K_19
    __K_19 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_19'), 'K_19', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_19', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 252, 9), )

    
    K_19 = property(__K_19.value, __K_19.set, None, 'Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 22% albo 23%')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_20 uses Python identifier K_20
    __K_20 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_20'), 'K_20', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_20', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 257, 9), )

    
    K_20 = property(__K_20.value, __K_20.set, None, 'Kwota podatku nale\u017cnego - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 22% albo 23%')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_21 uses Python identifier K_21
    __K_21 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_21'), 'K_21', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_21', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 263, 8), )

    
    K_21 = property(__K_21.value, __K_21.set, None, 'Kwota netto - Wewn\u0105trzwsp\xf3lnotowa dostawa towar\xf3w')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_22 uses Python identifier K_22
    __K_22 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_22'), 'K_22', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_22', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 268, 8), )

    
    K_22 = property(__K_22.value, __K_22.set, None, 'Kwota netto - Eksport towar\xf3w')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_23 uses Python identifier K_23
    __K_23 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_23'), 'K_23', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_23', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 274, 9), )

    
    K_23 = property(__K_23.value, __K_23.set, None, 'Kwota netto - Wewn\u0105trzwsp\xf3lnotowe nabycie towar\xf3w')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_24 uses Python identifier K_24
    __K_24 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_24'), 'K_24', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_24', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 279, 9), )

    
    K_24 = property(__K_24.value, __K_24.set, None, 'Kwota podatku nale\u017cnego - Wewn\u0105trzwsp\xf3lnotowe nabycie towar\xf3w')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_25 uses Python identifier K_25
    __K_25 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_25'), 'K_25', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_25', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 286, 9), )

    
    K_25 = property(__K_25.value, __K_25.set, None, 'Kwota netto - Import towar\xf3w podlegaj\u0105cy rozliczeniu zgodnie z art. 33a ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_26 uses Python identifier K_26
    __K_26 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_26'), 'K_26', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_26', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 291, 9), )

    
    K_26 = property(__K_26.value, __K_26.set, None, 'Kwota podatku nale\u017cnego - Import towar\xf3w podlegaj\u0105cy rozliczeniu zgodnie z art. 33a ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_27 uses Python identifier K_27
    __K_27 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_27'), 'K_27', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_27', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 298, 9), )

    
    K_27 = property(__K_27.value, __K_27.set, None, 'Kwota netto - Import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_28 uses Python identifier K_28
    __K_28 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_28'), 'K_28', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_28', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 303, 9), )

    
    K_28 = property(__K_28.value, __K_28.set, None, 'Kwota podatku nale\u017cnego - Import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_29 uses Python identifier K_29
    __K_29 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_29'), 'K_29', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_29', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 310, 9), )

    
    K_29 = property(__K_29.value, __K_29.set, None, 'Kwota netto - Import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_30 uses Python identifier K_30
    __K_30 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_30'), 'K_30', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_30', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 315, 9), )

    
    K_30 = property(__K_30.value, __K_30.set, None, 'Kwota podatku nale\u017cnego - Import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_31 uses Python identifier K_31
    __K_31 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_31'), 'K_31', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_31', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 321, 8), )

    
    K_31 = property(__K_31.value, __K_31.set, None, 'Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia dostawca)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_32 uses Python identifier K_32
    __K_32 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_32'), 'K_32', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_32', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 327, 9), )

    
    K_32 = property(__K_32.value, __K_32.set, None, 'Kwota netto - Dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_33 uses Python identifier K_33
    __K_33 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_33'), 'K_33', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_33', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 332, 9), )

    
    K_33 = property(__K_33.value, __K_33.set, None, 'Kwota podatku nale\u017cnego - Dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_34 uses Python identifier K_34
    __K_34 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_34'), 'K_34', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_34', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 339, 9), )

    
    K_34 = property(__K_34.value, __K_34.set, None, 'Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_35 uses Python identifier K_35
    __K_35 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_35'), 'K_35', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_35', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 344, 9), )

    
    K_35 = property(__K_35.value, __K_35.set, None, 'Kwota podatku nale\u017cnego - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_36 uses Python identifier K_36
    __K_36 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_36'), 'K_36', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_36', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 350, 8), )

    
    K_36 = property(__K_36.value, __K_36.set, None, 'Kwota podatku nale\u017cnego od towar\xf3w i us\u0142ug obj\u0119tych spisem z natury, o kt\xf3rym mowa w art. 14 ust. 5 ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_37 uses Python identifier K_37
    __K_37 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_37'), 'K_37', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_37', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 355, 8), )

    
    K_37 = property(__K_37.value, __K_37.set, None, 'Zwrot odliczonej lub zwr\xf3conej kwoty wydatkowanej na zakup kas rejestruj\u0105cych, o kt\xf3rym mowa w art. 111 ust. 6 ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_38 uses Python identifier K_38
    __K_38 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_38'), 'K_38', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_38', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 360, 8), )

    
    K_38 = property(__K_38.value, __K_38.set, None, 'Kwota podatku nale\u017cnego od wewn\u0105trzwsp\xf3lnotowego nabycia \u015brodk\xf3w transportu, wykazanego w elemencie K_24, podlegaj\u0105ca wp\u0142acie w terminie, o kt\xf3rym mowa w art. 103 ust. 3, w zwi\u0105zku z ust. 4 ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_39 uses Python identifier K_39
    __K_39 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_39'), 'K_39', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_2_httpjpk_mf_gov_plwzor201711131113K_39', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 365, 8), )

    
    K_39 = property(__K_39.value, __K_39.set, None, 'Kwota podatku od wewn\u0105trzwsp\xf3lnotowego nabycia paliw silnikowych, podlegaj\u0105ca wp\u0142acie w terminach,\no kt\xf3rych mowa w art. 103 ust. 5a i 5b ustawy')

    _ElementMap.update({
        __LpSprzedazy.name() : __LpSprzedazy,
        __NrKontrahenta.name() : __NrKontrahenta,
        __NazwaKontrahenta.name() : __NazwaKontrahenta,
        __AdresKontrahenta.name() : __AdresKontrahenta,
        __DowodSprzedazy.name() : __DowodSprzedazy,
        __DataWystawienia.name() : __DataWystawienia,
        __DataSprzedazy.name() : __DataSprzedazy,
        __K_10.name() : __K_10,
        __K_11.name() : __K_11,
        __K_12.name() : __K_12,
        __K_13.name() : __K_13,
        __K_14.name() : __K_14,
        __K_15.name() : __K_15,
        __K_16.name() : __K_16,
        __K_17.name() : __K_17,
        __K_18.name() : __K_18,
        __K_19.name() : __K_19,
        __K_20.name() : __K_20,
        __K_21.name() : __K_21,
        __K_22.name() : __K_22,
        __K_23.name() : __K_23,
        __K_24.name() : __K_24,
        __K_25.name() : __K_25,
        __K_26.name() : __K_26,
        __K_27.name() : __K_27,
        __K_28.name() : __K_28,
        __K_29.name() : __K_29,
        __K_30.name() : __K_30,
        __K_31.name() : __K_31,
        __K_32.name() : __K_32,
        __K_33.name() : __K_33,
        __K_34.name() : __K_34,
        __K_35.name() : __K_35,
        __K_36.name() : __K_36,
        __K_37.name() : __K_37,
        __K_38.name() : __K_38,
        __K_39.name() : __K_39
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Sumy kontrolne dla ewidencji sprzedaży VAT"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 378, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}LiczbaWierszySprzedazy uses Python identifier LiczbaWierszySprzedazy
    __LiczbaWierszySprzedazy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszySprzedazy'), 'LiczbaWierszySprzedazy', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_3_httpjpk_mf_gov_plwzor201711131113LiczbaWierszySprzedazy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 380, 8), )

    
    LiczbaWierszySprzedazy = property(__LiczbaWierszySprzedazy.value, __LiczbaWierszySprzedazy.set, None, 'Liczba wierszy ewidencji sprzeda\u017cy, w okresie kt\xf3rego dotyczy JPK')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}PodatekNalezny uses Python identifier PodatekNalezny
    __PodatekNalezny = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PodatekNalezny'), 'PodatekNalezny', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_3_httpjpk_mf_gov_plwzor201711131113PodatekNalezny', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 385, 8), )

    
    PodatekNalezny = property(__PodatekNalezny.value, __PodatekNalezny.set, None, 'Podatek nale\u017cny wg ewidencji sprzeda\u017cy w okresie, kt\xf3rego dotyczy JPK - suma kwot z element\xf3w K_16, K_18, K_20, K_24, K_26, K_28, K_30, K_33, K_35, K_36 i K_37 pomniejszona o kwot\u0119 z element\xf3w K_38 i K_39')

    _ElementMap.update({
        __LiczbaWierszySprzedazy.name() : __LiczbaWierszySprzedazy,
        __PodatekNalezny.name() : __PodatekNalezny
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Ewidencja zakupu VAT"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 399, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}LpZakupu uses Python identifier LpZakupu
    __LpZakupu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LpZakupu'), 'LpZakupu', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113LpZakupu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 401, 8), )

    
    LpZakupu = property(__LpZakupu.value, __LpZakupu.set, None, 'Lp. wiersza ewidencji zakupu VAT')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}NrDostawcy uses Python identifier NrDostawcy
    __NrDostawcy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrDostawcy'), 'NrDostawcy', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113NrDostawcy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 406, 8), )

    
    NrDostawcy = property(__NrDostawcy.value, __NrDostawcy.set, None, 'Numer, za pomoc\u0105 kt\xf3rego dostawca (kontrahent) jest zidentyfikowany na potrzeby podatku lub podatku od warto\u015bci dodanej')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}NazwaDostawcy uses Python identifier NazwaDostawcy
    __NazwaDostawcy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NazwaDostawcy'), 'NazwaDostawcy', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113NazwaDostawcy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 411, 8), )

    
    NazwaDostawcy = property(__NazwaDostawcy.value, __NazwaDostawcy.set, None, 'Imi\u0119 i nazwisko lub nazwa dostawcy (kontrahenta)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}AdresDostawcy uses Python identifier AdresDostawcy
    __AdresDostawcy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresDostawcy'), 'AdresDostawcy', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113AdresDostawcy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 416, 8), )

    
    AdresDostawcy = property(__AdresDostawcy.value, __AdresDostawcy.set, None, 'Adres dostawcy (kontrahenta)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}DowodZakupu uses Python identifier DowodZakupu
    __DowodZakupu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DowodZakupu'), 'DowodZakupu', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113DowodZakupu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 421, 8), )

    
    DowodZakupu = property(__DowodZakupu.value, __DowodZakupu.set, None, 'Numer dowodu zakupu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}DataZakupu uses Python identifier DataZakupu
    __DataZakupu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataZakupu'), 'DataZakupu', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113DataZakupu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 426, 8), )

    
    DataZakupu = property(__DataZakupu.value, __DataZakupu.set, None, 'Data wystawienia dowodu zakupu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}DataWplywu uses Python identifier DataWplywu
    __DataWplywu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWplywu'), 'DataWplywu', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113DataWplywu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 431, 8), )

    
    DataWplywu = property(__DataWplywu.value, __DataWplywu.set, None, 'Data wp\u0142ywu dowodu zakupu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_43 uses Python identifier K_43
    __K_43 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_43'), 'K_43', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113K_43', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 437, 9), )

    
    K_43 = property(__K_43.value, __K_43.set, None, 'Kwota netto - Nabycie towar\xf3w i us\u0142ug zaliczanych u podatnika do \u015brodk\xf3w trwa\u0142ych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_44 uses Python identifier K_44
    __K_44 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_44'), 'K_44', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113K_44', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 442, 9), )

    
    K_44 = property(__K_44.value, __K_44.set, None, 'Kwota podatku naliczonego - Nabycie towar\xf3w i us\u0142ug zaliczanych u podatnika do \u015brodk\xf3w trwa\u0142ych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_45 uses Python identifier K_45
    __K_45 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_45'), 'K_45', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113K_45', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 449, 9), )

    
    K_45 = property(__K_45.value, __K_45.set, None, 'Kwota netto - Nabycie towar\xf3w i us\u0142ug pozosta\u0142ych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_46 uses Python identifier K_46
    __K_46 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_46'), 'K_46', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113K_46', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 454, 9), )

    
    K_46 = property(__K_46.value, __K_46.set, None, 'Kwota podatku naliczonego - Nabycie towar\xf3w i us\u0142ug pozosta\u0142ych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_47 uses Python identifier K_47
    __K_47 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_47'), 'K_47', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113K_47', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 460, 8), )

    
    K_47 = property(__K_47.value, __K_47.set, None, 'Korekta podatku naliczonego od nabycia \u015brodk\xf3w trwa\u0142ych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_48 uses Python identifier K_48
    __K_48 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_48'), 'K_48', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113K_48', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 465, 8), )

    
    K_48 = property(__K_48.value, __K_48.set, None, 'Korekta podatku naliczonego od pozosta\u0142ych naby\u0107')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_49 uses Python identifier K_49
    __K_49 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_49'), 'K_49', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113K_49', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 470, 8), )

    
    K_49 = property(__K_49.value, __K_49.set, None, 'Korekta podatku naliczonego, o kt\xf3rej mowa w art. 89b ust. 1 ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}K_50 uses Python identifier K_50
    __K_50 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_50'), 'K_50', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_4_httpjpk_mf_gov_plwzor201711131113K_50', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 475, 8), )

    
    K_50 = property(__K_50.value, __K_50.set, None, 'Korekta podatku naliczonego, o kt\xf3rej mowa w art. 89b ust. 4 ustawy')

    _ElementMap.update({
        __LpZakupu.name() : __LpZakupu,
        __NrDostawcy.name() : __NrDostawcy,
        __NazwaDostawcy.name() : __NazwaDostawcy,
        __AdresDostawcy.name() : __AdresDostawcy,
        __DowodZakupu.name() : __DowodZakupu,
        __DataZakupu.name() : __DataZakupu,
        __DataWplywu.name() : __DataWplywu,
        __K_43.name() : __K_43,
        __K_44.name() : __K_44,
        __K_45.name() : __K_45,
        __K_46.name() : __K_46,
        __K_47.name() : __K_47,
        __K_48.name() : __K_48,
        __K_49.name() : __K_49,
        __K_50.name() : __K_50
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Sumy kontrolne dla ewidencji zakupu VAT"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 487, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}LiczbaWierszyZakupow uses Python identifier LiczbaWierszyZakupow
    __LiczbaWierszyZakupow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyZakupow'), 'LiczbaWierszyZakupow', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_5_httpjpk_mf_gov_plwzor201711131113LiczbaWierszyZakupow', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 489, 8), )

    
    LiczbaWierszyZakupow = property(__LiczbaWierszyZakupow.value, __LiczbaWierszyZakupow.set, None, 'Liczba wierszy ewidencji zakupu, w okresie kt\xf3rego dotyczy JPK')

    
    # Element {http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}PodatekNaliczony uses Python identifier PodatekNaliczony
    __PodatekNaliczony = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PodatekNaliczony'), 'PodatekNaliczony', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_5_httpjpk_mf_gov_plwzor201711131113PodatekNaliczony', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 494, 8), )

    
    PodatekNaliczony = property(__PodatekNaliczony.value, __PodatekNaliczony.set, None, 'Razem kwota podatku naliczonego do odliczenia - suma kwot z element\xf3w K_44, K_46, K_47, K_48, K_49 i K_50')

    _ElementMap.update({
        __LiczbaWierszyZakupow.name() : __LiczbaWierszyZakupow,
        __PodatekNaliczony.name() : __PodatekNaliczony
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = TKodFormularza
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 39, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is TKodFormularza
    
    # Attribute kodSystemowy uses Python identifier kodSystemowy
    __kodSystemowy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodSystemowy'), 'kodSystemowy', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_6_kodSystemowy', pyxb.binding.datatypes.string, fixed=True, unicode_default='JPK_VAT (3)', required=True)
    __kodSystemowy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 42, 6)
    __kodSystemowy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 42, 6)
    
    kodSystemowy = property(__kodSystemowy.value, __kodSystemowy.set, None, None)

    
    # Attribute wersjaSchemy uses Python identifier wersjaSchemy
    __wersjaSchemy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wersjaSchemy'), 'wersjaSchemy', '__httpjpk_mf_gov_plwzor201711131113_CTD_ANON_6_wersjaSchemy', pyxb.binding.datatypes.string, fixed=True, unicode_default='1-1', required=True)
    __wersjaSchemy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 43, 7)
    __wersjaSchemy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 43, 7)
    
    wersjaSchemy = property(__wersjaSchemy.value, __wersjaSchemy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kodSystemowy.name() : __kodSystemowy,
        __wersjaSchemy.name() : __wersjaSchemy
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


JPK = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JPK'), CTD_ANON, documentation='Jednolity plik kontrolny dla ewidencji zakupu i sprzeda\u017cy VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 126, 1))
Namespace.addCategoryObject('elementBinding', JPK.name().localName(), JPK)



TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), CTD_ANON_6, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 38, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), STD_ANON, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 48, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), STD_ANON_3, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 55, 3), unicode_default='0'))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), TDataCzas, scope=TNaglowek, documentation='Data i czas wytworzenia JPK_VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 62, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), TData, scope=TNaglowek, documentation='Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 67, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), TData, scope=TNaglowek, documentation='Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 72, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NazwaSystemu'), STD_ANON_, scope=TNaglowek, documentation='Nazwa systemu, z kt\xf3rego pochodz\u0105 dane', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 77, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 38, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 48, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 55, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 62, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOd')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 67, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataDo')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 72, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NazwaSystemu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 77, 3))
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
TNaglowek._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), TNaglowek, scope=CTD_ANON, documentation='Nag\u0142\xf3wek JPK_VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 132, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 137, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SprzedazWiersz'), CTD_ANON_2, scope=CTD_ANON, documentation='Ewidencja sprzeda\u017cy oraz naby\u0107 towar\xf3w i us\u0142ug dla kt\xf3rych podmiot obowi\u0105zany jest naliczy\u0107 podatek nale\u017cny - tj. wewn\u0105trzwsp\xf3lnotowe nabycia towar\xf3w, import towar\xf3w podlegaj\u0105cych rozliczeniu zgodnie z art. 33 a ustawy, import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28 b ustawy, import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28 b ustawy, dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca), dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 161, 5)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SprzedazCtrl'), CTD_ANON_3, scope=CTD_ANON, documentation='Sumy kontrolne dla ewidencji sprzeda\u017cy VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 374, 5)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ZakupWiersz'), CTD_ANON_4, scope=CTD_ANON, documentation='Ewidencja zakupu VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 395, 5)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ZakupCtrl'), CTD_ANON_5, scope=CTD_ANON, documentation='Sumy kontrolne dla ewidencji zakupu VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 483, 5)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 160, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 394, 4))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Naglowek')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 132, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 137, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SprzedazWiersz')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 161, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SprzedazCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 374, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ZakupWiersz')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 395, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ZakupCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 483, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIP'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNrNIP, scope=CTD_ANON_, documentation='Identyfikator podatkowy NIP', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 140, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa'), STD_ANON_2, scope=CTD_ANON_, documentation='Pe\u0142na nazwa', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 145, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Email'), TAdresEmail, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 156, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 156, 7))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIP')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 140, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PelnaNazwa')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 145, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Email')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 156, 7))
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
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LpSprzedazy'), TNaturalnyJPK, scope=CTD_ANON_2, documentation='Lp. wiersza ewidencji sprzeda\u017cy VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 167, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrKontrahenta'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNrIdentyfikacjiPodatkowej, scope=CTD_ANON_2, documentation='Numer, za pomoc\u0105 kt\xf3rego kontrahent jest zidentyfikowany na potrzeby podatku lub podatku od warto\u015bci dodanej', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 172, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NazwaKontrahenta'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Imi\u0119 i nazwisko lub nazwa kontrahenta', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 177, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresKontrahenta'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Adres kontrahenta', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 182, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DowodSprzedazy'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Numer dowodu sprzeda\u017cy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 187, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWystawienia'), TDataT, scope=CTD_ANON_2, documentation='Data wystawienia dowodu sprzeda\u017cy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 192, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSprzedazy'), TDataT, scope=CTD_ANON_2, documentation='Data sprzeda\u017cy, o ile jest okre\u015blona i r\xf3\u017cni si\u0119 od daty wystawienia dowodu sprzeda\u017cy. W przeciwnym przypadku - pole puste', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 197, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_10'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, zwolnione od podatku', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 202, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_11'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug poza terytorium kraju', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 207, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_12'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - w tym \u015bwiadczenie us\u0142ug, o kt\xf3rych mowa w art. 100 ust. 1 pkt 4 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 212, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_13'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 0%', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 217, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_14'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - w tym dostawa towar\xf3w, o kt\xf3rej mowa w art. 129 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 222, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_15'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 5%', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 228, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_16'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 5%', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 233, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_17'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 7% albo 8%', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 240, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_18'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 7% albo 8%', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 245, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_19'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 22% albo 23%', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 252, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_20'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 22% albo 23%', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 257, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_21'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Wewn\u0105trzwsp\xf3lnotowa dostawa towar\xf3w', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 263, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_22'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Eksport towar\xf3w', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 268, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_23'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Wewn\u0105trzwsp\xf3lnotowe nabycie towar\xf3w', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 274, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_24'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego - Wewn\u0105trzwsp\xf3lnotowe nabycie towar\xf3w', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 279, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_25'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Import towar\xf3w podlegaj\u0105cy rozliczeniu zgodnie z art. 33a ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 286, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_26'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego - Import towar\xf3w podlegaj\u0105cy rozliczeniu zgodnie z art. 33a ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 291, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_27'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 298, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_28'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego - Import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 303, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_29'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 310, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_30'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego - Import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 315, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_31'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia dostawca)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 321, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_32'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 327, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_33'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego - Dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 332, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_34'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota netto - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 339, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_35'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 344, 9)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_36'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego od towar\xf3w i us\u0142ug obj\u0119tych spisem z natury, o kt\xf3rym mowa w art. 14 ust. 5 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 350, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_37'), TKwotowy, scope=CTD_ANON_2, documentation='Zwrot odliczonej lub zwr\xf3conej kwoty wydatkowanej na zakup kas rejestruj\u0105cych, o kt\xf3rym mowa w art. 111 ust. 6 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 355, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_38'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego od wewn\u0105trzwsp\xf3lnotowego nabycia \u015brodk\xf3w transportu, wykazanego w elemencie K_24, podlegaj\u0105ca wp\u0142acie w terminie, o kt\xf3rym mowa w art. 103 ust. 3, w zwi\u0105zku z ust. 4 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 360, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_39'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku od wewn\u0105trzwsp\xf3lnotowego nabycia paliw silnikowych, podlegaj\u0105ca wp\u0142acie w terminach,\no kt\xf3rych mowa w art. 103 ust. 5a i 5b ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 365, 8)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 197, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 202, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 207, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 212, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 217, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 222, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 227, 8))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 239, 8))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 251, 8))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 263, 8))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 268, 8))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 273, 8))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 285, 8))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 297, 8))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 309, 8))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 321, 8))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 326, 8))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 338, 8))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 350, 8))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 355, 8))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 360, 8))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 365, 8))
    counters.add(cc_21)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LpSprzedazy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 167, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrKontrahenta')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 172, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NazwaKontrahenta')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 177, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresKontrahenta')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 182, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DowodSprzedazy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 187, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWystawienia')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 192, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSprzedazy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 197, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_10')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 202, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_11')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 207, 8))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_12')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 212, 8))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_13')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 217, 8))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_14')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 222, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_15')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 228, 9))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_16')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 233, 9))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_17')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 240, 9))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_18')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 245, 9))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_19')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 252, 9))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_20')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 257, 9))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_21')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 263, 8))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_22')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 268, 8))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_23')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 274, 9))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_24')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 279, 9))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_25')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 286, 9))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_26')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 291, 9))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_27')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 298, 9))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_28')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 303, 9))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_29')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 310, 9))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_30')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 315, 9))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_31')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 321, 8))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_32')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 327, 9))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_33')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 332, 9))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_34')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 339, 9))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_35')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 344, 9))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_36')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 350, 8))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_37')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 355, 8))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_38')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 360, 8))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_39')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 365, 8))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    transitions.append(fac.Transition(st_34, [
         ]))
    transitions.append(fac.Transition(st_35, [
         ]))
    transitions.append(fac.Transition(st_36, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
         ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
         ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
         ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
         ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
         ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
         ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, True) ]))
    st_36._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszySprzedazy'), TNaturalnyJPK, scope=CTD_ANON_3, documentation='Liczba wierszy ewidencji sprzeda\u017cy, w okresie kt\xf3rego dotyczy JPK', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 380, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PodatekNalezny'), TKwotowy, scope=CTD_ANON_3, documentation='Podatek nale\u017cny wg ewidencji sprzeda\u017cy w okresie, kt\xf3rego dotyczy JPK - suma kwot z element\xf3w K_16, K_18, K_20, K_24, K_26, K_28, K_30, K_33, K_35, K_36 i K_37 pomniejszona o kwot\u0119 z element\xf3w K_38 i K_39', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 385, 8)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszySprzedazy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 380, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PodatekNalezny')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 385, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LpZakupu'), TNaturalnyJPK, scope=CTD_ANON_4, documentation='Lp. wiersza ewidencji zakupu VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 401, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrDostawcy'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNrIdentyfikacjiPodatkowej, scope=CTD_ANON_4, documentation='Numer, za pomoc\u0105 kt\xf3rego dostawca (kontrahent) jest zidentyfikowany na potrzeby podatku lub podatku od warto\u015bci dodanej', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 406, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NazwaDostawcy'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Imi\u0119 i nazwisko lub nazwa dostawcy (kontrahenta)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 411, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresDostawcy'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Adres dostawcy (kontrahenta)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 416, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DowodZakupu'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Numer dowodu zakupu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 421, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataZakupu'), TDataT, scope=CTD_ANON_4, documentation='Data wystawienia dowodu zakupu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 426, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWplywu'), TDataT, scope=CTD_ANON_4, documentation='Data wp\u0142ywu dowodu zakupu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 431, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_43'), TKwotowy, scope=CTD_ANON_4, documentation='Kwota netto - Nabycie towar\xf3w i us\u0142ug zaliczanych u podatnika do \u015brodk\xf3w trwa\u0142ych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 437, 9)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_44'), TKwotowy, scope=CTD_ANON_4, documentation='Kwota podatku naliczonego - Nabycie towar\xf3w i us\u0142ug zaliczanych u podatnika do \u015brodk\xf3w trwa\u0142ych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 442, 9)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_45'), TKwotowy, scope=CTD_ANON_4, documentation='Kwota netto - Nabycie towar\xf3w i us\u0142ug pozosta\u0142ych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 449, 9)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_46'), TKwotowy, scope=CTD_ANON_4, documentation='Kwota podatku naliczonego - Nabycie towar\xf3w i us\u0142ug pozosta\u0142ych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 454, 9)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_47'), TKwotowy, scope=CTD_ANON_4, documentation='Korekta podatku naliczonego od nabycia \u015brodk\xf3w trwa\u0142ych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 460, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_48'), TKwotowy, scope=CTD_ANON_4, documentation='Korekta podatku naliczonego od pozosta\u0142ych naby\u0107', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 465, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_49'), TKwotowy, scope=CTD_ANON_4, documentation='Korekta podatku naliczonego, o kt\xf3rej mowa w art. 89b ust. 1 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 470, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_50'), TKwotowy, scope=CTD_ANON_4, documentation='Korekta podatku naliczonego, o kt\xf3rej mowa w art. 89b ust. 4 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 475, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 431, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 436, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 448, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 460, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 465, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 470, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 475, 8))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LpZakupu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 401, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrDostawcy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 406, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NazwaDostawcy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 411, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresDostawcy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 416, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DowodZakupu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 421, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataZakupu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 426, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWplywu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 431, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_43')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 437, 9))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_44')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 442, 9))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_45')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 449, 9))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_46')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 454, 9))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_47')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 460, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_48')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 465, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_49')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 470, 8))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_50')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 475, 8))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyZakupow'), TNaturalnyJPK, scope=CTD_ANON_5, documentation='Liczba wierszy ewidencji zakupu, w okresie kt\xf3rego dotyczy JPK', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 489, 8)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PodatekNaliczony'), TKwotowy, scope=CTD_ANON_5, documentation='Razem kwota podatku naliczonego do odliczenia - suma kwot z element\xf3w K_44, K_46, K_47, K_48, K_49 i K_50', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 494, 8)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyZakupow')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 489, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PodatekNaliczony')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd', 494, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()

