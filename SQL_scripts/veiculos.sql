-- Table: public.veiculos

-- DROP TABLE public.veiculos;

CREATE TABLE public.veiculos
(
    veiculo_id integer NOT NULL DEFAULT nextval('veiculo_veiculo_id_seq'::regclass),
    placa character varying(8) COLLATE pg_catalog."default",
    renavam character varying(11) COLLATE pg_catalog."default",
    data_registro timestamp(4) with time zone DEFAULT now(),
    utilizacao character varying(25) COLLATE pg_catalog."default",
    dominio character varying(20) COLLATE pg_catalog."default",
    apolice character varying(25) COLLATE pg_catalog."default",
    poltronas smallint,
    eixos smallint,
    pbt character varying(11) COLLATE pg_catalog."default",
    ano_chassi smallint,
    n_chassi character varying(25) COLLATE pg_catalog."default",
    valor_chassi character varying(20) COLLATE pg_catalog."default",
    situacao text COLLATE pg_catalog."default",
    indicador_idade_old smallint,
    ano_carroceria smallint,
    valor_carroceria character varying(20) COLLATE pg_catalog."default",
    piques_poltrona smallint,
    distancia_minima smallint,
    distancia_maxima smallint,
    peso_dianteiro character varying(5) COLLATE pg_catalog."default",
    peso_traseiro character varying(10) COLLATE pg_catalog."default",
    cores character varying(50) COLLATE pg_catalog."default",
    equipamentos_id character varying(400) COLLATE pg_catalog."default",
    delegatario_id smallint,
    pneumaticos smallint,
    cilindros smallint,
    potencia smallint,
    modelo_chassi_id smallint,
    modelo_carroceria_id smallint,
    delegatario_compartilhado smallint,
    equipa smallint[],
    acessibilidade_id smallint[],
    CONSTRAINT veiculo_pkey PRIMARY KEY (veiculo_id),
    CONSTRAINT delegatario FOREIGN KEY (delegatario_id)
        REFERENCES public.delegatario (delegatario_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
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

CREATE INDEX placa_index
    ON public.veiculos USING btree
    (placa COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;