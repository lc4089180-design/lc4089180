#Write a MovieTicket class that takes movie_name, seat_number, and price as properties. Add a method apply_discount(percent) that reduces the price by the given percent and prints the new price.<br><br><em><strong>Hint:</strong> Use self.price to update the price inside the method.</em>
class MovieTicket:
    def __init__(self, movie_name, seat_number, price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * percent / 100
        self.price = self.price - discount
        print("New ticket price:", self.price)


ticket = MovieTicket("Jawan", "A10", 500)

ticket.apply_discount(20)