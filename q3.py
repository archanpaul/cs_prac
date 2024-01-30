# 3. Write menu driven python program to perform the following operations into cvs file books.csv
#    1) Add a new book 2) Show all books 3) Delete a book 4) Exit

import csv


def add_new_book(file_name):
    with open(file_name, 'a', newline='') as file:
        csvwriter = csv.writer(file)
        book_name = input("Enter book_name: ")
        book_author = input("Enter book_author: ")
        csvwriter.writerow([book_name, book_author])


def show_all_books(file_name):
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)


def delete_book(file_name):
    book_name = input("Enter book for deletion: ")

    # Read all rows excluding rows matching book_name
    data = []
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] != book_name:
                data.append(row)

    # Write data into csv
    with open(file_name, 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(data)


def mainmenu():
    file_name = "./book.csv"

    while True:
        print("\nChoices available:")
        print("1. Add New Book")
        print("2. Show All Books")
        print("3. Delete a Book")
        print("4: Exit")
        choice = int(input("Enter choice:"))

        if choice == 1:
            add_new_book(file_name)
        elif choice == 2:
            show_all_books(file_name)
        elif choice == 3:
            delete_book(file_name)
        elif choice == 4:
            print("\nExiting...")
            break


mainmenu()
