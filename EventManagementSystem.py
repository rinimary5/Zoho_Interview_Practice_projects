from datetime import datetime,timedelta
class Events:
    def __init__(self,eid,ename,edetails,edate):
        self.event_id=eid
        self.event_name=ename
        self.event_details= edetails
        self.event_date=edate
    def __str__(self):
        return(f"Event Id:{self.event_id},Event Name:{self.event_name},Event Details:{self.event_details},Event Date:{self.event_date}")

class Register:
    def __init__(self,user,event):
        self.user=user
        self.event=event
    def __str__(self):
        return(f"User Name{self.user.user_name},Registered Event Name:{self.event.event_name}")
class User:
    def __init__(self,uid,uname):
        self.user_id=uid
        self.user_name=uname
    def __str__(self):
        return(f"User Id:{self.user_id},User Name:{self.user_name}")



class Manager:
    def __init__(self):
        self.event_obj=[]
        self.user_obj=[]
        self.register_obj=[]
        self.notification=[]
    def createEvent(self,ename,edetails,edate):
        eid=len(self.event_obj)+1
        newEvent=Events(eid,ename,edetails,edate)
        self.event_obj.append(newEvent)

    def updateEvent(self,eid,ename,edetails,edate):
        for i in self.event_obj:
            if eid==i.event_id:
                event=i
        event.event_name=ename
        event.event_details=edetails
        event.even_date=edate

    def deleteEvent(self,eid):
        for i in self.event_obj:
            if eid==i.event_id:
                event=i
        self.event_obj.remove(event)

    def RegisterUser(self, uname):
        uid=len(self.user_obj)+1
        newUser=User(uid,uname)
        self.user_obj.append(newUser)
    def EventRegistration(self,uid,eid):
        print(self.event_obj)
        for i in self.user_obj:
            if uid==i.user_id:
                user=i
        #print(user)
        for i in self.event_obj:
            if eid==i.event_id:
                event=i
        #print(event)
        newRegister=Register(user,event)
        self.register_obj.append(newRegister)

    def DisplayEventDetails(self,eid):
        for i in self.event_obj:
            if eid==i.event_id:
                event=i
        print(event)

    def CancelRegistration(self,uid,eid):
        for i in self.event_obj:
            if eid==i.event_id:
                event=i
        for i in self.user_obj:
            if uid==i.user_id:
                user=i
        for i in self.register_obj:
            if i.user.user_id==uid and i.event.event_id==eid:
                register=i
        self.register_obj.remove(register)

    def Notification(self,uid,eid,days_before):
        for i in self.event_obj:
            if eid==i.event_id:
                event=i
        for i in self.user_obj:
            if uid==i.user_id:
                user=i
        notification_date=(datetime.strptime(event.event_date,'%Y-%m-%d')-timedelta(days=days_before)).strftime('%Y-%m-%d')
        self.notification.append((user,event,notification_date))






def admin(manager):
    while True:
        print("1.Create Event")
        print("2.Update Event")
        print("3.Delete Event")
        print("4.Back")
        ch=input("Enter your choice")
        if ch=='1':
            ename=input("Enter event name:")
            edetails=input("Enter event details:")
            edate=input("Enter event date(yyyy-mm-dd):")
            manager.createEvent(ename,edetails,edate)
        elif ch=='2':
            eid=int(input("Enter the event id that you want to update:"))
            ename=input("Enter new event name:")
            edetails=input("Enter new event details:")
            edate=input("Enter new event date:")
            manager.updateEvent(eid,ename,edetails,edate)
        elif ch=='3':
            eid=int(input("Enter the event id that you want to delete: "))
            manager.deleteEvent(eid)
        elif ch=='4':
            break


def user(manager):
    while True:
        print("1.User Registration")
        print("2.Register for event")
        print("3.Cancel Registration")
        print("4.View Event Details")
        print("5.Back")
        ch=input("Enter your choice:")
        if ch=='1':
            uname=input("Enter User Name:")
            manager.RegisterUser(uname)
        elif ch=='2':
            uid=int(input("Enter User Id:"))
            eid = int(input("Enter Event Id that you want to register:"))
            manager.EventRegistration(uid,eid)
            days_before = int(input("Enter days before event to send reminder: "))
            manager.Notification(uid,eid,days_before)
        elif ch=='3':
            uid = int(input("Enter User Id:"))
            eid = int(input("Enter Event Id that you want to Cancel:"))
            manager.CancelRegistration(uid,eid)
        elif ch=='4':
            eid=int(input("enter event id whose details you want to view:"))
            manager.DisplayEventDetails(eid)
        elif ch=='5':
            break


def main():
    manager=Manager()
    while True:
        print("1.Admin")
        print("2.User")
        print("3.Exit")
        ch=input("Enter your choice")
        if ch=='1':
            admin(manager)
        elif ch=='2':
            user(manager)
        elif ch=='3':
            break

if __name__=="__main__":
    main()






















