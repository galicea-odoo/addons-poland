# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/fa/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:f6dc490aae685cb16052f6c98bdffbe7d3803cde
# Generated 2018-03-08 13:30:04.721724 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://jpk.mf.gov.pl/wzor/2016/03/09/03095/

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
Namespace = pyxb.namespace.NamespaceForURI('http://jpk.mf.gov.pl/wzor/2016/03/09/03095/', create_if_missing=True)
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


# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TKodFormularza
class TKodFormularza (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Symbol wzoru formularza"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodFormularza')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 5, 1)
    _Documentation = 'Symbol wzoru formularza'
TKodFormularza._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodFormularza, enum_prefix=None)
TKodFormularza.JPK_FA = TKodFormularza._CF_enumeration.addEnumeration(unicode_value='JPK_FA', tag='JPK_FA')
TKodFormularza._InitializeFacetMap(TKodFormularza._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodFormularza', TKodFormularza)
_module_typeBindings.TKodFormularza = TKodFormularza

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TCelZlozenia
class TCelZlozenia (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Określenie celu złożenia JPK"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCelZlozenia')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 13, 1)
    _Documentation = 'Okre\u015blenie celu z\u0142o\u017cenia JPK'
TCelZlozenia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TCelZlozenia, enum_prefix=None)
TCelZlozenia._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
TCelZlozenia._InitializeFacetMap(TCelZlozenia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TCelZlozenia', TCelZlozenia)
_module_typeBindings.TCelZlozenia = TCelZlozenia

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 41, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TKwotowy
class TKwotowy (pyxb.binding.datatypes.decimal):

    """Wartość numeryczna 18 znaków max, w tym 2 znaki po przecinku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwotowy')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 71, 1)
    _Documentation = 'Warto\u015b\u0107 numeryczna 18 znak\xf3w max, w tym 2 znaki po przecinku'
TKwotowy._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TKwotowy._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
TKwotowy._InitializeFacetMap(TKwotowy._CF_fractionDigits,
   TKwotowy._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TKwotowy', TKwotowy)
_module_typeBindings.TKwotowy = TKwotowy

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TZnakowyJPK
class TZnakowyJPK (pyxb.binding.datatypes.token):

    """Typ znakowy ograniczony do 256 znaków"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TZnakowyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 88, 1)
    _Documentation = 'Typ znakowy ograniczony do 256 znak\xf3w'
TZnakowyJPK._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TZnakowyJPK._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
TZnakowyJPK._InitializeFacetMap(TZnakowyJPK._CF_minLength,
   TZnakowyJPK._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TZnakowyJPK', TZnakowyJPK)
_module_typeBindings.TZnakowyJPK = TZnakowyJPK

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TIlosciJPK
class TIlosciJPK (pyxb.binding.datatypes.decimal):

    """Wykorzystywany do określenia ilości. Wartość numeryczna 22 znaki max, w tym 6 po przecinku."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIlosciJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 97, 1)
    _Documentation = 'Wykorzystywany do okre\u015blenia ilo\u015bci. Warto\u015b\u0107 numeryczna 22 znaki max, w tym 6 po przecinku.'
TIlosciJPK._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(6))
TIlosciJPK._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(22))
TIlosciJPK._InitializeFacetMap(TIlosciJPK._CF_fractionDigits,
   TIlosciJPK._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TIlosciJPK', TIlosciJPK)
_module_typeBindings.TIlosciJPK = TIlosciJPK

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaturalnyJPK
class TNaturalnyJPK (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny):

    """Liczby naturalne większe od zera"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaturalnyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 80, 1)
    _Documentation = 'Liczby naturalne wi\u0119ksze od zera'
TNaturalnyJPK._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny, value=pyxb.binding.datatypes.integer(0))
TNaturalnyJPK._InitializeFacetMap(TNaturalnyJPK._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'TNaturalnyJPK', TNaturalnyJPK)
_module_typeBindings.TNaturalnyJPK = TNaturalnyJPK

# Atomic simple type: [anonymous]
class STD_ANON_ (TZnakowyJPK, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 415, 8)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.VAT = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='VAT', tag='VAT')
STD_ANON_.KOREKTA = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='KOREKTA', tag='KOREKTA')
STD_ANON_.ZAL = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='ZAL', tag='ZAL')
STD_ANON_.POZ = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='POZ', tag='POZ')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (TZnakowyJPK, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 565, 8)
    _Documentation = None
