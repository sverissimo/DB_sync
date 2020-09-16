from entities.empresas import fields


def field_conversor(f):
    for i, j in fields:
        if(f == i):
            return j
