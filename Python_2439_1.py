'''
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''

N=int(input()) # 사용자로부터 정수 입력받기
num=N # num에 N 대입
m=1 # m을 1로 초기화

for i in range(N):
    for j in range(num-m):
        print(" ", end="")
    for k in range(m):
        print("*", end="")
    m+=1;
    print()
