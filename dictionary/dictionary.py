#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  dictionary.py
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

################################################################################
#
#
#   Imports
#
#

import lzma

import zipfile
from html import escape, unescape


import json
from abc import ABCMeta, abstractmethod

from io import StringIO

from icu import UnicodeString as Ustr

from coventreiya.utils.lists import is_item_list
from coventreiya.utils.lists import list_str2Str
from coventreiya.utils.ver import ver

from coventreiya.morphology.roots.abc import root_abc

from coventreiya.morphology.word_stem.abc import cmp_root 
from coventreiya.morphology.word_stem.abc import abc as wordStem_abc
from coventreiya.morphology.word_stem.abc import org_infixes
from coventreiya.morphology.word.word import Word as word_abc

""" # some old stuff...
################################################################################
#
#
#   Old Compression Utility Functions.. 
#     now moved into the Dictiopnary Class...
#     and then removed to be "static" module level functions...
#

#def __compressor():
#	return lzma.LZMACompressor(format=lzma.FORMAT_XZ, check=lzma.CHECK_SHA256)
	
#def __decompressor():
#	return lzma.LZMADecompressor(format=lzma.FORMAT_XZ)

def __compress(data):
	return lzma.compress(data, format=lzma.FORMAT_XZ, check=lzma.CHECK_SHA256)

def __decompress(data):
	return lzma.decompress(data, format=lzma.FORMAT_XZ)
	
#
#
#
################################################################################
################################################################################
#
#
#   Old Dictionary Creation/Opening Utility Functions..
#     now moved into the Dictiopnary Class...
#

def createDictionaryFile(nameOrFile):
	return zipfile.ZipFile(nameOrFile, mode='x', compression=zipfile.ZIP_LZMA, allowZip64=True) 
	
def openDictionaryFile(nameOrFile):
	tmp = zipfile.ZipFile(nameOrFile, mode='a', compression=zipfile.ZIP_LZMA, allowZip64=True)
	try:
		err_ = tmp.testzip()
		if err_ is not None:
			raise ValueError()
	except:
		raise
	else:
		return tmp
		
#
#
#
#
################################################################################
"""

"""
################################################################################
#
# The Dictionary File's Internal Structures: 
#
# *I think that the internal file structure differs between the 2 types 
#   (XML & JSON) is that the "actual" internal file structures will 
#   be in XML or JSON.
#
# * the internal folders/files structure with any given 1-6 Syllable 
#   Root:
#   
#   + FileName.zip
#   |-- index.ext
#     + C1/
#     |-- C1.ext
#     |-- C1_0.ext
#     |-- ...
#     |-- C1_n.ext
#       + C2/
#       |-- C2.ext
#       |-- C2_0.ext
#       |-- ...
#       |-- C2_n.ext
#         + C3/
#         |-- C3.ext
#         |-- C3_0.ext
#         |-- ...
#         |-- C3_n.ext
#           + C4/
#           |-- C4.ext
#           |-- C4_0.ext
#           |-- ...
#           |-- C4_n.ext
#             + C5/
#             |-- C5.ext
#             |-- C5_0.ext
#             |-- ...
#             |-- C5_n.ext
#               + C6/
#               |-- C6.ext
#               |-- C6_0.ext
#               |-- ...
#               |-- C6_n.ext
#
#
#   For each such available root. Where "ext" is ether "xml" or "json", 
#     "n" is some integer and each CX.ext file in essense is a 
#     "index file" pointing each search into the correct "sub-file" 
#     while the "index.ext" file at the filesystem's root contains a 
#     "list" of all "C1"'s  in the Dictionary (including href-s to the 
#     folder[s]).
#   Basically, for any n-Length ( 1 <= n <= 6 ) Word Stem, 
#     it's Root is copied and broken into a list of it's Syllabic / 
#     Consonant Components and used to create a file Name such as 
#     "C1/../CN.ext". 
#     For each member of the list (C1 to CN), there should be an entry 
#     in the coresponding 'level''s "CX.ext" file who's "href" is a 
#     path to the 'level' down's folder. In "CN.ext" the href is either 
#     to the 
#
#  * the internal structure of the "index.ext" file:
#
#     + File-Type Declaration (?)     
#     + Index 
#     | -- Language
#     | -- Version
#     | -- Part (?)
#     | -- NextPart (href?) (?)
#     | -- PrevPart (href?) (?)
#        + Root
#        | -- Value
#        | -- href
#        ...
#        + Root
#        | -- Value
#        | -- href
#
#
#  * the internal structure of the "CX.ext" file:
#
#     + File-Type Declaration (?)     
#     + Index
#     | -- Current ( "C1[/.../CN]" )
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
#  * the internal structure of the "CX_n.ext" file:
#     
#     + File-Type Declaration (?)     
#     + Root
#     | -- Value ( "C1[/.../CN]" )
#     | -- Lexical_Category
#        + WordStem
#        | -- Value (an IPA string)
#        | -- Infixes
#           + Gloss (Meaning)
#           | -- Language
#           | == <Meaning/Gloss>
#                 ...
#              ...
#           ...
#        ...
#        + Word
#        | -- Stem (an IPA string)
#        | -- Value (an IPA string)
#        | -- Prefixes
#        | -- Suffixes
#           + Gloss (Meaning)
#           | -- Language
#           | == <Meaning/Gloss>
#                 ...
#              ...
#           ...
#        ...
#
################################################################################
"""

