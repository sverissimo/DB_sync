-- Table: public.procuracoes

CREATE SEQUENCE IF NOT EXISTS procuracoes_id_seq as SMALLINT
START 1;

ALTER SEQUENCE procuracoes_id_seq RESTART WITH 1;

DROP TABLE IF EXISTS public.procuracoes;
CREATE TABLE public.procuracoes
(
    procuracao_id smallint NOT NULL DEFAULT nextval('procuracoes_id_seq'::regclass),
    codigo_empresa integer,
    status text COLLATE pg_catalog."default",
    vencimento date,
    procuradores jsonb,
    created_at timestamp with time zone DEFAULT now(),
    CONSTRAINT procuracao_pkey PRIMARY KEY (procuracao_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.procuracoes
    OWNER to svom;