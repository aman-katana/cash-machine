from controller.payments import Payments
from model.bank_model import bank
from model.debit_card import card


class Payments2(Payments):

    def pay2(self, card_num, place, amount):

        if self.if_enough(card_num, amount):
            # print("Взять деньги с card в размере amount положить в place")
            try:
                if place in bank.get_accounts(self.name):
                    now_amount = card_num["balance"] - int(amount)
                    # print("# Запись в историю куда оправились деньги")
                    card.set_balance(card_num=card_num["num"], amount=now_amount)
                    card.set_current_card(card.get_card_by_num(card_num["num"]))
                    return True
                else:
                    return None
            except:
                return None

        else:
            return False


pay_fine = Payments2("fine", 334455)