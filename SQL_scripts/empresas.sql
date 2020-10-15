-- Table: public.empresas
DROP TABLE IF EXISTS public.empresas;

CREATE TABLE public.empresas
(
    delegatario_id smallserial,
    codigo_empresa integer,
    razao_social text COLLATE pg_catalog."default",
    situacao text COLLATE pg_catalog."default",
    vencimento_contrato date,
    cnpj text COLLATE pg_catalog."default",
    inscricao_estadual text COLLATE pg_catalog."default",
    rua text COLLATE pg_catalog."default",
    cidade text COLLATE pg_catalog."default",
    uf text COLLATE pg_catalog."default",
    telefone text COLLATE pg_catalog."default",
    email text COLLATE pg_catalog."default",
    numero smallint,
    complemento text COLLATE pg_catalog."default",
    bairro text COLLATE pg_catalog."default",
    created_at timestamp with time zone DEFAULT now(),
    cep text COLLATE pg_catalog."default",
    CONSTRAINT empresas_pkey PRIMARY KEY (delegatario_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.empresas
    OWNER to svom;

-- Index: razao_social
DROP INDEX IF EXISTS public.razao_social;

CREATE INDEX razao_social
    ON public.empresas USING btree
    (razao_social COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;