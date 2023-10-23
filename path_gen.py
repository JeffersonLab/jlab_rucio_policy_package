def construct_surl_jlab(dsn: str, scope: str, filename: str) -> str:
    """
    Defines relative SURL for new replicas. This method
    contains DQ2 convention. To be used for non-deterministic sites.

    @return: relative SURL for new replica.
    @rtype: str
    """

    fields = dsn.split("/")
    nfields = len(fields)
    if nfields == 0:
        return '/other/%s' % (filename)
    else:
        return '%s/%s' % (dsn, filename)
