-- Table: public.laudos

DROP TABLE IF EXISTS public.laudos;

CREATE TABLE public.laudos
(
    id character varying(30) COLLATE pg_catalog."default" NOT NULL,
    validade date,
    empresa_id smallint,
    codigo_empresa integer,
    veiculo_id integer,
    created_at timestamp with time zone DEFAULT now()
    --CONSTRAINT laudos_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.laudos
    OWNER to svom;