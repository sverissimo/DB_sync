import re


def get_mercosul_plate(obs):
    if not obs or obs == '':
        return False

    has_mercosul_plate = re.search('Placa Oficial: ', obs)

    if has_mercosul_plate:
        index_tuple = has_mercosul_plate.span()
        init = index_tuple[1]
        end = init+8
        placa = obs[init: end]
        placa = placa.replace(' ', '-')
        print(placa)
        return placa
    else:
        return False
