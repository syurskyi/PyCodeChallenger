class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        current = ListNode(0)
        dummy = current

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return dummy.next


class TestMergeTwoLists:
    @staticmethod
    def create_linked_list(nodes):
        dummy = ListNode(0)
        current = dummy
        for node in nodes:
            current.next = ListNode(node)
            current = current.next
        return dummy.next

    @staticmethod
    def linked_list_to_list(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    @staticmethod
    def run_tests():
        test_cases = [
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([], [], []),
            ([], [0], [0]),
        ]

        solution = Solution()

        for list1, list2, expected in test_cases:
            list1_head = TestMergeTwoLists.create_linked_list(list1)
            list2_head = TestMergeTwoLists.create_linked_list(list2)

            result_head = solution.mergeTwoLists(list1_head, list2_head)
            result = TestMergeTwoLists.linked_list_to_list(result_head)

            assert result == expected, f"Expected: {expected}, Got: {result}"
            print(f"Input: list1={list1}, list2={list2}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestMergeTwoLists.run_tests()
