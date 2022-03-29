class Operator:
    def sum(*arr):
        res = 0
        for i in arr:
            res += i
        return res
    
    def proc(*arr):
        res = 1
        for i in arr:
            res *= i
        return res
    
    def cleanerDupl(arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res
        
    def union(*arrs):
        res = []
        for arr in arrs:
            for i in arr:
                res.append(i)
        return Operator.cleanerDupl(res)  
        
    def intersect(*arrs):
        res = []
        for arr in arrs:
            for i in arr:
               pass
               
    def print_arr(arr):
        txt = "["
        for i,e in enumerate(arr):
            txt += str(e)
            if i < len(arr)-1:
                txt += ","
        txt += "]" 
        return txt
        
    def print_dict(dict):
        txt = "{\n"
        for key in dict:
            txt += " "+str(key)+": "+Operator.print_arr(dict[key])+"\n"
        txt += "}"
        return txt
        
    def print_tuple(tuple):
        txt = "("
        for i in tuple:
            txt += " "+str(i)
            if i < len(tuple)-1:
                txt += ","
        txt += ")"
        return txt