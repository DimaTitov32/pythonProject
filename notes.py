import os
import json
from datetime import datetime

def create_new_file():
  """Функция для создания новой заметки"""
  note_id = input("Введите идентификатор заметки: ")
  filename = f"{note_id}.json"
  if os.path.exists(filename):
    print("Заметка с таким идентификатором уже существует.")
  else:
    note_title = input("Введите заголовок заметки: ")
    note_body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
      "id": note_id,
      "title": note_title,
      "body": note_body,
      "created_timestamp": timestamp,
      "modified_timestamp": timestamp
    }
    with open(filename, "w") as file:
      json.dump(note, file)
    print(f"Заметка с идентификатором {note_id} успешно создана.")

def add_to_file():
  """Функция для добавления текста в заметку"""
  note_id = input("Введите идентификатор заметки: ")
  filename = f"{note_id}.json"
  if os.path.exists(filename):
    with open(filename, "r") as file:
      note = json.load(file)
    print(f"Текущий текст заметки:\n{note['body']}")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_text = input("Введите текст для добавления: ")
    note["body"] += f"\n{new_text}"
    note["modified_timestamp"] = timestamp
    with open(filename, "w") as file:
      json.dump(note, file)
    print(f"Текст успешно добавлен в заметку с идентификатором {note_id}.")
  else:
    print("Заметка с таким идентификатором не существует.")

def read_file():
  """Функция для чтения содержимого заметки"""
  note_id = input("Введите идентификатор заметки: ")
  filename = f"{note_id}.json"
  if os.path.exists(filename):
    with open(filename, "r") as file:
      note = json.load(file)
      print(f"Заголовок заметки: {note['title']}")
      print(f"Текст заметки:\n{note['body']}")
      print(f"Дата создания заметки: {note['created_timestamp']}")
      print(f"Дата последнего изменения заметки: {note['modified_timestamp']}")
  else:
    print("Заметка с таким идентификатором не существует.")

def edit_file():
  """Функция для редактирования заметки"""
  note_id = input("Введите идентификатор заметки: ")
  filename = f"{note_id}.json"
  if os.path.exists(filename):
    with open(filename, "r") as file:
      note = json.load(file)
      print(f"Текущий текст заметки:\n{note['body']}")
      line_number = int(input("Введите номер строки, которую нужно отредактировать: "))
      lines = note["body"].split("\n")
      if line_number > len(lines):
        print("Номер строки вне диапазона.")
      else:
        new_text = input("Введите новый текст: ")
        lines[line_number-1] = new_text
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note["body"] = "\n".join(lines)
        note["modified_timestamp"] = timestamp
        with open(filename, "w") as file:
          json.dump(note, file)
        print(f"Текст успешно изменен в заметке с идентификатором {note_id}.")
  else:
    print("Заметка с таким идентификатором не существует.")

def delete_file():
  """Функция для удаления заметки"""
  note_id = input("Введите идентификатор заметки: ")
  filename = f"{note_id}.json"
  if os.path.exists(filename):
    os.remove(filename)
    print(f"Заметка с идентификатором {note_id} успешно удалена.")
  else:
    print("Заметка с таким идентификатором не существует.")

def start_program():
  """Функция для запуска программы"""
  print("Программа для создания заметок.")
  print("1 - Создать новую заметку")
  print("2 - Добавить текст в заметку")
  print("3 - Читать заметку")
  print("4 - Редактировать заметку")
  print("5 - Удалить заметку")
  print("6 - Выход")
  choice = input("Введите номер действия: ")
  if choice == "1":
    create_new_file()
  elif choice == "2":
    add_to_file()
  elif choice == "3":
    read_file()
  elif choice == "4":
    edit_file()
  elif choice == "5":
    delete_file()
  elif choice == "6":
    exit()
  else:
    print("Некорректный ввод. Попробуйте еще раз.")
    start_program()

start_program()
