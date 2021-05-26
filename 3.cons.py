l=list(map(int,input().split()))

def maxone(l):
      count=0
      flag=0
      for i in range(len(l)):
          
          if l[i]==0:
              count=0
          else:
              count=count+1
              flag=max(flag,count)
      
      print(flag)
         
              
      
maxone(l)
            
        
    
            
    
            
