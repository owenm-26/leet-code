class Solution(object):
    def stringCompression(chars):
        s = []
        i=0
        while i < len(chars)-1:
            streak = 1
            print('i',i)

            while streak + i < len(chars) and chars[i+ streak -1] == (chars[i+streak]):
                streak +=1
            
            if(streak == 1):
                s.append(chars[i])
            elif(streak > 10):
                s.append(chars[i])
                for i in range(len(str(streak))):
                    s.append(str(streak)[i])
            else:
                s.append(chars[i])
                s.append(str(streak))
            i += streak 
            
               
            
        chars = s
        return chars
    answer = stringCompression( ["a","b","b","b","b","b","b","b","b","b","b","b","b"])
    print(answer)