
class ver:
    def __init__(self, major=0, minor=0, patch=0):
        self.__major = int(major) if int(major) > -1 else 0
        self.__minor = int(minor) if int(minor) > -1 else 0
        self.__patch = int(patch) if int(patch) > -1 else 0

    def __str__(self):
        return "{}.{}.{}".format(self.__major,
                                 self.__minor,
                                 self.__patch)

    def __hash__(self):
        i = self.__major & 0xffffffffffffffff
        j = self.__minor & 0xffffffffffffffff
        k = self.__patch & 0xffffffffffffffff
        return ( i  << 128 ) | ( j  << 64 ) | k

    def major(self):
        return self.__major

    def minor(self):
        return self.__minor

    def patch(self):
        return self.__patch

    def max_value(self):
        ''' The MAXIMAL value for any of the version fields. '''
        return 0xffffffffffffffff

    def min_value(self):
        ''' The MINIMAL value for any of the version fields. '''
        return 0

    def __gt__(self, other):
        if isinstance(other,ver):
            if self.__major > other.major():
                return True
            elif self.__minor > other.minor():
                return True
            elif self.__patch > other.patch():
                return True
            else:
                return False
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other,ver):
            if self.__major < other.major():
                return True
            elif self.__minor < other.minor():
                return True
            elif self.__patch < other.patch():
                return True
            else:
                return False
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other,ver):
            if self.__major != other.major():
                return False
            elif self.__minor != other.minor():
                return False
            elif self.__patch != other.patch():
                return False
            else:
                return True
        else:
            return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return not (self > other)

    def __ge__(self, other):
        return not (self < other)

    def __bool__(self):
        return self.__major != 0 and self.__minor != 0 and self.__patch != 0

    def __len__(self):
        return 3

def gen_ver(major=0, minor=0, patch=0, version=None):
    if version is None or not isinstance(version,ver):
        if isinstance(major,int)and isinstance(minor,int)and isinstance(patch,int):
            return ver(major, minor, patch)
        else:
            raise TypeError()
    else:
        return version

class Versioned:
    def __init__(self, major=0, minor=0, patch=0, version=None):
        self.__version = gen_ver(major, minor, patch, version)

    def version(self):
        return self.__version

    def __gt__(self, other):
        if isinstance(other, Versioned):
            return self.__version > other.version()
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Versioned):
            return self.__version < other.version()
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Versioned):
            return self.__version == other.version()
        else:
            return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return not (self > other)

    def __ge__(self, other):
        return not (self < other)

     
    
class Version_Registry:
    def __init__(self, cls):
        self.__versions = dict()
        self.__current = None
        if issubclass(type(cls), Versioned):
            self.__cls = type(cls)
        else:
            raise TypeError()

    def register(self, new_version , functor ):
        if isinstance(new_version, self.__cls):
            if isinstance(new_version.version(),ver):
                if new_version.version() not in self.__versions:
                    self.__versions[ new_version.version() ] = (new_version, functor)
                return new_version
            else:
                raise TypeError("An UnSupported Version Type was Used!")
        else:
            raise TypeError("An UnSupported Type was Attempted to be Registered!")

    def get(self, major=0, minor=0, patch=0, version=None):
        v = gen_ver(major, minor, patch, version)
        if v not in self.__versions:
            raise ValueError("An Unregistered Version was requested!")
        else:
            return self.__versions[v]

    def gen(self, major=0, minor=0, patch=0, version=None, **kw):
        v = gen_ver(major, minor, patch, version)
        if v not in self.__versions:
            raise ValueError("An Unregistered Version was requested!")
        else:
            f = self.__versions[v][1]
            return f(kw)

    def current(self, new_ver=None):
        if new_ver is not None and isinstance(new_ver,ver):
            if self.__current is None or new_ver != self.__current.version():
                self.__current = self.gen(new_ver)
        return self.__current

    def __contains__(self, item):
        v = None
        if isinstance(item, self.__cls):
            v = item.version()
        elif isinstance(item, ver):
            v = item
        elif isinstance(item, tuple) and len(item) == 3:
            v = gen_ver(major=item[0], minor=item[1],
                        patch=item[2], version=None)
        else:
            raise TypeError("An UnSupported Type was Used!")
        return v in self.__versions

    def __iter__(self):
        return iter(self.__versions.keys())

    def __len__(self):
        return len(self.__versions.keys())

    def __getitem__(self,key):
        v = None
        if isinstance(key, ver):
            v = key
        elif isinstance(key, tuple) and len(key) == 3:
            v = gen_ver(major=key[0], minor=key[1],
                        patch=key[2], version=None)
        elif isinstance(key, int):
            if 0 <= key < len(self.__versions.keys()):
                i = list(self.__versions.keys())
                v = i[key]
            else:
                raise IndexError()
        else:
            raise TypeError()
        if v in self.__versions:
            return self.__versions[v]
        else:
            raise KeyError()
            
                





        
