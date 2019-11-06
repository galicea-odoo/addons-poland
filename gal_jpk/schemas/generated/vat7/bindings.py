# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/vat7/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:a5c83123b568e5b660c71f8ffda5a5dc1f9c58a6
# Generated 2018-03-08 13:30:04.761509 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://crd.gov.pl/wzor/2016/08/05/3412/

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
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_02_05_eD_ORDZU_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_02_05_eD_ORDZU__bindings
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_08_03_eD_VATZZ_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_08_03_eD_VATZZ__bindings
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZD_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZD__bindings
import pyxb.binding.datatypes
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZT_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZT__bindings
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://crd.gov.pl/wzor/2016/08/05/3412/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_zzu = _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_02_05_eD_ORDZU__bindings.Namespace
_Namespace_zzu.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_vzd = _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZD__bindings.Namespace
_Namespace_vzd.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_vzt = _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZT__bindings.Namespace
_Namespace_vzt.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_vzz = _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_08_03_eD_VATZZ__bindings.Namespace
_Namespace_vzz.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_etd = _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.Namespace
_Namespace_etd.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://crd.gov.pl/wzor/2016/08/05/3412/}TKodFormularza
class TKodFormularza (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Symbol wzoru formularza"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodFormularza')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 7, 1)
    _Documentation = 'Symbol wzoru formularza'
TKodFormularza._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodFormularza, enum_prefix=None)
TKodFormularza.VAT_7 = TKodFormularza._CF_enumeration.addEnumeration(unicode_value='VAT-7', tag='VAT_7')
TKodFormularza._InitializeFacetMap(TKodFormularza._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodFormularza', TKodFormularza)
_module_typeBindings.TKodFormularza = TKodFormularza

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 33, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='17', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 446, 6)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TRok):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 50, 4)
    _Documentation = None
STD_ANON_2._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_2, value=pyxb.binding.datatypes.gYear('2016'))
STD_ANON_2._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_2, value=pyxb.binding.datatypes.gYear('2030'))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_minInclusive,
   STD_ANON_2._CF_maxInclusive)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 340, 5)
    _Documentation = None
STD_ANON_3._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_3, value=pyxb.binding.datatypes.integer(0))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxInclusive)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TZnakowy):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 457, 5)
    _Documentation = None
STD_ANON_4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_maxLength)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 467, 5)
    _Documentation = None
STD_ANON_5._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_5, value=pyxb.binding.datatypes.date('2016-08-01'))
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_minInclusive)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwota2Nieujemna):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 94, 5)
    _Documentation = None
