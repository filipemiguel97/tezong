import smartpy as sp

class smartTable(sp.Contract):
    def __init__(self, game_owner, initialBuyIn):
        self.init(game_owner=game_owner, buyIn = initialBuyIn, initialBuyIn=initialBuyIn, player_challenger = game_owner, player_defender = game_owner)
    
    @sp.entry_point
    def new_defender(self):
        sp.verify_equal(self.data.player_defender, self.data.game_owner, "The table already has a defender")
        self.data.player_defender = sp.sender

    @sp.entry_point
    def buy_in(self):
        sp.verify_equal(self.data.player_challenger, self.data.game_owner, "The table already has a challenger")
        sp.verify_equal(sp.amount, self.data.buyIn, "Incorrect buy in ammount")
        self.data.player_challenger = sp.sender

    @sp.entry_point
    def challenger_won(self, gas_fee):
        sp.verify_equal(sp.sender, self.data.game_owner)
        send_to_owner = sp.split_tokens(sp.balance, 1,10)
        sp.send(self.data.game_owner, send_to_owner)
        sp.send(self.data.player_challenger, sp.balance - send_to_owner - gas_fee)
        self.data.player_defender = self.data.player_challenger
        self.data.player_challenger = self.data.game_owner
        self.data.buyIn = self.data.initialBuyIn

    @sp.entry_point
    def defender_won(self):
        sp.verify_equal(sp.sender, self.data.game_owner)
        sp.send(self.data.player_defender, sp.split_tokens(self.data.buyIn, 5, 7))
        sp.send(self.data.game_owner, sp.split_tokens(self.data.buyIn, 1,10))
        self.data.player_challenger = self.data.game_owner
        self.data.buyIn = sp.split_tokens(self.data.buyIn, 6, 5)

    @sp.entry_point
    def defender_left(self, gas_fee):
        sp.verify_equal(sp.sender, self.data.game_owner)
        self.data.player_defender = self.data.game_owner
        sp.send(self.data.game_owner, sp.balance - gas_fee)
        self.data.buyIn = self.data.initialBuyIn

game_owner = sp.test_account("Myself")
Joao = sp.test_account("Joao")
Mohith = sp.test_account("Mohith")

@sp.add_test(name = "smartTable")
def test():
    c1 = smartTable(game_owner.address, sp.tez(5))
    scenario = sp.test_scenario()

    scenario.h1("add defender")
    scenario += c1
    c1.new_defender().run(sender=Joao.address)
    scenario.verify(c1.data.player_defender == Joao.address)

    scenario.h1("buy in")
    c1.buy_in().run(sender=Mohith.address, amount=sp.tez(5))
    scenario.verify(c1.data.player_challenger == Mohith.address)

    scenario.h1("defender won")
    c1.defender_won().run(sender=game_owner.address)
    scenario.verify(c1.data.player_defender == Joao.address)
    scenario.verify(c1.data.player_challenger == game_owner.address)
    scenario.verify(c1.data.buyIn == sp.tez(6))

    scenario.h1("challenger won")
    c1.buy_in().run(sender=Mohith.address, amount=sp.tez(6))
    c1.challenger_won(sp.mutez(5)).run(sender=game_owner.address)
    scenario.verify(c1.data.player_defender == Mohith.address)
    scenario.verify(c1.data.player_challenger == game_owner.address)

    scenario.h1("defender left")
    c1.defender_left(sp.mutez(5)).run(sender=game_owner.address)
    scenario.verify(c1.data.player_defender == game_owner.address)
    scenario.verify(c1.data.game_owner == game_owner.address)

sp.add_compilation_target("smartTable_comp", smartTable(game_owner.address, sp.tez(5)))
