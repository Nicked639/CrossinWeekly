import random
def race(qiwang, tianji):
    '''
    将齐王的马抽象为一个列表 [3,6,9]，田忌的马抽象为另一个列表 [2,5,8]
    分别代表各自的下、中、上等马。
    设计一个函数 race()，将两个列表作为参数传递给 race()
    将背景资料的策略抽象为代码使田忌赢得比赛，函数返回每轮对阵情况

    '''
    qiwang.sort()
    tianji.sort()
    race1 = (qiwang[2], tianji[0])
    race2 = (qiwang[1], tianji[2])
    race3 = (qiwang[0], tianji[1])
    r = [race1, race2, race3]
    return r

g = [3,6,9]
t = [2,5,8]


# 田忌的策略
def tianji_s():
    '''
    附加题
    1、如果你是某公子手下的谋士，已知同级别中己方的马优于田忌的马，
    事先不知道对方派遣顺序，不过可以根据上一轮对方的派出的马匹制定本轮的选择。
    为公子制定一种派遣策略，使赢得比赛的几率最大。
    提示：田忌的策略可用 random 确定
    g = [3,6,9]
    t = [2,5,8]
    '''
    random.shuffle(t)
    return t


# 公子的策略
def gongzi_s():
    return [6,9,3]
        
def gongzi_win():
    if gongzi_s()[0] > tianji_s()[0]:
        return True
    else:
        if gongzi_s()[1] > tianji_s()[1] and gongzi_s()[2] > tianji_s()[2]:
            return True
        else:
            return False


import itertools
def fujia2(gz,tj):
    '''
    现在将马分为 优、上、中、下、劣 五等，五局三胜制，抽象为列表[2,4,6,8,10] 与 [1,3,5,7,9] ，
    其他条件不变，计算出田忌有多少种赢得比赛的可能。
    '''
    win_time = 0
    gz_l = list(itertools.permutations(gz,len(gz)))
    tj_l = list(itertools.permutations(tj,len(tj)))
    l1 = []
    for i in gz_l:
        for j in tj_l:
            if fujia2_win(i,j):
                win_time += 1
                print(i,"<--",j)
    print("Tj win %s" %win_time)
def fujia2_win(g,t):
    n = 0
    for i in range(len(g)):
        if t[i] > g[i]:
            n += 1
    if n >= 3:
        return True
    else:
        return False
        
    

# 至少 1000 次测试
n = 0
for i in range(1000):
    if gongzi_win():
        n += 1
print(n)
gz = [2,4,6,8,10]
tj = [1,3,5,7,9]
fujia2(gz, tj)
# qiwang = [3, 6, 9]
# tianji = [2, 5, 8]
# print(race(qiwang, tianji))

