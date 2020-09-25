-- Table: public.laudos

DROP TABLE IF EXISTS public.laudo;

CREATE TABLE public.laudo
(
    id character varying(30) COLLATE pg_catalog."default" NOT NULL,
    validade date,
    empresa_id smallint,
    veiculo_id integer,
    created_at timestamp with time zone DEFAULT now(),
    CONSTRAINT laudo_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.laudos
    OWNER to svom;