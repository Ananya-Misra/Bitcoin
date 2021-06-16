import csv
final=[]
weight1=[]
weight_sum=0
fee_sum=[]
# FUNCTION FOR SEACHING FOR PARENT FEE AND INCLUDING IT BEFORE THE TRANSACTION ID IN FINAL LIST
def search(trans,parents,arr,weight,pos):
    x =parents[pos].split(";")
    for value in x:
     io=0
     f=0
     for val in trans:
        if(val==value):
            pos1=io
            final.append(val)
            weight1.append(weight[pos1])
            global weight_sum
            weight_sum= weight_sum+int(weight[pos1])
            fee_sum.append(arr[pos1])
             # REMOVING TRANSACTION ID AND DETAILS OF PARENT AFTER APPENDING TO FINAL LIST
            arr.pop(pos1)
            trans.pop(pos1)
            weight.pop(pos1)
            parents.pop(pos1)
            f=1
            break
        io=io+1     
     if(f==1):
         pos=pos-1
    return pos

#FUNCTION FOR FINDING THE LARGEST FEE TRANSACTION ID AND APPENDING IT TO FINAL LIST 
def find(arr,parents,trans,weight,pos):
      global weight_sum
      if(parents[pos]!=""):
        pos=search(trans,parents,arr,weight,pos)      
      final.append(trans[pos]) 
      weight1.append(weight[pos])
      fee_sum.append(arr[pos])
      weight_sum= weight_sum+int(weight[pos])
      
    # REMOVING TRANSACTION ID AND ITS DETAILS AFTER APPENDING TO FINAL LIST
      arr.pop(pos)
      trans.pop(pos)
      weight.pop(pos)
      parents.pop(pos)

# READING FROM CSV
with open("C:\\Users\\HP\\Desktop\\mempool.csv", 'r') as file:
    reader = csv.reader(file)
    arr = []
    parents=[]
    trans=[]
    weight=[]  
    # INITIALIZING ARRAYS FOR FEE, TRANSACTION, PARENT, AND WEIGHT
    for row in reader:
        if(row[1]!="fee"):
            arr.append(row[1])
            parents.append(row[3])
            trans.append(row[0])
            weight.append(row[2])
    
    #FINDING THE LARGEST FEE AND CHECKING FOR ITS PARENTS TILL WEIGHT SUM DOESN'T EXCEED 4,000,000 
    while(weight_sum<4000000):
        pos=0
        s=0
        i1=0
        for large in arr:
            if(int(large)>s):
                s=int(large)
                pos=i1
            i1=i1+1  
        find(arr,parents,trans,weight,pos)  
# CREATING FINAL LIST WHERE WEIGHT SUM DOESN'T EXCEED 4,000,000 
summer=fees=fee1=summer1=0
transactions=[]
for finale in range(len(final)):
    summer=summer+int(weight1[finale]) 
    fees=fees+int(fee_sum[finale]) 
    if(int(summer) < 4000000): 
      transactions.append(final[finale])
      summer1=summer
      fee1=fees


# CREATING FINAL REQUIRED BLOCK WITH THE 4 ATTRIBUTES REFFERED THIS YOUTUBE VIDEO LINK https://www.youtube.com/watch?v=pYasYyjByKI&list=RDCMUC8wZnXYK_CGKlBcZp-GxYPA&start_radio=1&rv=pYasYyjByKI&t=0
import hashlib
class Block:
        def __init__(self,transaction_list,fee,weight,parents):
            self.weigt=int(weight)
            self.transaction_list=transaction_list
            self.fee=int(fee)
            self.parents=parents
            self.block_data="-".join(transaction_list)+"-"+str(fee)+"-"+str(weight)+"-"+parents
            self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()
        def prints_transactions(self):
            for id in self.transaction_list:
                print(id)

# CREATING INSTANCE OF THE CLASS BLOCK
initial_block=Block(transactions,fee1,summer1,"")
initial_block.prints_transactions()

       