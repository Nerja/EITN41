# rsakey.py http://snmplabs.com/pyasn1/example-use-case.html#grab-asn-1-schema-for-ssh-keys

class Version(Integer):
    pass

class RSAPrivateKey(Sequence):
    componentType = NamedTypes(
        NamedType('version', Version()),
        NamedType('modulus', Integer()),
        NamedType('publicExponent', Integer()),
        NamedType('privateExponent', Integer()),
        NamedType('prime1', Integer()),
        NamedType('prime2', Integer()),
        NamedType('exponent1', Integer()),
        NamedType('exponent2', Integer()),
        NamedType('coefficient', Integer())
    )
