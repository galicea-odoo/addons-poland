# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/wb/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:2b35b821580fbb35d0876802756abe9a1492c527
# Generated 2018-03-08 13:30:04.720976 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://jpk.mf.gov.pl/wzor/2016/03/09/03092/

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
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://jpk.mf.gov.pl/wzor/2016/03/09/03092/', create_if_missing=True)
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 21, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}TKwotowy
class TKwotowy (pyxb.binding.datatypes.decimal):

    """Wartość numeryczna 18 znaków max, w tym 2 znaki po przecinku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwotowy')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 51, 1)
    _Documentation = 'Warto\u015b\u0107 numeryczna 18 znak\xf3w max, w tym 2 znaki po przecinku'
TKwotowy._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TKwotowy._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
TKwotowy._InitializeFacetMap(TKwotowy._CF_fractionDigits,
   TKwotowy._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TKwotowy', TKwotowy)
_module_typeBindings.TKwotowy = TKwotowy

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}TZnakowyJPK
class TZnakowyJPK (pyxb.binding.datatypes.token):

    """Typ znakowy ograniczony do 256 znaków"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TZnakowyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 68, 1)
    _Documentation = 'Typ znakowy ograniczony do 256 znak\xf3w'
TZnakowyJPK._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TZnakowyJPK._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
TZnakowyJPK._InitializeFacetMap(TZnakowyJPK._CF_minLength,
   TZnakowyJPK._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TZnakowyJPK', TZnakowyJPK)
_module_typeBindings.TZnakowyJPK = TZnakowyJPK

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}TKodFormularza
class TKodFormularza (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Symbol wzoru formularza"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodFormularza')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 77, 1)
    _Documentation = 'Symbol wzoru formularza'
TKodFormularza._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodFormularza, enum_prefix=None)
TKodFormularza.JPK_WB = TKodFormularza._CF_enumeration.addEnumeration(unicode_value='JPK_WB', tag='JPK_WB')
TKodFormularza._InitializeFacetMap(TKodFormularza._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodFormularza', TKodFormularza)
_module_typeBindings.TKodFormularza = TKodFormularza

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}TCelZlozenia
class TCelZlozenia (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Określenie celu złożenia JPK"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCelZlozenia')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 85, 1)
    _Documentation = 'Okre\u015blenie celu z\u0142o\u017cenia JPK'
TCelZlozenia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TCelZlozenia, enum_prefix=None)
TCelZlozenia._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
TCelZlozenia._InitializeFacetMap(TCelZlozenia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TCelZlozenia', TCelZlozenia)
_module_typeBindings.TCelZlozenia = TCelZlozenia

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 128, 5)
    _Documentation = None
