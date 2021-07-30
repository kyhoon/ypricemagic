from brownie import Contract, chain

if chain.id == 1:
    weth = Contract("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    usdc = Contract("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
    dai = Contract("0x6B175474E89094C44Da98b954EedeAC495271d0F")
    wbtc = Contract("0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599")
    usdt = Contract("0xdAC17F958D2ee523a2206206994597C13D831ec7")
    sushi = Contract("0x6B3595068778DD592e39A122f4f5a5cF09C90fE2")

    STABLECOINS = {
        "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48": "usdc",
        "0x0000000000085d4780B73119b644AE5ecd22b376": "tusd",
        "0x6B175474E89094C44Da98b954EedeAC495271d0F": "dai",
        "0xdAC17F958D2ee523a2206206994597C13D831ec7": "usdt",
        "0x4Fabb145d64652a948d72533023f6E7A623C7C53": "busd",
        "0x57Ab1ec28D129707052df4dF418D58a2D46d5f51": "susd",
        "0x1456688345527bE1f37E9e627DA0837D6f08C925": "usdp",
        "0x674C6Ad92Fd080e4004b2312b45f796a192D27a0": "usdn",
        "0x853d955aCEf822Db058eb8505911ED77F175b99e": "frax",
        "0x5f98805A4E8be255a32880FDeC7F6728C6568bA0": "lusd",
        "0xBC6DA0FE9aD5f3b0d58160288917AA56653660E9": "alusd",
        "0x8e870d67f660d95d5be530380d0ec0bd388289e1": "pax"
    }

    PROXIES = {
        # NOTE: Proxy address : current implementation
        '0xC011A72400E58ecD99Ee497CF89E3775d4bd732F': '0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f', # snx
        '0x0Ba45A8b5d5575935B8158a88C631E9F9C95a2e5': '0x88df592f8eb5d7bd38bfef7deb0fbc02cf3778a0', # trb
    }
elif chain.id == 56:
    weth = Contract("0x8d0e18c97e5dd8ee2b539ae8cd3a3654df5d79e5")
    usdc = Contract("0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d")
    dai = Contract("0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3")
    wbtc = Contract("0x2ccb7c8c51e55c2364b555ff6e6e3f7246499e16")
    usdt = Contract("0x55d398326f99059ff775485246999027b3197955")
    sushi = Contract("0x947950bcc74888a40ffa2593c5798f11fc9124c4")

    STABLECOINS = {
        "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d": "usdc",
        "0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3": "dai",
        "0x55d398326f99059ff775485246999027b3197955": "usdt",
        "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56": "busd",
        "0x23396cF899Ca06c4472205fC903bDB4de249D6fC": "wust"
    }
    PROXIES = {}