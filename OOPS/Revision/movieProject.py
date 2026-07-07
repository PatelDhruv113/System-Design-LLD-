class Movie:

    def __init__(self, movie_name: str, total_seats: int, ticket_price: int):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_tickets(self, num_of_tickets: int):

        if num_of_tickets > self.total_seats - self.booked_seats:
            print("Sorry, not enough seats available")
        else:
            self.booked_seats += num_of_tickets
            self.total_seats -= num_of_tickets
            print(f"Your ticket is booked")
            print(f"Total price = {self.ticket_price * num_of_tickets}\n")
            print(f"Total booked={self.booked_seats}\n") 

    def show_status(self) -> None:
        print(f"Movie name={self.movie_name}")
        print(f"Seats available={self.total_seats}")

movie = Movie("Dhruv", 100, 49)
movie.show_status()
movie.book_tickets(70)