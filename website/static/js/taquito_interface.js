const tezos  = new window.TezosToolKit("https://rpc.ghostnet.teztnets.xyz");
class smart_table {
    constructor(smart_contract_address){
        this.contract = tezos.contract.at(smart_contract_address)
        this.player_defender = player_defender;
        this.player_challenger = player_challenger;
        this.smart_contract_address=smart_contract_address;
    }

    buy_in_challenger(challenger_id){
        this.player_challenger = challenger_id;
        // taquito logic
    }

    challenger_won(){
        this.player_defender = this.player_challenger;
        this.player_challenger = "";
        // taquito logic
    }

    defender_won(){
        this.player_challenger = "";
        // taquito logic
    }
}

var table_1 = smart_table("KT1Af6L4Z1W9Jz6c5Abdg3xz6kVj8KHbSzRu");