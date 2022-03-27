import json
import csv


def main():
    with open("users.json", "r") as users_file:
        users = json.load(users_file)

    users_required = []
    for user in users:
        temp_dict = {"name": user.get("name"),
                     "gender": user.get("gender"),
                     "address": user.get("address"),
                     "age": user.get("age")}
        users_required.append(temp_dict)

    with open("books.csv", "r") as books_file:
        all_books = [book for book in csv.DictReader(books_file)]

    books_gen = (book for book in all_books)
    user_books = []

    while True:
        try:
            for user in users_required:
                try:
                    user_books = user["books"]
                except KeyError:
                    user["books"] = []
                user_books.append(next(books_gen))
                user["books"] = user_books
                user_books = []
        except StopIteration:
            break

    with open("result.json", "w") as file:
        file.write(json.dumps(users_required, indent=4))


if __name__ == "__main__":
    main()
