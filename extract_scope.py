import fnmatch

def extract_scope_jlab(did, scopes):
    split_did = did.split('/')
    if did.startswith("/mss/clas12"):
        if len(split_did) > 4:
            if split_did[4].find("data") > -1:
                scope = "hallb.clas12.raw"
                return scope, did
        scope  = "hallb.clas12"
        return scope, did

    if did.startswith("/mss/halld"):
        if fnmatch.fnmatch(did,"mss.halld.RunPeriod*.rawdata*"):
            scope = "halld.gluex.raw"
            return scope, did
        if did.startswith("mss.halld"):
            scope = "halld.gluex"
            return scope, did
              
    if did.startswith("/mss/halla/sbs"):
        if len(split_did) > 5:
            if split_did[5].find('raw') > -1:
                scope = split_did[2] + "." + split_did[3] + "." + split_did[4] + ".raw"
                return scope, did
            scope =  "hallb.sbs." + split_did[4]
            return scope, did

    if did.startswith("/mss/hall"):
            if len(split_did) > 4:
                if split_did[5].find('raw') > -1:
                    scope = split_did[2] + "." + split_did[3] + ".raw"
                    return scope, did
            scope = split_did[2] + "." + split_did[3]
            return scope, did
    scope = 'jlab'
    return scope, did