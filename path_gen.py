def construct_surl_jlab(dsn: str, scope: str, filename: str) -> str:
    """
    Defines relative SURL for new replicas. This method
    contains DQ2 convention. To be used for non-deterministic sites.
    Method imported from DQ2.

    @return: relative SURL for new replica.
    @rtype: str
    """
    # check how many dots in dsn
    fields = dsn.split('.')
    nfields = len(fields)

    if nfields == 0:
        return '/other/other/%s' % (filename)
    elif nfields == 1:
        stripped_dsn = __strip_dsn(dsn)
        return '/other/%s/%s' % (stripped_dsn, filename)
    elif nfields == 2:
        project = fields[0]
        stripped_dsn = __strip_dsn(dsn)
        return '/%s/%s/%s' % (project, stripped_dsn, filename)
    elif nfields < 5 or re.match('user*|group*', fields[0]):
        project = fields[0]
        f2 = fields[1]
        f3 = fields[2]
        stripped_dsn = __strip_dsn(dsn)
        return '/%s/%s/%s/%s/%s' % (project, f2, f3, stripped_dsn, filename)
    else:
        project = fields[0]
        dataset_type = fields[4]
        if nfields == 5:
            tag = 'other'
        else:
            tag = __strip_tag(fields[-1])
        stripped_dsn = __strip_dsn(dsn)
        return '/%s/%s/%s/%s/%s' % (project, dataset_type, tag, stripped_dsn, filename)