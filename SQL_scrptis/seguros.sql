-- Table: public.seguros

-- DROP TABLE public.seguros;

CREATE TABLE public.seguros
(
    id smallint NOT NULL DEFAULT nextval('seguro_id_seq'::regclass),
    apolice character varying(25) COLLATE pg_catalog."default",
    seguradora_id smallint,
    data_emissao date,
    vencimento date,
    delegatario_id smallint,
    created_at timestamp(4) with time zone DEFAULT now(),
    situacao text COLLATE pg_catalog."default",
    CONSTRAINT seguro_pk PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.seguros
    OWNER to postgres;

-- Index: apolice_index

DROP INDEX public.apolice_index;

CREATE INDEX apolice_index
    ON public.seguros USING btree
    (apolice COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;