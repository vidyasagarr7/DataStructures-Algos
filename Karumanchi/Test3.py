

class Bike:
    def __init__(self,name='Celarifare',pressure=0):
        self.name = name
        self.tyre_pressure = pressure if pressure > 0 else 0

    def status(self):
        print('Object name {} and pressure {}'.format(self.name,self.tyre_pressure))

    def move(self,distance):
        if distance < 1 :
            print('bike cant move a distance less than one')

        else  :
            if distance <= self.tyre_pressure*1000 :
                print('bike is moved by the distance {}'.format(distance))
                self.tyre_pressure = self.tyre_pressure - distance/1000
            else :
                print('bike doesnt have enough tyre pressure to be moved')
        self.status()

    def repressurise(self,amount_pressure):
        if amount_pressure >= 1:
            self.tyre_pressure = self.tyre_pressure + amount_pressure
            print('tyre pressure of {} has been added '.format(amount_pressure))
        else :
            print('bike cant be repressurized with amount less than one')
        self.status()

if __name__=="__main__":
    bike = Bike()