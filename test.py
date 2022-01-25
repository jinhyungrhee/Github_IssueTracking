import random

class Heap:  # max_heap
    def __init__(self, L=[]):
        self.A = L

    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):
        while n > 2*k + 1:  # 자식 노드가 있는가?
            L, R = 2*k + 1, 2*k + 2
            m = k  # m = (A[k], A[L], A[R])중 큰 값을 가지는 index
            if self.A[k] < self.A[L]:
                m = L
            if n > R:
                if self.A[m] < self.A[R]:
                    m = R
            if k == m:  # 내가 가장 큰 값인 경우
                break
            else:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m

    def make_heap(self):  # 차례대로 모든 애들에 대해서 heapify_down 적용(마지막에 있는 노드부터 역순으로)
        n = (len(self.A))
        for k in range(n - 1, -1, -1):  # n-1(마지막 인덱스)부터 0(root)까지 뒤에서부터 하나씩
            self.heapify_down(k, n)

    def heap_sort(self):  # heap을 사용한 정렬
        n = len(self.A)
        for k in range(len(self.A) - 1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]  # 첫 인덱스와 마지막 인덱스를 교환
            n = n - 1  # A[n-1]은 정렬되었으므로 (큰 수들을 하나씩 제외시키는 것)
            self.heapify_down(0, n)

    def heapify_up(self, k):  # 올라가면서 A[k]를 재배치
        while k > 0 and self.A[(k - 1) // 2] < self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)


S = [random.randint(0, 100) for _ in range(20)]
H = Heap(S)
print("Original: ", H)
H.make_heap()
print("Heapified: ", H)
insert = 10
H.insert(insert)
print(f"")

# 결과
# Original:  [37, 12, 54, 81, 9, 57, 49, 61, 33, 12, 70, 4, 24, 26, 3, 82, 41, 85, 25, 24]
# Heapified:  [85, 82, 57, 81, 70, 54, 49, 61, 37, 24, 9, 4, 24, 26, 3, 12, 41, 33, 25, 12]