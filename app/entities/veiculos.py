from get_mercosul_plate import get_mercosul_plate

file_names = {
    'xls_file': 'ConsultaVeiculos.xls',
    'sql_file': 'veiculos.sql'
}

# Esse tem alem do Postgres: sipro, obs
# Aquém do Postgres: id, indicador_idade, acessibildade_id
# Convertidos: equipamentos_id, codigo_empresa, modelo_carroceria_id, modelo_chassi_id, delegatario_compartilhado_id
fields = [
    ('Placa', 'placa'),
    ('RENAVAM', 'renavam'),
    ('Data de Registro', 'data_registro'),
    ('Utilização', 'utilizacao'),
    ('Delegatário', 'delegatario'),
    ('Código', 'codigo_empresa'),
    ('Situação', 'situacao'),
    ('Leasing', 'dominio'),
    ('Apólice', 'apolice'),
    ('Empresas autorizadas a compartilhar', 'delegatario_compartilhado'),
    ('Poltronas', 'poltronas'),
    ('Eixos', 'eixos'),
    ('PBT', 'pbt'),
    ('Modelo chassi', 'modelo_chassi'),
    ('Ano chassi', 'ano_chassi'),
    ('Número chassi', 'n_chassi'),
    ('Valor Chassi', 'valor_chassi'),
    ('Modelo carroceria', 'modelo_carroceria'),
    ('Ano carroceria', 'ano_carroceria'),
    ('Valor carroceria', 'valor_carroceria'),
    ('SIPRO', 'sipro'),
    ('Cilindros', 'cilindros'),
    ('Potência', 'potencia'),
    ('Piques Poltrona', 'piques_poltrona'),
    ('Dist. Minima', 'distancia_minima'),
    ('Dist. Máxima', 'distancia_maxima'),
    ('Peso Dianteiro', 'peso_dianteiro'),
    ('Peso Traseiro', 'peso_traseiro'),
    ('Cores', 'cores'),
    ('Equipamentos', 'equipamentos'),
    ('Observação', 'obs')
]

steps = [7, 2, 29, 33]


def formatData(data):
    i = 0
    for d in data:
        if d['dominio'] == 'Sim':
            d['dominio'] = 'Leasing'
        if d['dominio'] == 'Não':
            d['dominio'] = 'Veículo próprio'
        d['modelo_chassi'] = d['modelo_chassi'].replace('0 500 R eliminar', '0500 R').replace(
            'OF 1722/59 eliminar', 'OF-1722/59').replace(' - ', '-').replace('OF 1722', 'OF-1722').replace(
            '0500 RS 1836/30 eliminar', 'O-500 RS 1836/30')

        d['modelo_carroceria'] = d['modelo_carroceria'].upper()

        # Se houver placa mercosul no campo obs, traz direto p cá
        new_plate = get_mercosul_plate(d['obs'])

        # Acrescenta placa antiga na observação e atualiza a placa do veículo.
        if new_plate:
            ob = d['obs']
            old_plate = d['placa']
            d['obs'] = f'{ob}. Placa fictícia: {old_plate}'
            d['placa'] = new_plate
            i += 1
            """
            if i < 10:
                print(d)
            """
    print('veiculos data parsed. ' + str(i) + ' new plates added.')
    return data
