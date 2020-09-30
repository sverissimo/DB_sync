-- Table: public.veiculos

DROP TABLE IF EXISTS public.veiculos;

ALTER SEQUENCE veiculo_id_seq RESTART WITH 1;

CREATE TABLE public.veiculos
(
    veiculo_id integer NOT NULL DEFAULT nextval('veiculo_id_seq'::regclass),
    placa character varying(8) COLLATE pg_catalog."default",
    renavam character varying(11) COLLATE pg_catalog."default",
    data_registro timestamp(4) with time zone DEFAULT now(),
    delegatario_id smallint,
    codigo_empresa integer,
    delegatario text COLLATE pg_catalog."default",
    situacao text COLLATE pg_catalog."default",
    utilizacao text COLLATE pg_catalog."default",
    dominio text COLLATE pg_catalog."default",
    apolice text COLLATE pg_catalog."default",
    cilindros smallint,
    potencia smallint,
    n_chassi character varying(25) COLLATE pg_catalog."default",
    ano_chassi smallint,
    valor_chassi character varying(20) COLLATE pg_catalog."default",
    modelo_chassi_id smallint,
    modelo_chassi text COLLATE pg_catalog."default",
    ano_carroceria smallint,
    valor_carroceria character varying(20) COLLATE pg_catalog."default",
    modelo_carroceria_id smallint,
    modelo_carroceria text COLLATE pg_catalog."default",
    poltronas smallint,
    piques_poltrona smallint,
    distancia_minima numeric(9, 2),
    distancia_maxima numeric(9, 2),
    eixos smallint,
    pneumaticos smallint,
    peso_dianteiro character varying(8) COLLATE pg_catalog."default",
    peso_traseiro character varying(10) COLLATE pg_catalog."default",
    pbt character varying(11) COLLATE pg_catalog."default",
    cores text COLLATE pg_catalog."default",
    equipamentos text COLLATE pg_catalog."default",
    delegatario_compartilhado text COLLATE pg_catalog."default",
    compartilhado_id smallint,
    equipamentos_id jsonb,
    acessibilidade_id jsonb,
    sipro text COLLATE pg_catalog."default",    
    obs text COLLATE pg_catalog."default",
    CONSTRAINT veiculos_pkey PRIMARY KEY (veiculo_id),
    /* CONSTRAINT delegatario_id FOREIGN KEY (delegatario_id)
        REFERENCES public.empresas (delegatario_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID, */
    CONSTRAINT modelo_carroceria FOREIGN KEY (modelo_carroceria_id)
        REFERENCES public.modelo_carroceria (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT modelo_chassi FOREIGN KEY (modelo_chassi_id)
        REFERENCES public.modelo_chassi (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.veiculos
    OWNER to svom;

-- Index: placa_index

-- DROP INDEX public.placa_index;

CREATE INDEX placaZ_index
    ON public.veiculos USING btree
    (placa COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;