contacts = {
    "number": 4,
    "students": [
        {'name': 'Dane Hermansen', 'email': 'dane@example.com'},
        {'name': 'Hermione', 'email': 'hermione@example.com'},
        {'name': 'Ron', 'email': 'ron@example.com'},
        {'name': 'Harry Potter', 'email': 'harry@example.com'},
    ]
    
}
for student in contacts["students"]:
    print(student['email'])