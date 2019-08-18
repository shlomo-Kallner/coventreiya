

##################################################################
#
# Imports
#

from enum import Enum

from coventreiya.morphology.affix.infix import Consonant as Cons_affix_abc
from coventreiya.morphology.affix.infix import Cons_infix_matcher
from coventreiya.morphology.affix.infix import Vowel as Vol_affix_abc

from coventreiya.morphology.affix.abc import set_abc as affix_set

from coventreiya.phonotactics.onsets.ver_1_5_7 import ver_1_5_7 as onset_match
from coventreiya.phonotactics.nucleus.ver_1_5_7 import ver_1_5_7 as nucleus_match
from coventreiya.phonotactics.codas.ver_1_5_7 import ver_1_5_7 as coda_match

from coventreiya.utils.fsm import fsm_state
from coventreiya.utils.lists import is_item_list

from coventreiya.utils.gen import gen_list, gen_str1
from coventreiya.utils.gen import gen_actual, gen_unique


##################################################################
#
# Coventreiya Morphology  -  Affix - Consonant Infixxes' Base Class
#

class Consonants(Cons_affix_abc):
	def __init__(self, name="", value=None, cons_=None, is_onset=False, 
	             has_neg=False, has_def=True, has_alt=False, has_null=True):
					 if bool(is_onset):
						 match_ = onset_match()
					 else:
						 match_ = coda_match()
					 super().__init__(name, value, cons_, match_, is_onset, 
					                  has_neg, has_def, has_alt, has_null,
					                  1, 3, 5, None)
	pass
	
#def gen_Consonants_lambda( is_onset=False, has_neg=False, has_def=True, 
#                           has_alt=False, has_null=True ):
#	return lambda str_: Consonants( str_, is_onset, has_neg, has_def,
#					                has_alt, has_null)

##################################################################
#
# Coventreiya Morphology  -  Affix - Consonant Infixxes' Actual Classes
#

