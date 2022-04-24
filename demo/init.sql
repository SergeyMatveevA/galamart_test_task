create table post (
    id serial,
    title varchar(255) not null,
    body text,
    jsonb_field jsonb
);

insert into post (title, body, jsonb_field) values (
'first_row',
'It is test task',
'{ "data":[ {"empry_text": "", "non_empty_text": "dgfnjhsgf"} , {"interger": 4456, "bool": true} ] }'
);