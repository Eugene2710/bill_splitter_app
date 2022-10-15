from typing import Dict, List

from models.items_to_split import ItemsToSplit, Bill, ItemToSplit, PeopleName, PeopleBill


def _get_people_to_list_of_items(items_to_split: ItemsToSplit) -> Dict[PeopleName, List[ItemToSplit]]:
    people_to_list_of_items: Dict[PeopleName, List[ItemToSplit]] = {}
    for item in items_to_split.items:
        people_for_item: List[PeopleName] = item.people
        for people in people_for_item:
            people_to_list_of_items[people] = people_to_list_of_items.get(people, [])
            people_to_list_of_items[people].append(item)
    return people_to_list_of_items


def _calculate_people_bill(people_to_list_of_items: Dict[PeopleName, List[ItemToSplit]]) -> Bill:
    people_bills: List[PeopleBill] = []
    for people_name, contributed_items in people_to_list_of_items.items():
        total_people_bill: float = 0.0
        for item in contributed_items:
            item_bill: float = item.price / len(item.people)
            total_people_bill += item_bill
        people_bill: PeopleBill = PeopleBill(
            name=people_name,
            bill=round(total_people_bill,2),
            itemsToSplit=contributed_items
        )
        people_bills.append(people_bill)
    return Bill(peopleBills=people_bills)


def split_bill(items_to_split: ItemsToSplit) -> Bill:
    people_to_list_of_items: Dict[PeopleName, List[ItemToSplit]] = _get_people_to_list_of_items(items_to_split)
    bill: Bill = _calculate_people_bill(people_to_list_of_items)
    return bill