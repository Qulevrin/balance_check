from web3 import Web3, HTTPProvider

rpc = 'https://mainnet.base.org'

with open('wallets.txt', 'r', encoding='utf-8-sig') as file:
    private_keys = [line.strip() for line in file]

output_file = 'balances.txt'


class Account:
    def __init__(self, private_key: str):
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        self.account = self.web3.eth.account.from_key(private_key)
        self.wallet_address = self.account.address

    def balance(self):
        return round(self.web3.eth.get_balance(self.wallet_address) / 10 ** 18, 5)


def main(private_keys, output_file):
    total_balance = 0
    with open(output_file, 'w') as output:
        for private_key in private_keys:
            account = Account(private_key)
            account_balance = account.balance()
            print('ETH:', account_balance)
            total_balance += account_balance
            output.write(f'{account_balance:.5f}\n')
    return total_balance


total_eth = main(private_keys, output_file)
print('Total ETH:', round(total_eth, 5))
