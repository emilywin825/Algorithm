# [Silver II] 최소 힙 - 1927 

[문제 링크](https://www.acmicpc.net/problem/1927) 

### 성능 요약

메모리: 38340 KB, 시간: 120 ms

### 분류

자료 구조, 우선순위 큐

### 제출 일자

2025년 7월 3일 12:36:30

### 문제 설명

<p>널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.</p>

<ol>
	<li>배열에 자연수 x를 넣는다.</li>
	<li>배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.</li>
</ol>

<p>프로그램은 처음에 비어있는 배열에서 시작하게 된다.</p>

### 입력 

 <p>첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. x는 2<sup>31</sup>보다 작은 자연수 또는 0이고, 음의 정수는 입력으로 주어지지 않는다.</p>

### 출력 

 <p>입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.</p>

