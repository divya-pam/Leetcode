class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n==0: return True
        for i in range(len(flowerbed)):
            if n==0:return True
            if len(flowerbed) ==1 and flowerbed[0]==0:
                n-=1
                flowerbed[i]=1
            if i==0 and i<len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i+1]==0 and i==0:
                flowerbed[i]=1
                n-=1
            elif i>0 and i<(len(flowerbed)-1) and flowerbed[i-1:i+2]==[0]*3:
                flowerbed[i]=1
                n-=1
            elif i==len(flowerbed)-1 and flowerbed[-1]==0 and flowerbed[-2]==0:
                flowerbed[i]=1
                n-=1
        return True if n==0 else False



        if len(flowerbed)==1 and flowerbed[0]==0 and n==1:return True
        if len(flowerbed)==1 and n>=1: return False
        for i in range(len(flowerbed)-1):
            if n==0: return True
            if i>0 and flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                n-=1
            elif flowerbed[i]==0 and flowerbed[i+1]==0 and i==0:
                flowerbed[i]=1
                n-=1
        if flowerbed[-1]==0 and flowerbed[-2]==0 and n>0:
            n-=1
        if n==0:return True 
        else:  False
