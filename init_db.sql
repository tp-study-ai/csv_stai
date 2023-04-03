SET timezone TO '+03';

create table task
(
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    public_tests text[],
    private_tests text[],
    generated_tests text[],
    difficulty text,
    cf_contest_id text,
    cf_index text,
    cf_points text,
    cf_rating text,
    cf_tags text,
    time_limit text,
    memory_limit_bytes text,
    link text,
    task_ru text,
    input text,
    output text,
    note text
);

SET timezone TO '+03';

create table task
(
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    public_tests text[],
    private_tests text[],
    generated_tests text[],
    difficulty text,
    cf_contest_id text,
    cf_index text,
    cf_points text,
    cf_rating text,
    cf_tags text,
    time_limit text,
    memory_limit_bytes text,
    link text,
    task_ru text,
    input text,
    output text,
    note text
);

INSERT INTO task (name, description, public_tests, private_tests, generated_tests, difficulty, cf_contest_id, cf_index, cf_points, cf_rating, cf_tags, time_limit, memory_limit_bytes, link, task_ru, input, output, note) VALUES