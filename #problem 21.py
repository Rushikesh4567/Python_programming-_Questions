#problem 21
class Movie:
    def __init__(self):
        self.movies = {}

    def add_movie(self, name, rating):
        if 0 <= rating <= 10:
            self.movies[name] = rating
            print(f"Movie '{name}' added with rating {rating}.")
        else:
            print("Invalid rating. Please enter a rating between 0 and 10.")

    def update_rating(self, name, new_rating):
        if name in self.movies:
            if 0 <= new_rating <= 10:
                self.movies[name] = new_rating
                print(f"Rating for '{name}' updated to {new_rating}.")
            else:
                print("Invalid rating. Please enter a rating between 0 and 10.")
        else:
            print(f"Movie '{name}' not found.")

    def display_movies(self):
        if self.movies:
            print("\nDisplay Movie:")
            for name, rating in self.movies.items():
                print(f"{name}: {rating}/10")
        else:
            print("No movies found.")

# Main function
collection = Movie()

while True:
    print("\nMovie  Menu:")
    print("1. Add Movie title")
    print("2. Enter Rating")
    print("3. Display Movies")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter movie name: ")
        genre=input("Enter genre of movie ")
        rating = float(input("Enter movie rating (0-10): "))
        collection.add_movie(name, rating)
    elif choice == "2":
        name = input("Enter movie name: ")
        genre=input("Enter genre of movie ")
        new_rating = float(input("Enter new rating (0-10): "))
        collection.update_rating(name, new_rating)
    elif choice == "3":
        collection.display_movies()
    elif choice == "4":
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
