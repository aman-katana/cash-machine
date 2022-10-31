from controller.transactions import Transactions
from model.bank_model import bank
from model.debit_card import card


class Transactions2(Transactions):

    def get_transfer(self, lst):
        try:
            amount = sum(lst)
            place = card.get_current_card()
            now_amount = place["balance"] + int(amount)
            card.set_balance(card_num=place["num"], amount=now_amount)
            card.set_current_card(card.get_card_by_num(place["num"]))

            for i in lst:
                bank.banknote_plus(i)
            else:
                return True
        except:
            return False


cash2 = Transactions("get")
