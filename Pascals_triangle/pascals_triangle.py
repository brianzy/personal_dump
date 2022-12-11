class solution():
    def __init__(self,layer):
        self.layer = layer
    def PascalsT(self):
        result = []
        for i in range(self.layer):
            item=[1 for a in range(i+1)]
            if len(item)>2:
                new_list=[]
                for index, a in enumerate(result[-1]) :
                    if index+1 != len(result[-1]):
                        new_list.append(result[-1][index]+result[-1][index+1])
                #print(new_list)
                item = [item[0]]+new_list+[item[-1]]
            result.append(item)
        #print (result)
        return result    