STD_ANON_6._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwota2Nieujemna, value=pyxb.binding.datatypes.anySimpleType('0'))
STD_ANON_6._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwota2Nieujemna, value=pyxb.binding.datatypes.anySimpleType('2'))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_minExclusive,
   STD_ANON_6._CF_maxExclusive)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Complex type {http://crd.gov.pl/wzor/2016/08/05/3412/}TNaglowek with content type ELEMENT_ONLY
class TNaglowek (pyxb.binding.basis.complexTypeDefinition):
    """Nagłówek deklaracji"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaglowek')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 15, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}KodFormularza uses Python identifier KodFormularza
    __KodFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), 'KodFormularza', '__httpcrd_gov_plwzor201608053412_TNaglowek_httpcrd_gov_plwzor201608053412KodFormularza', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 20, 3), )

    
    KodFormularza = property(__KodFormularza.value, __KodFormularza.set, None, None)

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}WariantFormularza uses Python identifier WariantFormularza
    __WariantFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), 'WariantFormularza', '__httpcrd_gov_plwzor201608053412_TNaglowek_httpcrd_gov_plwzor201608053412WariantFormularza', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 32, 3), )

    
    WariantFormularza = property(__WariantFormularza.value, __WariantFormularza.set, None, None)

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}CelZlozenia uses Python identifier CelZlozenia
    __CelZlozenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), 'CelZlozenia', '__httpcrd_gov_plwzor201608053412_TNaglowek_httpcrd_gov_plwzor201608053412CelZlozenia', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 39, 3), )

    
    CelZlozenia = property(__CelZlozenia.value, __CelZlozenia.set, None, None)

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}Rok uses Python identifier Rok
    __Rok = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rok'), 'Rok', '__httpcrd_gov_plwzor201608053412_TNaglowek_httpcrd_gov_plwzor201608053412Rok', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 49, 3), )

    
    Rok = property(__Rok.value, __Rok.set, None, None)

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}Miesiac uses Python identifier Miesiac
    __Miesiac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Miesiac'), 'Miesiac', '__httpcrd_gov_plwzor201608053412_TNaglowek_httpcrd_gov_plwzor201608053412Miesiac', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 57, 3), )

    
    Miesiac = property(__Miesiac.value, __Miesiac.set, None, None)

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}KodUrzedu uses Python identifier KodUrzedu
    __KodUrzedu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), 'KodUrzedu', '__httpcrd_gov_plwzor201608053412_TNaglowek_httpcrd_gov_plwzor201608053412KodUrzedu', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 58, 3), )

    
    KodUrzedu = property(__KodUrzedu.value, __KodUrzedu.set, None, None)

    _ElementMap.update({
        __KodFormularza.name() : __KodFormularza,
        __WariantFormularza.name() : __WariantFormularza,
        __CelZlozenia.name() : __CelZlozenia,
        __Rok.name() : __Rok,
        __Miesiac.name() : __Miesiac,
        __KodUrzedu.name() : __KodUrzedu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TNaglowek = TNaglowek
Namespace.addCategoryObject('typeBinding', 'TNaglowek', TNaglowek)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """DEKLARACJA DLA PODATKU OD TOWARÓW I USŁUG"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 65, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}Naglowek uses Python identifier Naglowek
    __Naglowek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), 'Naglowek', '__httpcrd_gov_plwzor201608053412_CTD_ANON_httpcrd_gov_plwzor201608053412Naglowek', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 67, 4), )

    
    Naglowek = property(__Naglowek.value, __Naglowek.set, None, 'Nag\u0142\xf3wek deklaracji')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}Podmiot1 uses Python identifier Podmiot1
    __Podmiot1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), 'Podmiot1', '__httpcrd_gov_plwzor201608053412_CTD_ANON_httpcrd_gov_plwzor201608053412Podmiot1', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 72, 4), )

    
    Podmiot1 = property(__Podmiot1.value, __Podmiot1.set, None, None)

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}Pouczenia uses Python identifier Pouczenia
    __Pouczenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pouczenia'), 'Pouczenia', '__httpcrd_gov_plwzor201608053412_CTD_ANON_httpcrd_gov_plwzor201608053412Pouczenia', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 86, 4), )

    
    Pouczenia = property(__Pouczenia.value, __Pouczenia.set, None, 'Warto\u015b\u0107 1 oznacza potwierdzenie zapoznania si\u0119 z tre\u015bci\u0105 i akceptacj\u0119 poni\u017cszych poucze\u0144:\n\t\t\t\t\t\t\t\tW przypadku niewp\u0142acenia w obowi\u0105zuj\u0105cym terminie kwoty z poz. 54 lub wp\u0142acenia jej w niepe\u0142nej wysoko\u015bci, niniejsza deklaracja stanowi podstaw\u0119 do wystawienia tytu\u0142u wykonawczego zgodnie z przepisami ustawy z dnia 17 czerwca 1966 r. o post\u0119powaniu egzekucyjnym w administracji (Dz. U. z 2016 r. poz. 599, z p\xf3\u017an. zm.).\n\nZa podanie nieprawdy lub zatajenie prawdy i przez to nara\u017cenie podatku na uszczuplenie grozi odpowiedzialno\u015b\u0107 przewidziana w Kodeksie karnym skarbowym.\n\t\t\t\t\t\t\t\t')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}Zalaczniki uses Python identifier Zalaczniki
    __Zalaczniki = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Zalaczniki'), 'Zalaczniki', '__httpcrd_gov_plwzor201608053412_CTD_ANON_httpcrd_gov_plwzor201608053412Zalaczniki', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 101, 4), )

    
    Zalaczniki = property(__Zalaczniki.value, __Zalaczniki.set, None, None)

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}PozycjeSzczegolowe uses Python identifier PozycjeSzczegolowe
    __PozycjeSzczegolowe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe'), 'PozycjeSzczegolowe', '__httpcrd_gov_plwzor201608053412_CTD_ANON_httpcrd_gov_plwzor201608053412PozycjeSzczegolowe', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 114, 1), )

    
    PozycjeSzczegolowe = property(__PozycjeSzczegolowe.value, __PozycjeSzczegolowe.set, None, None)

    _ElementMap.update({
        __Naglowek.name() : __Naglowek,
        __Podmiot1.name() : __Podmiot1,
        __Pouczenia.name() : __Pouczenia,
        __Zalaczniki.name() : __Zalaczniki,
        __PozycjeSzczegolowe.name() : __PozycjeSzczegolowe
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
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 102, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/}Zalacznik_ORD-ZU uses Python identifier Zalacznik_ORD_ZU
    __Zalacznik_ORD_ZU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_zzu, 'Zalacznik_ORD-ZU'), 'Zalacznik_ORD_ZU', '__httpcrd_gov_plwzor201608053412_CTD_ANON__httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZUZalacznik_ORD_ZU', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 36, 1), )

    
    Zalacznik_ORD_ZU = property(__Zalacznik_ORD_ZU.value, __Zalacznik_ORD_ZU.set, None, 'UZASADNIENIE PRZYCZYN KOREKTY DEKLARACJI')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}Wniosek_VAT-ZD uses Python identifier Wniosek_VAT_ZD
    __Wniosek_VAT_ZD = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vzd, 'Wniosek_VAT-ZD'), 'Wniosek_VAT_ZD', '__httpcrd_gov_plwzor201608053412_CTD_ANON__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDWniosek_VAT_ZD', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 36, 1), )

    
    Wniosek_VAT_ZD = property(__Wniosek_VAT_ZD.value, __Wniosek_VAT_ZD.set, None, 'ZAWIADOMIENIE O SKORYGOWANIU PODSTAWY OPODATKOWANIA ORAZ KWOTY PODATKU NALE\u017bNEGO')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZT/}Wniosek_VAT-ZT uses Python identifier Wniosek_VAT_ZT
    __Wniosek_VAT_ZT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vzt, 'Wniosek_VAT-ZT'), 'Wniosek_VAT_ZT', '__httpcrd_gov_plwzor201608053412_CTD_ANON__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZTWniosek_VAT_ZT', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZT/VAT-ZT(5)_v2-0E.xsd', 36, 1), )

    
    Wniosek_VAT_ZT = property(__Wniosek_VAT_ZT.value, __Wniosek_VAT_ZT.set, None, 'WNIOSEK O PRZYSPIESZENIE TERMINU ZWROTU PODATKU')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/08/03/eD/VATZZ/}Wniosek_VAT-ZZ uses Python identifier Wniosek_VAT_ZZ
    __Wniosek_VAT_ZZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vzz, 'Wniosek_VAT-ZZ'), 'Wniosek_VAT_ZZ', '__httpcrd_gov_plwzor201608053412_CTD_ANON__httpcrd_gov_plxmlschematydziedzinowemf20160803eDVATZZWniosek_VAT_ZZ', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/08/03/eD/VATZZ/VAT-ZZ(5)_v2-1E.xsd', 63, 1), )

    
    Wniosek_VAT_ZZ = property(__Wniosek_VAT_ZZ.value, __Wniosek_VAT_ZZ.set, None, 'WNIOSEK O ZWROT PODATKU VAT')

    _ElementMap.update({
        __Zalacznik_ORD_ZU.name() : __Zalacznik_ORD_ZU,
        __Wniosek_VAT_ZD.name() : __Wniosek_VAT_ZD,
        __Wniosek_VAT_ZT.name() : __Wniosek_VAT_ZT,
        __Wniosek_VAT_ZZ.name() : __Wniosek_VAT_ZZ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 115, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_10 uses Python identifier P_10
    __P_10 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_10'), 'P_10', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_10', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 117, 4), )

    
    P_10 = property(__P_10.value, __P_10.set, None, 'Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, zwolnione od podatku')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_11 uses Python identifier P_11
    __P_11 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_11'), 'P_11', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_11', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 122, 4), )

    
    P_11 = property(__P_11.value, __P_11.set, None, 'Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug poza terytorium kraju')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_12 uses Python identifier P_12
    __P_12 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_12'), 'P_12', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_12', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 127, 4), )

    
    P_12 = property(__P_12.value, __P_12.set, None, 'Podstawa opodatkowania - w tym \u015bwiadczenie us\u0142ug, o kt\xf3rych mowa w art. 100 ust. 1 pkt 4 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_13 uses Python identifier P_13
    __P_13 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_13'), 'P_13', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_13', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 132, 4), )

    
    P_13 = property(__P_13.value, __P_13.set, None, 'Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 0%')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_14 uses Python identifier P_14
    __P_14 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_14'), 'P_14', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_14', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 137, 4), )

    
    P_14 = property(__P_14.value, __P_14.set, None, 'Podstawa opodatkowania - w tym dostawa towar\xf3w, o kt\xf3rej mowa w art. 129 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_15 uses Python identifier P_15
    __P_15 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_15'), 'P_15', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_15', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 143, 5), )

    
    P_15 = property(__P_15.value, __P_15.set, None, 'Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 5%')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_16 uses Python identifier P_16
    __P_16 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_16'), 'P_16', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_16', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 148, 5), )

    
    P_16 = property(__P_16.value, __P_16.set, None, 'Podatek nale\u017cny - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 5%')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_17 uses Python identifier P_17
    __P_17 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_17'), 'P_17', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_17', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 155, 5), )

    
    P_17 = property(__P_17.value, __P_17.set, None, 'Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 7% albo 8%')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_18 uses Python identifier P_18
    __P_18 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_18'), 'P_18', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_18', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 160, 5), )

    
    P_18 = property(__P_18.value, __P_18.set, None, 'Podatek nale\u017cny - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 7% albo 8%')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_19 uses Python identifier P_19
    __P_19 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_19'), 'P_19', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_19', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 167, 5), )

    
    P_19 = property(__P_19.value, __P_19.set, None, 'Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 22% albo 23%')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_20 uses Python identifier P_20
    __P_20 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_20'), 'P_20', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_20', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 172, 5), )

    
    P_20 = property(__P_20.value, __P_20.set, None, 'Podatek nale\u017cny - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 22% albo 23%')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_21 uses Python identifier P_21
    __P_21 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_21'), 'P_21', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_21', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 178, 4), )

    
    P_21 = property(__P_21.value, __P_21.set, None, 'Podstawa opodatkowania - Wewn\u0105trzwsp\xf3lnotowa dostawa towar\xf3w')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_22 uses Python identifier P_22
    __P_22 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_22'), 'P_22', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_22', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 183, 4), )

    
    P_22 = property(__P_22.value, __P_22.set, None, 'Podstawa opodatkowania - Eksport towar\xf3w')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_23 uses Python identifier P_23
    __P_23 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_23'), 'P_23', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_23', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 189, 5), )

    
    P_23 = property(__P_23.value, __P_23.set, None, 'Podstawa opodatkowania - Wewn\u0105trzwsp\xf3lnotowe nabycie towar\xf3w')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_24 uses Python identifier P_24
    __P_24 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_24'), 'P_24', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_24', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 194, 5), )

    
    P_24 = property(__P_24.value, __P_24.set, None, 'Podatek nale\u017cny - Wewn\u0105trzwsp\xf3lnotowe nabycie towar\xf3w')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_25 uses Python identifier P_25
    __P_25 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_25'), 'P_25', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_25', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 201, 5), )

    
    P_25 = property(__P_25.value, __P_25.set, None, 'Podstawa opodatkowania - Import towar\xf3w podlegaj\u0105cy rozliczeniu zgodnie z art. 33a ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_26 uses Python identifier P_26
    __P_26 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_26'), 'P_26', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_26', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 206, 5), )

    
    P_26 = property(__P_26.value, __P_26.set, None, 'Podatek nale\u017cny - Import towar\xf3w podlegaj\u0105cy rozliczeniu zgodnie z art. 33a ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_27 uses Python identifier P_27
    __P_27 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_27'), 'P_27', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_27', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 213, 5), )

    
    P_27 = property(__P_27.value, __P_27.set, None, 'Podstawa opodatkowania - Import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_28 uses Python identifier P_28
    __P_28 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_28'), 'P_28', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_28', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 218, 5), )

    
    P_28 = property(__P_28.value, __P_28.set, None, 'Podatek nale\u017cny - Import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_29 uses Python identifier P_29
    __P_29 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_29'), 'P_29', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_29', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 225, 5), )

    
    P_29 = property(__P_29.value, __P_29.set, None, 'Podstawa opodatkowania - Import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_30 uses Python identifier P_30
    __P_30 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_30'), 'P_30', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_30', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 230, 5), )

    
    P_30 = property(__P_30.value, __P_30.set, None, 'Podatek nale\u017cny - Import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_31 uses Python identifier P_31
    __P_31 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_31'), 'P_31', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_31', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 236, 4), )

    
    P_31 = property(__P_31.value, __P_31.set, None, 'Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia dostawca)')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_32 uses Python identifier P_32
    __P_32 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_32'), 'P_32', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_32', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 242, 5), )

    
    P_32 = property(__P_32.value, __P_32.set, None, 'Podstawa opodatkowania - Dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca)')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_33 uses Python identifier P_33
    __P_33 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_33'), 'P_33', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_33', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 247, 5), )

    
    P_33 = property(__P_33.value, __P_33.set, None, 'Podatek nale\u017cny - Dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca)')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_34 uses Python identifier P_34
    __P_34 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_34'), 'P_34', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_34', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 254, 5), )

    
    P_34 = property(__P_34.value, __P_34.set, None, 'Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_35 uses Python identifier P_35
    __P_35 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_35'), 'P_35', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_35', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 259, 5), )

    
    P_35 = property(__P_35.value, __P_35.set, None, 'Podatek nale\u017cny - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_36 uses Python identifier P_36
    __P_36 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_36'), 'P_36', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_36', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 265, 4), )

    
    P_36 = property(__P_36.value, __P_36.set, None, 'Kwota podatku nale\u017cnego od towar\xf3w i us\u0142ug obj\u0119tych spisem z natury, o kt\xf3rym mowa w art. 14 ust. 5 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_37 uses Python identifier P_37
    __P_37 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_37'), 'P_37', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_37', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 270, 4), )

    
    P_37 = property(__P_37.value, __P_37.set, None, 'Zwrot odliczonej lub zwr\xf3conej kwoty wydatkowanej na zakup kas rejestruj\u0105cych, o kt\xf3rym mowa w art. 111 ust. 6 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_38 uses Python identifier P_38
    __P_38 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_38'), 'P_38', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_38', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 275, 4), )

    
    P_38 = property(__P_38.value, __P_38.set, None, 'Kwota podatku nale\u017cnego od wewn\u0105trzwsp\xf3lnotowego nabycia \u015brodk\xf3w transportu, wykazanego w poz. 24, podlegaj\u0105ca wp\u0142acie w terminie, o kt\xf3rym mowa w art. 103 ust. 3, w zwi\u0105zku z ust. 4 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_39 uses Python identifier P_39
    __P_39 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_39'), 'P_39', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_39', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 280, 4), )

    
    P_39 = property(__P_39.value, __P_39.set, None, 'Kwota podatku od wewn\u0105trzwsp\xf3lnotowego nabycia paliw silnikowych, podlegaj\u0105ca wp\u0142acie w terminach, o kt\xf3rych mowa w art. 103 ust. 5a i 5b ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_40 uses Python identifier P_40
    __P_40 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_40'), 'P_40', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_40', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 286, 5), )

    
    P_40 = property(__P_40.value, __P_40.set, None, 'Razem - Podstawa opodatkowania')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_41 uses Python identifier P_41
    __P_41 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_41'), 'P_41', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_41', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 291, 5), )

    
    P_41 = property(__P_41.value, __P_41.set, None, 'Razem - Podatek nale\u017cny')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_42 uses Python identifier P_42
    __P_42 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_42'), 'P_42', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_42', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 297, 4), )

    
    P_42 = property(__P_42.value, __P_42.set, None, 'Kwota nadwy\u017cki z poprzedniej deklaracji')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_43 uses Python identifier P_43
    __P_43 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_43'), 'P_43', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_43', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 303, 5), )

    
    P_43 = property(__P_43.value, __P_43.set, None, 'Warto\u015b\u0107 netto - Nabycie towar\xf3w i us\u0142ug zaliczanych u podatnika do \u015brodk\xf3w trwa\u0142ych')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_44 uses Python identifier P_44
    __P_44 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_44'), 'P_44', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_44', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 308, 5), )

    
    P_44 = property(__P_44.value, __P_44.set, None, 'Podatek naliczony - Nabycie towar\xf3w i us\u0142ug zaliczanych u podatnika do \u015brodk\xf3w trwa\u0142ych')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_45 uses Python identifier P_45
    __P_45 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_45'), 'P_45', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_45', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 315, 5), )

    
    P_45 = property(__P_45.value, __P_45.set, None, 'Warto\u015b\u0107 netto - Nabycie towar\xf3w i us\u0142ug pozosta\u0142ych')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_46 uses Python identifier P_46
    __P_46 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_46'), 'P_46', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_46', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 320, 5), )

    
    P_46 = property(__P_46.value, __P_46.set, None, 'Podatek naliczony - Nabycie towar\xf3w i us\u0142ug pozosta\u0142ych')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_47 uses Python identifier P_47
    __P_47 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_47'), 'P_47', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_47', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 326, 4), )

    
    P_47 = property(__P_47.value, __P_47.set, None, 'Korekta podatku naliczonego od nabycia \u015brodk\xf3w trwa\u0142ych')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_48 uses Python identifier P_48
    __P_48 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_48'), 'P_48', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_48', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 331, 4), )

    
    P_48 = property(__P_48.value, __P_48.set, None, 'Korekta podatku naliczonego od pozosta\u0142ych naby\u0107')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_49 uses Python identifier P_49
    __P_49 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_49'), 'P_49', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_49', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 336, 4), )

    
    P_49 = property(__P_49.value, __P_49.set, None, 'Korekta podatku naliczonego, o kt\xf3rej mowa w art. 89b ust. 1 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_50 uses Python identifier P_50
    __P_50 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_50'), 'P_50', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_50', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 346, 4), )

    
    P_50 = property(__P_50.value, __P_50.set, None, 'Korekta podatku naliczonego, o kt\xf3rej mowa w art. 89b ust. 4 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_51 uses Python identifier P_51
    __P_51 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_51'), 'P_51', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_51', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 351, 4), )

    
    P_51 = property(__P_51.value, __P_51.set, None, 'Razem kwota podatku naliczonego do odliczenia')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_52 uses Python identifier P_52
    __P_52 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_52'), 'P_52', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_52', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 356, 4), )

    
    P_52 = property(__P_52.value, __P_52.set, None, 'Kwota wydatkowana na zakup kas rejestruj\u0105cych, do odliczenia w danym okresie rozliczeniowym')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_53 uses Python identifier P_53
    __P_53 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_53'), 'P_53', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_53', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 361, 4), )

    
    P_53 = property(__P_53.value, __P_53.set, None, 'Kwota podatku obj\u0119ta zaniechaniem poboru')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_54 uses Python identifier P_54
    __P_54 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_54'), 'P_54', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_54', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 366, 4), )

    
    P_54 = property(__P_54.value, __P_54.set, None, 'Kwota podatku podlegaj\u0105cego wp\u0142acie do urz\u0119du skarbowego')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_55 uses Python identifier P_55
    __P_55 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_55'), 'P_55', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_55', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 371, 4), )

    
    P_55 = property(__P_55.value, __P_55.set, None, 'Kwota wydatkowana na zakup kas rejestruj\u0105cych, przys\u0142uguj\u0105ca do zwrotu w danym okresie rozliczeniowym')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_56 uses Python identifier P_56
    __P_56 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_56'), 'P_56', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_56', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 376, 4), )

    
    P_56 = property(__P_56.value, __P_56.set, None, 'Nadwy\u017cka podatku naliczonego nad nale\u017cnym')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_57 uses Python identifier P_57
    __P_57 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_57'), 'P_57', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_57', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 381, 4), )

    
    P_57 = property(__P_57.value, __P_57.set, None, 'Kwota do zwrotu na rachunek bankowy wskazany przez podatnika')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_58 uses Python identifier P_58
    __P_58 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_58'), 'P_58', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_58', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 386, 4), )

    
    P_58 = property(__P_58.value, __P_58.set, None, 'w tym kwota do zwrotu - w terminie 25 dni')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_59 uses Python identifier P_59
    __P_59 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_59'), 'P_59', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_59', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 391, 4), )

    
    P_59 = property(__P_59.value, __P_59.set, None, 'w tym kwota do zwrotu - w terminie 60 dni')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_60 uses Python identifier P_60
    __P_60 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_60'), 'P_60', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_60', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 396, 4), )

    
    P_60 = property(__P_60.value, __P_60.set, None, 'w tym kwota do zwrotu - w terminie 180 dni')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_61 uses Python identifier P_61
    __P_61 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_61'), 'P_61', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_61', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 401, 4), )

    
    P_61 = property(__P_61.value, __P_61.set, None, 'Kwota do przeniesienia na nast\u0119pny okres rozliczeniowy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_62 uses Python identifier P_62
    __P_62 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_62'), 'P_62', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_62', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 406, 4), )

    
    P_62 = property(__P_62.value, __P_62.set, None, 'Podatnik wykonywa\u0142 w okresie rozliczeniowym czynno\u015bci, o kt\xf3rych mowa w art. 119 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_63 uses Python identifier P_63
    __P_63 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_63'), 'P_63', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_63', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 411, 4), )

    
    P_63 = property(__P_63.value, __P_63.set, None, 'Podatnik wykonywa\u0142 w okresie rozliczeniowym czynno\u015bci, o kt\xf3rych mowa w art. 120 ust. 4 lub 5 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_64 uses Python identifier P_64
    __P_64 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_64'), 'P_64', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_64', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 416, 4), )

    
    P_64 = property(__P_64.value, __P_64.set, None, 'Podatnik wykonywa\u0142 w okresie rozliczeniowym czynno\u015bci, o kt\xf3rych mowa w art. 122 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_65 uses Python identifier P_65
    __P_65 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_65'), 'P_65', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_65', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 421, 4), )

    
    P_65 = property(__P_65.value, __P_65.set, None, 'Podatnik wykonywa\u0142 w okresie rozliczeniowym czynno\u015bci, o kt\xf3rych mowa w art. 136 ustawy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_66 uses Python identifier P_66
    __P_66 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_66'), 'P_66', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_66', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 426, 4), )

    
    P_66 = property(__P_66.value, __P_66.set, None, 'Do niniejszej deklaracji do\u0142\u0105czono Wniosek o zwrot podatku (VAT-ZZ): 1 - tak, 2 - nie')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_67 uses Python identifier P_67
    __P_67 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_67'), 'P_67', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_67', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 431, 4), )

    
    P_67 = property(__P_67.value, __P_67.set, None, 'Do niniejszej deklaracji do\u0142\u0105czono Wniosek o przyspieszenie terminu zwrotu podatku (VAT-ZT): 1 - tak, 2 - nie')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_68 uses Python identifier P_68
    __P_68 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_68'), 'P_68', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_68', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 437, 5), )

    
    P_68 = property(__P_68.value, __P_68.set, None, 'Do niniejszej deklaracji do\u0142\u0105czono Zawiadomienie o skorygowaniu podstawy opodatkowania oraz kwoty podatku nale\u017cnego (VAT-ZD): 1 - tak, 2 - nie')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_69 uses Python identifier P_69
    __P_69 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_69'), 'P_69', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_69', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 442, 5), )

    
    P_69 = property(__P_69.value, __P_69.set, None, 'Je\u017celi w poz. 68 zaznaczono kwadrat nr 1, nale\u017cy poda\u0107 liczb\u0119 za\u0142\u0105cznik\xf3w VAT-ZD')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_73 uses Python identifier P_73
    __P_73 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_73'), 'P_73', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_73', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 453, 4), )

    
    P_73 = property(__P_73.value, __P_73.set, None, 'Telefon kontaktowy')

    
    # Element {http://crd.gov.pl/wzor/2016/08/05/3412/}P_74 uses Python identifier P_74
    __P_74 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_74'), 'P_74', '__httpcrd_gov_plwzor201608053412_CTD_ANON_2_httpcrd_gov_plwzor201608053412P_74', False, pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 463, 4), )

    
    P_74 = property(__P_74.value, __P_74.set, None, 'Data wype\u0142nienia')

    _ElementMap.update({
        __P_10.name() : __P_10,
        __P_11.name() : __P_11,
        __P_12.name() : __P_12,
        __P_13.name() : __P_13,
        __P_14.name() : __P_14,
        __P_15.name() : __P_15,
        __P_16.name() : __P_16,
        __P_17.name() : __P_17,
        __P_18.name() : __P_18,
        __P_19.name() : __P_19,
        __P_20.name() : __P_20,
        __P_21.name() : __P_21,
        __P_22.name() : __P_22,
        __P_23.name() : __P_23,
        __P_24.name() : __P_24,
        __P_25.name() : __P_25,
        __P_26.name() : __P_26,
        __P_27.name() : __P_27,
        __P_28.name() : __P_28,
        __P_29.name() : __P_29,
        __P_30.name() : __P_30,
        __P_31.name() : __P_31,
        __P_32.name() : __P_32,
        __P_33.name() : __P_33,
        __P_34.name() : __P_34,
        __P_35.name() : __P_35,
        __P_36.name() : __P_36,
        __P_37.name() : __P_37,
        __P_38.name() : __P_38,
        __P_39.name() : __P_39,
        __P_40.name() : __P_40,
        __P_41.name() : __P_41,
        __P_42.name() : __P_42,
        __P_43.name() : __P_43,
        __P_44.name() : __P_44,
        __P_45.name() : __P_45,
        __P_46.name() : __P_46,
        __P_47.name() : __P_47,
        __P_48.name() : __P_48,
        __P_49.name() : __P_49,
        __P_50.name() : __P_50,
        __P_51.name() : __P_51,
        __P_52.name() : __P_52,
        __P_53.name() : __P_53,
        __P_54.name() : __P_54,
        __P_55.name() : __P_55,
        __P_56.name() : __P_56,
        __P_57.name() : __P_57,
        __P_58.name() : __P_58,
        __P_59.name() : __P_59,
        __P_60.name() : __P_60,
        __P_61.name() : __P_61,
        __P_62.name() : __P_62,
        __P_63.name() : __P_63,
        __P_64.name() : __P_64,
        __P_65.name() : __P_65,
        __P_66.name() : __P_66,
        __P_67.name() : __P_67,
        __P_68.name() : __P_68,
        __P_69.name() : __P_69,
        __P_73.name() : __P_73,
        __P_74.name() : __P_74
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = TKodFormularza
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 21, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is TKodFormularza
    
    # Attribute kodSystemowy uses Python identifier kodSystemowy
    __kodSystemowy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodSystemowy'), 'kodSystemowy', '__httpcrd_gov_plwzor201608053412_CTD_ANON_3_kodSystemowy', pyxb.binding.datatypes.string, fixed=True, unicode_default='VAT-7 (17)', required=True)
    __kodSystemowy._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 24, 7)
    __kodSystemowy._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 24, 7)
    
    kodSystemowy = property(__kodSystemowy.value, __kodSystemowy.set, None, None)

    
    # Attribute kodPodatku uses Python identifier kodPodatku
    __kodPodatku = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodPodatku'), 'kodPodatku', '__httpcrd_gov_plwzor201608053412_CTD_ANON_3_kodPodatku', pyxb.binding.datatypes.string, fixed=True, unicode_default='VAT', required=True)
    __kodPodatku._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 25, 7)
    __kodPodatku._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 25, 7)
    
    kodPodatku = property(__kodPodatku.value, __kodPodatku.set, None, None)

    
    # Attribute rodzajZobowiazania uses Python identifier rodzajZobowiazania
    __rodzajZobowiazania = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rodzajZobowiazania'), 'rodzajZobowiazania', '__httpcrd_gov_plwzor201608053412_CTD_ANON_3_rodzajZobowiazania', pyxb.binding.datatypes.token, fixed=True, unicode_default='Z', required=True)
    __rodzajZobowiazania._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 26, 7)
    __rodzajZobowiazania._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 26, 7)
    
    rodzajZobowiazania = property(__rodzajZobowiazania.value, __rodzajZobowiazania.set, None, None)

    
    # Attribute wersjaSchemy uses Python identifier wersjaSchemy
    __wersjaSchemy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wersjaSchemy'), 'wersjaSchemy', '__httpcrd_gov_plwzor201608053412_CTD_ANON_3_wersjaSchemy', pyxb.binding.datatypes.string, fixed=True, unicode_default='1-0E', required=True)
    __wersjaSchemy._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 27, 7)
    __wersjaSchemy._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 27, 7)
    
    wersjaSchemy = property(__wersjaSchemy.value, __wersjaSchemy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kodSystemowy.name() : __kodSystemowy,
        __kodPodatku.name() : __kodPodatku,
        __rodzajZobowiazania.name() : __rodzajZobowiazania,
        __wersjaSchemy.name() : __wersjaSchemy
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TCelZlozenia
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 40, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TCelZlozenia
    
    # Attribute poz uses Python identifier poz
    __poz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'poz'), 'poz', '__httpcrd_gov_plwzor201608053412_CTD_ANON_4_poz', pyxb.binding.datatypes.string, fixed=True, unicode_default='P_7', required=True)
    __poz._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 43, 7)
    __poz._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 43, 7)
    
    poz = property(__poz.value, __poz.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __poz.name() : __poz
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TPodmiotDowolnyBezAdresu2):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 73, 5)
    _ElementMap = _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TPodmiotDowolnyBezAdresu2._ElementMap.copy()
    _AttributeMap = _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TPodmiotDowolnyBezAdresu2._AttributeMap.copy()
    # Base type is _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TPodmiotDowolnyBezAdresu2
    
    # Element OsobaFizyczna ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaFizyczna) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TPodmiotDowolnyBezAdresu2
    
    # Element OsobaNiefizyczna ({http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}OsobaNiefizyczna) inherited from {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/}TPodmiotDowolnyBezAdresu2
    
    # Attribute rola uses Python identifier rola
    __rola = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rola'), 'rola', '__httpcrd_gov_plwzor201608053412_CTD_ANON_5_rola', pyxb.binding.datatypes.string, fixed=True, unicode_default='Podatnik', required=True)
    __rola._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 76, 8)
    __rola._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 76, 8)
    
    rola = property(__rola.value, __rola.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rola.name() : __rola
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


Deklaracja = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Deklaracja'), CTD_ANON, documentation='DEKLARACJA DLA PODATKU OD TOWAR\xd3W I US\u0141UG', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 61, 1))
Namespace.addCategoryObject('elementBinding', Deklaracja.name().localName(), Deklaracja)

PozycjeSzczegolowe = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe'), CTD_ANON_2, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 114, 1))
Namespace.addCategoryObject('elementBinding', PozycjeSzczegolowe.name().localName(), PozycjeSzczegolowe)



TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), CTD_ANON_3, scope=TNaglowek, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 20, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), STD_ANON, scope=TNaglowek, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 32, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), CTD_ANON_4, scope=TNaglowek, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 39, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rok'), STD_ANON_2, scope=TNaglowek, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 49, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Miesiac'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TMiesiac, scope=TNaglowek, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 57, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKodUS, scope=TNaglowek, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 58, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 20, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 32, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 39, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rok')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 49, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Miesiac')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 57, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 58, 3))
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
TNaglowek._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), TNaglowek, scope=CTD_ANON, documentation='Nag\u0142\xf3wek deklaracji', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 67, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), CTD_ANON_5, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 72, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pouczenia'), STD_ANON_6, scope=CTD_ANON, documentation='Warto\u015b\u0107 1 oznacza potwierdzenie zapoznania si\u0119 z tre\u015bci\u0105 i akceptacj\u0119 poni\u017cszych poucze\u0144:\n\t\t\t\t\t\t\t\tW przypadku niewp\u0142acenia w obowi\u0105zuj\u0105cym terminie kwoty z poz. 54 lub wp\u0142acenia jej w niepe\u0142nej wysoko\u015bci, niniejsza deklaracja stanowi podstaw\u0119 do wystawienia tytu\u0142u wykonawczego zgodnie z przepisami ustawy z dnia 17 czerwca 1966 r. o post\u0119powaniu egzekucyjnym w administracji (Dz. U. z 2016 r. poz. 599, z p\xf3\u017an. zm.).\n\nZa podanie nieprawdy lub zatajenie prawdy i przez to nara\u017cenie podatku na uszczuplenie grozi odpowiedzialno\u015b\u0107 przewidziana w Kodeksie karnym skarbowym.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 86, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Zalaczniki'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 101, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 114, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 101, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Naglowek')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 67, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 72, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 81, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pouczenia')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 86, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Zalaczniki')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 101, 4))
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
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_zzu, 'Zalacznik_ORD-ZU'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_02_05_eD_ORDZU__bindings.CTD_ANON, scope=CTD_ANON_, documentation='UZASADNIENIE PRZYCZYN KOREKTY DEKLARACJI', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 36, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vzd, 'Wniosek_VAT-ZD'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZD__bindings.CTD_ANON, scope=CTD_ANON_, documentation='ZAWIADOMIENIE O SKORYGOWANIU PODSTAWY OPODATKOWANIA ORAZ KWOTY PODATKU NALE\u017bNEGO', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 36, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vzt, 'Wniosek_VAT-ZT'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZT__bindings.CTD_ANON, scope=CTD_ANON_, documentation='WNIOSEK O PRZYSPIESZENIE TERMINU ZWROTU PODATKU', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZT/VAT-ZT(5)_v2-0E.xsd', 36, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vzz, 'Wniosek_VAT-ZZ'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_08_03_eD_VATZZ__bindings.CTD_ANON, scope=CTD_ANON_, documentation='WNIOSEK O ZWROT PODATKU VAT', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/08/03/eD/VATZZ/VAT-ZZ(5)_v2-1E.xsd', 63, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 104, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 105, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 106, 7))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 107, 7))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vzz, 'Wniosek_VAT-ZZ')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 104, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vzt, 'Wniosek_VAT-ZT')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 105, 7))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vzd, 'Wniosek_VAT-ZD')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 106, 7))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_zzu, 'Zalacznik_ORD-ZU')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 107, 7))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_10'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, zwolnione od podatku', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 117, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_11'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug poza terytorium kraju', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 122, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_12'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - w tym \u015bwiadczenie us\u0142ug, o kt\xf3rych mowa w art. 100 ust. 1 pkt 4 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 127, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_13'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 0%', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 132, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_14'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - w tym dostawa towar\xf3w, o kt\xf3rej mowa w art. 129 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 137, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_15'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 5%', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 143, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_16'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek nale\u017cny - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 5%', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 148, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_17'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 7% albo 8%', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 155, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_18'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek nale\u017cny - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 7% albo 8%', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 160, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_19'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 22% albo 23%', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 167, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_20'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek nale\u017cny - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug na terytorium kraju, opodatkowane stawk\u0105 22% albo 23%', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 172, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_21'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Wewn\u0105trzwsp\xf3lnotowa dostawa towar\xf3w', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 178, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_22'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Eksport towar\xf3w', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 183, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_23'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Wewn\u0105trzwsp\xf3lnotowe nabycie towar\xf3w', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 189, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_24'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek nale\u017cny - Wewn\u0105trzwsp\xf3lnotowe nabycie towar\xf3w', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 194, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_25'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Import towar\xf3w podlegaj\u0105cy rozliczeniu zgodnie z art. 33a ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 201, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_26'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek nale\u017cny - Import towar\xf3w podlegaj\u0105cy rozliczeniu zgodnie z art. 33a ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 206, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_27'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 213, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_28'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek nale\u017cny - Import us\u0142ug z wy\u0142\u0105czeniem us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 218, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_29'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 225, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_30'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek nale\u017cny - Import us\u0142ug nabywanych od podatnik\xf3w podatku od warto\u015bci dodanej, do kt\xf3rych stosuje si\u0119 art. 28b ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 230, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_31'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia dostawca)', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 236, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_32'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca)', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 242, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_33'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek nale\u017cny - Dostawa towar\xf3w, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wype\u0142nia nabywca)', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 247, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_34'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podstawa opodatkowania - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 254, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_35'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek nale\u017cny - Dostawa towar\xf3w oraz \u015bwiadczenie us\u0142ug, dla kt\xf3rych podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wype\u0142nia nabywca)', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 259, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_36'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego od towar\xf3w i us\u0142ug obj\u0119tych spisem z natury, o kt\xf3rym mowa w art. 14 ust. 5 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 265, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_37'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Zwrot odliczonej lub zwr\xf3conej kwoty wydatkowanej na zakup kas rejestruj\u0105cych, o kt\xf3rym mowa w art. 111 ust. 6 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 270, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_38'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota podatku nale\u017cnego od wewn\u0105trzwsp\xf3lnotowego nabycia \u015brodk\xf3w transportu, wykazanego w poz. 24, podlegaj\u0105ca wp\u0142acie w terminie, o kt\xf3rym mowa w art. 103 ust. 3, w zwi\u0105zku z ust. 4 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 275, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_39'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota podatku od wewn\u0105trzwsp\xf3lnotowego nabycia paliw silnikowych, podlegaj\u0105ca wp\u0142acie w terminach, o kt\xf3rych mowa w art. 103 ust. 5a i 5b ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 280, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_40'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Razem - Podstawa opodatkowania', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 286, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_41'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Razem - Podatek nale\u017cny', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 291, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_42'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota nadwy\u017cki z poprzedniej deklaracji', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 297, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_43'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Warto\u015b\u0107 netto - Nabycie towar\xf3w i us\u0142ug zaliczanych u podatnika do \u015brodk\xf3w trwa\u0142ych', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 303, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_44'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek naliczony - Nabycie towar\xf3w i us\u0142ug zaliczanych u podatnika do \u015brodk\xf3w trwa\u0142ych', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 308, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_45'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Warto\u015b\u0107 netto - Nabycie towar\xf3w i us\u0142ug pozosta\u0142ych', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 315, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_46'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Podatek naliczony - Nabycie towar\xf3w i us\u0142ug pozosta\u0142ych', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 320, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_47'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Korekta podatku naliczonego od nabycia \u015brodk\xf3w trwa\u0142ych', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 326, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_48'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Korekta podatku naliczonego od pozosta\u0142ych naby\u0107', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 331, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_49'), STD_ANON_3, scope=CTD_ANON_2, documentation='Korekta podatku naliczonego, o kt\xf3rej mowa w art. 89b ust. 1 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 336, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_50'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Korekta podatku naliczonego, o kt\xf3rej mowa w art. 89b ust. 4 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 346, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_51'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaC, scope=CTD_ANON_2, documentation='Razem kwota podatku naliczonego do odliczenia', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 351, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_52'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota wydatkowana na zakup kas rejestruj\u0105cych, do odliczenia w danym okresie rozliczeniowym', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 356, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_53'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota podatku obj\u0119ta zaniechaniem poboru', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 361, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_54'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota podatku podlegaj\u0105cego wp\u0142acie do urz\u0119du skarbowego', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 366, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_55'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota wydatkowana na zakup kas rejestruj\u0105cych, przys\u0142uguj\u0105ca do zwrotu w danym okresie rozliczeniowym', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 371, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_56'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Nadwy\u017cka podatku naliczonego nad nale\u017cnym', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 376, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_57'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota do zwrotu na rachunek bankowy wskazany przez podatnika', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 381, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_58'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='w tym kwota do zwrotu - w terminie 25 dni', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 386, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_59'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='w tym kwota do zwrotu - w terminie 60 dni', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 391, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_60'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='w tym kwota do zwrotu - w terminie 180 dni', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 396, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_61'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_2, documentation='Kwota do przeniesienia na nast\u0119pny okres rozliczeniowy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 401, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_62'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TWybor1, scope=CTD_ANON_2, documentation='Podatnik wykonywa\u0142 w okresie rozliczeniowym czynno\u015bci, o kt\xf3rych mowa w art. 119 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 406, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_63'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TWybor1, scope=CTD_ANON_2, documentation='Podatnik wykonywa\u0142 w okresie rozliczeniowym czynno\u015bci, o kt\xf3rych mowa w art. 120 ust. 4 lub 5 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 411, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_64'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TWybor1, scope=CTD_ANON_2, documentation='Podatnik wykonywa\u0142 w okresie rozliczeniowym czynno\u015bci, o kt\xf3rych mowa w art. 122 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 416, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_65'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TWybor1, scope=CTD_ANON_2, documentation='Podatnik wykonywa\u0142 w okresie rozliczeniowym czynno\u015bci, o kt\xf3rych mowa w art. 136 ustawy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 421, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_66'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TWybor1_2, scope=CTD_ANON_2, documentation='Do niniejszej deklaracji do\u0142\u0105czono Wniosek o zwrot podatku (VAT-ZZ): 1 - tak, 2 - nie', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 426, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_67'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TWybor1_2, scope=CTD_ANON_2, documentation='Do niniejszej deklaracji do\u0142\u0105czono Wniosek o przyspieszenie terminu zwrotu podatku (VAT-ZT): 1 - tak, 2 - nie', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 431, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_68'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TWybor1_2, scope=CTD_ANON_2, documentation='Do niniejszej deklaracji do\u0142\u0105czono Zawiadomienie o skorygowaniu podstawy opodatkowania oraz kwoty podatku nale\u017cnego (VAT-ZD): 1 - tak, 2 - nie', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 437, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_69'), STD_ANON_, scope=CTD_ANON_2, documentation='Je\u017celi w poz. 68 zaznaczono kwadrat nr 1, nale\u017cy poda\u0107 liczb\u0119 za\u0142\u0105cznik\xf3w VAT-ZD', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 442, 5)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_73'), STD_ANON_4, scope=CTD_ANON_2, documentation='Telefon kontaktowy', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 453, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_74'), STD_ANON_5, scope=CTD_ANON_2, documentation='Data wype\u0142nienia', location=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 463, 4)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 117, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 122, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 127, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 132, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 137, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 142, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 154, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 166, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 178, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 183, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 188, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 200, 4))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 212, 4))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 224, 4))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 236, 4))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 241, 4))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 253, 4))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 265, 4))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 270, 4))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 275, 4))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 280, 4))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 286, 5))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 297, 4))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 302, 4))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 314, 4))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 326, 4))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 331, 4))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 336, 4))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 346, 4))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 351, 4))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 356, 4))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 361, 4))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 371, 4))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 376, 4))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 386, 4))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 391, 4))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 396, 4))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 401, 4))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 406, 4))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 411, 4))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 416, 4))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 421, 4))
    counters.add(cc_41)
    cc_42 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 426, 4))
    counters.add(cc_42)
    cc_43 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 431, 4))
    counters.add(cc_43)
    cc_44 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 436, 4))
    counters.add(cc_44)
    cc_45 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 442, 5))
    counters.add(cc_45)
    cc_46 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 453, 4))
    counters.add(cc_46)
    cc_47 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 463, 4))
    counters.add(cc_47)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_10')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 117, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_11')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 122, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_12')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 127, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_13')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 132, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_14')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 137, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_15')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 143, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_16')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 148, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_17')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 155, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_18')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 160, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_19')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 167, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_20')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 172, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_21')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 178, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_22')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 183, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_23')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 189, 5))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_24')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 194, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_25')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 201, 5))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_26')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 206, 5))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_27')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 213, 5))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_28')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 218, 5))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_29')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 225, 5))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_30')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 230, 5))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_31')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 236, 4))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_32')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 242, 5))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_33')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 247, 5))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_34')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 254, 5))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_35')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 259, 5))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_36')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 265, 4))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_37')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 270, 4))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_38')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 275, 4))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_39')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 280, 4))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_40')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 286, 5))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_41')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 291, 5))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_42')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 297, 4))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_43')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 303, 5))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_44')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 308, 5))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_45')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 315, 5))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_46')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 320, 5))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_47')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 326, 4))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_48')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 331, 4))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_49')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 336, 4))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_50')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 346, 4))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_51')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 351, 4))
    st_41 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_52')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 356, 4))
    st_42 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_53')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 361, 4))
    st_43 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_54')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 366, 4))
    st_44 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_55')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 371, 4))
    st_45 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_56')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 376, 4))
    st_46 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_57')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 381, 4))
    st_47 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_47)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_58')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 386, 4))
    st_48 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_48)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_59')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 391, 4))
    st_49 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_49)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_60')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 396, 4))
    st_50 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_50)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_61')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 401, 4))
    st_51 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_51)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_62')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 406, 4))
    st_52 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_52)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_63')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 411, 4))
    st_53 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_53)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_64')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 416, 4))
    st_54 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_54)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_41, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_65')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 421, 4))
    st_55 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_55)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_42, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_66')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 426, 4))
    st_56 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_56)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_43, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_67')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 431, 4))
    st_57 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_57)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_44, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_68')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 437, 5))
    st_58 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_58)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_44, False))
    final_update.add(fac.UpdateInstruction(cc_45, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_69')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 442, 5))
    st_59 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_59)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_46, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_73')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 453, 4))
    st_60 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_60)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_47, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_74')), pyxb.utils.utility.Location('http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd', 463, 4))
    st_61 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_61)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
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
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
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
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
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
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
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
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
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
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
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
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
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
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
         ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
         ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    transitions.append(fac.Transition(st_35, [
         ]))
    transitions.append(fac.Transition(st_37, [
         ]))
    transitions.append(fac.Transition(st_38, [
         ]))
    transitions.append(fac.Transition(st_39, [
         ]))
    transitions.append(fac.Transition(st_40, [
         ]))
    transitions.append(fac.Transition(st_41, [
         ]))
    transitions.append(fac.Transition(st_42, [
         ]))
    transitions.append(fac.Transition(st_43, [
         ]))
    transitions.append(fac.Transition(st_44, [
         ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
         ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
         ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
         ]))
    transitions.append(fac.Transition(st_46, [
         ]))
    transitions.append(fac.Transition(st_47, [
         ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_46._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_48, [
         ]))
    transitions.append(fac.Transition(st_49, [
         ]))
    transitions.append(fac.Transition(st_50, [
         ]))
    transitions.append(fac.Transition(st_51, [
         ]))
    transitions.append(fac.Transition(st_52, [
         ]))
    transitions.append(fac.Transition(st_53, [
         ]))
    transitions.append(fac.Transition(st_54, [
         ]))
    transitions.append(fac.Transition(st_55, [
         ]))
    transitions.append(fac.Transition(st_56, [
         ]))
    transitions.append(fac.Transition(st_57, [
         ]))
    transitions.append(fac.Transition(st_58, [
         ]))
    transitions.append(fac.Transition(st_60, [
         ]))
    transitions.append(fac.Transition(st_61, [
         ]))
    st_47._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_48._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_49._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_50._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_51._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_52._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_53._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_54._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_41, True) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_41, False) ]))
    st_55._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_42, True) ]))
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_42, False) ]))
    st_56._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_57, [
        fac.UpdateInstruction(cc_43, True) ]))
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_43, False) ]))
    st_57._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_44, True) ]))
    transitions.append(fac.Transition(st_59, [
         ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_44, False) ]))
    st_58._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_58, [
        fac.UpdateInstruction(cc_44, True),
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_59, [
        fac.UpdateInstruction(cc_45, True) ]))
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_44, False),
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_44, False),
        fac.UpdateInstruction(cc_45, False) ]))
    st_59._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_60, [
        fac.UpdateInstruction(cc_46, True) ]))
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_46, False) ]))
    st_60._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_61, [
        fac.UpdateInstruction(cc_47, True) ]))
    st_61._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_etd, 'OsobaFizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 421, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_etd, 'OsobaNiefizyczna')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/StrukturyDanych_v4-0E.xsd', 422, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_4()

