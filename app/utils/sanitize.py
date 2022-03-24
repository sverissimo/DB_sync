def sanitize_value(value):
    # Sanitize dos strings de nome de seguradora padronizando/trim e evitando caracteres especiais
    value = (
        value.strip().replace("S/A", "S.A.").replace("SA", "S.A.").replace("'", "''")
    )
    new_value = " ".join(value.split())
    return new_value