STD_ANON_._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_._CF_pattern.addPattern(pattern='[A-Z]{2}[0-9]{2}[0-9A-Z]{10,30}')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_pattern)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}TNaturalnyJPK
class TNaturalnyJPK (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny):

    """Liczby naturalne większe od zera"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaturalnyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 60, 1)
    _Documentation = 'Liczby naturalne wi\u0119ksze od zera'
TNaturalnyJPK._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny, value=pyxb.binding.datatypes.integer(0))
TNaturalnyJPK._InitializeFacetMap(TNaturalnyJPK._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'TNaturalnyJPK', TNaturalnyJPK)
_module_typeBindings.TNaturalnyJPK = TNaturalnyJPK

# Complex type {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}TNaglowek with content type ELEMENT_ONLY
class TNaglowek (pyxb.binding.basis.complexTypeDefinition):
    """Nagłówek JPK_WB"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaglowek')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 5, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}KodFormularza uses Python identifier KodFormularza
    __KodFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), 'KodFormularza', '__httpjpk_mf_gov_plwzor2016030903092_TNaglowek_httpjpk_mf_gov_plwzor2016030903092KodFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 10, 3), )

    
    KodFormularza = property(__KodFormularza.value, __KodFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}WariantFormularza uses Python identifier WariantFormularza
    __WariantFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), 'WariantFormularza', '__httpjpk_mf_gov_plwzor2016030903092_TNaglowek_httpjpk_mf_gov_plwzor2016030903092WariantFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 20, 3), )

    
    WariantFormularza = property(__WariantFormularza.value, __WariantFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}CelZlozenia uses Python identifier CelZlozenia
    __CelZlozenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), 'CelZlozenia', '__httpjpk_mf_gov_plwzor2016030903092_TNaglowek_httpjpk_mf_gov_plwzor2016030903092CelZlozenia', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 27, 3), )

    
    CelZlozenia = property(__CelZlozenia.value, __CelZlozenia.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}DataWytworzeniaJPK uses Python identifier DataWytworzeniaJPK
    __DataWytworzeniaJPK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), 'DataWytworzeniaJPK', '__httpjpk_mf_gov_plwzor2016030903092_TNaglowek_httpjpk_mf_gov_plwzor2016030903092DataWytworzeniaJPK', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 28, 3), )

    
    DataWytworzeniaJPK = property(__DataWytworzeniaJPK.value, __DataWytworzeniaJPK.set, None, 'Data i czas wytworzenia JPK_WB')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}DataOd uses Python identifier DataOd
    __DataOd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), 'DataOd', '__httpjpk_mf_gov_plwzor2016030903092_TNaglowek_httpjpk_mf_gov_plwzor2016030903092DataOd', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 33, 3), )

    
    DataOd = property(__DataOd.value, __DataOd.set, None, 'Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_WB')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}DataDo uses Python identifier DataDo
    __DataDo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), 'DataDo', '__httpjpk_mf_gov_plwzor2016030903092_TNaglowek_httpjpk_mf_gov_plwzor2016030903092DataDo', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 38, 3), )

    
    DataDo = property(__DataDo.value, __DataDo.set, None, 'Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_WB')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}DomyslnyKodWaluty uses Python identifier DomyslnyKodWaluty
    __DomyslnyKodWaluty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), 'DomyslnyKodWaluty', '__httpjpk_mf_gov_plwzor2016030903092_TNaglowek_httpjpk_mf_gov_plwzor2016030903092DomyslnyKodWaluty', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 43, 3), )

    
    DomyslnyKodWaluty = property(__DomyslnyKodWaluty.value, __DomyslnyKodWaluty.set, None, 'Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_WB')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}KodUrzedu uses Python identifier KodUrzedu
    __KodUrzedu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), 'KodUrzedu', '__httpjpk_mf_gov_plwzor2016030903092_TNaglowek_httpjpk_mf_gov_plwzor2016030903092KodUrzedu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 48, 3), )

    
    KodUrzedu = property(__KodUrzedu.value, __KodUrzedu.set, None, None)

    _ElementMap.update({
        __KodFormularza.name() : __KodFormularza,
        __WariantFormularza.name() : __WariantFormularza,
        __CelZlozenia.name() : __CelZlozenia,
        __DataWytworzeniaJPK.name() : __DataWytworzeniaJPK,
        __DataOd.name() : __DataOd,
        __DataDo.name() : __DataDo,
        __DomyslnyKodWaluty.name() : __DomyslnyKodWaluty,
        __KodUrzedu.name() : __KodUrzedu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TNaglowek = TNaglowek
Namespace.addCategoryObject('typeBinding', 'TNaglowek', TNaglowek)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Jednolity plik kontrolny dla wyciągu bankowego"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 101, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}Naglowek uses Python identifier Naglowek
    __Naglowek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), 'Naglowek', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_httpjpk_mf_gov_plwzor2016030903092Naglowek', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 103, 4), )

    
    Naglowek = property(__Naglowek.value, __Naglowek.set, None, 'Nag\u0142\xf3wek JPK_WB')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}Podmiot1 uses Python identifier Podmiot1
    __Podmiot1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), 'Podmiot1', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_httpjpk_mf_gov_plwzor2016030903092Podmiot1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 108, 4), )

    
    Podmiot1 = property(__Podmiot1.value, __Podmiot1.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}NumerRachunku uses Python identifier NumerRachunku
    __NumerRachunku = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumerRachunku'), 'NumerRachunku', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_httpjpk_mf_gov_plwzor2016030903092NumerRachunku', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 124, 4), )

    
    NumerRachunku = property(__NumerRachunku.value, __NumerRachunku.set, None, 'Numer IBAN rachunku, kt\xf3rego dotyczy wyci\u0105g')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}Salda uses Python identifier Salda
    __Salda = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Salda'), 'Salda', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_httpjpk_mf_gov_plwzor2016030903092Salda', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 134, 4), )

    
    Salda = property(__Salda.value, __Salda.set, None, 'Salda wyci\u0105gu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}WyciagWiersz uses Python identifier WyciagWiersz
    __WyciagWiersz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WyciagWiersz'), 'WyciagWiersz', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_httpjpk_mf_gov_plwzor2016030903092WyciagWiersz', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 153, 4), )

    
    WyciagWiersz = property(__WyciagWiersz.value, __WyciagWiersz.set, None, 'Szczeg\xf3\u0142owe wiersze (zapisy) wyci\u0105gu bankowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}WyciagCtrl uses Python identifier WyciagCtrl
    __WyciagCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WyciagCtrl'), 'WyciagCtrl', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_httpjpk_mf_gov_plwzor2016030903092WyciagCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 193, 4), )

    
    WyciagCtrl = property(__WyciagCtrl.value, __WyciagCtrl.set, None, 'Sumy kontrolne dla wyci\u0105gu bankowego')

    _ElementMap.update({
        __Naglowek.name() : __Naglowek,
        __Podmiot1.name() : __Podmiot1,
        __NumerRachunku.name() : __NumerRachunku,
        __Salda.name() : __Salda,
        __WyciagWiersz.name() : __WyciagWiersz,
        __WyciagCtrl.name() : __WyciagCtrl
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
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 109, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}IdentyfikatorPodmiotu uses Python identifier IdentyfikatorPodmiotu
    __IdentyfikatorPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), 'IdentyfikatorPodmiotu', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON__httpjpk_mf_gov_plwzor2016030903092IdentyfikatorPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 111, 7), )

    
    IdentyfikatorPodmiotu = property(__IdentyfikatorPodmiotu.value, __IdentyfikatorPodmiotu.set, None, 'Dane identyfikuj\u0105ce podmiot')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}AdresPodmiotu uses Python identifier AdresPodmiotu
    __AdresPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), 'AdresPodmiotu', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON__httpjpk_mf_gov_plwzor2016030903092AdresPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 116, 7), )

    
    AdresPodmiotu = property(__AdresPodmiotu.value, __AdresPodmiotu.set, None, 'Adres podmiotu')

    _ElementMap.update({
        __IdentyfikatorPodmiotu.name() : __IdentyfikatorPodmiotu,
        __AdresPodmiotu.name() : __AdresPodmiotu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Salda wyciągu"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 138, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}SaldoPoczatkowe uses Python identifier SaldoPoczatkowe
    __SaldoPoczatkowe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SaldoPoczatkowe'), 'SaldoPoczatkowe', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903092SaldoPoczatkowe', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 140, 7), )

    
    SaldoPoczatkowe = property(__SaldoPoczatkowe.value, __SaldoPoczatkowe.set, None, 'Saldo pocz\u0105tkowe wyci\u0105gu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}SaldoKoncowe uses Python identifier SaldoKoncowe
    __SaldoKoncowe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SaldoKoncowe'), 'SaldoKoncowe', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903092SaldoKoncowe', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 145, 7), )

    
    SaldoKoncowe = property(__SaldoKoncowe.value, __SaldoKoncowe.set, None, 'Saldo ko\u0144cowe wyci\u0105gu')

    _ElementMap.update({
        __SaldoPoczatkowe.name() : __SaldoPoczatkowe,
        __SaldoKoncowe.name() : __SaldoKoncowe
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Szczegółowe wiersze (zapisy) wyciągu bankowego"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 157, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}NumerWiersza uses Python identifier NumerWiersza
    __NumerWiersza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumerWiersza'), 'NumerWiersza', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903092NumerWiersza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 159, 7), )

    
    NumerWiersza = property(__NumerWiersza.value, __NumerWiersza.set, None, 'Kolejny numer wiersza (zapisu) wyci\u0105gu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}DataOperacji uses Python identifier DataOperacji
    __DataOperacji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataOperacji'), 'DataOperacji', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903092DataOperacji', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 164, 7), )

    
    DataOperacji = property(__DataOperacji.value, __DataOperacji.set, None, 'Data operacji')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}NazwaPodmiotu uses Python identifier NazwaPodmiotu
    __NazwaPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NazwaPodmiotu'), 'NazwaPodmiotu', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903092NazwaPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 169, 7), )

    
    NazwaPodmiotu = property(__NazwaPodmiotu.value, __NazwaPodmiotu.set, None, 'Nazwa podmiotu b\u0119d\u0105cego stron\u0105 operacji')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}OpisOperacji uses Python identifier OpisOperacji
    __OpisOperacji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpisOperacji'), 'OpisOperacji', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903092OpisOperacji', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 174, 7), )

    
    OpisOperacji = property(__OpisOperacji.value, __OpisOperacji.set, None, 'Opis operacji/transakcji')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}KwotaOperacji uses Python identifier KwotaOperacji
    __KwotaOperacji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KwotaOperacji'), 'KwotaOperacji', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903092KwotaOperacji', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 179, 7), )

    
    KwotaOperacji = property(__KwotaOperacji.value, __KwotaOperacji.set, None, 'Kwota operacji')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}SaldoOperacji uses Python identifier SaldoOperacji
    __SaldoOperacji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SaldoOperacji'), 'SaldoOperacji', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903092SaldoOperacji', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 184, 7), )

    
    SaldoOperacji = property(__SaldoOperacji.value, __SaldoOperacji.set, None, 'Saldo operacji')

    
    # Attribute typ uses Python identifier typ
    __typ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typ'), 'typ', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_3_typ', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='G', required=True)
    __typ._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 190, 6)
    __typ._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 190, 6)
    
    typ = property(__typ.value, __typ.set, None, None)

    _ElementMap.update({
        __NumerWiersza.name() : __NumerWiersza,
        __DataOperacji.name() : __DataOperacji,
        __NazwaPodmiotu.name() : __NazwaPodmiotu,
        __OpisOperacji.name() : __OpisOperacji,
        __KwotaOperacji.name() : __KwotaOperacji,
        __SaldoOperacji.name() : __SaldoOperacji
    })
    _AttributeMap.update({
        __typ.name() : __typ
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Sumy kontrolne dla wyciągu bankowego"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 197, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}LiczbaWierszy uses Python identifier LiczbaWierszy
    __LiczbaWierszy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszy'), 'LiczbaWierszy', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903092LiczbaWierszy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 199, 7), )

    
    LiczbaWierszy = property(__LiczbaWierszy.value, __LiczbaWierszy.set, None, 'Liczba wierszy wyci\u0105gu bankowego, w okresie kt\xf3rego dotyczy wyci\u0105g')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}SumaObciazen uses Python identifier SumaObciazen
    __SumaObciazen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaObciazen'), 'SumaObciazen', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903092SumaObciazen', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 204, 7), )

    
    SumaObciazen = property(__SumaObciazen.value, __SumaObciazen.set, None, 'Suma kwot obci\u0105\u017ce\u0144 rachunku w okresie, kt\xf3rego dotyczy wyci\u0105g')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03092/}SumaUznan uses Python identifier SumaUznan
    __SumaUznan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaUznan'), 'SumaUznan', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903092SumaUznan', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 209, 7), )

    
    SumaUznan = property(__SumaUznan.value, __SumaUznan.set, None, 'Suma kwot uzna\u0144 rachunku w okresie, kt\xf3rego dotyczy wyci\u0105g')

    _ElementMap.update({
        __LiczbaWierszy.name() : __LiczbaWierszy,
        __SumaObciazen.name() : __SumaObciazen,
        __SumaUznan.name() : __SumaUznan
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = TKodFormularza
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is TKodFormularza
    
    # Attribute kodSystemowy uses Python identifier kodSystemowy
    __kodSystemowy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodSystemowy'), 'kodSystemowy', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_5_kodSystemowy', pyxb.binding.datatypes.string, fixed=True, unicode_default='JPK_WB (1)', required=True)
    __kodSystemowy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 14, 7)
    __kodSystemowy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 14, 7)
    
    kodSystemowy = property(__kodSystemowy.value, __kodSystemowy.set, None, None)

    
    # Attribute wersjaSchemy uses Python identifier wersjaSchemy
    __wersjaSchemy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wersjaSchemy'), 'wersjaSchemy', '__httpjpk_mf_gov_plwzor2016030903092_CTD_ANON_5_wersjaSchemy', pyxb.binding.datatypes.string, fixed=True, unicode_default='1-0', required=True)
    __wersjaSchemy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 15, 7)
    __wersjaSchemy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 15, 7)
    
    wersjaSchemy = property(__wersjaSchemy.value, __wersjaSchemy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kodSystemowy.name() : __kodSystemowy,
        __wersjaSchemy.name() : __wersjaSchemy
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


JPK = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JPK'), CTD_ANON, documentation='Jednolity plik kontrolny dla wyci\u0105gu bankowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 97, 1))
Namespace.addCategoryObject('elementBinding', JPK.name().localName(), JPK)



TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), CTD_ANON_5, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 10, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), STD_ANON, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 20, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), TCelZlozenia, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 27, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TDataCzas, scope=TNaglowek, documentation='Data i czas wytworzenia JPK_WB', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 28, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_WB', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 33, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_WB', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 38, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings.currCode_Type, scope=TNaglowek, documentation='Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_WB', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 43, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKodUS, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 48, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 10, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 20, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 27, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 28, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOd')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 33, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataDo')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 38, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 43, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 48, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TNaglowek._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), TNaglowek, scope=CTD_ANON, documentation='Nag\u0142\xf3wek JPK_WB', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 103, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 108, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumerRachunku'), STD_ANON_, scope=CTD_ANON, documentation='Numer IBAN rachunku, kt\xf3rego dotyczy wyci\u0105g', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 124, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Salda'), CTD_ANON_2, scope=CTD_ANON, documentation='Salda wyci\u0105gu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 134, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WyciagWiersz'), CTD_ANON_3, scope=CTD_ANON, documentation='Szczeg\xf3\u0142owe wiersze (zapisy) wyci\u0105gu bankowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 153, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WyciagCtrl'), CTD_ANON_4, scope=CTD_ANON, documentation='Sumy kontrolne dla wyci\u0105gu bankowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 193, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Naglowek')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 103, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 108, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumerRachunku')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 124, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Salda')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 134, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WyciagWiersz')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 153, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WyciagCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 193, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TIdentyfikatorOsobyNiefizycznej, scope=CTD_ANON_, documentation='Dane identyfikuj\u0105ce podmiot', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 111, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TAdresPolski, scope=CTD_ANON_, documentation='Adres podmiotu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 116, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 111, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 116, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SaldoPoczatkowe'), TKwotowy, scope=CTD_ANON_2, documentation='Saldo pocz\u0105tkowe wyci\u0105gu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 140, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SaldoKoncowe'), TKwotowy, scope=CTD_ANON_2, documentation='Saldo ko\u0144cowe wyci\u0105gu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 145, 7)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SaldoPoczatkowe')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 140, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SaldoKoncowe')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 145, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumerWiersza'), TNaturalnyJPK, scope=CTD_ANON_3, documentation='Kolejny numer wiersza (zapisu) wyci\u0105gu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 159, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataOperacji'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_3, documentation='Data operacji', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 164, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NazwaPodmiotu'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Nazwa podmiotu b\u0119d\u0105cego stron\u0105 operacji', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 169, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpisOperacji'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Opis operacji/transakcji', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 174, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KwotaOperacji'), TKwotowy, scope=CTD_ANON_3, documentation='Kwota operacji', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 179, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SaldoOperacji'), TKwotowy, scope=CTD_ANON_3, documentation='Saldo operacji', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 184, 7)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumerWiersza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 159, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOperacji')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 164, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NazwaPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 169, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpisOperacji')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 174, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KwotaOperacji')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 179, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SaldoOperacji')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 184, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszy'), TNaturalnyJPK, scope=CTD_ANON_4, documentation='Liczba wierszy wyci\u0105gu bankowego, w okresie kt\xf3rego dotyczy wyci\u0105g', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 199, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaObciazen'), TKwotowy, scope=CTD_ANON_4, documentation='Suma kwot obci\u0105\u017ce\u0144 rachunku w okresie, kt\xf3rego dotyczy wyci\u0105g', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 204, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaUznan'), TKwotowy, scope=CTD_ANON_4, documentation='Suma kwot uzna\u0144 rachunku w okresie, kt\xf3rego dotyczy wyci\u0105g', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 209, 7)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 199, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaObciazen')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 204, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaUznan')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd', 209, 7))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()

