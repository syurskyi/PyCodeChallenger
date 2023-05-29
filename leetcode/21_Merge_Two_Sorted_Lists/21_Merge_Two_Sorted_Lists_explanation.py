class ListNode:
    # The ListNode class represents a node in a linked list. It has two attributes: val, which stores the value
    # of the node, and next, which points to the next node in the linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # The Solution class defines a method mergeTwoLists that takes two linked lists, l
        # ist1 and list2, as input and returns the merged sorted linked list.
        current = ListNode(0)
        # current is initialized as a new ListNode object with a value of 0.
        # It serves as a temporary node to build the merged list.
        dummy = current
        # dummy is assigned the reference to current initially.
        # It will hold the reference to the head of the merged list.

        while list1 and list2:
            # This while loop iterates as long as both list1 and list2 have nodes.
            if list1.val <= list2.val:
                # It compares the values of the current nodes from list1 and list2.
                # If the value of the current node in list1 is less than or equal to the value
                # of the current node in list2, the current.next is set to the current node in list1, and list1 is
                # moved to the next node.
                current.next = list1
                list1 = list1.next
            else:
                # If the value of the current node in list1 is greater than the value of the current node in list2,
                # then current.next is set to the current node in list2, and list2 is moved to the next node.
                current.next = list2
                list2 = list2.next
            current = current.next
            # Finally, current is moved to the next node.

        current.next = list1 or list2
        # After the while loop, there may be remaining nodes in either list1 or list2.
        # If list1 still has nodes, current.next is set to list1. Otherwise,
        # if list2 still has nodes, current.next is set to list2. This appends the remaining nodes to the merged list.

        return dummy.next
    # The head of the merged list is dummy.next, which points to the first node of the merged list.
    # It is returned as the result of the mergeTwoLists method.


class TestMergeTwoLists:
    # The TestMergeTwoLists class contains static methods to assist in creating and manipulating
    # linked lists for testing.
    @staticmethod
    def create_linked_list(nodes):
        # The create_linked_list method takes a list of values (nodes) as input and creates
        # a linked list from those values.
        dummy = ListNode(0)
        # It initializes a dummy node with a value of 0 and a current node that points to the dummy node.
        current = dummy
        for node in nodes:
            # It iterates over each value in nodes, creates a new ListNode with the current value,
            # assigns it as the next node of the current node, and moves the current node to the next node.
            current.next = ListNode(node)
            current = current.next
        return dummy.next
    # Finally, it returns the head of the linked list (dummy.next), excluding the dummy node.

    @staticmethod
    def linked_list_to_list(head):
        # Finally, it returns the head of the linked list (dummy.next), excluding the dummy node.
        result = []
        # It initializes an empty list result.
        current = head
        # It iterates over the linked list by starting from the head and traversing each node using the next pointer
        while current:
            # In each iteration, it appends the value of the current node (current.val) to the result list
            # and moves to the next node.
            result.append(current.val)
            current = current.next
        return result
    # Once it reaches the end of the linked list (when current becomes None), it returns the result list.

    @staticmethod
    def run_tests():
        # The run_tests method runs the test cases for the mergeTwoLists method.
        test_cases = [
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([], [], []),
            ([], [0], [0]),
        ]
        # Each test case represents the input lists and the expected output for the mergeTwoLists method.

        solution = Solution()
        # An instance of the Solution class is created to access the mergeTwoLists method.

        for list1, list2, expected in test_cases:
            # The code then iterates over each test case.
            list1_head = TestMergeTwoLists.create_linked_list(list1)
            list2_head = TestMergeTwoLists.create_linked_list(list2)
            # For each test case, it creates linked lists list1_head and list2_head using the create_linked_list method

            result_head = solution.mergeTwoLists(list1_head, list2_head)
            result = TestMergeTwoLists.linked_list_to_list(result_head)
            # It calls the mergeTwoLists method with the created linked lists and assigns
            # the resulting head to result_head
            # The linked_list_to_list method is used to convert result_head into a list (result).

            assert result == expected, f"Expected: {expected}, Got: {result}"
            # It compares result with the expected merged list (expected) and asserts their equality.
            print(f"Input: list1={list1}, list2={list2}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestMergeTwoLists.run_tests()
