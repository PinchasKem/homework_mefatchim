'''
 עץ חיפוש בינארי 
 עם יכולת הוספה חיפוש ומחיקה
'''


class Node:
    def __init__(self, license_plate, car_details):
        self.license_plate = license_plate
        self.car_details = car_details
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, license_plate, car_details):
        if self.root is None:
            self.root = Node(license_plate, car_details)
        else:
            self._insert_recursive(self.root, license_plate, car_details)

    def _insert_recursive(self, current_node, license_plate, car_details):
        if license_plate < current_node.license_plate:
            if current_node.left is None:
                current_node.left = Node(license_plate, car_details)
            else:
                self._insert_recursive(current_node.left, license_plate, car_details)
        elif license_plate > current_node.license_plate:
            if current_node.right is None:
                current_node.right = Node(license_plate, car_details)
            else:
                self._insert_recursive(current_node.right, license_plate, car_details)
        else:
            current_node.car_details = car_details

    def search(self, license_plate):
        return self._search_recursive(self.root, license_plate)

    def _search_recursive(self, current_node, license_plate):
        if current_node is None or current_node.license_plate == license_plate:
            return current_node
        if license_plate < current_node.license_plate:
            return self._search_recursive(current_node.left, license_plate)
        return self._search_recursive(current_node.right, license_plate)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(f"{node.license_plate} {node.car_details}")
            self._inorder_recursive(node.right)
    
    def delete(self, license_plate):
        self.root = self._delete_recursive(self.root, license_plate)

    def _delete_recursive(self, current_node, license_plate):
        if current_node is None:
            return None

        if license_plate < current_node.license_plate:
            current_node.left = self._delete_recursive(current_node.left, license_plate)
        elif license_plate > current_node.license_plate:
            current_node.right = self._delete_recursive(current_node.right, license_plate)
        else:

            if current_node.left is None and current_node.right is None:
                return None

            if current_node.left is None:
                return current_node.right
            if current_node.right is None:
                return current_node.left

            successor = self._find_min(current_node.right)
            current_node.license_plate = successor.license_plate
            current_node.car_details = successor.car_details
            current_node.right = self._delete_recursive(current_node.right, successor.license_plate)

        return current_node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

