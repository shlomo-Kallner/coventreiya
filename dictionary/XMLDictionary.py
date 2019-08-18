#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  XMLDictionary.py
#  
#  Copyright 2017 shlomo <shlomo.kallner@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

__package__ = 'dictionary'

##################################################################
#
# Imports
#

import zipfile
#from html import escape, unescape

try:
  from lxml import etree
except ImportError:
  try:
    # Python 2.5
    import xml.etree.ElementTree as etree

from io import StringIO, BytesIO

from icu import UnicodeString as Ustr

from coventreiya.utils.lists import is_item_list
from coventreiya.utils.lists import list_str2Str
from coventreiya.utils.ver import ver

from coventreiya.morphology.roots.abc import root_abc

from coventreiya.morphology.word_stem.abc import cmp_root 
from coventreiya.morphology.word_stem.abc import abc as wordStem_abc

from coventreiya.dictionary import Dictionary
from coventreiya.dictionary import genCurrentRootName
from coventreiya.dictionary import genSubRootName
from coventreiya.dictionary import genInternalFilename
from coventreiya.dictionary import compress
from coventreiya.dictionary import decompress
from coventreiya.dictionary import extractLC
from coventreiya.dictionary import extractLCN
from coventreiya.dictionary import extractLCV
from coventreiya.dictionary import escapedBytes
from coventreiya.dictionary import unescapeBytes

################################################################################
#
#
#   The XML based Dictionary class.
#
#

