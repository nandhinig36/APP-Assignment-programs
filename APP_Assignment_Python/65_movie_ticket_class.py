# Q65: Create three movie ticket objects using a constructor.
class MovieTicket:
    def __init__(self, movie_name, theatre, seat_number):
        self.movie_name = movie_name
        self.theatre = theatre
        self.seat_number = seat_number

    def display(self):
        print("Movie name:", self.movie_name)
        print("Theatre:", self.theatre)
        print("Seat number:", self.seat_number)

if __name__ == "__main__":
    ticket1 = MovieTicket("Interstellar", "PVR", "A10")
    ticket2 = MovieTicket("Inception", "INOX", "B12")
    ticket3 = MovieTicket("The Dark Knight", "Cinepolis", "C08")

    print("TICKET 1")
    ticket1.display()
    print("\nTICKET 2")
    ticket2.display()
    print("\nTICKET 3")
    ticket3.display()
