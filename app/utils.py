import os

from solc import compile_files
from web3 import Web3, RPCProvider
from web3.contract import ConciseContract

from core.settings import CONTRACT_DIR


def deploy_contract(name):
    """
    Compile and deploy a contract to the network.
    :param name: a name of a contract
    :return: an instance of a contract and the first account from test net
    """

    path = os.path.join(CONTRACT_DIR, '{}'.format(name))
    compiled_sol = compile_files(
        [
            path
        ]
    )
    contract_interface = compiled_sol[
        '{}:{}'.format(path, os.path.basename(name).split('.')[0])
    ]

    web3 = Web3(RPCProvider())
    contract = web3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )
    tx_hash = contract.deploy(
        transaction={
            'from': web3.eth.accounts[0],
            'gas': 3000000
        }
    )

    # Get tx receipt to get contract address
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)

    return (
        web3.eth.contract(
            address=tx_receipt['contractAddress'],
            abi=contract_interface['abi'],
            ContractFactoryClass=ConciseContract
        ),
        web3.eth.accounts[0]
    )
