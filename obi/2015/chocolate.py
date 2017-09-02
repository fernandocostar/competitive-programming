
N = int(input())
X1, Y1 = map(int, input().split(" "))
X2, Y2 = map(int, input().split(" "))

print ("S") if ( (X1 <= N/2 and X2 > N/2 ) or (X2 <= N/2 and X1 > N/2 ) or (Y1 <= N/2 and Y2 > N/2 ) or (Y2 <= N/2 and Y1 > N/2 ) )else print("N")
