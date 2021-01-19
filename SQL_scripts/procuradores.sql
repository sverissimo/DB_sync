-- Table: public.procuradores

-- DROP TABLE IF EXISTS public.procuradores;

CREATE SEQUENCE IF NOT EXISTS procuradores_id_seq as SMALLINT
START 1;

ALTER SEQUENCE procuradores_id_seq RESTART WITH 1;

CREATE TABLE public.procuradores
(
    procurador_id smallint NOT NULL DEFAULT nextval('procuradores_id_seq'::regclass),
    nome_procurador text COLLATE pg_catalog."default",
    email_procurador text COLLATE pg_catalog."default",
    tel_procurador character varying(20) COLLATE pg_catalog."default",
    cpf_procurador character varying(14) COLLATE pg_catalog."default",
    empresas integer[],
    created_at timestamp with time zone DEFAULT now(),
    CONSTRAINT procurador_pkey PRIMARY KEY (procurador_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.procuradores
    OWNER to svom;