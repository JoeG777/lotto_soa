import pytest

from src.customer.application.models import LottoDraw, Bet
from src.customer.application.bets_matcher import calculate_winning_class, match_bets

@pytest.mark.parametrize("test_bet, test_draw, expected_winning_class", [
    (Bet(user="1234",winning_numbers=[1,2,3,4,5,6], super_number=[0]), LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]),1),
    (Bet(user="1234",winning_numbers=[1,2,3,4,5,6], super_number=[1]), LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]),2),
    (Bet(user="1234",winning_numbers=[1,2,3,4,5,49], super_number=[0]), LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]),3),
    (Bet(user="1234",winning_numbers=[1,2,3,4,5,49], super_number=[1]), LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]),4),
    (Bet(user="1234",winning_numbers=[1,2,3,4,48,49], super_number=[0]), LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]),5),
    (Bet(user="1234",winning_numbers=[1,2,3,4,48,49], super_number=[1]), LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]),6),
    (Bet(user="1234",winning_numbers=[1,2,3,47,48,49], super_number=[0]), LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]),7),
    (Bet(user="1234",winning_numbers=[1,2,3,47,48,49], super_number=[1]), LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]),8),
    (Bet(user="1234",winning_numbers=[1,2,46,47,48,49], super_number=[0]), LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]),9),

])
def test_calculate_winning_class(test_bet, test_draw, expected_winning_class):
    calculated_winning_class = calculate_winning_class(test_draw, test_bet)
    assert calculated_winning_class == expected_winning_class

@pytest.mark.parametrize("test_bets, test_draw",[
    ([Bet(user="1234",winning_numbers=[1,2,3,4,5,6], super_number=[1]),
    Bet(user="1234",winning_numbers=[1,2,3,4,5,49], super_number=[0]),
    Bet(user="1234",winning_numbers=[1,2,3,4,5,49], super_number=[1]),
    Bet(user="1234",winning_numbers=[1,2,3,4,48,49], super_number=[0]),
    Bet(user="1234",winning_numbers=[1,2,3,4,48,49], super_number=[1]),
    Bet(user="1234",winning_numbers=[1,2,3,47,48,49], super_number=[0]),
    Bet(user="1234",winning_numbers=[1,2,3,47,48,49], super_number=[1]),
    Bet(user="1234",winning_numbers=[1,2,46,47,48,49], super_number=[0])
], LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]))
])
def test_match_bets(test_bets, test_draw):

    resulting_bets = match_bets(test_draw, test_bets)
    assert sum([bet.winning_class != 0 for bet in resulting_bets]) == len(test_bets)