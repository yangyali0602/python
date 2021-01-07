

def counter(votes):
    count_dict = {}
    for i in votes:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


def append_vote(vote_list=[],max_votes = 10000):
    votes_name = []
    key_words_list = ['stop','delete_last','clear','menu']
    num_votes = 0
    while num_votes < max_votes:
        num_votes+=1
        a = input('输入命令或者指定投票给:').strip()
        if a in key_words_list:
            print('运行命令成功')
            if a == 'stop':
                break
            if a == 'delete_last':
                votes_name.pop()
            if a == 'clear':
                votes_name = []
            if a == 'menu':
                print('进入菜单页')
        elif a in [str(i) for i in range(1,len(vote_list)+1)]:
            votes_name.append(vote_list[int(a)-1])
            print('投票%s成功'%vote_list[int(a)-1])
        elif a not in vote_list:
            name = ','.join(vote_list)
            print('请投票给: %s 其中一人'%name)
        else:
            votes_name.append(a)
            print('投票%s成功'%a)
        b = input('是否继续投票(任意键:继续，stop:结束投票，help:查看命令，stats:查看当前统计信息)：').strip()
        if b == 'stop':
            break
        if b == 'help':
            print('内置命令：')
            print('1.stop:输入stop结束投票')
            print('2.delete_last:输入delete_last删除上一条投票')
            print('3.clear:输入clear删除所有投票')
            print('4.menu:回到菜单选择')
            print('------------------------------------------')
        if b == 'stats':
            count = counter(votes_name)
            describe(count,temp=True)

    return votes_name


def sort_by_value(votes,top_k = None):
    items=votes.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort(reverse=True)
    if top_k:
        return backitems[:top_k]
        # return [[backitems[i][1],backitems[i][0]] for i in range(top_k)]
    else:
        return backitems
        # return [[backitems[i][1],backitems[i][0]] for i in range(len(backitems))]


def describe(votes,temp=False):
    sum_votes = sum([v for v in votes.values()])
    if len(votes) ==0:
        mean_votes = '没有投票，无法计算平均票数'
    else:
        mean_votes = sum_votes/len(votes)
        mean_votes = float('%.2f'%mean_votes)
    if temp is True:
        print('目前总票数为：%s'%str(sum_votes))
    else:
        print('总票数：%s'%str(sum_votes))
        print('平均票数：%s' % mean_votes)
    final = sort_by_value(votes,10)
    for ind,i in enumerate(final):
        if temp is True:
            print('目前投票票数第%s名是 %s ，票数为:%s, 占总票数：%.2f%%' % (str(ind+1),i[1],str(votes[i[1]]),100*i[0]/sum_votes))
        else:
            print('本次投票票数第%s名是 %s ，票数为:%s, 占总票数：%.2f%%' % (str(ind+1),i[1],str(votes[i[1]]),100*i[0]/sum_votes))


def append_candidates():
    vote_list =[]
    while 1:
        candidate = input('输入第%s位候选名:'%(len(vote_list)+1)).strip()
        if candidate == 'finish':
            if len(vote_list) !=0:
                break
            else:
                print('请输入候选人名')
        elif candidate == 'delete':
            vote_list.pop()
        elif len(candidate)==0:
            pass
        else:
            vote_list.append(candidate)
            print('添加候选名成功')
        prompt = input('按任意键继续输入候选名(输入finish退出，并开始投票)')
        if prompt.strip() == 'finish':
            if len(vote_list) !=0:
                break
            else:
                print('请输入候选人名')
        candi_name = ','.join(vote_list)
        print('当前候选人名单为：%s'%candi_name)
    return vote_list


def online_voting():
    print('欢迎使用在线投票系统')
    print('使用规则介绍：')
    print('1.启动在线投票系统之后，会出现命令解释，这是在之后的投票过程中的一些功能命令')
    print('2.之后，系统会提醒您输入候选名单，例如本次投票的候选名单为(张三、李四)，我们需要对其一个一个按顺序输入其名字')
    print('3.输入完信息之后，需要按enter提交')
    print('在线投票系统已经开启')
    print('------------------------------------------')
    print('请输入本次投票的候选名单')
    print('如果发现候选名填错，可以输入delete来删除上一个填入的候选名')
    vote_list = append_candidates()
    seq_vote_list = [str(i)+'.'+vote_list[i-1] for i in range(1,len(vote_list)+1)]
    name = ' ,'.join(seq_vote_list)
    print('本次投票候选名单为  %s'%name)
    print('请输入候选名单的内容，或者输入其序号，例如：输入1代表投票给候选名单的第一位')
    print('------------------------------------------')
    print('投票内置命令如下：')
    print('1.stop:输入stop结束投票')
    print('2.delete_last:输入delete_last删除上一条投票')
    # print('2.-:输入\'候选名\'-\'n票数\'删除这个候选名n票')
    # print('例如 zhangsan-2 表示将zhangsan的票数减2票')
    print('3.clear:输入clear删除所有投票')
    print('4.menu:回到菜单选择')
    # print('5.save:保存记录')
    print('------------------------------------------')
    votes = append_vote(vote_list=vote_list)
    votes_count = counter(votes)
    print('投票已经结束')
    print('------------------------------------------')
    print('输出统计信息：')
    describe(votes_count)


if __name__ == '__main__':
    online_voting()
    # a = {'a':789,'b':123,'c':1,'d':2}
    # value = sort_by_value(a)
    # print(value)
    # print(a.items())

