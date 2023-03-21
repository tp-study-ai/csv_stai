import sys
import csv

import psycopg2

conn = psycopg2.connect(database="yutfut",
                        host="127.0.0.1",
                        user="yutfut",
                        password="yutfut",
                        port="5432")

csv.field_size_limit(sys.maxsize)
cursor = conn.cursor()


def print_hi(a):
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # print(a)
    # print(len(a))
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if len(a) == 2:
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return ["null"]
    che = []
    key_string = ""

    i = 0
    while True:
        if a[i] == "]":
            break
        if a[i] == '"':
            i += 1
            while True:
                if a[i] == "\\":
                    i += 2
                    continue
                if a[i] == '"':
                    che.append(key_string)
                    key_string = ""
                    i += 1
                    break
                key_string += a[i]
                i += 1
        if a[i] == "[":
            i += 1
            continue
        if a[i] == ":":
            i += 1
            continue
        if a[i] == ",":
            i += 1
            continue
        if a[i] == "\n":
            i += 1
            continue

        if a[i] == " ":
            if key_string != "":
                che.append(key_string)
                key_string = ""
            i += 1
            continue

        key_string += a[i]
        i += 1
        if i >= len(a):
            break
    return che


data = []

with open('new_file3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(
            [
                row[1],
                row[2],
                row[3],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
                row[11],
                row[12],
                row[13],
                row[14],
                row[15],
                row[16],
                row[17],
                row[18]
            ]
        )

for item in data:
    if item == data[0]:
        continue
    # print(item[2])
    # print(print_hi(item[2]))
    # if len(item[2]) == 0:
    #     item[2] == ""
    cursor.execute(
    '''INSERT INTO task (name, description, public_tests, difficulty, cf_contest_id, cf_index, cf_points, cf_rating, cf_tags, time_limit, memory_limit_bytes, link, task_ru, input, output, note) VALUES(E'{0}', E'{1}', ARRAY{2}, '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', E'{12}', E'{13}', E'{14}', E'{15}');'''.format(
        item[0].replace("'", r"\'"), item[1].replace('\\', r"\\").replace("'", r"\'"), print_hi(item[2]), item[3], item[4], item[5],
        item[6], item[7], str(item[8].replace("'", "")), item[9], item[10], item[11], item[12].replace('\\', r"\\").replace("'", r"\'"), item[13].replace('\\', r"\\").replace("'", r"\'"), item[14].replace('\\', r"\\").replace("'", r"\'"), item[15].replace('\\', r"\\").replace("'", r"\'")))
    conn.commit()

# [intput: "example" output: "example", intput: "example" output: "example"]
# ['intput', 'example', 'output']

# f = open('init_db/init.sql', 'w')
# for item in data:
#     f.write(
#         f'("{item[0]}", "{item[1]}", ARRAY"{print_hi(item[2])}", "{item[3]}", "{item[4]}", "{item[5]}", "{item[6]}", "{item[7]}", "{item[8]}", "{item[9]}", "{item[10]}", "{item[11]}"),\n')

# SET timezone TO '+03';
#
# create table task
# (
#     id integer,
#     name text,
#     description text,
#     public_tests text[],
#     difficulty text,
#     cf_contest_id text,
#     cf_index text,
#     cf_points text,
#     cf_rating text,
#     cf_tags text,
#     time_limit text,
#     memory_limit_bytes text,
#     link text
# );
#
# INSERT INTO task (name, description, public_tests, difficulty, cf_contest_id, cf_index, cf_points, cf_rating, cf_tags, time_limit, memory_limit_bytes, link) VALUES


# DROP TABLE IF EXISTS task CASCADE;
#
# SET timezone TO '+03';
#
# create table task
# (
#     id integer,
#     name string,
#     description string,
#     public_tests string,
#     private_tests string,
#     generated_tests string,
#     difficulty string,
#     cf_contest_id string,
#     cf_index string,
#     cf_points string,
#     cf_rating string,
#     cf_tags string,
#     time_limit string,
#     memory_limit_bytes string,
#     link string
# );

# SET timezone TO '+03';
#
# create table task
# (
#     id SERIAL PRIMARY KEY,
#     name text,
#     description text,
#     public_tests text[],
#     difficulty text,
#     cf_contest_id text,
#     cf_index text,
#     cf_points text,
#     cf_rating text,
#     cf_tags text,
#     time_limit text,
#     memory_limit_bytes text,
#     link text
# );

    # task_ru text,
    # input text,
    # output text,
    # note text