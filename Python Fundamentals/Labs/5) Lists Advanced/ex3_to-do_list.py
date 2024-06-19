def process_todo_list():
    todo_notes = []

    while True:
        note = input()
        if note == "End":
            break
        todo_notes.append(note)

    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split("-")[0]))
    return [note.split("-")[1] for note in sorted_notes]


result = process_todo_list()
print(result)
