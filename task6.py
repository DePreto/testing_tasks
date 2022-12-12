"""
ЗАДАНИЕ
Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные поля.

Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
 - getAll() Должен возвращать изначальный массив элементов.
 - getItem(id) Принимает id элемента и возвращает сам объект элемента;
 - getChildren(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
 - getAllParents(id) Принимает id элемента и возвращает массив из цепочки родительских элементов,
начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

Требования: максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях,
в идеале, прямой доступ к элементам без поиска их в массиве.


Исходные данные:
class TreeStore:
    pass


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)

Примеры использования:
 - ts.getAll() // [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]

 - ts.getItem(7) // {"id":7,"parent":4,"type":None}

 - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
 - ts.getChildren(5) // []

 - ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]
"""


class Node:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.parent = kwargs.get("parent")
        self.children = []
        if "type" in kwargs:
            self.type = kwargs.get("type")

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if key in ("children", ):
                pass
            elif isinstance(value, Node):
                result[key] = value.id
            else:
                result[key] = value
        return result


class TreeStore:
    def __init__(self, items):
        self.nodes_by_id = {}
        self.head = None
        for item in items:
            self.add_node(item)

    def getAll(self):
        nodes = self.head.children
        result = []
        while nodes:
            crt_node = nodes.pop(0)
            result.append(crt_node.to_dict())
            nodes.extend(crt_node.children)
        return result

    def getItem(self, item_id):
        # TODO можно реализовать и перебором в ширину/глубину, но по тз - прямой доступ к объектам
        item = self.nodes_by_id.get(item_id)
        if item:
            return item.to_dict()

    def getChildren(self, item_id):
        item = self.nodes_by_id.get(item_id)
        result = []
        if item:
            result.extend(item.children)
            index = 0
            while index < len(result):
                result.extend(result[index].children)
                index += 1
        return list(map(lambda x: x.to_dict(), result))

    def getAllParents(self, item_id):
        crt_node = self.nodes_by_id.get(item_id)
        result = []
        if crt_node:
            result.append(crt_node)  # TODO по тз требуется включить и переданный элемент (что != примеру)
            parent = crt_node.parent
            while parent and parent.id != "root":
                result.append(parent)
                parent = parent.parent
        return list(map(lambda x: x.to_dict(), result))

    def add_node(self, item):
        if self.head is None:
            self.head = Node(
                **{
                    "id": item["parent"],
                    "parent": None,
                }
            )
            parent = self.head
        else:
            nodes = [self.head]
            parent = None
            while nodes and not parent:
                check_parent = nodes.pop(0)
                if check_parent.id == item["parent"]:
                    parent = check_parent
                else:
                    nodes.extend(check_parent.children)
        node = Node(
            **item
        )
        node.parent = parent
        parent.children.append(node)
        self.nodes_by_id[node.id] = node


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)
print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))
