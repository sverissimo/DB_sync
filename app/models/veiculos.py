from utils.format_placa import format_placa
from utils.get_mercosul_plate import get_mercosul_plate


file_names = {"xls_file": "ConsultaVeiculos.xls", "sql_file": "veiculos.sql"}

# Esse tem além do Postgres: sipro, obs
# Aquém do Postgres: id, indicador_idade, acessibilidade_id
# Convertidos: equipamentos_id, codigo_empresa, modelo_carroceria_id, modelo_chassi_id, delegatario_compartilhado_id
fields = [
    ("Placa", "placa"),
    ("RENAVAM", "renavam"),
    ("Data de Registro", "data_registro"),
    ("Utilização", "utilizacao"),
    ("Delegatário", "delegatario"),
    ("Código", "codigo_empresa"),
    ("Situação", "situacao"),
    ("Leasing", "dominio"),
    ("Apólice", "apolice"),
    ("Empresas autorizadas a compartilhar", "delegatario_compartilhado"),
    ("Poltronas", "poltronas"),
    ("Eixos", "eixos"),
    ("PBT", "pbt"),
    ("Modelo chassi", "modelo_chassi"),
    ("Ano chassi", "ano_chassi"),
    ("Número chassi", "n_chassi"),
    ("Valor Chassi", "valor_chassi"),
    ("Modelo carroceria", "modelo_carroceria"),
    ("Ano carroceria", "ano_carroceria"),
    ("Valor carroceria", "valor_carroceria"),
    ("SIPRO", "sipro"),
    ("Cilindros", "cilindros"),
    ("Potência", "potencia"),
    ("Piques Poltrona", "piques_poltrona"),
    ("Dist. Minima", "distancia_minima"),
    ("Dist. Máxima", "distancia_maxima"),
    ("Peso Dianteiro", "peso_dianteiro"),
    ("Peso Traseiro", "peso_traseiro"),
    ("Cores", "cores"),
    ("Equipamentos", "equipamentos"),
    ("Observação", "obs"),
]

# old_steps = [7, 2, 29, 33]
#non_admin_steps = [4, 3, 3, 25, 29]
steps = [4, 6, 4, 25, 29]


# Converte a string em kg para string em ton
def kg_to_ton(weight):
    kg = weight.replace(".", "")
    kg = int(kg)
    ton = kg / 1000
    ton = str(ton)
    return ton


def formatData(data):
    i = 0
    for d in data:
        if d["placa"][3] != "-":
            d["placa"] = format_placa(d["placa"])
        if d["dominio"] == "Sim":
            d["dominio"] = "Leasing"
        if d["dominio"] == "Não":
            d["dominio"] = "Veículo próprio"
        d["modelo_chassi"] = (
            d["modelo_chassi"]
            .replace("0 500 R eliminar", "0500 R")
            .replace("OF 1722/59 eliminar", "OF-1722/59")
            .replace(" - ", "-")
            .replace("OF 1722", "OF-1722")
            .replace("0500 RS 1836/30 eliminar", "O-500 RS 1836/30")
            .replace("OF - 1722", "OF-1722")
        )

        d["modelo_carroceria"] = d["modelo_carroceria"].upper()

        # Se houver placa mercosul no campo obs, traz direto p cá
        new_plate = get_mercosul_plate(d["obs"])

        # Altera kg para tonelada em pesodianteiro/traseiro e pbt
        for key in d:
            if key == "peso_dianteiro" or key == "peso_traseiro" or key == "pbt":
                d[key] = kg_to_ton(d[key])

        # Acrescenta placa antiga na observação e atualiza a placa do veículo.
        if new_plate:
            ob = d["obs"]
            old_plate = d["placa"]
            d["obs"] = f"{ob}. Placa fictícia: {old_plate}"
            d["placa"] = new_plate
            i += 1
            """
            if i < 10:
                print(d)
            """
    print(" veiculos data parsed. " + str(i) + " new plates added.")
    return data