class Animacy(affix_set):
	class enum_(int, Enum):
		#min_ = 0
		Inanimate_ = 0
		#Inanimate_Energy_ = 1 # is this needed?
		# special [sub]categories of the possibly Inanimate 
		Spatial_Location_ = 1
		Temporal_Location_ = 2 # aka an Event
		Concept_ = 3
		# the Full Categories of the Animate
		Viroid_ = 4
		Protists_ = 5
		Microbes_ = 6
		Fungi_ = 7
		Plant_ = 8
		Animalistic_ = 9
		#the compounds
		Spatial_Temporal_Location_ = 10
		# Inanimate_:
		Inanimate_Spatial_Location_ = 11
		Inanimate_Temporal_Location_ = 12
		Inanimate_Spatial_Temporal_Location_ = 13
		# Concept_:
		Concept_Spatial_Location_ = 14
		Concept_Temporal_Location_ = 15
		Concept_Spatial_Temporal_Location_ = 16
		# Viroid_:
		Viroid_Spatial_Location_ = 17
		Viroid_Temporal_Location_ = 18
		Viroid_Spatial_Temporal_Location_ = 19
		# Protists_:
		Protists_Spatial_Location_ = 20
		Protists_Temporal_Location_ = 21
		Protists_Spatial_Temporal_Location_ = 22
		# Microbes_:
		Microbes_Spatial_Location_ = 23
		Microbes_Temporal_Location_ = 24
		Microbes_Spatial_Temporal_Location_ = 25
		# Fungi_:
		Fungi_Spatial_Location_ = 26
		Fungi_Temporal_Location_ = 27
		Fungi_Spatial_Temporal_Location_ = 28
		# Plant_:
		Plant_Spatial_Location_ = 29
		Plant_Temporal_Location_ = 30
		Plant_Spatial_Temporal_Location_ = 31
		# Animalistic_:
		Animalistic_Spatial_Location_ = 32
		Animalistic_Temporal_Location_ = 33
		Animalistic_Spatial_Temporal_Location_ = 34
		## :
		#Spatial_Location_ = 
		#Temporal_Location_ = 
		#Spatial_Temporal_Location_ = 
		#max_ = 10
		
    def __init__(self):
		is_onset=False
		has_neg=False 
		has_def=True 
		has_alt=False 
		has_null=False
		name_ = "Animacy"
		func_ = lambda str_, value: Consonants( name_, value, str_, 
												is_onset, has_neg, 
												has_def, has_alt, 
	                                            has_null )
	    super().__init__( Consonants, name_, has_neg, has_def, 
	                      func_( [ "[θ]" ], self.enum_.Inanimate_ ), 
	                      self.enum_.Inanimate_,
	                      None, 1,3,5, None )
	    func2_ = lambda str_, value: super()[ value ] = func_( str_, value )
	    # begin constructing the set's contents here:
	    #func2_( [ "[ɡ]" ], self.enum_.Inanimate_Energy_ )
	    func2_( [ "[ɫ]" ], self.enum_.Spatial_Location_ )
	    func2_( [ "[t]" ], self.enum_.Temporal_Location_ )
	    func2_( [ "[d]" ], self.enum_.Concept_ )
	    func2_( [ "[ʃ]" ], self.enum_.Viroid_ )
	    func2_( [ "[ɹ̠]" ], self.enum_.Protists_ )
	    func2_( [ "[k]" ], self.enum_.Microbes_ )
	    func2_( [ "[f]" ], self.enum_.Fungi_ )
	    func2_( [ "[p]" ], self.enum_.Plant_ )
	    func2_( [ "[x]" ], self.enum_.Animalistic_ )
	    #the compounds
		func2_( [ "[ɫ]", "[t]" ], self.enum_.Spatial_Temporal_Location_ ) 
	    # Inanimate_:
		func2_( [ "[ɫ]", "[θ]" ], self.enum_.Inanimate_Spatial_Location_ ) 
	    func2_( [ "[θ]", "[t]" ], self.enum_.Inanimate_Temporal_Location_ ) 
	    func2_( [ "[ɫ]", "[θ]", "[t]" ], self.enum_.Inanimate_Spatial_Temporal_Location_ ) 
	    # Concept_:
		func2_( [ "[ɫ]", "[d]" ], self.enum_.Concept_Spatial_Location_ ) 
	    func2_( [ "[d]", "[t]" ], self.enum_.Concept_Temporal_Location_ ) 
	    func2_( [ "[ɫ]", "[d]", "[t]" ], self.enum_.Concept_Spatial_Temporal_Location_ ) 
	    # Viroid_:
		func2_( [ "[ɫ]", "[ʃ]" ], self.enum_.Viroid_Spatial_Location_ ) 
	    func2_( [ "[ʃ]", "[t]" ], self.enum_.Viroid_Temporal_Location_ ) 
	    func2_( [ "[ɫ]", "[ʃ]", "[t]" ], self.enum_.Viroid_Spatial_Temporal_Location_ ) 
	    # Protists_:
		func2_( [ "[ɹ̠]","[ɫ]" ], self.enum_.Protists_Spatial_Location_ ) 
	    func2_( [ "[ɹ̠]", "[t]" ], self.enum_.Protists_Temporal_Location_ ) 
	    func2_( [ "[ɹ̠]","[ɫ]", "[t]" ], self.enum_.Protists_Spatial_Temporal_Location_ ) 
	    # Microbes_:
		func2_( [ "[ɫ]", "[k]" ], self.enum_.Microbes_Spatial_Location_ ) 
	    func2_( [ "[k]", "[t]" ], self.enum_.Microbes_Temporal_Location_ ) 
	    func2_( [ "[ɫ]", "[k]", "[t]" ], self.enum_.Microbes_Spatial_Temporal_Location_ ) 
	    # Fungi_:
		func2_( [ "[ɫ]", "[f]" ], self.enum_.Fungi_Spatial_Location_ ) 
	    func2_( [ "[f]", "[t]" ], self.enum_.Fungi_Temporal_Location_ ) 
	    func2_( [ "[ɫ]", "[f]", "[t]" ], self.enum_.Fungi_Spatial_Temporal_Location_ ) 
	    # Plant_:
		func2_( [ "[ɫ]", "[p]" ], self.enum_.Plant_Spatial_Location_ ) 
	    func2_( [ "[p]", "[t]" ], self.enum_.Plant_Temporal_Location_ ) 
	    func2_( [ "[ɫ]", "[p]", "[t]" ], self.enum_.Plant_Spatial_Temporal_Location_ ) 
	    # Animalistic_:
		func2_( [ "[ɫ]", "[x]" ], self.enum_.Animalistic_Spatial_Location_ ) 
	    func2_( [ "[x]", "[t]" ], self.enum_.Animalistic_Temporal_Location_ ) 
	    func2_( [ "[ɫ]", "[x]", "[t]" ], self.enum_.Animalistic_Spatial_Temporal_Location_ ) 
	    #func2_( , self.enum_. ) 
	    #func2_( , self.enum_. ) 
	    #func2_( , self.enum_. ) 
	    
    def __setitem__(self, key, value):
		"""
		   Completely disregard *value* 
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
        return super()[key]
        
    def add(self, index, item=None, alt_item=None):
		"""
		   Completely disregard *item* and *alt_item*
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
        return super()[index]
        
    pass
	

