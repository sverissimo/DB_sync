-- Table: public.seguros

DROP TABLE IF EXISTS public.seguros;

CREATE TABLE public.seguros
(
    id smallint NOT NULL DEFAULT nextval('seguro_id_seq'::regclass),
    apolice text varying(25) COLLATE pg_catalog."default",
    seguradora_id smallint,
    data_emissao date,
    vencimento date,
    delegatario_id smallint,
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