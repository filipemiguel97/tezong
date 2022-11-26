import smartpy as sp

tstorage = sp.TRecord(buyIn = sp.TIntOrNat, owner = sp.TString).layout(("buyIn", "owner"))
tparameter = sp.TVariant(store = sp.TIntOrNat).layout("store")
tprivates = { }
tviews = { }
