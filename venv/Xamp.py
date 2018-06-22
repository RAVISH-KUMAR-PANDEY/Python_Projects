import mysql.connector
class student:
    def __init__(self,roll, name,age,email,address):
        self.roll=roll
        self.name=name
        self.age=age
        self.email=email
        self.address=address

    def Show(self):
        print("Roll: {}, Name:{}, ".format(self.roll,self.name))

    def getdetails(self):
        data = "{},{},{},{},{}\n".format(self.name, self.roll, self.age, self.email, self.address)
        return data

s1 = student(1,"Ravish",20,"abc@gmail.com","Redwood Shores")
s2=student(2,"Jappan",21,"abd@gmail.com","Ludhiana")
s1.Show()
'''
file=open("Students.txt",'a')
data1=s1.getdetails()
data2=s2.getdetails()
file.write(data1)
file.write(data2)
file.close()
'''
con = mysql.connector.connect(user="root",password='',host='127.0.0.1',database='Ravish')
print(con.is_connected())
#print(type(con))
cursor=con.cursor()

#sql="insert into student values(null,'Ravi',20,'abc@example.com','Doraha') "
#cursor.execute(sql)
#con.commit()
#sql1="insert into student values (null,'{}','{}','{}','{}')".format(s2.name,s2.age,s2.email,s2.address)
#cursor.execute(sql1)
#con.commit()
print("Student Saved!!")

sql2="select * from student"
cursor.execute(sql2)

#row = cursor.fetchone()
#print(row)
Stud=[]
for row in cursor:
    print(row)
    s=student(row[0],row[1],row[2],row[3],row[4])
    Stud.append(s)

