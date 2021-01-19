-- Table: public.socios

CREATE SEQUENCE IF NOT EXISTS socios_id_seq as SMALLINT
START 1;

ALTER SEQUENCE socios_id_seq RESTART WITH 1;

DROP TABLE IF EXISTS public.socios;

CREATE TABLE public.socios
(
    socio_id smallint NOT NULL DEFAULT nextval('socios_id_seq'::regclass),
    cpf_socio character varying(14) COLLATE pg_catalog."default",
    nome_socio text COLLATE pg_catalog."default",
    codigo_empresa integer,
    email_socio text COLLATE pg_catalog."default",    
    tel_socio character varying(20) COLLATE pg_catalog."default",
    share numeric(5,2),
    empresas text COLLATE pg_catalog."default",
    created_at timestamp with time zone DEFAULT now()    
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.socios
    OWNER to svom;