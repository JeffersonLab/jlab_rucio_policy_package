import hashlib

def lfn2pfn_jlab(scope, name, rse, rse_attrs, protocol_attrs):
    """
    Given a LFN, convert it directly to a path using the mapping:
        path -> path
    using a determinitic function, to choose what.
    (example here is hash(default)
    :param scope: Scope of the LFN.
    :param name: File name of the LFN.
    :param rse: RSE for PFN (ignored)
    :param rse_attrs: RSE attributes for PFN (ignored)
    :param protocol_attrs: RSE protocol attributes for PFN (ignored)
    :returns: Path for use in the PFN generation.
    """
    del rse
    del rse_attrs
    del protocol_attrs
    hstr = hashlib.md5(('%s:%s' % (scope, name)).encode('utf-8')).hexdigest()
    if scope.startswith('user') or scope.startswith('group'):
        scope = scope.replace('.', '/')
    return '%s/%s/%s/%s' % (scope, hstr[0:2], hstr[2:4], name)
