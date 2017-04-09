#乒乓序列从1开始计数，并且始终向上或向下计数。在元素k处，如果k是7的倍数或包含数字7，方向将切换。乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和28个元素：
#1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
def pingpong(n,k):
	if not (type(n) == int and type(k) == int and n >0 and k >0):
		raise Exception('n or k type error! \nthey should be positive int!')
	i = 1
	flag = 1
	ans = 0
	while(i <= n):
		ans = ans + flag
		if i % k == 0 or str(k) in list(str(i)):
			flag = flag * (-1) # change direction
		i += 1
	return ans
print(pingpong(21,7))
			 
	
	
