from app.utils import deploy_contract

contract, account = deploy_contract('Product.sol')
setter = contract.setProduct(
    'My name',
    'Cats',
    'sku_num',
    'http://localhost',
    transact={'from': account}
)
