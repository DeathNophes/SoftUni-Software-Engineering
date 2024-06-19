def is_valid(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    win_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for symbol in win_symbols:
        for uninterrupted_length in range(10, 5, -1):
            # We iterate through all possible combinations for a winning ticket for all symbols backwards
            winning_repetition = symbol * uninterrupted_length  # str
            if winning_repetition in left_part and winning_repetition in right_part:    # Winning ticket
                if uninterrupted_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_length}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_length}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]    # We remove the space on left and right
for current_ticket in tickets:
    print(is_valid(current_ticket))