class XMLDictionary(Dictionary):
	def __init__(self, filename="", create_=True, Language="",
	             Version=None, Part="", NextPart="", PrevPart=""):
		self.__cache = dict()
		super().__init__(filename, create_, Language, Version, Part, 
			             Version, Part, NextPart, PrevPart)
		
	def getInternalFileExt(self):
		return "xml"
			
	def parseFile(self, data):
		xTmp = etree.parse(data)
		#self.__cache[filename] = xTmp
		return xTmp
		
	#def loadFile(self, filename):
	#	if filename not in self.__cache:
	#		try:
	#			ztmp = self.file.getinfo(filename)
	#			fTmp = self.file.open(ztmp)
	#			bTmp = decompress(fTmp.read())
	#			xTmp = etree.parse(bTmp)
	#			# I no longer see why I wanted to keep around the 
	#			#  binary pre-parsed data once parsed, so .. 
	#			# replaced it with None for now..
	#			# was " [ None, xTmp, True ] "
	#			# Now, completely removed and replaced 
	#			# with the node directly...
	#			self.__cache[filename] = xTmp
	#			return xTmp
	#		except:
	#			raise
	#	else:
	#		raise FileExistsError()
			
	##################################################
	#
	#  the cache search method...
	#
	##################################################
			
	def cacheSearch(self, filename, checker=None):
		"""
		If *checker* is not None and a *node* checks-out,
		return the *node* from cache or None.
		Else (*checker* is None) return True or False if *filename*
		is present in the cache..
		"""
		if checker is None:
			return filename in self.__cache
		else:
			tmp = None
			if filename in self.__cache:
				xTmp = self.__cache[filename]
				#if isinstance(tmp, list):
				#	xTmp = tmp[1]
				#else:
				#	xTmp = tmp
				if checker(xTmp):
					tmp = xTmp
			return tmp
		
	def cacheAdd(self, filename, node=None):
		if node is not None:
			if filename not in self.__cache:
				# add some type and data checks...
				self.__cache[filename] = node
			return node
		else:
			raise ValueError()
			
	##################################################
	#
	# the "Internal Structure" Index File Methods.. 
	#
	##################################################
			
	def createInternalStructure(self, Language_="", Version_=None, 
	             Part_=None, NextPart_="", PrevPart_=""):
		"""
		#  * the internal structure of the "index.ext" file:
		#
		#     + File-Type Declaration (?)     
		#     + Index 
		#     | -- Language (str)
		#     | -- Version ("major.minor.patch" or a Ver Object) (?)
		#     | -- Part (int/str) (?)
		#     | -- NextPart (href/filename) (?)
		#     | -- PrevPart (href/filename) (?)
		#        + Root
		#        | -- Value
		#        | -- href
		#        ...
		#        + Root
		#        | -- Value
		#        | -- href
		#
		"""
		attrib = dict()
		ver_ = None
		if isinstance(Version_, ver):
			ver_ = str(Version_)
		elif Version_ is None:
			ver_ = '0.0.0'
		attrib["Version"] = escapedBytes(ver_)
		lang_ = None
		if isinstance(Language_, str) and Language_ != "":
			lang_ = Language_
		else:
			lang_ = 'None'
		attrib["Language"] = escapedBytes(lang_)
		part_ = None
		if isinstance(Part_, int):
			part_ = str(Part_)
		elif isinstance(Part_, str):
			part_ = str(int(Part_,10))
		else:
			part_ = "0"
		attrib["Part"] = escapedBytes(part_)
		next_ = None
		if isinstance(NextPart_, str) and NextPart_ != "":
			next_ = NextPart_
		else:
			next_ = 'None'
		attrib["NextPart"] = escapedBytes(next_)
		prev_ = None
		if isinstance(PrevPart_, str) and PrevPart_ != "":
			prev_ = PrevPart_
		else:
			prev_ = 'None'
		attrib["PrevPart"] = escapedBytes(prev_)
		self.__cache[b"index.xml"] = etree.Element( "Index", attrib )
		
	def loadInternalStructure(self):
		"""
		#     + Index 
		#     | -- Language (str)
		#     | -- Version ("major.minor.patch" or a Ver Object) (?)
		#     | -- Part (int/str) (?)
		#     | -- NextPart (href/filename) (?)
		#     | -- PrevPart (href/filename) (?)
		"""
		try:
			ztmp = self.loadFile(b"index.xml")
			bol = True
			if ztmp.tag == "Index":
				lst_ = [ "Version", "Language", "Part", 
				         "NextPart", "PrevPart" ]
				for i in lst_:
					if i not in ztmp.attrib:
						bol = False
			if not bol:
				raise ValueError()
		except:
			raise
			
	def __searchInternalStructure(self, root):
		zTmp = self.__cache[b"index.xml"]
		srTmp = genCurrentRootName(root)
		rTmp = None
		for i in zTmp:
			if i.tag == "Root" and i.get("Value") == srTmp:
				rTmp = i
				break
		return rTmp
		
	def __addInternalStructure(self, root):
		"""
		#        + Root
		#        | -- Value
		#        | -- href
		"""
		rTmp = self.__searchInternalStructure(root)
		if rTmp is not None:
			zTmp = self.__cache[b"index.xml"]
			val_ = genCurrentRootName(root)
			href_ = genInternalFilename(root, "xml")
			attrib = { "Value": val_, "href": href_ }
			rTmp = etree.SubElement(zTmp, "Root", attrib)
			
	class XMLNodeBase(Dictionary.InternalNodeBase):
		def __init__(self, parent_=None, create=True, data_=None, 
		             args={}):
			self.__node = None
			super().__init__(parent_, create, data_, args)
			
		@abstractmethod
		def create(self, args={}):
			pass
			
		@abstractmethod
		def check(self, data):
			pass
			
		def parse(self, data=None):
			xTmp = None
			# StringIO, BytesIO
			if isinstance(data, str):
				xTmp = etree.parse(StringIO(data))
			elif isinstance(data, bytes):
				xTmp = etree.parse(BytesIO(data))
			elif isinstance(data, StringIO) or isinstance(data, BytesIO):
				xTmp = etree.parse(data)
			elif isinstance(data, etree._Element):
				xTmp = data
			if self.check(xTmp):
				self.__node = xTmp
			else:
				raise ValueError()
			
		def tostring(self):
			return etree.tostring(self.__node, encoding="utf-8", 
			                      xml_declaration=True)
			
		def node(self, node=None):
			if isinstance(node, etree._Element):
				self.__node = node
			return self.__node
			
		def __iter__(self):
			return iter(self.__node)
			
		def __getitem__(self, key):
			return self.__node.__getitem__(key)
			
		def __setitem__(self, key, value):
			self.__node.__setitem__(key, value)
			
		def get(self, key, default=None):
			return self.__node.get(key, default)
			
		def set(self, key, value):
			self.__node.set(key, value)
			
		def __getattr__(self, name):
			if name == "tag":
				return self.__node.tag
			else:
				raise AttributeError()
				
		def __setattr__(self, name, value):
			if name == "tag":
				if isinstance(value, str) or isinstance(value, bytes):
					self.__node.tag = value
				else:
					raise TypeError()
			else:
				object.__setattr__(self, name, value)
			
	class XMLIndexNode(XMLNodeBase):
		def __init__(self, parent_=None, create=True, data_=None, 
		             args={}):
			super().__init__(parent_, create, filename, args)
			
		def create(self, args={}):
			self.node(etree.Element( "Index", args ))
			
		def check(self, data):
			bol = isinstance(data, etree._Element)
			if bol and data.tag == "Index":
				lst_ = [ "Version", "Language", "Part", 
				         "NextPart", "PrevPart" ]
				for i in lst_:
					if i not in data.attrib:
						bol = False
			return bol
			
		pass
		
	class XMLIndexSubNode(XMLNodeBase):
		def __init__(self, parent_=None, create=True, data_=None, 
		             args={}):
			super().__init__(parent_, create, filename, args)
			
		def create(self, args={}):
			parent_ = None
			if "XML_Parent_" in args:
				parent_ = args["XML_Parent_"]
				del args["XML_Parent_"]
			self.node(etree.SubElement( parent_, "Root", args ))
			
		def check(self, data):
			bol = isinstance(data, etree._Element)
			if bol and data.tag == "Root":
				lst_ = [ "Value", "href" ]
				for i in lst_:
					if i not in data.attrib:
						bol = False
			return bol
			
		pass
			
	class XMLIndexFile(Dictionary.IndexFile):
		def __init__(self, parent_=None, create_=True, Language_="", 
		             Version_=None, Part_=None, NextPart_="", 
		             PrevPart_=""):
			super().__init__(parent_, create_, Language_=, Version_, 
			                 Part_, NextPart_, PrevPart_)
			
		def create(self, args={}):
			self.node(XMLIndexNode(self.parent(), True, None, args))
			
		def parse(self, data=None):
			self.node(XMLIndexNode(self.parent(), False, None, dict()))
			
		def getVersion(self):
			return self.node().get("Version")
			
		def getLanguage(self):
			return self.node().get("Language")
			
		def getPart(self):
			return self.node().get("Part")
			
		def getNextPart(self):
			return self.node().get("NextPart")
			
		def getPrevPart(self):
			return self.node().get("PrevPart")
			
		def search(self, root_):
			ext_ = self.parent().getInternalFileExt()
			srTmp = genCurrentRootName(root)
			href_ = genInternalFilename(root_, ext_)
			rTmp = None
			for i in self.node():
				if i.tag == "Root" and i.get("Value") == srTmp \
				and i.get("href") == href_:
					rTmp = i
					#rTmp = XMLIndexSubNode( self.parent(), False, i, 
					#                        dict() )
					break
			return rTmp
						
		def add(self, root_):
			rTmp = self.search(root_)
			if rTmp is not None:
				val_ = genCurrentRootName(root_)
				ext_ = self.parent().getInternalFileExt()
				href_ = genInternalFilename(root_, ext_)
				attrib = { "Value": val_, 
				           "href": href_ #,
				           #"XML_Parent_": self.node().node() 
				           }
				rTmp = etree.SubElement(self.node().node(), "Root", 
				                        attrib)
				#rTmp = XMLIndexSubNode( self.parent(), True, i, 
				#                        attrib )
			return rTmp
			
		pass 
			
	##################################################
	#
	#
	#
	##################################################
			
	def createInteralFile(self, filename, current=""):
		"""
		#  * the internal structure of the "CX.ext" file:
		#
		#     + File-Type Declaration (?)     
		#     + Index
		#     | -- Current ( "C1[/.../CX]" )
		#        + Root
		#        | -- Value
		#        | -- Lexical_Category
		#        | -- href
		#        ...
		#        + Root
		#        | -- Value
		#        | -- Lexical_Category
		#        | -- href
		#
		#
		#    Note:  Lexical_Category will be empty or "None" if this 
		#           just a pass through entry.
		#
		"""		
		## get the "C1/[.../]CX.xml" file name...
		#ext_ = self.getInternalFileExt()
		#filename = genInternalFilename(root,ext_)
		if filename not in self.file.namelist() and filename not in self.__cache:
			## get the escaped "C1/[.../]CX" root name ...
			#eStr_ = escape(genCurrentRootName(root),True)
			eStr_ = escape(current,True)
			sTmp = etree.Element("Index", Current=eStr_)
			self.__cache[filename] = sTmp
			return sTmp
		else:
			raise FileExistsError()
	    
	def loadInteralFile(self, filename):
		"""
		#     + Index
		#     | -- Current ( "C1[/.../CX]" )
		"""
		try:
			 ztmp = self.loadFile(filename)
			 if ztmp.tag == "Index" and "Current" in ztmp.attrib:
				 return ztmp
			 else:
				 raise ValueError()
		except:
			raise
		
	def __check_root_node(self, node, current):
		"""
		#     + Index
		#     | -- Current ( "C1[/.../CX]" )
		"""
		return node.tag == "Index" and node.get("Current") == current
		
	def __create_child_node(self, node, str_, lcn_="None", ifnStr_=""):
		return etree.SubElement(node, "root", {"Value":str_,
		                                       "Lexical_Category":lcn_, 
		                                       "href":ifnStr_})
		                        
	def __check_child_node(self, node, val_, lc_="None"):
		"""
		#        + Root
		#        | -- Value
		#        | -- Lexical_Category
		#        | -- href
		#
		#    Note:  Lexical_Category will be empty or "None" if this 
		#           just a pass through entry.
		#
		"""
		return node.tag == "Root" and node.get("Value") == val_ \
		and node.get("Lexical_Category") == lc_ and "href" in node.attrib
		
	def __cxSubNodeSearch(self, node, eStr_, lcn_, nStr_):
		# basically "get all child nodes that equals x, y, and z."
		res_ = list()
		for child in node:
			if self.__check_child_node(child, eStr_, lcn_):
				if child.get("href") == nStr_:
					res_.append(child)
		return res_	
		
	##################################################
	#
	#
	#
	##################################################
	
	def createInteralNFile(self, filename, value="", lexicalCategory=""):
		"""
		#  * the internal structure of the "CX_n.ext" file:
		#     
		#     + File-Type Declaration (?)     
		#     + Root
		#     | -- Value  ( "C1[/.../CN]" )
		#     | -- Lexical_Category
		#        + WordStem
		#        | -- Value (an [escaped] IPA string ...)
		#        | -- Infixes
		#           + Meaning/Gloss
		#           | -- Language
		#           | == <Meaning/Gloss>
		#                 ...
		#              ...
		#           ...
		#        ...
		#        + Word
		#        | -- Stem (an [escaped] IPA string)
		#        | -- Prefixes
		#        | -- Suffixes
		#           + Meaning/Gloss
		#           | -- Language
		#           | == <Meaning/Gloss>
		#                 ...
		#              ...
		#           ...
		#        ...
		#
		"""
		if filename not in self.file.namelist() and filename not in self.__cache:
			str_ = escape(value,True)
			lcStr_ = escape(lexicalCategory,True)
			sTmp = etree.Element("Root", Value=str_, 
			                     Lexical_Category=lcStr_)
			self.__cache[filename] = sTmp
			return sTmp
		else:
			raise FileExistsError()
		
	def loadInteralNFile(self, filename):
		"""
		#     + Root
		#     | -- Value  ( "C1[/.../CN]" )
		#     | -- Lexical_Category
		"""
		try:
			ztmp = self.loadFile(filename)
			bol = True
			if ztmp.tag == "Root":
				lst_ = [ "Value", "Lexical_Category" ]
				for i in lst_:
					if i not in ztmp.attrib:
						bol = False
				if bol and "href" in ztmp.attrib:
					# must not have a "href" attribute!
					bol = False
			if not bol:
				raise ValueError()
			else:
				return ztmp
		except:
			raise
		
	def __check_NFile_root_node(self, node, val_, lc_):
		"""
		#     + Root
		#     | -- Value  ( "C1[/.../CN]" )
		#     | -- Lexical_Category
		"""
		return node.tag == "Root" and node.get("Value") == val_ \
		and node.get("Lexical_Category") == lc_ \
		and "href" not in ztmp.attrib
		
	##################################################
	#
	#
	#
	##################################################
	
	def __create_Word_node(self, node, stem_, val_, prefixes, suffixes ):
		"""
		#        + Word
		#        | -- Stem (an [escaped] IPA string)
		#        | -- Value (an [escaped] IPA string ...)
		#        | -- Prefixes
		#        | -- Suffixes
		#           + Gloss (Meaning)
		#           | -- Language
		#           | == <Meaning/Gloss>
		"""
		atrib = dict()
		atrib["Stem"] = stem_
		atrib["Value"] = val_
		for i in prefixes:
			v_ = escape(i.value().name.rstrip('_'),True)
			n_ = escape(i.name(),True)
			atrib[n_] = v_
		for i in suffixes:
			v_ = escape(i.value().name.rstrip('_'),True)
			n_ = escape(i.name(),True)
			atrib[n_] = v_
		return etree.SubElement(node, "Word", atrib )
		                        
	def __check_Word_node(self, node, stem_, val_, prefixes_, suffixes_):
		"""
		# Formerly named: __check_NFile_child1_node
		#
		#        + Word
		#        | -- Stem (an [escaped] IPA string)
		#        | -- Value (an [escaped] IPA string ...)
		#        | -- Prefixes
		#        | -- Suffixes
		#           + Gloss (Meaning)
		#           | -- Language
		#           | == <Meaning/Gloss>
		"""
		bol = (node.tag == "Word") and (node.get("Stem") == stem_)\
		and (node.get("Value") == val_)
		if bol:
			for i in prefixes_:
				v_ = escape(i.value().name.rstrip('_'),True)
				n_ = escape(i.name(),True)
				if node.get(n_) != v_:
					bol = False
		if bol:
			for i in suffixes_:
				v_ = escape(i.value().name.rstrip('_'),True)
				n_ = escape(i.name(),True)
				if node.get(n_) != v_:
					bol = False
		return bol
		
	def __cnWordSearch(self, node, stem_, val_, prefixes_, suffixes_):
		# basically "get all Word nodes that equals x, y, and z."
		res_ = list()
		for i in node:
			if self.__check_Word_node(i, stem_, val_, prefixes_, suffixes_):
				res_.append(i)
		return res_
		
	##################################################
	#
	#
	#
	##################################################
	
	def __create_WordStem_node(self, node, val_, con_infixxes, vol_infixxes):
		"""
		#        + WordStem
		#        | -- Value (an [escaped] IPA string ...)
		#        | -- Infixes
		#           + Gloss (Meaning)
		#           | -- Language
		#           | == <Meaning/Gloss>
		"""
		atrib = dict()
		atrib["Value"] = val_
		for i in con_infixxes:
			v_ = escape(i.value().name.rstrip('_'),True)
			n_ = escape(i.name(),True)
			atrib[n_] = v_
		for i in vol_infixxes:
			v_ = escape(i.value().name.rstrip('_'),True)
			n_ = escape(i.name(),True)
			atrib[n_] = v_
		return etree.SubElement(node, "WordStem", atrib )
		
	def __check_WordStem_node(self, node, val_, con_infixxes, vol_infixxes):
		"""
		# Formerly named: __check_NFile_child_node
		# 
		#        + WordStem
		#        | -- Value (an [escaped] IPA string ...)
		#        | -- Infixes
		#           + Meaning/Gloss
		#           | -- Language
		#           | == <Meaning/Gloss>
		"""
		bol = (node.tag == "WordStem") and (node.get("Value") == val_)
		if bol:
			for i in con_infixxes:
				v_ = escape(i.value().name.rstrip('_'),True)
				n_ = escape(i.name(),True)
				if node.get(n_) != v_:
					bol = False
		if bol:
			for i in vol_infixxes:
				v_ = escape(i.value().name.rstrip('_'),True)
				n_ = escape(i.name(),True)
				if node.get(n_) != v_:
					bol = False
		return bol
		
	def __cnWordStemSearch(self, node, val_, con_infixxes, vol_infixxes):
		# basically "get all WordStem nodes that equals x, y, and z."
		res_ = list()
		for i in node:
			if self.__check_WordStem_node(i, val_, con_infixxes, vol_infixxes):
				res_.append(i)
		return res_
		
	##################################################
	#
	#
	#
	##################################################
	
	def __create_Gloss_node(self, node, lang_, gloss_):
		"""
		#           + Gloss (Meaning)
		#           | -- Language
		#           | == <Meaning/Gloss>
		"""
		sTmp = etree.SubElement(node, "Gloss", {"Language":lang_,})
		sTmp.text = escape(gloss_,True)
		return sTmp
		
	def __check_Gloss_node(self, node, lang_, gloss_):
		"""
		# Formerly named: __check_NFile_subchild_node
		# 
		#           + Gloss (Meaning)
		#           | -- Language
		#           | == <Meaning/Gloss>
		"""
		return node.tag == "Gloss" and len(node.attrib) == 1 \
		and node.get("Language") == lang_ and node.text == gloss_
		
	def __cnGlossSearch(self, node, lang_, gloss_):
		"""
		#           + Gloss (Meaning)
		#           | -- Language
		#           | == <Meaning/Gloss>
		"""
		# basically "get all Gloss nodes that equals x, y, and z."
		res_ = list()
		for i in node:
			if self.__check_Gloss_node(i, lang_, gloss_):
				res_.append(i)
		return res_
		
	##################################################
	#
	#
	#
	##################################################
	#		
	#def __cxNodeSearch(self, node, eStr_):
	#	res_ = None
	#	if self.__check_root_node(node,eStr_):
	#		res_ = node
	#	return res_
	#		
	#def __cnNodeSearch(self, node, eStr_, lcn_):
	#	return self.__check_NFile_root_node(node, eStr_, lcn_)
	#	
	##################################################
	#
	#
	#
	##################################################
	
	def getRootFileChecker(self, root):
		# get the escaped "C1/[.../]CX" root name ...
		eStr_ = escape(genCurrentRootName(root),True)
		return lambda tmp: self.__check_root_node(tmp, eStr_)
			
	def addRoot(self, root):
		# get the "C1/[.../]CX.xml" file name...
		ext_ = self.getInternalFileExt()
		cxFStr_ = genInternalFilename(root,ext_)
		# get the escaped "C1/[.../]CX" root name ...
		eStr_ = escape(genCurrentRootName(root),True)
		rTmp = self.rootSearch(root)
		r2Tmp = self.__searchInternalStructure(root)
		if rTmp is None:
			rTmp = self.createInteralFile(cxFStr_, eStr_)
		if r2Tmp is None:
			self.__addInternalStructure(root)
		return rTmp
		
	class XMLRootFile(Dictionary.RootFile):
		def __init__(self, parent_=None, root=None, create_=True):
			self.__node = None
			super().__init__(parent_, root, create_)
			
		def parse(self, data_):
			self.__node = etree.parse(data_)
			
		def tostring(self):
			return etree.tostring(self.__node, encoding="utf-8", 
			                      xml_declaration=True)
		
	##################################################
	#
	#
	#
	##################################################
	
	def getwordStemFileChecker(self, wordStem):
		lcn_ = extractLCN(wordStem)
		# get the escaped "C1/[.../]CX" root name ...
		eStr_ = escape(genCurrentRootName(wordStem.root()),True)
		return lambda tmp: self.__check_NFile_root_node(tmp, eStr_, 
		                                                lcn_)
			
	def addWordStemFile(self, wordStem):
		# check if the "C1/[.../]CX_n.xml" file exists...
		wsfTmp = self.wordStemFileSearch(wordStem)
		if wsfTmp is None:
			# if not check and build the root as well..
			rTmp = self.addRoot(wordStem.root())
			# now build the WordStem File..
			# first the required data..
			#lc_ = extractLC(wordStem)
			lcv_ = extractLCV(wordStem)
			lcn_ = extractLCN(wordStem)
			# get the "C1/[.../]CX_n.xml" file name ...
			cnFStr_ = genInternalFilename(wordStem.root(),"xml",
			                                   lcv_)
			# get the escaped "C1/[.../]CX" root name ...
			eStr_ = escape(genCurrentRootName(wordStem.root()),
			                                       True)
			# and now the file itself ..
			wsfTmp = self.createInteralNFile(cnFStr_, eStr_, lcn_)
			# now check in the "CX.xml" root [ index ] file for any 
			#  sub-nodes with the href..
			chTmp = self.__cxSubNodeSearch(rTmp, eStr_, lcn_, cnFStr_)
			if not (len(chTmp) > 0):
				# if it's not there, build it! 
				sTmp = self.__create_child_node(rTmp, eStr_, lcn_, 
				                                cnFStr_) 
		return wsfTmp
		
	##################################################
	#
	#
	#
	##################################################
	
	def wordStemSearch(self, wordStem):
		"""This method should search both the file 
		   *and* the internal Cache structures...
		   Should Return either a list of *wordStem*-LC child nodes
		   or an empty list...
		"""
		fTmp = self.wordStemFileSearch(wordStem)
		if fTmp is not None:
			# check for the wordStem in ifnStr_
			cons_ = wordStem.con_infixxes()
			vols_ = wordStem.vol_infixxes()
			ipaStr_ = escape(wordStem.str(),True)
			return self.__cnWordStemSearch(fTmp, ipaStr_, cons_, vols_)
		else:
			return list()
			
	def addWordStem(self, wordStem, gloss={}):
		wTmp = None
		# check for the wordStem in the Word Stem File..
		cons_ = wordStem.con_infixxes()
		vols_ = wordStem.vol_infixxes()
		ipaStr_ = escape(wordStem.str(),True)
		wsfTmp = self.addWordStemFile(wordStem) 
		wsTmp = self.wordStemSearch(wordStem)
		if len(wsTmp) > 0:
			wTmp = wsTmp[0]
			# maybe add checks for duplicates?
		else:
			# create the new WordStem node
			wTmp = self.__create_WordStem_node(wsfTmp, ipaStr_, cons_, 
			                                   vols_)
		if isinstance(gloss,dict) and len(gloss) > 0:
			for i in gloss:
				# __cnGlossSearch(self, node, lang_, gloss_)
				gTmp = self.__cnGlossSearch(wTmp, i, gloss[i])
				if len(gTmp) <= 0:
					self.__create_Gloss_node(wTmp, i, gloss[i])
		return wTmp
		
	##################################################
	#
	#
	#
	##################################################
			
	def wordSearch(self, word_):
		"""This method should search both the file 
		   *and* the internal Cache structures...
		   Should Return either a Structure with a
		   __contains__ , a __iter__ and a __getitem__
		   method set that can be searched/indexed with
		   the *root* or *word* ( a dict ) using 
		   *genInternalFilename* ...
		"""
		stem_ = word_.wordStem()
		wsTmp = self.wordStemSearch(stem_)
		res_ = list()
		if len(wsTmp) > 0:
			pre_ = word_.prefixes()
			suf_ = word_.suffixes()
			val_ = word_.str(strip=True)
			for i in wsTmp:
				res_.extend(self.__cnWordSearch(i, stem_, val_, pre_, 
				                                suf_))
		return res_
		
	def addWord(self, word_, gloss={}):
		pass
		
	##################################################
	#
	#
	#
	##################################################
	
	def writeFile(self, node):
		if isinstance(node, etree._Element):
			return etree.tostring(node, encoding="utf-8", 
			                      xml_declaration=True)
		else:
			return node.tostring()
			
	def flush(self):
		"""This method should *flush* all internal cache structures 
		   to disk.
		"""
		# write some other stuff to disk...
		## write the new 
		# now write the cache[files] to disk..
		for i in self.__cache:
			t1 = self.__cache[i]
			str_ = self.writeFile(t1)
			self.saveFile(i, str_)
		
	


#
#
#
##################################################################

##################################################################
#
# Tests Main
#

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