class Sentience(affix_set):
	class enum_(int, Enum):
		#min_ = 0
		NotSentient_ = 0
		Sentient_ = 1
		Supernatural_ = 2
		Deity_ = 3
		#max_ = 3
		
	def __init__(self):
		is_onset=False
		has_neg=False
		has_def=True 
		has_alt=True 
		has_null=True
		name_ = "Sentience"
		func_ = lambda str_, value, has_alt_=has_alt: Consonants( name_, 
		                                               value, str_, 
	                                                   is_onset, 
	                                                   has_neg, has_def,
					                                   has_alt_, 
					                                   has_null)
		super().__init__( Consonants, name_, has_neg, has_def, 
		                  func_( [ "" ] , self.enum_.NotSentient_, False ), 
		                  self.enum_.NotSentient_,
		                  None, 1,3,5, None)
		func2_ = lambda value, str_, alt_: super().add( value, 
		                                                func_( str_, value ), 
		                                                func_( alt_, value ) )
		func2_( self.enum_.Sentient_, [ "[w]" ], [ "[j]" ] )
		func2_( self.enum_.Supernatural_, [ "[v]" ], [ "[ʕ]" ] )
		func2_( self.enum_.Deity_, [ "[ʔ]" ], [ "[l]" ] )
		
	def __setitem__(self, key, value):
		"""
		   Completely disregard *value* 
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
        return super()[key]
        
    def add(self, index, item=None, alt_item=None):
		"""
		   Completely disregard *item* and *alt_item*
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
        return super()[index]
        
    pass
	
class Lexical_Category(affix_set):
	class enum_(int, Enum):
		#min_ = 0
		#NotApplicable_ = 0
		Noun_ = 0
		Adjective_ = 1
		Verb_ = 2
		Adverb_ = 3
		Gerund_ = 4
		#Number_ = 5
		#Interjection_ = 6
		# add here a number of Number_ Compounds of the above... neah!
		#max_ = 5
		
	def __init__(self):
		is_onset=False
		has_neg=False
		has_def=True
		has_alt=False 
		has_null=True
		name_ = "Lexical_Category"
		func_ = lambda str_, value: Consonants( name_, value, str_, 
		                                        is_onset, has_neg, 
	                                            has_def, has_alt, 
	                                            has_null)
	    super().__init__( Consonants, name_, has_neg, has_def, 
	                        func_( [ "[n]" ], self.enum_.Noun_ ), 
	                        self.enum_.Noun_,
	                        None, 1,3,5, None)
	    func2_ = lambda value, str_: super()[ value ] = func_( str_, value )
	    func2_( self.enum_.Adjective_, [ "[ŋ]" ] )
	    func2_( self.enum_.Verb_, [ "[v]" ] )
	    func2_( self.enum_.Adverb_, [ "[ʒ]" ] )
	    func2_( self.enum_.Gerund_, [ "[m]" ] )
	    #func2_( self.enum_.Number_, [ "[s]" ] )
	    # add here a number of Number_ Compounds of the above... neah!
	    #func2_( self.enum_.Interjection_, [ "[j]" ] )
	    
	def __setitem__(self, key, value):
		"""
		   Completely disregard *value* 
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
        return super()[key]
        
    def add(self, index, item=None, alt_item=None):
		"""
		   Completely disregard *item* and *alt_item*
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
        return super()[index]
        
    pass
	

