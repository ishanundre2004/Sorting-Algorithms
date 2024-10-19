class MergeSort:
    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = MergeSort.sort(arr[:mid])
        right = MergeSort.sort(arr[mid:])

        return MergeSort.merge(left, right)

    @staticmethod
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

# Example usage
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Merge Sort:", MergeSort.sort(arr))
