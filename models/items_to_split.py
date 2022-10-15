from typing import List, NewType

from pydantic import BaseModel

ItemName = NewType("ItemName", str)
PeopleName = NewType("PeopleName", str)

# The pydantic.BaseModel is a class which we can use to create data classes
# Data classes represents data, and its expected fields
# Improves readability
# BaseModel -> Allows you to avoid the need for a constructor defined, even with multiple fields
class ItemToSplit(BaseModel):
    name: ItemName
    price: float
    people: List[PeopleName]

class ItemsToSplit(BaseModel):
    items: List[ItemToSplit]


class PeopleBill(BaseModel):
    name: PeopleName
    bill: float
    itemsToSplit: List[ItemToSplit]


class Bill(BaseModel):
    peopleBills: List[PeopleBill]


# if __name__ == "__main__":
#     # Pydantic helps us check if the fields are valid
#     item_to_split: ItemsToSplit = ItemToSplit(name=10.0, price="10.0", people=[])