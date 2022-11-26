import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(buyIn = sp.TIntOrNat, owner = sp.TString).layout(("buyIn", "owner")))
    self.init(buyIn = 5,
              owner = 'me')

  @sp.entry_point
  def store(self, params):
    self.data.buyIn = params

sp.add_compilation_target("test", Contract())