def gen_Consonant_Infixes():
	return [ Lexical_Category(), Animacy(), Sentience() ]
	
class __Cons_Infix_matcher_1_3_5(Cons_infix_matcher):
	def __init__(self):
		min_length = 1
        max_length = 3
		super().__init__(min_length, max_length, 1, 3, 5, None)
		
	def matcher(self):
		"""Returns the Match Data Object."""
		pass
        
    def matcher_func(self, inp_, mat_):
		"""
		The Function that DOES the Matching based
		on some Input (*inp_*) and some Match Data Object...
		"""
		pass

    def categories(self):
        ''' Generate the Categories Lists. '''
        return gen_Consonant_Infixes()

    def replacment_map(self):
        ''' Generate the Replacement Map. '''
        cat_ = self.categories()
        return { 0 : cat_[0],
                 1 : cat_[1],
                 2 : cat_[2] } 
        
    pass
	
def gen_all_Consonant_sets():
	"""
	Returns a list of lists.
	Each member list will contain 
	one possible variant of Consonant Infix Sets.
	"""
	cat_ = gen_Consonant_Infixes()
	repl_map = { }
	for i in range(0, len(cat_)):
		repl_map[i] = cat_[i]
	res = [ [0,], 
	        [0,1,]
	        [0,1,2,], ]
    return gen_actual(res, repl_map)
    
	
##################################################################
#
# Coventreiya Morphology  -  Affix - Vowel Infixxes' Base Class
#

class Vowels(Vol_affix_abc):
	def __init__( self, name="", value=None, vowel_=None, has_neg=False, has_def=True, 
	              has_alt=False, has_null=True ):
					  matcher = __nucleus_match()
					  super().__init__(name,value,vowel_,matcher,has_neg,
					                   has_def,has_alt,has_null,
					                   1, 3, 5, None)
	pass

#def gen_Vowels_lambda( has_neg=False, has_def=True, has_alt=False, 
#                       has_null=True ):
#	return lambda str_: Vowels( str_, has_neg, has_def, has_alt,
#						        has_null )

##################################################################
#
# Coventreiya Morphology  -  Affix - Vowel Infixxes' Actual Classes
#
	
class system1(affix_set):
	def __init__(self, name_="", enum_cls=None):
		if (issubclass(enum_cls, int) issubclass(enum_cls, Enum)):
			self.__enum = enum_cls
		else:
			raise TypeError()
		has_neg=False
		has_def=True
		has_alt=False
		has_null=False
		d = dict({ 0 : [ "[ä]" ],
	               1 : [ "[e]" ],
	               2 : [ "[ʊ]" ],
	               3 : [ "[ɛ]" ] })
	    func_ = lambda val_: Vowels( name_, val_, d[val_.value], 
	                                 has_neg, has_def, has_alt, has_null )
		super().__init__( Vowels, name_, has_neg, has_def,
	                      func_( enum_cls(0) ), 
	                      enum_cls(0).value, None, 1,3,5,None)
	    for i in enum_cls:
			if i.value != 0:
				super()[i] = func_( i )
			
	def __setitem__(self, key, value):
		"""
		   Completely disregard *value* 
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
		return super()[key]
        
    def add(self, index, item=None, alt_item=None):
		"""
		   Completely disregard *item* and *alt_item*
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
        return super()[index]
        
    pass
    	
	
