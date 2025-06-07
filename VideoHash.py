from videohash import VideoHash
from pathlib import Path

# 函数：生成视频哈希并比较
# url1 = "https://user-images.githubusercontent.com/64683866/168872267-7c6682f8-7294-4d9a-8a68-8c6f44c06df6.mp4"
url1 = "https://upos-hz-mirrorakam.akamaized.net/upgcxcode/26/43/30037444326/30037444326-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1748167013&gen=playurlv2&os=akam&oi=1759421563&trid=2c8c6d5cb9224459aab86ec1d0cbfca9h&mid=0&platform=html5&og=hw&upsig=ff8f9effc9384fda17cecf6241066045&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&hdnts=exp=1748167013~hmac=4d382d9ce9f3450926107a1473a71a0b4ee05e34e9118da7799c992ca41a048a&bvc=vod&nettype=0&f=h_0_0&bw=58770&logo=80000000"
videohash1 = VideoHash(url=url1)
print("视频1哈希值：", videohash1.hash)
url2 = "https://user-images.githubusercontent.com/64683866/168869109-1f77c839-6912-4e24-8738-42cb15f3ab47.mp4"
videohash2 = VideoHash(url=url2)
print("距离：",videohash1-videohash2)
print("视频2哈希值：", videohash2.hash)
if(videohash2.is_similar(videohash1)):
    print("视频1和视频2相似")
else:
    print("视频1和视频2不相似")

# from web3 import Web3
# from solcx import compile_source
# from solcx import install_solc, get_solc_version, get_installable_solc_versions, set_solc_version

# # 检查可用的 solc 版本
# print("可用的 solc 版本:", get_installable_solc_versions())

# # 尝试安装 solc 0.8.0
# try:
#     install_solc('0.8.0')
#     print("solc 0.8.0 安装成功")
# except Exception as e:
#     print(f"安装 solc 失败: {e}")
#     exit(1)

# # 设置 solc 版本
# try:
#     set_solc_version('0.8.0')
#     print("solc 版本设置为 0.8.0")
# except Exception as e:
#     print(f"设置 solc 版本失败: {e}")
#     exit(1)

# # 验证安装
# try:
#     print(f"当前 solc 版本: {get_solc_version()}")
# except Exception as e:
#     print(f"获取 solc 版本失败: {e}")



# # 连接到 Sepolia 测试网
# w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/f0dffd40d48a4f18bbe488ce8c72d70b'))  # 替换为你的 Infura 项目 ID
# if not w3.is_connected():
#     raise Exception("无法连接到 Sepolia 测试网")

# # 你的账户信息
# account = "0x0341d71cB29e3cFF3Ea63417124224ED17b141a4"  # 替换为你的测试网地址
# private_key = "ecb434fdd28fcaa088378c9f3f94d48c30ff69017719cef3ed5914ce03e0913d"  # 替换为你的私钥（注意安全！）

# # 编译 Solidity 合约
# with open("VideoHashStorage.sol", "r") as file:
#     contract_source = file.read()

# compiled_sol = compile_source(contract_source)
# contract_interface = compiled_sol['<stdin>:VideoHashStorage']

# # 部署合约
# contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
# nonce = w3.eth.get_transaction_count(account)
# txn = contract.constructor().build_transaction({
#     'from': account,
#     'nonce': nonce,
#     'gas': 1000000,
#     'gasPrice': w3.to_wei('10', 'gwei')  # Sepolia Gas 价格通常较低
# })
# signed_txn = w3.eth.account.sign_transaction(txn, private_key)
# txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
# txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
# contract_address = txn_receipt.contractAddress
# print(f"合约部署地址: {contract_address}")