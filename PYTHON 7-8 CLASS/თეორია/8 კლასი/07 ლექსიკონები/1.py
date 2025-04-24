# students = {
#   "students": [
#     {"id": 1, "name": "Paata", "age": 24},
#     {"id": 2, "name": "Nika", "age": 20},
#     {"id": 3, "name": "Lasha", "age": 21},
#   ],
#   "grades": [
#     {"Paata": "B"},
#     {"Nika": "A"},
#     {"Lasha": "C"},
#   ]
# }

# nika_grade = students["grades"]
# print(nika_grade)

# nika_grade = students["grades"][1]
# print(nika_grade)

# nika_grade = students["grades"][1]['Nika']
# print(nika_grade)


# ==========================================
# Student_id: 3, Name: Lasha, Grade" C

# students = {
#   "students": [
#     {"id": 1, "name": "Paata", "age": 24},
#     {"id": 2, "name": "Nika", "age": 20},
#     {"id": 3, "name": "Lasha", "age": 21},
#   ],
#   "grades": [
#     {"Paata": "B"},
#     {"Nika": "A"},
#     {"Lasha": "C"},
#   ]
# }

# st_id = students["students"][2]['id']
# st_name = students["students"][st_id - 1]['name']
# st_grade = students["grades"][st_id - 1][st_name]

# print(f"Student_id: {st_id}, Name: {st_name}, Grade: {st_grade}")



# ==========================================
# ID: 1, Name: Paata, Grade B
# ID: 2, Name: Nika, Grade A
# ID: 3, Name: Lasha, Grade C

# students = {
#   "students": [
#     {"id": 1, "name": "Paata", "age": 24},
#     {"id": 2, "name": "Nika", "age": 20},
#     {"id": 3, "name": "Lasha", "age": 21},
#   ],
#   "grades": [
#     {"Paata": "B"},
#     {"Nika": "A"},
#     {"Lasha": "C"},
#   ]
# }

# for student in students["students"]:
#   # st_id = student['id']
#   # st_name = student['name']
#   # st_grade = 'Not Available'

#   # for grade in students["grades"]:
#   #   if st_name in grade:
#   #     st_grade = grade[st_name]

#   st_id = student['id']
#   st_name = student['name']
#   st_grade = students["grades"][st_id - 1][st_name]

#   print(f"ID: {st_id}, Name: {st_name}, Grade: {st_grade}")



# =============================
# სხვადასხვა id

# students = {
#   "students": [
#     {"id": 20, "name": "Paata", "age": 24},
#     {"id": 100, "name": "Nika", "age": 20},
#     {"id": 1232, "name": "Lasha", "age": 21},
#   ],
#   "grades": [
#     {"Paata": "B"},
#     {"Nika": "A"},
#     {"Lasha": "C"},
#     {"Archil": "C"},
#     {"Alexandre": "C"},
#   ]
# }

# for student in students["students"]:
#   st_id = student['id']
#   st_name = student['name']
#   st_grade = 'Not Available'

#   for grade in students["grades"]:
#     if st_name in grade:
#       st_grade = grade[st_name]

#   print(f"ID: {st_id}, Name: {st_name}, Grade: {st_grade}")



# ==============================

# students = {
#   "students": [
#     {"id": 20, "name": "Paata", "age": 24},
#     {"id": 100, "name": "Nika", "age": 20},
#     {"id": 1232, "name": "Lasha", "age": 21},
#     {"id": 8564, "name": "Archil", "age": 32},
#   ],
#   "grades": [
#     {"Paata": "B"},
#     {"Nika": "A"},
#     {"lasha": "C"},
#     {"Alexandre": "C"},
#   ]
# }

# for student in students["students"]:
#   st_id = student['id']
#   st_name = student['name']
#   st_grade = 'Not Available'

#   for grade in students["grades"]:
#     if st_name in grade:
#       st_grade = grade[st_name]

#   print(f"ID: {st_id}, Name: {st_name}, Grade: {st_grade}")



# =========================
# ერთი და იგივე სახელების სტუდენტები


# students = {
#   "students": [
#     {"id": 20, "name": "Paata", "age": 24},
#     {"id": 25, "name": "Paata", "age": 21},
#     {"id": 31, "name": "Nika", "age": 22},
#     {"id": 100, "name": "Nika", "age": 20},
#     {"id": 1232, "name": "Lasha", "age": 21},
#     {"id": 8564, "name": "Archil", "age": 32},
#   ],
#   "grades": [
#     {"Paata": "B"},
#     {"Paata": "A"},
#     {"Nika": "A"},
#     {"Nika": "B"},
#     {"Lasha": "C"},
#     {"Alexandre": "C"},
#     {"Archil": "A"},
#   ]
# }

# for student in students["students"]:
#   st_id = student['id']
#   st_name = student['name']
#   st_grade = 'Not Available'

#   for grade in students["grades"]:
#     if st_name in grade:
#       st_grade = grade[st_name]

#   print(f"ID: {st_id}, Name: {st_name}, Grade: {st_grade}")



# =====================

students = {
  "students": [
    {"id": 20, "name": "Paata", "age": 24},
    {"id": 25, "name": "Paata", "age": 21},
    {"id": 31, "name": "Nika", "age": 22},
    {"id": 100, "name": "Nika", "age": 20},
    {"id": 1232, "name": "Lasha", "age": 21},
    {"id": 8564, "name": "Archil", "age": 32},
  ],
  "grades": [
    {"id": 12, "students_id": 20, "Paata": "B"},
    {"id": 187, "students_id": 25, "Paata": "A"},
    {"id": 1281, "students_id": 31, "Nika": "A"},
    {"id": 1369, "students_id": 100, "Nika": "B"},
    {"id": 2014, "students_id": 1232, "Lasha": "C"},
    {"id": 2187, "students_id": 1300, "Alexandre": "A"},
    {"id": 7007, "students_id": 8564, "Archil": "A"},
  ]
}

for student in students["students"]:
  st_id = student['id']
  st_name = student['name']
  st_grade = 'Grade not available'

  for grade in students["grades"]:
    if st_id == grade['students_id']:
      st_grade = grade[st_name]

  print(f"ID: {st_id}, Name: {st_name}, Grade: {st_grade}")