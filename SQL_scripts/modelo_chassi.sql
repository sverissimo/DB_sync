-- Table: public.modelo_chassi

-- DROP TABLE public.modelo_chassi;

CREATE TABLE public.modelo_chassi2
(
    id smallint NOT NULL DEFAULT nextval('modelo_chassi_id_seq'::regclass),
    marca_id smallint,
    modelo_chassi character varying(30) COLLATE pg_catalog."default",
	cmt decimal,
    CONSTRAINT "modeloChassi_pk" PRIMARY KEY (id),
    CONSTRAINT "marca_id_fk" FOREIGN KEY (marca_id)
        REFERENCES public.marca_chassi (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.modelo_chassi
    OWNER to svom;