from src.customer.application.models import LottoDraw, Bet
from src.customer.application.winning_classes import winning_classes

def match_bets(lotto_draw: LottoDraw, bets: list[Bet]) -> list[Bet]:
    for bet in bets:
        bet.winning_class = calculate_winning_class(lotto_draw, bet)
    return bets

def calculate_winning_class(lotto_draw: LottoDraw, bet: Bet):
    matching_winning_numbers = len(set(lotto_draw.winning_numbers).intersection(set(bet.winning_numbers)))
    matching_super_number = len(set(lotto_draw.super_number).intersection(set(bet.super_number)))
    return winning_classes.get((matching_winning_numbers, matching_super_number))