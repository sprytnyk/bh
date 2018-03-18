from flask import Blueprint, request, jsonify

from app.utils import deploy_contract

app_bp = Blueprint('app', __name__)
contract, account = deploy_contract('Product.sol')


@app_bp.route('/set-product/', methods=['POST'])
def set_product():
    if request.method == 'POST' and request.json:
        # Flask RESTFul would serve this job better, but we don't have enough
        # time.
        data = request.json
        result = contract.setProduct(
            data.get('name'),
            data.get('category'),
            data.get('sku_number'),
            data.get('url'),
            transact={'from': account}
        )
        return jsonify(result)
    return 'Feed me some data.'


@app_bp.route('/get-product/')
def get_product():
    if request.method == 'GET' and request.args.get('hash'):
        # Flask RESTFul would serve this job better, but we don't have enough
        # time.
        result = contract.getProduct(
            str(request.args.get('hash'))
        )
        return jsonify(result)
    return 'Feed me some data.'
