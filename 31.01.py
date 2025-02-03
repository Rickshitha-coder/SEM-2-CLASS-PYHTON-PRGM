class MovieTicketBooking:
    def __init__(self):
        self.seats = {
            'A': 20,
            'B': 19,
            'C': 18,
            'D': 17,
            'E': 16,
            'F': 15,
            'G': 14,
            'H': 13,
            'I': 12,
            'J': 11,
            'K': 10,
            'L': 9,
            'M': 8,
            'N': 7,
            'O': 6,
            'P': 5,
            'Q': 4,
            'R': 3,
            'S': 2,
            'T': 1,
            'U': 0,
            'V': 0,
            'W': 0,
            'X': 0,
            'Y': 0,
            'Z': 0
        }
        self.prices = {
            'First Class': {'rows': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'price': 200},
            'Second Class': {'rows': ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'], 'price': 150},
            'Economic Class': {'rows': ['Y', 'Z'], 'price': 50}
        }
        self.snacks = {
            'Popcorn': 100,
            'Ice Cream': 80,
            'Puffs': 60,
            'Tea': 40,
            'Soft Drinks': 50
        }

    def display_seats(self):
        print("Available Seats:")
        for row, cols in self.seats.items():
            print(f"{row}: {cols}")

    def book_seats(self):
        name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        date_of_birth = input("Enter your date of birth: ")
        num_seats = int(input("Enter the number of seats: "))
        self.display_seats()
        seat_selection = input("Select your seats (e.g., A2-A6): ")
        seat_range = seat_selection.split('-')
        start_seat = seat_range[0]
        end_seat = seat_range[1]
        start_row = start_seat[0]
        start_col = int(start_seat[1:])
        end_row = end_seat[0]
        end_col = int(end_seat[1:])
        total_price = 0
        for row in range(ord(start_row), ord(end_row) + 1):
            row_char = chr(row)
            for col in range(start_col, end_col + 1):
                if self.seats[row_char] >= col:
                    self.seats[row_char] -= 1
                    for category, details in self.prices.items():
                        if row_char in details['rows']:
                            total_price += details['price']
                        print("Your Booking Price is :",total_price)
                        break
                else:
                    print("Sorry, some seats are not available.")
                    return
        snack_selection = input("Do you want snacks? (Yes/No): ")
        if snack_selection.lower() == 'yes':
            print("Snacks Menu:")
            for snack, price in self.snacks.items():
                print(f"{snack}: {price}")
            snack_choice = input("Enter your snack choice: ")
            num_snacks = int(input("Enter the number of snacks: "))
            snack_price = self.snacks[snack_choice] * num_snacks
            print("Your Snack Price is :",snack_price)
            total_price += snack_price
            
        print(f"Hi {name}, you have successfully booked {num_seats} tickets.")
        print(f"Seats: {seat_selection}")
        print(f"Total price: {total_price}")

if __name__ == "__main__":
    booking = MovieTicketBooking()
    booking.book_seats()


