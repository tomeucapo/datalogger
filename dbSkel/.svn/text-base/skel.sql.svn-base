/*
   Definció de la base de dades del Datalogger
   Tomeu Capó 2006 (C)
*/

create table if not exists unitat (
             id         integer primary key autoincrement, 
             telefon    varchar(12), 
             descripcio varchar(40), 
             ubicacio   varchar(78),
             n_serie    varchar(20),
             v_firmware varchar(20)
);

create table if not exists config_entrades (
             id_unitat   integer,
             entrada     integer,
             tipus	 char constraint ERROR_CFG_TIPUS check(tipus in ('A','D')),
             descripcio  varchar(30),

             primary key (id_unitat, entrada, tipus) 
);

create table if not exists historic (
             data_hora     timestamp,
             id_unitat     integer,
             ent_analog_0  numeric,
             ent_analog_1  numeric,
             ent_analog_2  numeric,
             ent_analog_3  numeric,

             primary key (data_hora, id_unitat)
);

create unique index if not exists ndx_node_tlf on unitat (telefon);

create trigger if not exists borra_config before delete on unitat
begin
    delete from config_entrades where id_unitat = old.id;
end;
 
