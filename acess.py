import code as x 

x.create("shridhar",25)
#to create a key with key_name,value given and with no time-to-live property


x.create("src",70,3600) 



x.read("shridhar")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("src")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("shridhar",50)

x.modify("shridhar",55)
#it replaces the initial value of the respective key with new value 

 
x.delete("shridhar")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