################################################################################
#
#  Some Utility Functions..
#
#

def escapedBytes( str_ ):
	sTmp = None
	if isinstance(str_, str):
		sTmp = str_
	elif isinstance( str_, bytes ):
		sTmp = str_.decode(encoding="utf-8")
	else:
		raise TypeError()
	return escape(str_,True).encode("utf-8")
		
def unescapeBytes( str_ ):
	sTmp = None
	if isinstance(str_, str):
		sTmp = str_
	elif isinstance( str_, bytes ):
		sTmp = str_.decode(encoding="utf-8")
	else:
		raise TypeError()
	return unescape(sTmp).encode("utf-8")

def genCurrentRootName( root_ ):
	strm = StringIO()
	for i in range(0, len(root_)):
		strm.write(list_str2Str(root_[i]))
		if i != (len(root_) - 1):
			strm.write("/")
	return escapedBytes(strm.getvalue())
	
def __genSubRootName(root_, len_):
	if len(root_) == len_:
		return genCurrentRootName(root_)
	elif len_ < len(root_):
		strm = StringIO()
		for i in range(0, len_):
			strm.write(list_str2Str(root_[i]))
			if i != (len_ - 1):
				strm.write("/")
		return escapedBytes(strm.getvalue())
	else:
		raise ValueError()
		
def genInternalFilename( root_, ext="", num=None ):
	str_ = unescapeBytes( genCurrentRootName(root_) )
	strm = StringIO( str_.decode(encoding="utf-8") )
	strm.write("/")
	strm.write(list_str2Str(root_[len(root_) - 1]))
	if num is not None and isinstance(num,int):
		strm.write("_")
		strm.write(str(num))
	strm.write(".")
	strm.write(ext)
	# because these are the filenames within the ".zip" files
	# they had better be bytes objects!
	return escapedBytes(strm.getvalue())
	
def __genInternalSubFilename(root_, len_, ext=""):
	if len(root_) == len_:
		return genInternalFilename(root_, ext)
	elif len_ < len(root_):
		str_ = unescapeBytes( __genSubRootName(root_, len_) )
		strm = StringIO( str_.decode(encoding="utf-8") )
		strm.write("/")
		strm.write(list_str2Str(root_[len_ - 1]))
		strm.write(".")
		strm.write(ext)
		# because these are the filenames within the ".zip" files
		# they had better be bytes objects!
		return escapedBytes(strm.getvalue())
	else:
		raise ValueError()

def compress( data ):
	return lzma.compress(data, format=lzma.FORMAT_XZ, 
	                     check=lzma.CHECK_SHA256)
	
def decompress( data ):
	return lzma.decompress(data, format=lzma.FORMAT_XZ)
	
def extractLC( wordstem ):
	org_ = org_infixes(wordstem.con_infixxes())
	return org_["Lexical_Category"]
	
def extractLCN( wordstem ):
	lc_ = extractLC(wordstem)
	lcn_ = lc_.value().name
	str_ = escapedBytes(lcn_.rstrip('_'))
	return str_
	
def extractLCV( wordstem ):
	lc_ = extractLC(wordstem)
	lcv_ = lc_.value().value
	return int(lcv_)
	
