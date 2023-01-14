# index

[stackoverflow which is performant](https://stackoverflow.com/questions/56506410/why-is-on-better-than-o-nlogn)

- O(1) < O(logn) < O(n) < O(nlogn)
- it is important to remember that a time complexity is only an estimate of efficiency, because it hides the constant factors; n/2, 2n or 10n.

## time complexity

```

① O(1): 입력 크기 n과 계산 복잡도가 무관할 때

예) 계산 공식 n(n + 1) / 2를 이용한 1부터 n까지의 합(문제 1)

② O(logn): 입력 크기 n의 로그 값에 비례하여 계산 복잡도가 증가할 때

예) 이분 탐색(문제 12)

③ O(n): 입력 크기 n에 비례하여 계산 복잡도가 증가할 때

예) 최댓값 찾기(문제 2), 순차 탐색(문제 7)

④ O(n·logn): 입력 크기 n과 로그 n 값의 곱에 비례하여 계산 복잡도가 증가할 때

예) 병합 정렬(문제 10), 퀵 정렬(문제 11)

⑤ O(n2): 입력 크기 n의 제곱에 비례하여 계산 복잡도가 증가할 때

예) 선택 정렬(문제 8), 삽입 정렬(문제 9)

⑥ O(2n): 입력 크기가 n일 때 2의 n 제곱 값에 비례하여 계산 복잡도가 증가할 때

예) 하노이의 탑(문제 6)

```

## algorithm to use based on the input size

```
n <= 10    =>    O(n!)
n <= 20    =>    O(2n^)
n <= 500   =>    O(n3^)
n <= 5000  =>    O(n2^)
n <= 10 6^ =>    O(nlogn) or O(n)
n is large =>    O(1) or O(logn)

```
