class Taxi:
    def __init__(self,taxi_id):
        self.taxi_id=taxi_id
        self.earnings=0
        self.distance_covered=0
        self.loc='A'
        self.Available=True
    def __str__(self):
         return(f"Taxi id:{self.taxi_id},Earnings:{self.earnings},Location:{self.loc},Available:{self.Available}")


class BookingSystem:
    def __init__(self):
        self.taxis=[Taxi(i)for i in range(1,5)]


    def book_taxi(self,cus_n,pp,dp,):
        avail_taxi=[]
        temptax=[]
        tempdis=[]
        for tax in self.taxis:
            if tax.Available==True and tax.loc==pp:
                avail_taxi.append(tax)
        if not avail_taxi:
            avail_taxi=sorted([tax for tax in self.taxis if tax.Available==True],key=lambda t:(abs(ord(t.loc)-ord(pp)),t.earnings))
        if not avail_taxi:
            print("Taxi not available")
        dist = abs(ord(pp) - ord(dp)) * 15
        if dist <= 5:
            fare = 100
        else:
            fare = 100 + (dist - 5) * 10
        taxi_selec=avail_taxi[0]
        taxi_selec.Available=False
        taxi_selec.loc=dp
        taxi_selec.earnings+=fare

    def disp_ride_details(self,cus_n,pp,dp):
        dist = abs(ord(pp) - ord(dp)) * 15
        if dist <= 5:
            fare = 100
        else:
            fare = 100 + (dist - 5) * 10
        return (f"Customer Name:{cus_n},Pickup Location:{pp},Drop Location:{dp},Fare:{fare}")




    def trip_complete(self,taxi_id):
        for tax in self.taxis:
            if tax.taxi_id==taxi_id:
                tax.Available=True

    def display_taxi_avail(self):
        count=0
        for tax in self.taxis:
            #print(tax)
            if tax.Available==True:
                print(tax)
                count+=1
        #print(len(self.taxis))
        if count==0:
            print("0 taxis are available")


b1=BookingSystem()
#b1=BookingSystem('rini','A','C')
print("Available taxis:")
b1.display_taxi_avail()
b1.book_taxi('rini','A','C')
print(b1.disp_ride_details('rini','A','C'))
b1.book_taxi('Prisca','C','D')
print(b1.disp_ride_details('Prisca','C','D'))
b1.book_taxi('Jason','B','A')
print(b1.disp_ride_details('Jason','B','A'))
b1.book_taxi('Rohit','A','D')
print(b1.disp_ride_details('Rohit','A','D'))
print(f"No of taxis available after 4 rides booked:")
b1.display_taxi_avail()
b1.trip_complete(1)
print("Available taxi after completing 1st ride:")
b1.display_taxi_avail()
b1.trip_complete(2)
print("Available taxi after completing 2nd ride:")
b1.display_taxi_avail()
b1.trip_complete(3)
print("Available taxi after completing 3rd ride:")
b1.display_taxi_avail()
b1.trip_complete(4)
print("Available taxi after completing 4th ride:")
b1.display_taxi_avail()