class system2(affix_set):
	def __init__(self, name_="", enum_cls=None):
		if (issubclass(enum_cls, int) and issubclass(enum_cls, Enum)):
			self.__enum = enum_cls
		else:
			raise TypeError()
		has_neg=False
		has_def=True
		has_alt=False
		has_null=True
		d = dict({ 0 : [ "" ],
	               1 : [ "[i]" ],
	               2 : [ "[u]" ],
	               3 : [ "[o̞]" ],
	               4 : [ "[ɔ]" ],
	               5 : [ "[æ]" ],
	               6 : [ "[œ]" ] })
	    func_ = lambda val_, has_alt_=has_alt: Vowels( name_, val_, 
		                                               d[val_.value], 
	                                                   has_neg, has_def, 
	                                                   has_alt_, 
	                                                   has_null )
	    func2_ = lambda str_, val_, has_alt_=has_alt: Vowels( name_, 
	                                                   val_, str_, 
	                                                   has_neg, has_def, 
	                                                   has_alt_, 
	                                                   has_null )
	    super().__init__( Vowels, name_, has_neg, has_def,
	                    func_( enum_cls(0), True ), 
	                    enum_cls(0).value, 
	                    func2_( [ "[ɪ]" ], enum_cls(0), True ), 
	                    1,3,5,None)
	    for i in enum_cls:
			if i.value != 0:
				super()[i] = func_( i )
		
	def __setitem__(self, key, value):
		"""
		   Completely disregard *value* 
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
		return super()[key]
        
    def add(self, index, item=None, alt_item=None):
		"""
		   Completely disregard *item* and *alt_item*
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
		return super()[index]
		
    pass
    
########################################################################
#
#   A pair of Utility classes..
#
 
class all_of_system2(system2):
	class enum_(int,Enum):
		Zeroth_ = 0
		First_ = 1
		Second_ = 2
		Third_ = 3
		Fourth_ = 4
		Fifth_ = 5
		Sixth_ = 6
	def __init__(self, name_=""):
		super().__init__( name_, self.enum_ )
		
	pass

class all_of_system1(system1):
	class enum_(int,Enum):
		Zeroth_ = 0
		First_ = 1
		Second_ = 2
		Third_ = 3
	def __init__(self, name_=""):
		super().__init__( name_, self.enum_ )
		
	pass

	

########################################################################
#
#   The actual Vowel Infix classes..
#
 
class Modality(system2):
	class enum_(int, Enum):
		#min_ = 0
		Indicative_ = 0
		Declarative_ = 1
		Interrogative_ = 2
		Jussive_ = 3
		#NotApplicable_ = 4 # empty slot!!!
		Imperative_ = 5
		#max_ = 5
		
	def __init__(self):
		super().__init__( "Modality", self.enum_ )
		
	pass
	
class Abstractivity(system1):
	class enum_(int, Enum):
		#min_ = 0
		Concrete_ = 0
		Virtual_ = 1
		Abstract_ = 2
		#max_ = 2
		
	def __init__(self):
		super().__init__( "Abstractivity", self.enum_ )
		
	pass
	
def gen_Base_Vowel_Infixes():
	return [ Abstractivity(), Modality() ]  # 0 , 1


class Verb_Transitivity(system2):
	class enum_(int, Enum):
		#min_ = 0
		Intransitive_ = 0
		Transitive_ = 1
		Ditransitive_ = 2
		Tritransitive_ = 3
		#max_ = 3
		
	def __init__(self):
		super().__init__( "Verb.Transitivity", self.enum_ )
		
	pass
	

class Verb_Type(system1):
	class enum_(int, Enum):
		#min_ = 0
		Base_ = 0
		Derived1_ = 1
		Derived2_ = 2
		#max_ = 2
		
	def __init__(self):
		super().__init__( "Verb.Type", self.enum_ )
		
	pass
	

