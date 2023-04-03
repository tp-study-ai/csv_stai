import sys
import csv

import psycopg2

conn = psycopg2.connect(database="yutfut",
                        host="127.0.0.1",
                        user="yutfut",
                        password="yutfut",
                        port="5432")

cursor = conn.cursor()


# def parse_tests(a):
#     a = a.replace('[', "").replace(']', "")
#     a = a.split(" ")
#     che = []
#     for i in range(len(a)):
#         if a[i] == '' or a[i] == ',':
#             continue
#         if a[i] == "input:":
#             a[i] = a[i].replace("input:", "input")
#             che.append(a[i])
#             continue
#         if a[i] == "output:":
#             a[i] = a[i].replace("output:", "output")
#             che.append(a[i])
#             continue
#         a[i] = a[i][:len(a[i])-1]
#         a[i] = a[i].replace('"', '')
#         che.append(a[i])
#     return che

# def parse_tests(a):
#     # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     # print(a)
#     # print(len(a))
#     # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     if len(a) == 2:
#         # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         return ["null"]
#     che = []
#     key_string = ""
#
#     i = 0
#     while True:
#         if a[i] == "]":
#             break
#         if a[i] == '"':
#             i += 1
#             while True:
#                 if a[i] == "\\":
#                     i += 2
#                     continue
#                 if a[i] == '"':
#                     che.append(key_string)
#                     key_string = ""
#                     i += 1
#                     break
#                 key_string += a[i]
#                 i += 1
#         if a[i] == "[":
#             i += 1
#             continue
#         if a[i] == ":":
#             i += 1
#             continue
#         if a[i] == ",":
#             i += 1
#             continue
#         if a[i] == "\n":
#             i += 1
#             continue
#
#         if a[i] == " ":
#             if key_string != "":
#                 che.append(key_string)
#                 key_string = ""
#             i += 1
#             continue
#
#         key_string += a[i]
#         i += 1
#         if i >= len(a):
#             break
#     return che

# def parse_tests(text):
#     text = text[1:len(text)-1]
#     che = []
#     while(True):
#         input = text[0:5] # отрезали input
#         che.append(input) # положили input в лист
#         text = text[8:] # убрали input
#         pos = text.find("output:")
#         input_case = text[:pos-6]
#         che.append(input_case)
#
#         text = text[pos:]
#         output = text[:6]
#         che.append(output)
#
#         text = text[9:]
#         pos = text.find("input:")
#         if pos == -1:
#             # print(che)
#             # print(text)
#             pos = text.find('"')
#             output_case = text[:pos]
#             che.append(output_case)
#             # print(che)
#             return che
#         output_case = text[:pos - 8]
#         che.append(output_case)
#         # print(che)
#         text = text[pos:]

# def parse_tests(text):
#     text = text[1:len(text) - 1]
#     che = []
#     while (True):
#         input = text[0:5]  # отрезали input
#         # che.append(input)  # положили input в лист
#         text = text[8:]  # убрали input
#         pos = text.find("output:")
#         input_case = text[:pos - 6]
#         # che.append(input_case)
#
#         text = text[pos:]
#         output = text[:6]
#         # che.append(output)
#
#         text = text[9:]
#         pos = text.find("input:")
#         if pos == -1:
#             pos = text.find('"')
#             output_case = text[:pos]
#             # che.append(output_case)
#             if input_case.find("'") == -1 and output_case.find("'") == -1:
#                 che.append(input)
#                 che.append(input_case)
#                 che.append(output)
#                 che.append(output_case)
#             if len(che) == 0:
#                 return ["NULL"]
#             return che
#         output_case = text[:pos - 8]
#         # che.append(output_case)
#         text = text[pos:]
#         if input_case.find("'") == -1 and output_case.find("'") == -1:
#             che.append(input)
#             che.append(input_case)
#             che.append(output)
#             che.append(output_case)
#         else:
#             # print(input_case)
#             # print(output_case)
#             continue

