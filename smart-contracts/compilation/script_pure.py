import smartpy as sp

class smartTable(sp.Contract):
    def __init__(self, owner, buyIn):
        self.init(owner=owner, buyIn = buyIn)

    # @sp.entry_point
    # def set_buy_in(self, value):
    #     pass

    # @sp.entry_point
    # def pay_buy_in(self):
    #     pass
    
    @sp.entry_point
    def store(self, value):
        # Store a new value
        self.data.buyIn = value

@sp.add_test(name = "smartTable")
def test():
    scenario = sp.test_scenario()
    contract = smartTable("me", 5)
    scenario += contract
    contract.store(2)

# A a compilation target (produces compiled code)
sp.add_compilation_target("smartTableCompiled", smartTable("me", 5))