STD_ANON_2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.n23 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='23', tag='n23')
STD_ANON_2.n22 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='22', tag='n22')
STD_ANON_2.n8 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='8', tag='n8')
STD_ANON_2.n7 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
STD_ANON_2.n5 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
STD_ANON_2.n3 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
STD_ANON_2.n0 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
STD_ANON_2.zw = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='zw', tag='zw')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_maxLength,
   STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Complex type {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaglowek with content type ELEMENT_ONLY
class TNaglowek (pyxb.binding.basis.complexTypeDefinition):
    """Nagłówek JPK_FA"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaglowek')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}KodFormularza uses Python identifier KodFormularza
    __KodFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), 'KodFormularza', '__httpjpk_mf_gov_plwzor2016030903095_TNaglowek_httpjpk_mf_gov_plwzor2016030903095KodFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 30, 3), )

    
    KodFormularza = property(__KodFormularza.value, __KodFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}WariantFormularza uses Python identifier WariantFormularza
    __WariantFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), 'WariantFormularza', '__httpjpk_mf_gov_plwzor2016030903095_TNaglowek_httpjpk_mf_gov_plwzor2016030903095WariantFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 40, 3), )

    
    WariantFormularza = property(__WariantFormularza.value, __WariantFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}CelZlozenia uses Python identifier CelZlozenia
    __CelZlozenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), 'CelZlozenia', '__httpjpk_mf_gov_plwzor2016030903095_TNaglowek_httpjpk_mf_gov_plwzor2016030903095CelZlozenia', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 47, 3), )

    
    CelZlozenia = property(__CelZlozenia.value, __CelZlozenia.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}DataWytworzeniaJPK uses Python identifier DataWytworzeniaJPK
    __DataWytworzeniaJPK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), 'DataWytworzeniaJPK', '__httpjpk_mf_gov_plwzor2016030903095_TNaglowek_httpjpk_mf_gov_plwzor2016030903095DataWytworzeniaJPK', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 48, 3), )

    
    DataWytworzeniaJPK = property(__DataWytworzeniaJPK.value, __DataWytworzeniaJPK.set, None, 'Data i czas wytworzenia JPK_FA')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}DataOd uses Python identifier DataOd
    __DataOd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), 'DataOd', '__httpjpk_mf_gov_plwzor2016030903095_TNaglowek_httpjpk_mf_gov_plwzor2016030903095DataOd', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 53, 3), )

    
    DataOd = property(__DataOd.value, __DataOd.set, None, 'Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_FA')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}DataDo uses Python identifier DataDo
    __DataDo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), 'DataDo', '__httpjpk_mf_gov_plwzor2016030903095_TNaglowek_httpjpk_mf_gov_plwzor2016030903095DataDo', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 58, 3), )

    
    DataDo = property(__DataDo.value, __DataDo.set, None, 'Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_FA')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}DomyslnyKodWaluty uses Python identifier DomyslnyKodWaluty
    __DomyslnyKodWaluty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), 'DomyslnyKodWaluty', '__httpjpk_mf_gov_plwzor2016030903095_TNaglowek_httpjpk_mf_gov_plwzor2016030903095DomyslnyKodWaluty', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 63, 3), )

    
    DomyslnyKodWaluty = property(__DomyslnyKodWaluty.value, __DomyslnyKodWaluty.set, None, 'Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_FA')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}KodUrzedu uses Python identifier KodUrzedu
    __KodUrzedu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), 'KodUrzedu', '__httpjpk_mf_gov_plwzor2016030903095_TNaglowek_httpjpk_mf_gov_plwzor2016030903095KodUrzedu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 68, 3), )

    
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
    """Jednolity plik kontrolny dla faktur VAT"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 110, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}Naglowek uses Python identifier Naglowek
    __Naglowek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), 'Naglowek', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_httpjpk_mf_gov_plwzor2016030903095Naglowek', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 112, 4), )

    
    Naglowek = property(__Naglowek.value, __Naglowek.set, None, 'Nag\u0142\xf3wek JPK_FA')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}Podmiot1 uses Python identifier Podmiot1
    __Podmiot1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), 'Podmiot1', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_httpjpk_mf_gov_plwzor2016030903095Podmiot1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 122, 4), )

    
    Podmiot1 = property(__Podmiot1.value, __Podmiot1.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}Faktura uses Python identifier Faktura
    __Faktura = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Faktura'), 'Faktura', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_httpjpk_mf_gov_plwzor2016030903095Faktura', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 138, 4), )

    
    Faktura = property(__Faktura.value, __Faktura.set, None, 'Na podstawie art.106 a-q ustawy z 11 marca 2004 r. o podatku od towar\xf3w i us\u0142ug /Dz.U. z 2011 r. Nr 177, poz. 1054, z p\xf3\u017an. zm./')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}FakturaCtrl uses Python identifier FakturaCtrl
    __FakturaCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FakturaCtrl'), 'FakturaCtrl', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_httpjpk_mf_gov_plwzor2016030903095FakturaCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 457, 4), )

    
    FakturaCtrl = property(__FakturaCtrl.value, __FakturaCtrl.set, None, 'Sumy kontrolne dla faktur')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}StawkiPodatku uses Python identifier StawkiPodatku
    __StawkiPodatku = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StawkiPodatku'), 'StawkiPodatku', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_httpjpk_mf_gov_plwzor2016030903095StawkiPodatku', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 476, 4), )

    
    StawkiPodatku = property(__StawkiPodatku.value, __StawkiPodatku.set, None, 'Zestawienie stawek podatku, w okresie kt\xf3rego dotyczy JPK_FA')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}FakturaWiersz uses Python identifier FakturaWiersz
    __FakturaWiersz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FakturaWiersz'), 'FakturaWiersz', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_httpjpk_mf_gov_plwzor2016030903095FakturaWiersz', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 510, 4), )

    
    FakturaWiersz = property(__FakturaWiersz.value, __FakturaWiersz.set, None, 'Szczeg\xf3\u0142owe pozycje faktur')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}FakturaWierszCtrl uses Python identifier FakturaWierszCtrl
    __FakturaWierszCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FakturaWierszCtrl'), 'FakturaWierszCtrl', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_httpjpk_mf_gov_plwzor2016030903095FakturaWierszCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 583, 4), )

    
    FakturaWierszCtrl = property(__FakturaWierszCtrl.value, __FakturaWierszCtrl.set, None, 'Sumy kontrolne dla wierszy faktur')

    _ElementMap.update({
        __Naglowek.name() : __Naglowek,
        __Podmiot1.name() : __Podmiot1,
        __Faktura.name() : __Faktura,
        __FakturaCtrl.name() : __FakturaCtrl,
        __StawkiPodatku.name() : __StawkiPodatku,
        __FakturaWiersz.name() : __FakturaWiersz,
        __FakturaWierszCtrl.name() : __FakturaWierszCtrl
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
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 123, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}IdentyfikatorPodmiotu uses Python identifier IdentyfikatorPodmiotu
    __IdentyfikatorPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), 'IdentyfikatorPodmiotu', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON__httpjpk_mf_gov_plwzor2016030903095IdentyfikatorPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 125, 7), )

    
    IdentyfikatorPodmiotu = property(__IdentyfikatorPodmiotu.value, __IdentyfikatorPodmiotu.set, None, 'Dane identyfikuj\u0105ce podmiot')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}AdresPodmiotu uses Python identifier AdresPodmiotu
    __AdresPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), 'AdresPodmiotu', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON__httpjpk_mf_gov_plwzor2016030903095AdresPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 130, 7), )

    
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
    """Na podstawie art.106 a-q ustawy z 11 marca 2004 r. o podatku od towarów i usług /Dz.U. z 2011 r. Nr 177, poz. 1054, z późn. zm./"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 142, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_1 uses Python identifier P_1
    __P_1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_1'), 'P_1', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 144, 7), )

    
    P_1 = property(__P_1.value, __P_1.set, None, 'Data wystawienia')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_2A uses Python identifier P_2A
    __P_2A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_2A'), 'P_2A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_2A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 149, 7), )

    
    P_2A = property(__P_2A.value, __P_2A.set, None, 'Kolejny numer faktury, nadany w ramach jednej lub wi\u0119cej serii, kt\xf3ry w spos\xf3b jednoznaczny indentyfikuje faktur\u0119')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_3A uses Python identifier P_3A
    __P_3A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_3A'), 'P_3A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_3A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 154, 7), )

    
    P_3A = property(__P_3A.value, __P_3A.set, None, 'Imi\u0119 i nazwisko lub nazwa nabywcy towar\xf3w lub us\u0142ug. Pole opcjonalne dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 3 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_3B uses Python identifier P_3B
    __P_3B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_3B'), 'P_3B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_3B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 159, 7), )

    
    P_3B = property(__P_3B.value, __P_3B.set, None, 'Adres nabywcy. Pole opcjonalne dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 3 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_3C uses Python identifier P_3C
    __P_3C = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_3C'), 'P_3C', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_3C', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 164, 7), )

    
    P_3C = property(__P_3C.value, __P_3C.set, None, 'Imi\u0119 i nazwisko lub nazwa sprzedawcy towar\xf3w lub us\u0142ug')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_3D uses Python identifier P_3D
    __P_3D = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_3D'), 'P_3D', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_3D', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 169, 7), )

    
    P_3D = property(__P_3D.value, __P_3D.set, None, 'Adres sprzedawcy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_4A uses Python identifier P_4A
    __P_4A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_4A'), 'P_4A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_4A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 174, 7), )

    
    P_4A = property(__P_4A.value, __P_4A.set, None, 'Kod (prefiks) podatnika VAT UE dla przypadk\xf3w okre\u015blonych w art. 97 ust. 10 ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_4B uses Python identifier P_4B
    __P_4B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_4B'), 'P_4B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_4B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 179, 7), )

    
    P_4B = property(__P_4B.value, __P_4B.set, None, 'Numer, za pomoc\u0105 kt\xf3rego podatnik jest zidentyfikowany na potrzeby podatku, z zastrze\u017ceniem pkt 24 lit. a ustawy. Pole opcjonalne dla przypadku okre\u015blonego w art. 106e ust. 4 pkt 2 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_5A uses Python identifier P_5A
    __P_5A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_5A'), 'P_5A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_5A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 184, 7), )

    
    P_5A = property(__P_5A.value, __P_5A.set, None, 'Kod (prefiks) nabywcy - podatnika VAT UE dla przypadk\xf3w okre\u015blonych w art. 97 ust. 10 ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_5B uses Python identifier P_5B
    __P_5B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_5B'), 'P_5B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_5B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 189, 7), )

    
    P_5B = property(__P_5B.value, __P_5B.set, None, 'Numer, za pomoc\u0105 kt\xf3rego nabywca towar\xf3w lub us\u0142ug jest identyfikowany dla podatku lub podatku od warto\u015bci dodanej, pod kt\xf3rym otrzyma\u0142 on towary lub us\u0142ugi, z zastrze\u017ceniem pkt 24 lit. b ustawy. Pole opcjonalne dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 2 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_6 uses Python identifier P_6
    __P_6 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_6'), 'P_6', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_6', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 194, 7), )

    
    P_6 = property(__P_6.value, __P_6.set, None, 'Data dokonania lub zako\u0144czenia dostawy towar\xf3w lub wykonania us\u0142ugi lub data otrzymania zap\u0142aty, o kt\xf3rej mowa w art. 106b ust. 1 pkt 4, o ile taka data jest okre\u015blona i r\xf3\u017cni si\u0119 od daty wystawienia faktury')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_13_1 uses Python identifier P_13_1
    __P_13_1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_13_1'), 'P_13_1', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_13_1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 203, 8), )

    
    P_13_1 = property(__P_13_1.value, __P_13_1.set, None, 'Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 podstawow\u0105 - aktualnie 23% albo 22%.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_14_1 uses Python identifier P_14_1
    __P_14_1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_14_1'), 'P_14_1', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_14_1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 208, 8), )

    
    P_14_1 = property(__P_14_1.value, __P_14_1.set, None, 'Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 podstawow\u0105 - aktualnie 23% albo 22%.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_13_2 uses Python identifier P_13_2
    __P_13_2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_13_2'), 'P_13_2', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_13_2', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 218, 8), )

    
    P_13_2 = property(__P_13_2.value, __P_13_2.set, None, 'Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 pierwsz\u0105 - aktualnie 8 % albo 7%.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_14_2 uses Python identifier P_14_2
    __P_14_2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_14_2'), 'P_14_2', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_14_2', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 223, 8), )

    
    P_14_2 = property(__P_14_2.value, __P_14_2.set, None, 'Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 - aktualnie 8% albo 7%.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_13_3 uses Python identifier P_13_3
    __P_13_3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_13_3'), 'P_13_3', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_13_3', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 233, 8), )

    
    P_13_3 = property(__P_13_3.value, __P_13_3.set, None, 'Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 drug\u0105 - aktualnie 5%.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_14_3 uses Python identifier P_14_3
    __P_14_3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_14_3'), 'P_14_3', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_14_3', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 238, 8), )

    
    P_14_3 = property(__P_14_3.value, __P_14_3.set, None, 'Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 drug\u0105 - aktualnie 5%.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_13_4 uses Python identifier P_13_4
    __P_13_4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_13_4'), 'P_13_4', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_13_4', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 248, 8), )

    
    P_13_4 = property(__P_13_4.value, __P_13_4.set, None, 'Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 trzeci\u0105 - pole rezerwowe.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_14_4 uses Python identifier P_14_4
    __P_14_4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_14_4'), 'P_14_4', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_14_4', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 253, 8), )

    
    P_14_4 = property(__P_14_4.value, __P_14_4.set, None, 'Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 trzeci\u0105 - pole rezerwowe.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_13_5 uses Python identifier P_13_5
    __P_13_5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_13_5'), 'P_13_5', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_13_5', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 263, 8), )

    
    P_13_5 = property(__P_13_5.value, __P_13_5.set, None, 'Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 czwart\u0105 - pole rezerwowe. ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_14_5 uses Python identifier P_14_5
    __P_14_5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_14_5'), 'P_14_5', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_14_5', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 268, 8), )

    
    P_14_5 = property(__P_14_5.value, __P_14_5.set, None, 'Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 czwart\u0105 - pole rezerwowe.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_13_6 uses Python identifier P_13_6
    __P_13_6 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_13_6'), 'P_13_6', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_13_6', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 274, 7), )

    
    P_13_6 = property(__P_13_6.value, __P_13_6.set, None, 'Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 0%. Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true"), a tak\u017ce art. 106e ust. 4 pkt 3 i ust. 5 pkt 1-3 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_13_7 uses Python identifier P_13_7
    __P_13_7 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_13_7'), 'P_13_7', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_13_7', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 279, 7), )

    
    P_13_7 = property(__P_13_7.value, __P_13_7.set, None, 'Suma warto\u015bci sprzeda\u017cy zwolnionej. Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true"), a tak\u017ce art. 106e ust. 4 pkt 3 i ust. 5 pkt 1-3 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_15 uses Python identifier P_15
    __P_15 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_15'), 'P_15', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_15', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 284, 7), )

    
    P_15 = property(__P_15.value, __P_15.set, None, 'Kwota nale\u017cno\u015bci og\xf3\u0142em')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_16 uses Python identifier P_16
    __P_16 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_16'), 'P_16', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_16', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 289, 7), )

    
    P_16 = property(__P_16.value, __P_16.set, None, 'W przypadku dostawy towar\xf3w lub \u015bwiadczenia us\u0142ug, w odniesieniu do kt\xf3rych obowi\u0105zek podatkowy powstaje zgodnie z art. 19a ust. 5 pkt 1 lub art. 21 ust. 1 - wyrazy "metoda kasowa", nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_17 uses Python identifier P_17
    __P_17 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_17'), 'P_17', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_17', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 294, 7), )

    
    P_17 = property(__P_17.value, __P_17.set, None, 'W przypadku faktur, o kt\xf3rych mowa w art. 106d ust. 1 - wyraz "samofakturowanie", nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_18 uses Python identifier P_18
    __P_18 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_18'), 'P_18', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_18', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 299, 7), )

    
    P_18 = property(__P_18.value, __P_18.set, None, 'W przypadku dostawy towar\xf3w lub wykonania us\u0142ugi, dla kt\xf3rych obowi\u0105zanym do rozliczenia podatku, podatku od warto\u015bci dodanej lub podatku o podobnym charakterze jest nabywca towaru lub us\u0142ugi - wyrazy "odwrotne obci\u0105\u017cenie", nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_19 uses Python identifier P_19
    __P_19 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_19'), 'P_19', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_19', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 304, 7), )

    
    P_19 = property(__P_19.value, __P_19.set, None, 'W przypadku dostawy towar\xf3w lub \u015bwiadczenia us\u0142ug zwolnionych od podatku na podstawie art. 43 ust. 1, art. 113 ust. 1 i 9 albo przepis\xf3w wydanych na podstawie art. 82 ust. 3 nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_19A uses Python identifier P_19A
    __P_19A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_19A'), 'P_19A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_19A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 310, 8), )

    
    P_19A = property(__P_19A.value, __P_19A.set, None, 'Je\u015bli pole P_19 r\xf3wna si\u0119 "true" - nale\u017cy wskaza\u0107 przepis ustawy albo aktu wydanego na podstawie ustawy, na podstawie kt\xf3rego podatnik stosuje zwolnienie od podatku')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_19B uses Python identifier P_19B
    __P_19B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_19B'), 'P_19B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_19B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 315, 8), )

    
    P_19B = property(__P_19B.value, __P_19B.set, None, 'Je\u015bli pole P_19 r\xf3wna si\u0119 "true" - nale\u017cy wskaza\u0107 przepis dyrektywy 2006/112/WE, kt\xf3ry zwalnia od podatku tak\u0105 dostaw\u0119 towar\xf3w lub takie \u015bwiadczenie us\u0142ug')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_19C uses Python identifier P_19C
    __P_19C = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_19C'), 'P_19C', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_19C', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 320, 8), )

    
    P_19C = property(__P_19C.value, __P_19C.set, None, 'Je\u015bli pole P_19 r\xf3wna si\u0119 "true" - nale\u017cy wskaza\u0107 inn\u0105 podstaw\u0119 prawn\u0105 wskazuj\u0105c\u0105 na to, \u017ce dostawa towar\xf3w lub \u015bwiadczenie us\u0142ug korzysta ze zwolnienia\n')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_20 uses Python identifier P_20
    __P_20 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_20'), 'P_20', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_20', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 327, 7), )

    
    P_20 = property(__P_20.value, __P_20.set, None, 'W przypadku, o kt\xf3rym mowa w art. 106c ustawy nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_20A uses Python identifier P_20A
    __P_20A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_20A'), 'P_20A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_20A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 333, 8), )

    
    P_20A = property(__P_20A.value, __P_20A.set, None, 'Je\u015bli pole P_20 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 nazw\u0119 organu egzekucyjnego lub imi\u0119 i nazwisko komornika s\u0105dowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_20B uses Python identifier P_20B
    __P_20B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_20B'), 'P_20B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_20B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 338, 8), )

    
    P_20B = property(__P_20B.value, __P_20B.set, None, 'Je\u015bli pole P_20 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 adres organu egzekucyjnego lub komornika s\u0105dowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_21 uses Python identifier P_21
    __P_21 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_21'), 'P_21', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_21', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 344, 7), )

    
    P_21 = property(__P_21.value, __P_21.set, None, 'W przypadku faktur wystawianych w imieniu i na rzecz podatnika przez jego przedstawiciela podatkowego nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_21A uses Python identifier P_21A
    __P_21A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_21A'), 'P_21A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_21A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 350, 8), )

    
    P_21A = property(__P_21A.value, __P_21A.set, None, 'Je\u015bli pole P_21 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 nazw\u0119 lub imi\u0119 i nazwisko przedstawiciela podatkowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_21B uses Python identifier P_21B
    __P_21B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_21B'), 'P_21B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_21B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 355, 8), )

    
    P_21B = property(__P_21B.value, __P_21B.set, None, 'Je\u015bli pole P_21 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 adres przedstawiciela podatkowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_21C uses Python identifier P_21C
    __P_21C = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_21C'), 'P_21C', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_21C', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 360, 8), )

    
    P_21C = property(__P_21C.value, __P_21C.set, None, 'Je\u015bli pole P_21 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 numer przedstawiciela podatkowego, za pomoc\u0105 kt\xf3rego jest on zidentyfikowany na potrzeby podatku')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_22A uses Python identifier P_22A
    __P_22A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_22A'), 'P_22A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_22A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 372, 8), )

    
    P_22A = property(__P_22A.value, __P_22A.set, None, 'Data dopuszczenia nowego \u015brodka transportu do u\u017cytku')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_22B uses Python identifier P_22B
    __P_22B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_22B'), 'P_22B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_22B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 377, 8), )

    
    P_22B = property(__P_22B.value, __P_22B.set, None, 'Przebieg pojazdu - w przypadku pojazd\xf3w l\u0105dowych, o kt\xf3rych mowa w art. 2 pkt 10 lit. a ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_22C uses Python identifier P_22C
    __P_22C = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_22C'), 'P_22C', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_22C', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 382, 8), )

    
    P_22C = property(__P_22C.value, __P_22C.set, None, 'Liczba godzin roboczych u\u017cywania nowego \u015brodka transportu - w przypadku jednostek p\u0142ywaj\u0105cych, o kt\xf3rych mowa w art. 2 pkt 10 lit. b, oraz statk\xf3w powietrznych, o kt\xf3rych mowa w art. 2 pkt 10 lit. c ustawy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_23 uses Python identifier P_23
    __P_23 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_23'), 'P_23', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_23', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 388, 7), )

    
    P_23 = property(__P_23.value, __P_23.set, None, 'W przypadku faktur wystawianych przez drugiego w kolejno\u015bci podatnika, o kt\xf3rym mowa w art. 135 ust. 1 pkt 4 lit. b i c, w wewn\u0105trzwsp\xf3lnotowej transakcji tr\xf3jstronnej (procedurze uproszczonej) - dane okre\u015blone w art. 136, nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_106E_2 uses Python identifier P_106E_2
    __P_106E_2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_106E_2'), 'P_106E_2', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_106E_2', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 393, 7), )

    
    P_106E_2 = property(__P_106E_2.value, __P_106E_2.set, None, 'W przypadku \u015bwiadczenia us\u0142ug turystyki, dla kt\xf3rych podstaw\u0119 opodatkowania stanowi zgodnie z art. 119 ust. 1 kwota mar\u017cy, faktura - w zakresie danych okre\u015blonych w ust. 1 pkt 1-17 - powinna zawiera\u0107 wy\u0142\u0105cznie dane okre\u015blone w ust. 1 pkt 1-8 i 15-17, a tak\u017ce wyrazy "procedura mar\u017cy dla biur podr\xf3\u017cy", nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"\n')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_106E_3 uses Python identifier P_106E_3
    __P_106E_3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_106E_3'), 'P_106E_3', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_106E_3', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 400, 8), )

    
    P_106E_3 = property(__P_106E_3.value, __P_106E_3.set, None, 'W przypadku dostawy towar\xf3w u\u017cywanych, dzie\u0142 sztuki, przedmiot\xf3w kolekcjonerskich i antyk\xf3w, dla kt\xf3rych podstaw\u0119 opodatkowania stanowi zgodnie z art. 120 ust. 4 i 5 mar\u017ca, nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_106E_3A uses Python identifier P_106E_3A
    __P_106E_3A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_106E_3A'), 'P_106E_3A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095P_106E_3A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 405, 8), )

    
    P_106E_3A = property(__P_106E_3A.value, __P_106E_3A.set, None, 'Je\u017celi pole P_106E_3 r\xf3wna si\u0119 warto\u015bci "true", nale\u017cy poda\u0107 wyrazy: "procedura mar\u017cy - towary u\u017cywane" lub "procedura mar\u017cy - dzie\u0142a sztuki" lub "procedura mar\u017cy - przedmioty kolekcjonerskie i antyki"')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}RodzajFaktury uses Python identifier RodzajFaktury
    __RodzajFaktury = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RodzajFaktury'), 'RodzajFaktury', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095RodzajFaktury', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 411, 7), )

    
    RodzajFaktury = property(__RodzajFaktury.value, __RodzajFaktury.set, None, 'Rodzaj faktury: VAT - podstawowa; KOREKTA - koryguj\u0105ca; ZAL - faktura dokumentuj\u0105ca otrzymanie zap\u0142aty lub jej cz\u0119\u015bci przed dokonaniem czynno\u015bci (art.106b ust. 1 pkt 4 ustawy); POZ - pozosta\u0142e')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}PrzyczynaKorekty uses Python identifier PrzyczynaKorekty
    __PrzyczynaKorekty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrzyczynaKorekty'), 'PrzyczynaKorekty', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095PrzyczynaKorekty', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 425, 8), )

    
    PrzyczynaKorekty = property(__PrzyczynaKorekty.value, __PrzyczynaKorekty.set, None, 'Przyczyna korekty dla faktur koryguj\u0105cych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}NrFaKorygowanej uses Python identifier NrFaKorygowanej
    __NrFaKorygowanej = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrFaKorygowanej'), 'NrFaKorygowanej', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095NrFaKorygowanej', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 430, 8), )

    
    NrFaKorygowanej = property(__NrFaKorygowanej.value, __NrFaKorygowanej.set, None, 'Numer faktury korygowanej')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}OkresFaKorygowanej uses Python identifier OkresFaKorygowanej
    __OkresFaKorygowanej = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OkresFaKorygowanej'), 'OkresFaKorygowanej', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095OkresFaKorygowanej', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 435, 8), )

    
    OkresFaKorygowanej = property(__OkresFaKorygowanej.value, __OkresFaKorygowanej.set, None, 'Dla faktury koryguj\u0105cej - okres, do kt\xf3rego odnosi si\u0119 udzielany opust lub obni\u017cka, w przypadku gdy podatnik udziela opustu lub obni\u017cki ceny w odniesieniu do wszystkich dostaw towar\xf3w lub us\u0142ug dokonanych lub \u015bwiadczonych na rzecz jednego odbiorcy w danym okresie')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}ZALZaplata uses Python identifier ZALZaplata
    __ZALZaplata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ZALZaplata'), 'ZALZaplata', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095ZALZaplata', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 442, 8), )

    
    ZALZaplata = property(__ZALZaplata.value, __ZALZaplata.set, None, 'Dla faktury zaliczkowej - otrzymana kwota zap\u0142aty')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}ZALPodatek uses Python identifier ZALPodatek
    __ZALPodatek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ZALPodatek'), 'ZALPodatek', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903095ZALPodatek', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 447, 8), )

    
    ZALPodatek = property(__ZALPodatek.value, __ZALPodatek.set, None, 'Dla faktury zaliczkowej - kwota podatku wyliczona wed\u0142ug wzoru z art.106f ust. 1 pkt 3 ustawy')

    
    # Attribute typ uses Python identifier typ
    __typ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typ'), 'typ', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_2_typ', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='G', required=True)
    __typ._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 454, 6)
    __typ._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 454, 6)
    
    typ = property(__typ.value, __typ.set, None, None)

    _ElementMap.update({
        __P_1.name() : __P_1,
        __P_2A.name() : __P_2A,
        __P_3A.name() : __P_3A,
        __P_3B.name() : __P_3B,
        __P_3C.name() : __P_3C,
        __P_3D.name() : __P_3D,
        __P_4A.name() : __P_4A,
        __P_4B.name() : __P_4B,
        __P_5A.name() : __P_5A,
        __P_5B.name() : __P_5B,
        __P_6.name() : __P_6,
        __P_13_1.name() : __P_13_1,
        __P_14_1.name() : __P_14_1,
        __P_13_2.name() : __P_13_2,
        __P_14_2.name() : __P_14_2,
        __P_13_3.name() : __P_13_3,
        __P_14_3.name() : __P_14_3,
        __P_13_4.name() : __P_13_4,
        __P_14_4.name() : __P_14_4,
        __P_13_5.name() : __P_13_5,
        __P_14_5.name() : __P_14_5,
        __P_13_6.name() : __P_13_6,
        __P_13_7.name() : __P_13_7,
        __P_15.name() : __P_15,
        __P_16.name() : __P_16,
        __P_17.name() : __P_17,
        __P_18.name() : __P_18,
        __P_19.name() : __P_19,
        __P_19A.name() : __P_19A,
        __P_19B.name() : __P_19B,
        __P_19C.name() : __P_19C,
        __P_20.name() : __P_20,
        __P_20A.name() : __P_20A,
        __P_20B.name() : __P_20B,
        __P_21.name() : __P_21,
        __P_21A.name() : __P_21A,
        __P_21B.name() : __P_21B,
        __P_21C.name() : __P_21C,
        __P_22A.name() : __P_22A,
        __P_22B.name() : __P_22B,
        __P_22C.name() : __P_22C,
        __P_23.name() : __P_23,
        __P_106E_2.name() : __P_106E_2,
        __P_106E_3.name() : __P_106E_3,
        __P_106E_3A.name() : __P_106E_3A,
        __RodzajFaktury.name() : __RodzajFaktury,
        __PrzyczynaKorekty.name() : __PrzyczynaKorekty,
        __NrFaKorygowanej.name() : __NrFaKorygowanej,
        __OkresFaKorygowanej.name() : __OkresFaKorygowanej,
        __ZALZaplata.name() : __ZALZaplata,
        __ZALPodatek.name() : __ZALPodatek
    })
    _AttributeMap.update({
        __typ.name() : __typ
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Sumy kontrolne dla faktur"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 461, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}LiczbaFaktur uses Python identifier LiczbaFaktur
    __LiczbaFaktur = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaFaktur'), 'LiczbaFaktur', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903095LiczbaFaktur', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 463, 7), )

    
    LiczbaFaktur = property(__LiczbaFaktur.value, __LiczbaFaktur.set, None, 'Liczba faktur, w okresie kt\xf3rego dotyczy JPK_FA')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}WartoscFaktur uses Python identifier WartoscFaktur
    __WartoscFaktur = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscFaktur'), 'WartoscFaktur', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903095WartoscFaktur', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 468, 7), )

    
    WartoscFaktur = property(__WartoscFaktur.value, __WartoscFaktur.set, None, '\u0141\u0105czna warto\u015b\u0107 kwot brutto faktur w okresie, kt\xf3rego dotyczy JPK_FA')

    _ElementMap.update({
        __LiczbaFaktur.name() : __LiczbaFaktur,
        __WartoscFaktur.name() : __WartoscFaktur
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Zestawienie stawek podatku, w okresie którego dotyczy JPK_FA"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 480, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}Stawka1 uses Python identifier Stawka1
    __Stawka1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Stawka1'), 'Stawka1', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903095Stawka1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 482, 7), )

    
    Stawka1 = property(__Stawka1.value, __Stawka1.set, None, 'Warto\u015b\u0107 stawki podstawowej')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}Stawka2 uses Python identifier Stawka2
    __Stawka2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Stawka2'), 'Stawka2', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903095Stawka2', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 487, 7), )

    
    Stawka2 = property(__Stawka2.value, __Stawka2.set, None, 'Warto\u015b\u0107 stawki obni\u017conej pierwszej')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}Stawka3 uses Python identifier Stawka3
    __Stawka3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Stawka3'), 'Stawka3', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903095Stawka3', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 492, 7), )

    
    Stawka3 = property(__Stawka3.value, __Stawka3.set, None, 'Warto\u015b\u0107 stawki obni\u017conej drugiej')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}Stawka4 uses Python identifier Stawka4
    __Stawka4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Stawka4'), 'Stawka4', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903095Stawka4', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 497, 7), )

    
    Stawka4 = property(__Stawka4.value, __Stawka4.set, None, 'Warto\u015b\u0107 stawki obni\u017conej trzeciej - pole rezerwowe')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}Stawka5 uses Python identifier Stawka5
    __Stawka5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Stawka5'), 'Stawka5', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903095Stawka5', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 502, 7), )

    
    Stawka5 = property(__Stawka5.value, __Stawka5.set, None, 'Warto\u015b\u0107 stawki obni\u017conej czwartej - pole rezerwowe')

    _ElementMap.update({
        __Stawka1.name() : __Stawka1,
        __Stawka2.name() : __Stawka2,
        __Stawka3.name() : __Stawka3,
        __Stawka4.name() : __Stawka4,
        __Stawka5.name() : __Stawka5
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Szczegółowe pozycje faktur"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 514, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_2B uses Python identifier P_2B
    __P_2B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_2B'), 'P_2B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_2B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 516, 7), )

    
    P_2B = property(__P_2B.value, __P_2B.set, None, 'Kolejny numer faktury, nadany w ramach jednej lub wi\u0119cej serii, kt\xf3ry w spos\xf3b jednoznaczny indentyfikuje faktur\u0119')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_7 uses Python identifier P_7
    __P_7 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_7'), 'P_7', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_7', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 521, 7), )

    
    P_7 = property(__P_7.value, __P_7.set, None, 'Nazwa (rodzaj) towaru lub us\u0142ugi. Pole opcjonalne wy\u0142\u0105cznie dla przypadku okre\u015blonego w art 106j ust.3 pkt 2 ustawy (faktura korekta)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_8A uses Python identifier P_8A
    __P_8A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_8A'), 'P_8A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_8A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 526, 7), )

    
    P_8A = property(__P_8A.value, __P_8A.set, None, 'Miara dostarczonych towar\xf3w lub zakres wykonanych us\u0142ug. Pole opcjonalne dla przypadku okre\u015blonego w art 106e ust. 5 pkt 3 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_8B uses Python identifier P_8B
    __P_8B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_8B'), 'P_8B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_8B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 531, 7), )

    
    P_8B = property(__P_8B.value, __P_8B.set, None, 'Ilo\u015b\u0107 (liczba) dostarczonych towar\xf3w lub zakres wykonanych us\u0142ug. Pole opcjonalne dla przypadku okre\u015blonego w art 106e ust. 5 pkt 3 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_9A uses Python identifier P_9A
    __P_9A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_9A'), 'P_9A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_9A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 536, 7), )

    
    P_9A = property(__P_9A.value, __P_9A.set, None, 'Cena jednostkowa towaru lub us\u0142ugi bez kwoty podatku (cena jednostkowa netto). Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true") oraz dla przypadku okre\u015blonego w art 106e ust. 5 pkt 3 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_9B uses Python identifier P_9B
    __P_9B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_9B'), 'P_9B', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_9B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 541, 7), )

    
    P_9B = property(__P_9B.value, __P_9B.set, None, 'W przypadku zastosowania art.106e ustawy, cena wraz z kwot\u0105 podatku (cena jednostkowa brutto)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_10 uses Python identifier P_10
    __P_10 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_10'), 'P_10', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_10', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 546, 7), )

    
    P_10 = property(__P_10.value, __P_10.set, None, 'Kwoty wszelkich opust\xf3w lub obni\u017cek cen, w tym w formie rabatu z tytu\u0142u wcze\u015bniejszej zap\u0142aty, o ile nie zosta\u0142y one uwzgl\u0119dnione w cenie jednostkowej netto. Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true") oraz dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 1 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_11 uses Python identifier P_11
    __P_11 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_11'), 'P_11', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_11', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 551, 7), )

    
    P_11 = property(__P_11.value, __P_11.set, None, 'Warto\u015b\u0107 dostarczonych towar\xf3w lub wykonanych us\u0142ug, obj\u0119tych transakcj\u0105, bez kwoty podatku (warto\u015b\u0107 sprzeda\u017cy netto). Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true") oraz dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 3 ustawy.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_11A uses Python identifier P_11A
    __P_11A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_11A'), 'P_11A', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_11A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 556, 7), )

    
    P_11A = property(__P_11A.value, __P_11A.set, None, 'W przypadku zastosowania art. 106e ust.7 i 8 ustawy, warto\u015b\u0107 sprzeda\u017cy brutto')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}P_12 uses Python identifier P_12
    __P_12 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_12'), 'P_12', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903095P_12', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 561, 7), )

    
    P_12 = property(__P_12.value, __P_12.set, None, 'Stawka podatku. Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true"), a tak\u017ce art. 106e ust.4 pkt 3 i ust. 5 pkt 1-3 ustawy.')

    
    # Attribute typ uses Python identifier typ
    __typ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typ'), 'typ', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_5_typ', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='G', required=True)
    __typ._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 580, 6)
    __typ._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 580, 6)
    
    typ = property(__typ.value, __typ.set, None, None)

    _ElementMap.update({
        __P_2B.name() : __P_2B,
        __P_7.name() : __P_7,
        __P_8A.name() : __P_8A,
        __P_8B.name() : __P_8B,
        __P_9A.name() : __P_9A,
        __P_9B.name() : __P_9B,
        __P_10.name() : __P_10,
        __P_11.name() : __P_11,
        __P_11A.name() : __P_11A,
        __P_12.name() : __P_12
    })
    _AttributeMap.update({
        __typ.name() : __typ
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Sumy kontrolne dla wierszy faktur"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 587, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}LiczbaWierszyFaktur uses Python identifier LiczbaWierszyFaktur
    __LiczbaWierszyFaktur = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyFaktur'), 'LiczbaWierszyFaktur', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_6_httpjpk_mf_gov_plwzor2016030903095LiczbaWierszyFaktur', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 589, 7), )

    
    LiczbaWierszyFaktur = property(__LiczbaWierszyFaktur.value, __LiczbaWierszyFaktur.set, None, 'Liczba wierszy faktur, w okresie kt\xf3rego dotyczy JPK_FA')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}WartoscWierszyFaktur uses Python identifier WartoscWierszyFaktur
    __WartoscWierszyFaktur = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscWierszyFaktur'), 'WartoscWierszyFaktur', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_6_httpjpk_mf_gov_plwzor2016030903095WartoscWierszyFaktur', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 594, 7), )

    
    WartoscWierszyFaktur = property(__WartoscWierszyFaktur.value, __WartoscWierszyFaktur.set, None, '\u0141\u0105czna warto\u015b\u0107 kolumny P_11 tabeli FakturaWiersz w okresie, kt\xf3rego dotyczy JPK_FA')

    _ElementMap.update({
        __LiczbaWierszyFaktur.name() : __LiczbaWierszyFaktur,
        __WartoscWierszyFaktur.name() : __WartoscWierszyFaktur
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = TKodFormularza
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 31, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is TKodFormularza
    
    # Attribute kodSystemowy uses Python identifier kodSystemowy
    __kodSystemowy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodSystemowy'), 'kodSystemowy', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_7_kodSystemowy', pyxb.binding.datatypes.string, fixed=True, unicode_default='JPK_FA (1)', required=True)
    __kodSystemowy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 34, 7)
    __kodSystemowy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 34, 7)
    
    kodSystemowy = property(__kodSystemowy.value, __kodSystemowy.set, None, None)

    
    # Attribute wersjaSchemy uses Python identifier wersjaSchemy
    __wersjaSchemy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wersjaSchemy'), 'wersjaSchemy', '__httpjpk_mf_gov_plwzor2016030903095_CTD_ANON_7_wersjaSchemy', pyxb.binding.datatypes.string, fixed=True, unicode_default='1-0', required=True)
    __wersjaSchemy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 35, 7)
    __wersjaSchemy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 35, 7)
    
    wersjaSchemy = property(__wersjaSchemy.value, __wersjaSchemy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kodSystemowy.name() : __kodSystemowy,
        __wersjaSchemy.name() : __wersjaSchemy
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (TNaglowek):
    """Nagłówek JPK_FA"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 116, 5)
    _ElementMap = TNaglowek._ElementMap.copy()
    _AttributeMap = TNaglowek._AttributeMap.copy()
    # Base type is TNaglowek
    
    # Element KodFormularza ({http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}KodFormularza) inherited from {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaglowek
    
    # Element WariantFormularza ({http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}WariantFormularza) inherited from {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaglowek
    
    # Element CelZlozenia ({http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}CelZlozenia) inherited from {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaglowek
    
    # Element DataWytworzeniaJPK ({http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}DataWytworzeniaJPK) inherited from {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaglowek
    
    # Element DataOd ({http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}DataOd) inherited from {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaglowek
    
    # Element DataDo ({http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}DataDo) inherited from {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaglowek
    
    # Element DomyslnyKodWaluty ({http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}DomyslnyKodWaluty) inherited from {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaglowek
    
    # Element KodUrzedu ({http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}KodUrzedu) inherited from {http://jpk.mf.gov.pl/wzor/2016/03/09/03095/}TNaglowek
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