def parse_tests(text):
    text = text[1:len(text) - 1]
    che = []
    while (True):
        input = text[0:5]  # отрезали input
        # che.append(input)  # положили input в лист
        text = text[8:]  # убрали input
        pos = text.find('output: "')
        input_case = text[:pos-2].replace('\\', r"\\").replace("'", r"\'")

        # che.append(input_case)

        text = text[pos:]
        output = text[:6]
        # che.append(output)

        text = text[9:]
        pos = text.find('input: "')
        if pos == -1:
            pos = text.find('"')
            output_case = text[:pos].replace('\\', r"\\").replace("'", r"\'"),

            if input_case.find("'") == -1 and output_case.find("'") == -1:
                che.append(input)
                che.append(input_case)
                che.append(output)
                che.append(output_case)
            # che.append(input)
            # che.append(input_case)
            # che.append(output)
            # che.append(output_case)
            if len(che) == 0:
                return ["NULL"]
            return che
        output_case = text[:pos-4].replace('\\', r"\\").replace("'", r"\'"),

        text = text[pos:]
        che.append(input)
        che.append(input_case)
        che.append(output)
        che.append(output_case)

        # if input_case.find("'") == -1 and output_case.find("'") == -1:
        #     che.append(input)
        #     che.append(input_case)
        #     che.append(output)
        #     che.append(output_case)
        # else:
        #     # print(input_case)
        #     # print(output_case)
        #     continue

data = []


csv.field_size_limit(sys.maxsize)
with open('new_file3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # print("---------------------------------")
        #
        # print(type(row[4]))
        # print(row[4])
        # print("---------------------------------")
        # abc = dict(row[4])
        # print(abc)
        data.append(
            [
                row[1],  # name
                row[2],  # description
                row[3],  # public_tests
                row[4],  # private_tests
                row[5],  # generated_tests
                row[6],  # difficulty
                row[7],  # cf_contest_id
                row[8],  # cf_index
                row[9],  # cf_points
                row[10],  # cf_rating
                row[11],  # cf_tags
                row[12],  # time_limit
                row[13],  # memory_limit_bytes
                row[14],  # link
                row[15],  # task_ru
                row[16],  # input
                row[17],  # output
                row[18]  # note
            ]
        )
        # if i == 50:
        #     break

print("first")

i = 0

for item in data:
    if item == data[0]:
        continue
    if len(item[10]):
        item[10] = ["NULL"]
    # print("---------------------------------")
    # print(item[2])
    # print(parse_tests(item[2]))
    # print(item[3])
    # print(parse_tests(item[3]))
    # print(item[4])
    # print(parse_tests(item[4]))
    # print("---------------------------------")

    cursor.execute(
        '''INSERT INTO tasks (
        name,
        description,
        public_tests,
        private_tests,
        generated_tests,
        difficulty,
        cf_contest_id,
        cf_index,
        cf_points,
        cf_rating,
        cf_tags,
        time_limit,
        memory_limit_bytes,
        link,
        task_ru,
        input,
        output,
        note
        ) VALUES (
        E'{0}',
        E'{1}',
        ARRAY{2},
        ARRAY{3},
        ARRAY{4},
        '{5}',
        {6},
        '{7}',
        '{8}',
        '{9}',
        ARRAY{10},
        '{11}',
        '{12}',
        '{13}',
        E'{14}',
        E'{15}',
        E'{16}',
        E'{17}'
        );'''.format(
            item[0].replace("'", r"\'"),
            item[1].replace('\\', r"\\").replace("'", r"\'"),
            parse_tests(item[2]),
            parse_tests(item[3]),
            parse_tests(item[4]),
            item[5],
            item[6],
            item[7],
            item[8],
            item[9],
            item[10],
            # str(item[10].replace("'", "")),
            item[11],
            item[12],
            item[13],
            item[14].replace('\\', r"\\").replace("'", r"\'"),
            item[15].replace('\\', r"\\").replace("'", r"\'"),
            item[16].replace('\\', r"\\").replace("'", r"\'"),
            item[17].replace('\\', r"\\").replace("'", r"\'")))
    conn.commit()

print("end!")

# [intput: "example" output: "example", intput: "example" output: "example"]
# ['intput', 'example', 'output']

# i = 0
#
# f = open('../init_db/init.sql', 'w')
# for item in data:
#     if item == data[0]:
#         continue
#     i += 1
#     f.write(
#         '''(E'{0}', E'{1}', 'ARRAY{2}', 'ARRAY'{3}', ARRAY'{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', E'{14}', E'{15}', E'{16}', E'{17}'),\n'''.format(
#         item[0].replace("'", r"\'"), item[1].replace('\\', r"\\").replace("'", r"\'"), print_hi(item[2]), print_hi(item[3]), print_hi(item[4]), item[5], item[6], item[7],
#         item[8], item[9], str(item[10].replace("'", "")), item[11], item[12], item[13], item[14].replace('\\', r"\\").replace("'", r"\'"), item[15].replace('\\', r"\\").replace("'", r"\'"), item[16].replace('\\', r"\\").replace("'", r"\'"), item[17].replace('\\', r"\\").replace("'", r"\'")
#         )
#     )
#     if i == 10:
#         break

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
#     link text,
#     task_ru text,
#     input text,
#     output text,
#     note text
# );
