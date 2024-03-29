-- Table: public.seguros

DROP TABLE IF EXISTS public.seguros;

ALTER SEQUENCE seguro_id_seq RESTART WITH 1;

CREATE TABLE public.seguros
(
    id smallint NOT NULL DEFAULT nextval('seguro_id_seq'::regclass),
    apolice text COLLATE pg_catalog."default",
    seguradora_id smallint,
    data_emissao date,
    vencimento date,    
    codigo_empresa integer,
    created_at timestamp(4) with time zone DEFAULT now(),
    situacao text COLLATE pg_catalog."default",
    CONSTRAINT seguroZ_pk PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.seguros
    OWNER to svom;

-- Index: apolice_index

DROP INDEX IF EXISTS public.apoliceZ_index;

CREATE INDEX apoliceZ_index
    ON public.seguros USING btree
    (apolice COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;