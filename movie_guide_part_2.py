# Erick Hofer
# CIS261
# Movie Guide Part 2
filename = "movies.txt"
def write_movies():
    with open(filename, "w") as file:
        while True:
            title = input("Enter the movie title (or 'done' to finish): ")
            if title.lower() == 'done':
                break
            rating = input("Enter the movie rating: ")
            file.write(f"{title},{rating}\n")
def read_movies():
    movies = []
    with open(filename, "r") as file:
        for line in file:
            title, rating = line.strip().split(",")
            movies.append((title, rating))
    return movies
def display_movies(movies):
    print("\nMovie List:")
    for title, rating in movies:
        print(f"{title} - Rating: {rating}")
def add_movie(movies):
    title = input("Enter the movie title: ")
    rating = input("Enter the movie rating: ")
    movies.append((title, rating))
    with open(filename, "a") as file:
        file.write(f"{title},{rating}\n")
def delete_movie(movies):
    title = input("Enter the movie title to delete: ")
    movies = [movie for movie in movies if movie[0].lower() != title.lower()]
    with open(filename, "w") as file:
        for title, rating in movies:
            file.write(f"{title},{rating}\n")
    return movies
def display_menu():
    print("="*50)
    print("\nMovie Guide Menu:")
    print("="*50)
    print("1. List all movies")
    print("2. Add a movie")
    print("3. Delete a movie")
    print("4. Exit")
    print("="*50)
def main():
    write_movies()
    movies = read_movies()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            display_movies(movies)
        elif choice == '2':
            add_movie(movies)
        elif choice == '3':
            movies = delete_movie(movies)
        elif choice == '4':
            print("Exiting the Movie Guide. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()