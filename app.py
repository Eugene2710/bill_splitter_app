import json
from typing import Dict, Any

from flask import Flask
from flask import request

from models.items_to_split import ItemsToSplit, Bill
from utils.bill_splitter import split_bill

# __name__ -> app.py is executed directly, this will be "__main__"
# __name__ -> app.py is not executed directly, this will be the name of this file; "app"

# print(__name__)

# we pass in __name__ to let Flask know where to look for assets for the API;
# e.g html template

app: Flask = Flask(__name__)

# HTTP Protocol
# GET http://localhost:5000/split_bill
# GET, UPDATE, DELETE, POST
@app.route("/split_bill", methods=["GET"])
def get_split_bill() -> Dict[str, Any]:

    # get the input data from the client, from the global request object
    input_data: bytes = request.data

    input_data_dict: Dict[str, Any] = json.loads(input_data)
    items_to_split: ItemsToSplit = ItemsToSplit.parse_obj(input_data_dict)
    bill: Bill = split_bill(items_to_split)
    # mocked a hard-coded response
    return bill.dict()


if __name__ == "__main__":
    app.run(port=5000)