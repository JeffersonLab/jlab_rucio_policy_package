
from .path_gen import construct_surl_jlab
from .lfn2pfn import lfn2pfn_jlab
#from .extract_scope import extract_scope_jlab

SUPPORTED_VERSION = [ "1.30", "1.31", "32" ]

def get_algorithms():
    return {'lfn2pfn': {'belleii': lfn2pfn_jlab},
            'surl': {'belleii': construct_surl_jlab},
            #'scope': {'belleii': extract_scope_belleii}
           }
