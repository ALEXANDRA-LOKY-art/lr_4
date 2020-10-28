users=[["root","admin","guest","user","new_user","sasha"],["1","2","3","4","5","6"],["Sasha","Oleg","Pasha","Dasha","Semen","Andrey"],["Super User","Sis admin","Gen Dir","Manager","Client","Agent"]]
objects=[[0,1,2,3],["Object1","Object2","Object3","Object4"],["1","2","3","4"],["doc","txt","exe","rar"]]
def getAccess(user_id):
    object_id=int(input("Enter object number\n"))
    if (user_id==objects[2][object_id]):
        print("Allow access")
    else:
        print("Access denied. Not enough rights.")
def logIn(user_id):
    if (user_id in users[1]):
        return True
    return False
def allObjects():
    for object_id in range(len(objects[0])):
        print(str(objects[0][object_id])+" "+objects[1][object_id]+" "+objects[2][object_id]+" "+objects[3][object_id])
command=""
current_user=None
current_obj=None
while(command!="cl"):
    if (current_user==None):
        id=input("Enter user id : \n")
        if logIn(id):
            current_user=id
    command=input("Enter command : \n")
    if command=="w":
        allObjects()
        getAccess(current_user)
    if command=="r":
        allObjects()
        getAccess(current_user)
    if command=="e":
        allObjects()
        getAccess(current_user)