class Verb_Valency(system2):
	class enum_(int, Enum):
		#min_ = 0
		Normative_ = 0
		Reciprocal_ = 1
		ToDoCausative_ = 2
		ToBeCausative_ = 3
		#max_ = 1
		
	def __init__(self):
		super().__init__( "Verb.Valency", self.enum_ )
		
	pass
	

class Verb_Voice(system1):
	class enum_(int, Enum):
		#min_ = 0
		Active_ = 0
		Passive_ = 1
		Reflexive_ = 2
		#max_ = 2
		
	def __init__(self):
		super().__init__( "Verb.Voice", self.enum_ )
		
	pass
	

def gen_Verb_Vowel_Infixes():
	return [ Verb_Transitivity(), Verb_Type(), # 0 , 1
	             Verb_Valency(), Verb_Voice() ] # 2, 3

def gen_all_Verb_Vowel_sets():
	"""
	Returns a list of lists.
	Each member list will contain 
	one possible variant of Verb Vowel Infix Sets.
	"""
	cat_ = gen_Base_Vowel_Infixes()
	cat_.extend(gen_Verb_Vowel_Infixes())
	repl_map = {} 
	for i in range(0,len(cat_)):
		repl_map[i] = cat_[i]
	res_ = list()
	# for the 1 syllable length stems:
	res_.append([0,])
	res_.append([1,])
	res_.append([0,1,])
	# for the 2 syllable length stems:
	res_.append([0,4,5,])
	res_.append([1,4,5,])
	res_.append([0,1,4,5,])
	# for the rest:
	res_.append([0,1,2,3,4,5,]) 
	return gen_actual(res, repl_map)


class Noun_Countability(system2):
	class enum_(int, Enum):
		#min_ = 0
		NonCountable_ = 0
		Countable_ = 1
		Mass_ = 2
		#max_ = 1
		
	def __init__(self):
		super().__init__( "Noun.Countability", self.enum_ )
		
	pass
	
	
class Noun_Individuality(system1):
	class enum_(int, Enum):
		#min_ = 0
		Indivual_ = 0
		Collective_ = 1
		#max_ = 1
		
	def __init__(self):
		super().__init__( "Noun.Individuality", self.enum_ )
		
	pass
	
	
class Noun_Type(system2):
	class enum_(int, Enum):
		#min_ = 0
		Common_ = 0
		Derived1_ = 1
		Derived2_ = 2
		#max_ = 1
		
	def __init__(self):
		super().__init__( "Noun.Type", self.enum_ )
		
	pass
	
	
class Noun_Dependency(system1):
	class enum_(int, Enum):
		#min_ = 0
		Independent_ = 0
		Dependent_ = 1
		ConstructState_ = 2
		#max_ = 1
		
	def __init__(self):
		super().__init__( "Noun.Dependency", self.enum_ )
		
	pass
	
	
def gen_Noun_Vowel_Infixes():
	return [ Noun_Type(), Noun_Dependency(),  # 0 , 1
	         Noun_Countability(), Noun_Individuality() ] # 2, 3

def __gen_all_Noun_Vowel_sets():
	"""
	Returns a list of lists.
	Each member list will contain 
	one possible variant of Noun Vowel Infix Sets.
	"""
	cat_ = gen_Base_Vowel_Infixes()
	cat_.extend(gen_Noun_Vowel_Infixes())
	repl_map = {} 
	for i in range(0,len(cat_)):
		repl_map[i] = cat_[i]
	res_ = list()
	# for the 1 syllable length stems:
	res_.append([0,])
	res_.append([1,])
	res_.append([0,1,])
	# for the 2 syllable length stems:
	res_.append([0,4,5,])
	res_.append([1,4,5,])
	res_.append([0,1,4,5,])
	# for the rest:
	res_.append([0,1,2,3,4,5,]) 
	return gen_actual(res, repl_map)

