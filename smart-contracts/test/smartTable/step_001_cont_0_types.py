import smartpy as sp

tstorage = sp.TRecord(buyIn = sp.TMutez, game_owner = sp.TAddress, initialBuyIn = sp.TMutez, player_challenger = sp.TAddress, player_defender = sp.TAddress).layout((("buyIn", "game_owner"), ("initialBuyIn", ("player_challenger", "player_defender"))))
tparameter = sp.TVariant(buy_in = sp.TUnit, challenger_won = sp.TMutez, defender_left = sp.TMutez, defender_won = sp.TUnit, new_defender = sp.TUnit).layout((("buy_in", "challenger_won"), ("defender_left", ("defender_won", "new_defender"))))
tprivates = { }
tviews = { }
