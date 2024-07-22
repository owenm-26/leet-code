class RecentCounter(object):
    def __init__(self) -> None:
        self.counter = 0
        self.requestTimes = []
    
    def ping(self, t):
        self.counter += 1
        self.requestTimes.append(t)
        sameTime = 1
        for i in range(len(self.requestTimes)):
            if(t - 3000 <= self.requestTimes[i]):
                # print('t', t )
                # print('self.requestTimes[i]', self.requestTimes[i] )
                sameTime = len(self.requestTimes)-i
                break
        print(sameTime)
        return sameTime


recentCounter = RecentCounter()
recentCounter.ping(1);     #// requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   #// requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  #// requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  #// requests = [1, 100, 3001, 3002], range is [2,3002], return 3