################################################################################
#
#
#   The DictionaryRootFile ABC class - either JSON based or XML based.
#
#

class DictionaryBase(metaclass=ABCMeta):
	def __init__(self, create_=True, **kw):
		if create_:
			self.__node = self.create(kw)
		else:
			self.__node = self.load(kw)
			
	@abstractmethod
	def create(self, **kw):
		pass
		
	@abstractmethod
	def load(self, **kw):
		pass
		
	@abstractmethod
	def check(self, **kw):
		pass
		
	@abstractmethod
	def search(self, **kw):
		pass
		
	@abstractmethod
	def add(self, **kw):
		pass
		
	@abstractmethod
	def tostring(self):
		pass
	

class DictionaryRootFile(DictionaryBase):
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
	def __init__(self, create_=True, current_="", node=None):
		super().__init__(
		if create_:
			self.__node = self.create(current)
		else:
			self.__node = self.load(node)
			
	@abstractmethod
	def create(self, current):
		pass
		
	@abstractmethod
	def load(self, node):
		pass
		
	@abstractmethod
	def check(self, node):
		pass
		
	@abstractmethod
	def search(self, eStr_, lcn_, nStr_):
		pass
		
	@abstractmethod
	def add(self, str_, lcn_="None", ifnStr_=""):
		pass
		
	@abstractmethod
	def tostring(self):
		pass
	

################################################################################
#
#
#   The Dictionary ABC class - either JSON based or XML based.
#
#

class Dictionary(metaclass=ABCMeta):
	def __init__(self, filename="", create_=True, Language="",
	             Version=None, Part="", NextPart="", PrevPart=""):
		self.open(filename, create_, Language, Version, Part, 
			      Version, Part, NextPart, PrevPart)
		
	def open(self, filename="", create_=True, Language="",
	         Version=None, Part="", NextPart="", PrevPart=""):
		try:
			if bol(create_):
				self.__file = zipfile.ZipFile(filename, mode='x', 
				                            compression=zipfile.ZIP_LZMA, 
				                            allowZip64=True) 
				self.createInternalStructure(Language, Version, Part, 
			                                 Version, Part, NextPart,
			                                 PrevPart)
			else:
				self.__file = zipfile.ZipFile(filename, mode='a', 
				                            compression=zipfile.ZIP_LZMA, 
				                            allowZip64=True)
				err_ = self.__file.testzip()
				if err_ is not None:
					self.__file.close()
					self.__file = None
					raise ValueError("Method testzip() failed!")
				self.loadInternalStructure()
			self.__filename = filename
		except:
			raise
		
	def close(self):
		if self.__filename is not None:
			self.flush()
			self.__file.close()
			self.__filename = None
			self.__file = None
		else:
			pass
		
	def __del__(self):
		self.close()
		
	##################################################
	#
	#
	#
	##################################################
		
	def __enter__(self):
		return self
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.close()
		return False 
		
	##################################################
	#
	#
	#
	##################################################
		
	def filename(self):
		return self.__filename
		
	@abstractmethod
    def getInternalFileExt(self):
		pass
		
	@abstractmethod
    def flush(self):
		"""This method should *flush* all internal cache structures 
		   to disk (such as prior to closing...).
		"""
		pass
		
	##################################################
	#
	#
	#
	##################################################
		
	@abstractmethod
	def iter(self, **kw):
		"""This method should return a special iterator class
		   that should handle all the iterator funcions while being 
		   able to navigate the internal file-structure. 
		"""
		pass
		
	def __iter__(self):
		"""This method should return a special iterator class
		   that should handle all the iterator funcions while being 
		   able to navigate the internal file-structure. 
		"""
		return self.iter()
		
	@abstractmethod
    def search(self, item):
		pass
		
	@abstractmethod
    def __contains__(self, item):
		pass
		
	def __getitem__(self, key):
		# write a few checks of *key* ...
		return self.search(key)
		
	##################################################
	#
	#
	#
	##################################################
		
	@abstractmethod
	def parseFile(self, data):	
		pass
		
	@abstractmethod
	def cacheSearch(self, filename, checker=None):
		"""
		If *checker* is not None and a *node* checks-out,
		return the *node* from cache or None.
		Else (*checker* is None) return True or False if *filename*
		is present in the cache..
		"""
		pass
		
	@abstractmethod
	def cacheAdd(self, filename, node):
		"""
		Add a file's parsed node (and it's name) 
		to the cache, returns the node.
		"""
		pass
		
	def loadFile(self, filename):
		filename_ = escapedBytes( filename )
		try:
			ztmp = self.__file.getinfo(filename)
			fTmp = self.__file.open(ztmp)
			return decompress(fTmp.read())
		except:
				raise
		
	def loadFileAndCache(self, filename):
		filename_ = escapedBytes( filename )
		try:
			ztmp = self.__file.getinfo(filename)
			fTmp = self.__file.open(ztmp)
			bTmp = decompress(fTmp.read())
		    pTmp = self.parseFile(bTmp)
		    return self.cacheAdd(filename, pTmp)
		except:
				raise
				
	@abstractmethod
	def writeFile(self, node):
		"""
		Turn a File node into a savable file as a bytes or str object.
		Return the object.
		"""
		pass
				
	def saveFile(self, filename, data):
		fn_ = escapedBytes(
		if isinstance(filename,str):
			fn_ = filename.encode("utf-8") 
		elif isinstance(filename, bytes):
			fn_ = filename
		else:
			raise TypeError()
		dt_ = None
		if isinstance(data,str):
			dt_ = data.encode("utf-8") 
		elif isinstance(data, bytes):
			dt_ = data
		else:
			raise TypeError()
		self.__file.writestr(fn_, compress(dt_))
	
	def searchFile(self, filename, checker):
		""" Search for a [Sub-]Filename in the Zip file."""
		res_ = None
		if filename in self.__file.namelist():
			xTmp = self.loadFile(filename)
			if checker(xTmp):
				res_ = xTmp
		return res_
		
	def filenameSearch(self, filename, checker):
		""" 
		    Convenience Method to search both the cache 
		    and the Zip file for a given Filename.
		"""
		tmp = self.cacheSearch(filename, checker)
		if tmp is None:
			try:
				tmp = self.searchFile(filename, checker)
			except KeyError:
				tmp = None
		return tmp
		
	##################################################
	#
	#
	#
	##################################################
	
	@abstractmethod
	def createInternalStructure(self, Language_="", Version_=None, 
	                            Part_=None, NextPart_="", PrevPart_=""):
		"""
		###############################################################
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
		###############################################################
		"""
		pass
		
	@abstractmethod
	def loadInternalStructure(self):
		pass
		
	class InternalNodeBase(metaclass=ABCMeta):
		def __init__(self, parent_=None, create=True, data_=None, 
		             args={}):
			self.__parent = parent_
			if create:
				self.create(kw)
			else:
				self.parse(data_)
				
		def parent(self):
			return self.__parent
			
		def getInternalFileExt(self):
			return self.__parent.getInternalFileExt()
			
		@abstractmethod
		def node(self, node=None):
			pass
			
		@abstractmethod
		def parse(self, data=None):
			pass
			
		@abstractmethod
		def create(self, args={}):
			pass
			
		@abstractmethod
		def tostring(self):
			pass
			
		@abstractmethod
		def __iter__(self):
			pass
			
		@abstractmethod
		def __getitem__(self, key):
			pass
			
		@abstractmethod
		def __setitem__(self, key, value):
			pass
			
		@abstractmethod
		def get(self, key, default=None):
			pass
			
		@abstractmethod
		def set(self, key, value):
			pass
			
	class InternalFileBase(metaclass=ABCMeta):
		def __init__(self, parent_=None, create=True, filename="", 
		             args={}):
			if isinstance(filename, str):
				self.__filename = filename.encode(encoding="utf-8")
			elif isinstance(filename, bytes):
				self.__filename = filename
			if parent_ is not None:
				self.__parent = parent_
			else:
				raise ValueError()
			if create:
				self.create(args)
			else:
				self.parse(self.__parent.loadFile(self.__filename))
			self.__parent.cacheAdd(self.__filename, self)
		
		def filename(self):
			return self.__filename
			
		def parent(self):
			return self.__parent
			
		def getInternalFileExt(self):
			return self.__parent.getInternalFileExt()
			
		def node(self, node=None):
			if issubclass(node, InternalNodeBase):
				self.__node = node
			return self.__node
			
		@abstractmethod
		def parse(self, data=None):
			pass
			
		@abstractmethod
		def create(self, args={}):
			pass
			
		@abstractmethod
		def tostring(self):
			return self.__node.tostring()
			
			
		
	class IndexFile(InternalFileBase):
		"""
		###############################################################
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
		###############################################################
		"""
		def __init__(self, parent_=None, create_=True, Language_="", 
		             Version_=None, Part_=None, NextPart_="", 
		             PrevPart_=""):
			strm = StringIO("index.")
			strm.write(parent_.getInternalFileExt())
			filename_ = strm.getvalue().encode(encoding="utf-8") 
			args = dict()
			lang_ = None
			if isinstance(Language_, str) and Language_ != "":
				lang_ = Language_
			else:
				lang_ = 'None'
			args["Language"] = escapedBytes(lang_)
			ver_ = None
			if isinstance(Version_, ver):
				ver_ = str(Version_)
			elif Version_ is None:
				ver_ = '0.0.0'
			args["Version"] = escapedBytes(ver_)
			part_ = None
			if isinstance(Part_, int):
				part_ = str(Part_)
			elif isinstance(Part_, str):
				part_ = str(int(Part_,10))
			else:
				part_ = "0"
			args["Part"] = escapedBytes(part_)
			next_ = None
			if isinstance(NextPart_, str) and NextPart_ != "":
				next_ = NextPart_
			else:
				next_ = 'None'
			args["NextPart"] = escapedBytes(next_)
			prev_ = None
			if isinstance(PrevPart_, str) and PrevPart_ != "":
				prev_ = PrevPart_
			else:
				prev_ = 'None'
			args["PrevPart"] = escapedBytes(prev_)
			super().__init__(parent_, create_, filename_, args)
			
		#[ "Version", "Language", "Part", "NextPart", "PrevPart" ]
			
		@abstractmethod
		def getVersion(self):
			pass
			
		@abstractmethod
		def getLanguage(self):
			pass
			
		@abstractmethod
		def getPart(self):
			pass
			
		@abstractmethod
		def getNextPart(self):
			pass
			
		@abstractmethod
		def getPrevPart(self):
			pass
			
		@abstractmethod
		def add(self, root_):
			pass
			
		@abstractmethod
		def search(self, root_):
			pass
						
		
	##################################################
	#
	#
	#
	##################################################
		
	@abstractmethod
    def createInteralFile(self, filename, current=""):
		"""
		#  * the internal structure of the "CX.ext" file:
		#
		#     + File-Type Declaration (?)     
		#     + Index
		#     | -- Current
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
		pass
		
	@abstractmethod
	def loadInteralFile(self, filename):
		pass
		
	class RootFile(InternalFileBase):
		"""
		#  * the internal structure of the "CX.ext" file:
		#
		#     + File-Type Declaration (?)     
		#     + Index
		#     | -- Current
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
		def __init__(self, parent_=None, root=None, create_=True):
			ext_ = parent_.getInternalFileExt()
			# get the "C1/[.../]CX.ext" file name...
			filename_ = genInternalFilename(root,ext_)
			root_ = genCurrentRootName( root )
			args = { "root_" : root_ }
			super().__init__(parent_, create_, filename_, args)
			
		@abstractmethod
		def add(self, root, lexicalCategoryName=None, 
		        lexicalCategoryValue=None):
			pass
			
		@abstractmethod
		def search(self, root, lexicalCategoryName=None, 
		           lexicalCategoryValue=None):
			pass	
			
		@abstractmethod
		def getCurrent(self):
			pass
			
		pass
		
	##################################################
	#
	#
	#
	##################################################
		
	@abstractmethod
	def createInteralNFile(self, filename, value="", lexicalCategory=""):
		"""
		#  * the internal structure of the "CX_n.ext" file:
		#     
		#     + File-Type Declaration (?)     
		#     + Root
		#     | -- Value
		#     | -- Lexical_Category
		#        + WordStem
		#        | -- Value (IPA string ...)
		#        | -- Infixes
		#           + Meaning/Gloss
		#           | -- Language
		#           | == <Meaning/Gloss>
		#                 ...
		#              ...
		#           ...
		#        ...
		#        + Word
		#        | -- Stem (an XPath string? index? no it's IPA string!)
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
		pass
		
	@abstractmethod
	def loadInteralNFile(self, filename):
		pass
		
	class NFile(InternalFileBase):
		"""
		#  * the internal structure of the "CX_n.ext" file:
		#     
		#     + File-Type Declaration (?)     
		#     + Root
		#     | -- Value
		#     | -- Lexical_Category
		#        + WordStem
		#        | -- Value (IPA string ...)
		#        | -- Infixes
		#           + Meaning/Gloss
		#           | -- Language
		#           | == <Meaning/Gloss>
		#                 ...
		#              ...
		#           ...
		#        ...
		#        + Word
		#        | -- Stem (an XPath string? index? no it's IPA string!)
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
		def __init__(self, parent_=None, create_=True, root_=None, 
		             lcv_=0, lcn_=""):
			ext_ = self.getInternalFileExt()
			# get the "C1/[.../]CX_n.ext" file name ...
			filename_ = genInternalFilename(root_,ext_,lcv_)
			args = { "Value": filename, 
			         "Lexical_Category": lcn_ }
			super().__init__(parent_, create_, filename_, args)
			
		@abstractmethod
		def addWord(self, word, gloss={}):
			pass
			
		@abstractmethod
		def addWordStem(self, wordStem, gloss={}):
			pass
			
		@abstractmethod
		def getWordChecker(self):
			pass
			
		@abstractmethod
		def getwordStemChecker(self):
			pass
			
		@abstractmethod
		def searchWord(self, word):
			pass
			
		@abstractmethod
		def searchWordStem(self, wordStem):
			pass
		
	##################################################
	#
	#
	#
	##################################################
		
	@abstractmethod
	def getRootFileChecker(self, root):
		pass
		
	def rootSearch(self, root):
		"""This method should search both the file 
		   *and* the internal Cache structures...
		   Should Return either the *root*-file node or
		   None ...
		"""
		ext_ = self.getInternalFileExt()
		# get the "C1/[.../]CX.ext" file name...
		cxFStr_ = genInternalFilename(root,ext_)
		xFileLambda = self.getRootFileChecker(root)
		# checking for the "C1/[.../]CX.ext" file ..
		return self.filenameSearch(cxFStr_, xFileLambda )
		
	@abstractmethod
	def addRoot(self, root):
		pass
		
	##################################################
	#
	#
	#
	##################################################
		
	@abstractmethod
    def getwordStemFileChecker(self, wordStem):
		pass
		
		
	def wordStemFileSearch(self, wordStem):
		"""This method should search both the file 
		   *and* the internal Cache structures...
		   Should Return either the *wordStem*-LC root node
		   or None...
		"""
		#lc_ = extractLC(wordStem)
		lcv_ = extractLCV(wordStem)
		ext_ = self.getInternalFileExt()
		# get the "C1/[.../]CX_n.ext" file name ...
		cnFStr_ = genInternalFilename(wordStem.root(),ext_,lcv_)
		nFileLambda = self.getwordStemFileChecker(wordStem)
		# checking for the "C1/[.../]CX_n.xml" file ..
		return self.filenameSearch(cnFStr_, nFileLambda )
		
	@abstractmethod
	def addWordStemFile(self, wordStem):
		pass
		
	##################################################
	#
	#
	#
	##################################################
	
	@abstractmethod
    def wordStemSearch(self, wordStem):
		"""This method should search both the file 
		   *and* the internal Cache structures...
		   Should Return either a list of *wordStem*-LC child nodes
		   or an empty list...
		"""
		pass
		
	@abstractmethod
	def addWordStem(self, wordStem, gloss={}):
		pass
		
	##################################################
	#
	#
	#
	##################################################
	
	@abstractmethod
	def wordSearch(self, word_):
		"""This method should search both the file 
		   *and* the internal Cache structures...
		   Should Return either a Structure with a
		   __contains__ , a __iter__ and a __getitem__
		   method set that can be searched/indexed with
		   the *root* or *word* ( a dict ) using 
		   *genInternalFilename* ...
		"""
		pass
		
	@abstractmethod
	def addWord(self, word_, gloss={}):
		pass
	
	##################################################
	#
	#
	#
	##################################################
	
	


#
#
#
##################################################################

################################################################################
#
# Main/Testing suite...
#
#

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
