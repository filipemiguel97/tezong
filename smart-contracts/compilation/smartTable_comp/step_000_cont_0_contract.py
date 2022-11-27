import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(buyIn = sp.TMutez, game_owner = sp.TAddress, initialBuyIn = sp.TMutez, player_challenger = sp.TAddress, player_defender = sp.TAddress).layout((("buyIn", "game_owner"), ("initialBuyIn", ("player_challenger", "player_defender")))))
    self.init(buyIn = sp.tez(5),
              game_owner = sp.address('tz1XYLq45goZYYmNv4S6RSYFo5rGfbGUmqnk'),
              initialBuyIn = sp.tez(5),
              player_challenger = sp.address('tz1XYLq45goZYYmNv4S6RSYFo5rGfbGUmqnk'),
              player_defender = sp.address('tz1XYLq45goZYYmNv4S6RSYFo5rGfbGUmqnk'))

  @sp.entry_point
  def buy_in(self):
    sp.verify(sp.pack(sp.set_type_expr(self.data.player_challenger, sp.TAddress)) == sp.pack(sp.set_type_expr(self.data.game_owner, sp.TAddress)), 'The table already has a challenger')
    sp.verify(sp.pack(sp.set_type_expr(sp.amount, sp.TMutez)) == sp.pack(sp.set_type_expr(self.data.buyIn, sp.TMutez)), 'Incorrect buy in ammount')
    self.data.player_challenger = sp.sender

  @sp.entry_point
  def challenger_won(self, params):
    sp.verify(sp.pack(sp.set_type_expr(sp.sender, sp.TAddress)) == sp.pack(sp.set_type_expr(self.data.game_owner, sp.TAddress)))
    sp.send(self.data.game_owner, sp.split_tokens(sp.balance, 1, 10))
    sp.send(self.data.player_challenger, (sp.balance - sp.split_tokens(sp.balance, 1, 10)) - params)
    self.data.player_defender = self.data.player_challenger
    self.data.player_challenger = self.data.game_owner
    self.data.buyIn = self.data.initialBuyIn

  @sp.entry_point
  def defender_left(self, params):
    sp.verify(sp.pack(sp.set_type_expr(sp.sender, sp.TAddress)) == sp.pack(sp.set_type_expr(self.data.game_owner, sp.TAddress)))
    self.data.player_defender = self.data.game_owner
    sp.send(self.data.game_owner, sp.balance - params)
    self.data.buyIn = self.data.initialBuyIn

  @sp.entry_point
  def defender_won(self):
    sp.verify(sp.pack(sp.set_type_expr(sp.sender, sp.TAddress)) == sp.pack(sp.set_type_expr(self.data.game_owner, sp.TAddress)))
    sp.send(self.data.player_defender, sp.split_tokens(self.data.buyIn, 5, 7))
    sp.send(self.data.game_owner, sp.split_tokens(self.data.buyIn, 1, 10))
    self.data.player_challenger = self.data.game_owner
    self.data.buyIn = sp.split_tokens(self.data.buyIn, 6, 5)

  @sp.entry_point
  def new_defender(self):
    sp.verify(sp.pack(sp.set_type_expr(self.data.player_defender, sp.TAddress)) == sp.pack(sp.set_type_expr(self.data.game_owner, sp.TAddress)), 'The table already has a defender')
    self.data.player_defender = sp.sender

sp.add_compilation_target("test", Contract())