class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split('/')
        answer = ['/']
        print(pathList)
        
        for p in pathList:
            if p == '..':
                if len(answer) != 1:
                    answer.pop()
                    answer.pop()
            elif p == '.':
                continue
            elif p == "":
                continue
            else:
                answer.append(p)
                answer.append('/')
        
        if len(answer) != 1:
            answer.pop()
            
        answerStr = ''.join(map(str, answer))
        return answerStr