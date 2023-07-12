import json
import re

from flask import Flask
from flask_restful import Api, Resource, reqparse

# flask基本設定
app = Flask(__name__)
api = Api(app)

# 載入匯率
with open('exchange_rate.json') as f:
  currencies = json.load(f)['currencies']

class Convert(Resource):
  def get(self):
    # 參數設定
    parser = reqparse.RequestParser()
    parser.add_argument('source', required=True, location='args')
    parser.add_argument('target', required=True, location='args')
    parser.add_argument('amount', required=True, location='args')
    args = parser.parse_args()

    # 確認source幣別、target幣別
    if args['source'] not in currencies:
      return { 'msg': '不支援的source幣別' }
    if args['target'] not in currencies[args['source']]:
      return { 'msg': '不支援的target幣別' }

    try:
      # 分割幣別符號
      symbol, amount, _ = re.split('(\d+.*)', args['amount'])
      # 去除逗點並轉換成float
      amount = float(amount.replace(',', ''))
    except ValueError:
      return { 'msg': 'amount格式須為(幣別符號)+金額' }
    amount *= currencies[args['source']][args['target']]
    amount = f'{symbol}{amount:,.2f}'

    return { 'msg': 'success', 'amount': amount }

api.add_resource(Convert, '/api/convert')

if __name__ == '__main__':
  app.run()