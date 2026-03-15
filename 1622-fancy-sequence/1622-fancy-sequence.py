inv0=[0]*101
MOD=10**9+7
def compute_inv():
    if inv0[1]==1: return
    inv0[1]=1
    for m in range(2, 101):
        inv0[m]=pow(m, -1, MOD)
class Fancy:
    def __init__(self):
        self.n=0
        self.nums=[]
        self.add=[]
        self.inv=[]
        self.curMul=1
        self.curAdd=0
        self.curInv=1
        compute_inv()

    def append(self, val: int) -> None:
        self.nums.append(val)
        self.add.append(self.curAdd)
        self.inv.append(self.curInv)
        self.n+=1

    def addAll(self, inc: int) -> None:
        self.curAdd=(self.curAdd+inc)%MOD

    def multAll(self, m: int) -> None:
        self.curMul=(self.curMul*m)%MOD
        self.curAdd=(self.curAdd*m)%MOD
        self.curInv=(self.curInv*inv0[m])%MOD

    def getIndex(self, i: int) -> int:
        if i>=self.n: return -1
        return ((self.nums[i]-self.add[i])*self.inv[i]*self.curMul+self.curAdd)%MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)