JPK = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JPK'), CTD_ANON, documentation='Jednolity plik kontrolny dla faktur VAT', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 106, 1))
Namespace.addCategoryObject('elementBinding', JPK.name().localName(), JPK)



TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), CTD_ANON_7, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 30, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), STD_ANON, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 40, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), TCelZlozenia, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 47, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TDataCzas, scope=TNaglowek, documentation='Data i czas wytworzenia JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 48, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 53, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 58, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings.currCode_Type, scope=TNaglowek, documentation='Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 63, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKodUS, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 68, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 47, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 48, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOd')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 53, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataDo')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 58, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 63, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 68, 3))
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




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), CTD_ANON_8, scope=CTD_ANON, documentation='Nag\u0142\xf3wek JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 112, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 122, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Faktura'), CTD_ANON_2, scope=CTD_ANON, documentation='Na podstawie art.106 a-q ustawy z 11 marca 2004 r. o podatku od towar\xf3w i us\u0142ug /Dz.U. z 2011 r. Nr 177, poz. 1054, z p\xf3\u017an. zm./', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 138, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FakturaCtrl'), CTD_ANON_3, scope=CTD_ANON, documentation='Sumy kontrolne dla faktur', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 457, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StawkiPodatku'), CTD_ANON_4, scope=CTD_ANON, documentation='Zestawienie stawek podatku, w okresie kt\xf3rego dotyczy JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 476, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FakturaWiersz'), CTD_ANON_5, scope=CTD_ANON, documentation='Szczeg\xf3\u0142owe pozycje faktur', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 510, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FakturaWierszCtrl'), CTD_ANON_6, scope=CTD_ANON, documentation='Sumy kontrolne dla wierszy faktur', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 583, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Naglowek')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 112, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 122, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Faktura')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 138, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FakturaCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 457, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StawkiPodatku')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 476, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FakturaWiersz')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 510, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FakturaWierszCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 583, 4))
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
    transitions.append(fac.Transition(st_2, [
         ]))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TIdentyfikatorOsobyNiefizycznej, scope=CTD_ANON_, documentation='Dane identyfikuj\u0105ce podmiot', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 125, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TAdresPolski, scope=CTD_ANON_, documentation='Adres podmiotu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 130, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 125, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 130, 7))
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




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_1'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_2, documentation='Data wystawienia', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 144, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_2A'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Kolejny numer faktury, nadany w ramach jednej lub wi\u0119cej serii, kt\xf3ry w spos\xf3b jednoznaczny indentyfikuje faktur\u0119', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 149, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_3A'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Imi\u0119 i nazwisko lub nazwa nabywcy towar\xf3w lub us\u0142ug. Pole opcjonalne dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 3 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 154, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_3B'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Adres nabywcy. Pole opcjonalne dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 3 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 159, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_3C'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Imi\u0119 i nazwisko lub nazwa sprzedawcy towar\xf3w lub us\u0142ug', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 164, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_3D'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Adres sprzedawcy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 169, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_4A'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings.MSCountryCode_Type, scope=CTD_ANON_2, documentation='Kod (prefiks) podatnika VAT UE dla przypadk\xf3w okre\u015blonych w art. 97 ust. 10 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 174, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_4B'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNrNIP, scope=CTD_ANON_2, documentation='Numer, za pomoc\u0105 kt\xf3rego podatnik jest zidentyfikowany na potrzeby podatku, z zastrze\u017ceniem pkt 24 lit. a ustawy. Pole opcjonalne dla przypadku okre\u015blonego w art. 106e ust. 4 pkt 2 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 179, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_5A'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings.MSCountryCode_Type, scope=CTD_ANON_2, documentation='Kod (prefiks) nabywcy - podatnika VAT UE dla przypadk\xf3w okre\u015blonych w art. 97 ust. 10 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 184, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_5B'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNrNIP, scope=CTD_ANON_2, documentation='Numer, za pomoc\u0105 kt\xf3rego nabywca towar\xf3w lub us\u0142ug jest identyfikowany dla podatku lub podatku od warto\u015bci dodanej, pod kt\xf3rym otrzyma\u0142 on towary lub us\u0142ugi, z zastrze\u017ceniem pkt 24 lit. b ustawy. Pole opcjonalne dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 2 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 189, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_6'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_2, documentation='Data dokonania lub zako\u0144czenia dostawy towar\xf3w lub wykonania us\u0142ugi lub data otrzymania zap\u0142aty, o kt\xf3rej mowa w art. 106b ust. 1 pkt 4, o ile taka data jest okre\u015blona i r\xf3\u017cni si\u0119 od daty wystawienia faktury', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 194, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_13_1'), TKwotowy, scope=CTD_ANON_2, documentation='Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 podstawow\u0105 - aktualnie 23% albo 22%.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 203, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_14_1'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 podstawow\u0105 - aktualnie 23% albo 22%.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 208, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_13_2'), TKwotowy, scope=CTD_ANON_2, documentation='Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 pierwsz\u0105 - aktualnie 8 % albo 7%.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 218, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_14_2'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 - aktualnie 8% albo 7%.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 223, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_13_3'), TKwotowy, scope=CTD_ANON_2, documentation='Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 drug\u0105 - aktualnie 5%.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 233, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_14_3'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 drug\u0105 - aktualnie 5%.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 238, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_13_4'), TKwotowy, scope=CTD_ANON_2, documentation='Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 trzeci\u0105 - pole rezerwowe.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 248, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_14_4'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 trzeci\u0105 - pole rezerwowe.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 253, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_13_5'), TKwotowy, scope=CTD_ANON_2, documentation='Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 czwart\u0105 - pole rezerwowe. ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 263, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_14_5'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota podatku od sumy warto\u015bci sprzeda\u017cy netto ze stawk\u0105 obni\u017con\u0105 czwart\u0105 - pole rezerwowe.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 268, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_13_6'), TKwotowy, scope=CTD_ANON_2, documentation='Suma warto\u015bci sprzeda\u017cy netto ze stawk\u0105 0%. Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true"), a tak\u017ce art. 106e ust. 4 pkt 3 i ust. 5 pkt 1-3 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 274, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_13_7'), TKwotowy, scope=CTD_ANON_2, documentation='Suma warto\u015bci sprzeda\u017cy zwolnionej. Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true"), a tak\u017ce art. 106e ust. 4 pkt 3 i ust. 5 pkt 1-3 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 279, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_15'), TKwotowy, scope=CTD_ANON_2, documentation='Kwota nale\u017cno\u015bci og\xf3\u0142em', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 284, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_16'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='W przypadku dostawy towar\xf3w lub \u015bwiadczenia us\u0142ug, w odniesieniu do kt\xf3rych obowi\u0105zek podatkowy powstaje zgodnie z art. 19a ust. 5 pkt 1 lub art. 21 ust. 1 - wyrazy "metoda kasowa", nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 289, 7), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_17'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='W przypadku faktur, o kt\xf3rych mowa w art. 106d ust. 1 - wyraz "samofakturowanie", nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 294, 7), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_18'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='W przypadku dostawy towar\xf3w lub wykonania us\u0142ugi, dla kt\xf3rych obowi\u0105zanym do rozliczenia podatku, podatku od warto\u015bci dodanej lub podatku o podobnym charakterze jest nabywca towaru lub us\u0142ugi - wyrazy "odwrotne obci\u0105\u017cenie", nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 299, 7), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_19'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='W przypadku dostawy towar\xf3w lub \u015bwiadczenia us\u0142ug zwolnionych od podatku na podstawie art. 43 ust. 1, art. 113 ust. 1 i 9 albo przepis\xf3w wydanych na podstawie art. 82 ust. 3 nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 304, 7), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_19A'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Je\u015bli pole P_19 r\xf3wna si\u0119 "true" - nale\u017cy wskaza\u0107 przepis ustawy albo aktu wydanego na podstawie ustawy, na podstawie kt\xf3rego podatnik stosuje zwolnienie od podatku', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 310, 8), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_19B'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Je\u015bli pole P_19 r\xf3wna si\u0119 "true" - nale\u017cy wskaza\u0107 przepis dyrektywy 2006/112/WE, kt\xf3ry zwalnia od podatku tak\u0105 dostaw\u0119 towar\xf3w lub takie \u015bwiadczenie us\u0142ug', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 315, 8), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_19C'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Je\u015bli pole P_19 r\xf3wna si\u0119 "true" - nale\u017cy wskaza\u0107 inn\u0105 podstaw\u0119 prawn\u0105 wskazuj\u0105c\u0105 na to, \u017ce dostawa towar\xf3w lub \u015bwiadczenie us\u0142ug korzysta ze zwolnienia\n', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 320, 8), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_20'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='W przypadku, o kt\xf3rym mowa w art. 106c ustawy nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 327, 7), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_20A'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Je\u015bli pole P_20 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 nazw\u0119 organu egzekucyjnego lub imi\u0119 i nazwisko komornika s\u0105dowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 333, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_20B'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Je\u015bli pole P_20 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 adres organu egzekucyjnego lub komornika s\u0105dowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 338, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_21'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='W przypadku faktur wystawianych w imieniu i na rzecz podatnika przez jego przedstawiciela podatkowego nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 344, 7), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_21A'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Je\u015bli pole P_21 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 nazw\u0119 lub imi\u0119 i nazwisko przedstawiciela podatkowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 350, 8), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_21B'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Je\u015bli pole P_21 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 adres przedstawiciela podatkowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 355, 8), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_21C'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Je\u015bli pole P_21 r\xf3wna si\u0119 "true" - nale\u017cy poda\u0107 numer przedstawiciela podatkowego, za pomoc\u0105 kt\xf3rego jest on zidentyfikowany na potrzeby podatku', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 360, 8), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_22A'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_2, documentation='Data dopuszczenia nowego \u015brodka transportu do u\u017cytku', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 372, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_22B'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Przebieg pojazdu - w przypadku pojazd\xf3w l\u0105dowych, o kt\xf3rych mowa w art. 2 pkt 10 lit. a ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 377, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_22C'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Liczba godzin roboczych u\u017cywania nowego \u015brodka transportu - w przypadku jednostek p\u0142ywaj\u0105cych, o kt\xf3rych mowa w art. 2 pkt 10 lit. b, oraz statk\xf3w powietrznych, o kt\xf3rych mowa w art. 2 pkt 10 lit. c ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 382, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_23'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='W przypadku faktur wystawianych przez drugiego w kolejno\u015bci podatnika, o kt\xf3rym mowa w art. 135 ust. 1 pkt 4 lit. b i c, w wewn\u0105trzwsp\xf3lnotowej transakcji tr\xf3jstronnej (procedurze uproszczonej) - dane okre\u015blone w art. 136, nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 388, 7), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_106E_2'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='W przypadku \u015bwiadczenia us\u0142ug turystyki, dla kt\xf3rych podstaw\u0119 opodatkowania stanowi zgodnie z art. 119 ust. 1 kwota mar\u017cy, faktura - w zakresie danych okre\u015blonych w ust. 1 pkt 1-17 - powinna zawiera\u0107 wy\u0142\u0105cznie dane okre\u015blone w ust. 1 pkt 1-8 i 15-17, a tak\u017ce wyrazy "procedura mar\u017cy dla biur podr\xf3\u017cy", nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"\n', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 393, 7), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_106E_3'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='W przypadku dostawy towar\xf3w u\u017cywanych, dzie\u0142 sztuki, przedmiot\xf3w kolekcjonerskich i antyk\xf3w, dla kt\xf3rych podstaw\u0119 opodatkowania stanowi zgodnie z art. 120 ust. 4 i 5 mar\u017ca, nale\u017cy poda\u0107 warto\u015b\u0107 "true"; w przeciwnym przypadku - warto\u015b\u0107 - "false"', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 400, 8), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_106E_3A'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Je\u017celi pole P_106E_3 r\xf3wna si\u0119 warto\u015bci "true", nale\u017cy poda\u0107 wyrazy: "procedura mar\u017cy - towary u\u017cywane" lub "procedura mar\u017cy - dzie\u0142a sztuki" lub "procedura mar\u017cy - przedmioty kolekcjonerskie i antyki"', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 405, 8), unicode_default='false'))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RodzajFaktury'), STD_ANON_, scope=CTD_ANON_2, documentation='Rodzaj faktury: VAT - podstawowa; KOREKTA - koryguj\u0105ca; ZAL - faktura dokumentuj\u0105ca otrzymanie zap\u0142aty lub jej cz\u0119\u015bci przed dokonaniem czynno\u015bci (art.106b ust. 1 pkt 4 ustawy); POZ - pozosta\u0142e', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 411, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrzyczynaKorekty'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Przyczyna korekty dla faktur koryguj\u0105cych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 425, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrFaKorygowanej'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Numer faktury korygowanej', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 430, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OkresFaKorygowanej'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Dla faktury koryguj\u0105cej - okres, do kt\xf3rego odnosi si\u0119 udzielany opust lub obni\u017cka, w przypadku gdy podatnik udziela opustu lub obni\u017cki ceny w odniesieniu do wszystkich dostaw towar\xf3w lub us\u0142ug dokonanych lub \u015bwiadczonych na rzecz jednego odbiorcy w danym okresie', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 435, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ZALZaplata'), TKwotowy, scope=CTD_ANON_2, documentation='Dla faktury zaliczkowej - otrzymana kwota zap\u0142aty', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 442, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ZALPodatek'), TKwotowy, scope=CTD_ANON_2, documentation='Dla faktury zaliczkowej - kwota podatku wyliczona wed\u0142ug wzoru z art.106f ust. 1 pkt 3 ustawy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 447, 8)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 154, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 159, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 174, 7))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 179, 7))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 184, 7))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 189, 7))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 194, 7))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 199, 7))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 214, 7))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 229, 7))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 244, 7))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 259, 7))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 274, 7))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 279, 7))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 309, 7))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 310, 8))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 315, 8))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 320, 8))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 332, 7))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 349, 7))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 366, 7))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 377, 8))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 382, 8))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 399, 7))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 405, 8))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 424, 7))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 441, 7))
    counters.add(cc_26)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 144, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_2A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 149, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_3A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 154, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_3B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 159, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_3C')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 164, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_3D')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 169, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_4A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 174, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_4B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 179, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_5A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 184, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_5B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 189, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_6')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 194, 7))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_13_1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 203, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_14_1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 208, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_13_2')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 218, 8))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_14_2')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 223, 8))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_13_3')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 233, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_14_3')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 238, 8))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_13_4')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 248, 8))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_14_4')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 253, 8))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_13_5')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 263, 8))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_14_5')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 268, 8))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_13_6')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 274, 7))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_13_7')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 279, 7))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_15')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 284, 7))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_16')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 289, 7))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_17')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 294, 7))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_18')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 299, 7))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_19')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 304, 7))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_19A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 310, 8))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_19B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 315, 8))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_19C')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 320, 8))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_20')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 327, 7))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_20A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 333, 8))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_20B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 338, 8))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_21')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 344, 7))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_21A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 350, 8))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_21B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 355, 8))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_21C')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 360, 8))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_22A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 372, 8))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_22B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 377, 8))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_22C')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 382, 8))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_23')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 388, 7))
    st_41 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_106E_2')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 393, 7))
    st_42 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_106E_3')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 400, 8))
    st_43 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_106E_3A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 405, 8))
    st_44 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RodzajFaktury')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 411, 7))
    st_45 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrzyczynaKorekty')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 425, 8))
    st_46 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrFaKorygowanej')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 430, 8))
    st_47 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_47)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OkresFaKorygowanej')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 435, 8))
    st_48 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_48)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ZALZaplata')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 442, 8))
    st_49 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_49)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ZALPodatek')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 447, 8))
    st_50 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_50)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
         ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
         ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
         ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
         ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_15, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_16, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_34, [
         ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
         ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
         ]))
    transitions.append(fac.Transition(st_38, [
         ]))
    transitions.append(fac.Transition(st_41, [
         ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
         ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
         ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_39, [
         ]))
    transitions.append(fac.Transition(st_40, [
         ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False),
        fac.UpdateInstruction(cc_21, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, True),
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False),
        fac.UpdateInstruction(cc_22, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
         ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
         ]))
    transitions.append(fac.Transition(st_45, [
         ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_44, [
         ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, True),
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_23, False),
        fac.UpdateInstruction(cc_24, False) ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
         ]))
    transitions.append(fac.Transition(st_49, [
         ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_47, [
         ]))
    st_46._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_48, [
         ]))
    st_47._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_48._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_50, [
         ]))
    st_49._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_26, True) ]))
    st_50._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaFaktur'), TNaturalnyJPK, scope=CTD_ANON_3, documentation='Liczba faktur, w okresie kt\xf3rego dotyczy JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 463, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscFaktur'), TKwotowy, scope=CTD_ANON_3, documentation='\u0141\u0105czna warto\u015b\u0107 kwot brutto faktur w okresie, kt\xf3rego dotyczy JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 468, 7)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaFaktur')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 463, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscFaktur')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 468, 7))
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




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Stawka1'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TProcentowy, scope=CTD_ANON_4, documentation='Warto\u015b\u0107 stawki podstawowej', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 482, 7), unicode_default='0.23'))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Stawka2'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TProcentowy, scope=CTD_ANON_4, documentation='Warto\u015b\u0107 stawki obni\u017conej pierwszej', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 487, 7), unicode_default='0.08'))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Stawka3'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TProcentowy, scope=CTD_ANON_4, documentation='Warto\u015b\u0107 stawki obni\u017conej drugiej', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 492, 7), unicode_default='0.05'))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Stawka4'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TProcentowy, scope=CTD_ANON_4, documentation='Warto\u015b\u0107 stawki obni\u017conej trzeciej - pole rezerwowe', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 497, 7), unicode_default='0.00'))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Stawka5'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TProcentowy, scope=CTD_ANON_4, documentation='Warto\u015b\u0107 stawki obni\u017conej czwartej - pole rezerwowe', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 502, 7), unicode_default='0.00'))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Stawka1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 482, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Stawka2')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 487, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Stawka3')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 492, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Stawka4')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 497, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Stawka5')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 502, 7))
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
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_2B'), TZnakowyJPK, scope=CTD_ANON_5, documentation='Kolejny numer faktury, nadany w ramach jednej lub wi\u0119cej serii, kt\xf3ry w spos\xf3b jednoznaczny indentyfikuje faktur\u0119', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 516, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_7'), TZnakowyJPK, scope=CTD_ANON_5, documentation='Nazwa (rodzaj) towaru lub us\u0142ugi. Pole opcjonalne wy\u0142\u0105cznie dla przypadku okre\u015blonego w art 106j ust.3 pkt 2 ustawy (faktura korekta)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 521, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_8A'), TZnakowyJPK, scope=CTD_ANON_5, documentation='Miara dostarczonych towar\xf3w lub zakres wykonanych us\u0142ug. Pole opcjonalne dla przypadku okre\u015blonego w art 106e ust. 5 pkt 3 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 526, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_8B'), TIlosciJPK, scope=CTD_ANON_5, documentation='Ilo\u015b\u0107 (liczba) dostarczonych towar\xf3w lub zakres wykonanych us\u0142ug. Pole opcjonalne dla przypadku okre\u015blonego w art 106e ust. 5 pkt 3 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 531, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_9A'), TKwotowy, scope=CTD_ANON_5, documentation='Cena jednostkowa towaru lub us\u0142ugi bez kwoty podatku (cena jednostkowa netto). Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true") oraz dla przypadku okre\u015blonego w art 106e ust. 5 pkt 3 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 536, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_9B'), TKwotowy, scope=CTD_ANON_5, documentation='W przypadku zastosowania art.106e ustawy, cena wraz z kwot\u0105 podatku (cena jednostkowa brutto)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 541, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_10'), TKwotowy, scope=CTD_ANON_5, documentation='Kwoty wszelkich opust\xf3w lub obni\u017cek cen, w tym w formie rabatu z tytu\u0142u wcze\u015bniejszej zap\u0142aty, o ile nie zosta\u0142y one uwzgl\u0119dnione w cenie jednostkowej netto. Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true") oraz dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 1 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 546, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_11'), TKwotowy, scope=CTD_ANON_5, documentation='Warto\u015b\u0107 dostarczonych towar\xf3w lub wykonanych us\u0142ug, obj\u0119tych transakcj\u0105, bez kwoty podatku (warto\u015b\u0107 sprzeda\u017cy netto). Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true") oraz dla przypadku okre\u015blonego w art. 106e ust. 5 pkt 3 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 551, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_11A'), TKwotowy, scope=CTD_ANON_5, documentation='W przypadku zastosowania art. 106e ust.7 i 8 ustawy, warto\u015b\u0107 sprzeda\u017cy brutto', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 556, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_12'), STD_ANON_2, scope=CTD_ANON_5, documentation='Stawka podatku. Pole opcjonalne dla przypadk\xf3w okre\u015blonych w art. 106e ust.2 i 3 ustawy (gdy przynajmniej jedno z p\xf3l P_106E_2 i P_106E_3 przyjmuje warto\u015b\u0107 "true"), a tak\u017ce art. 106e ust.4 pkt 3 i ust. 5 pkt 1-3 ustawy.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 561, 7)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 521, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 526, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 531, 7))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 536, 7))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 541, 7))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 546, 7))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 551, 7))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 556, 7))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 561, 7))
    counters.add(cc_8)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_2B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 516, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_7')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 521, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_8A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 526, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_8B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 531, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_9A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 536, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_9B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 541, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_10')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 546, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_11')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 551, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_11A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 556, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_12')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 561, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyFaktur'), TNaturalnyJPK, scope=CTD_ANON_6, documentation='Liczba wierszy faktur, w okresie kt\xf3rego dotyczy JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 589, 7)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscWierszyFaktur'), TKwotowy, scope=CTD_ANON_6, documentation='\u0141\u0105czna warto\u015b\u0107 kolumny P_11 tabeli FakturaWiersz w okresie, kt\xf3rego dotyczy JPK_FA', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 594, 7)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyFaktur')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 589, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscWierszyFaktur')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 594, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 47, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 48, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOd')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 53, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataDo')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 58, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 63, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd', 68, 3))
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
CTD_ANON_8._Automaton = _BuildAutomaton_8()

