from web3 import Web3
# w3 = Web3()  # 不需要连接节点即可创建账户
# account = w3.eth.account.create()
# print(f"测试网地址: {account.address}")  # 替换 YOUR_SEPOLIA_ADDRESS
# print(f"私钥: {account.key.hex()}")  # 替换 YOUR_PRIVATE_KEY，保存好！


# w3 = Web3(Web3.HTTPProvider('hhttps://mainnet.infura.io/v3/f0dffd40d48a4f18bbe488ce8c72d70b'))
# account = "0x0341d71cB29e3cFF3Ea63417124224ED17b141a4"  # 替换为你的地址
# balance = w3.eth.get_balance(account)
# print(f"账户余额: {w3.from_wei(balance, 'ether')} ETH")