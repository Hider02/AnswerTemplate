# TODO Напишите функцию для поиска индекса товара
def search(itemslist, current_name):
    index = 0
    if current_name not in itemslist:
        return None
    else:
        while itemslist[index] != current_name:
            index += 1
        return index
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = search(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
