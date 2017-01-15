

class Player :
    """
    Player class
    """
    def __init__(self,name='',MAX_ITEMS=0,items=[]):
        self.name = name
        self.MAX_ITEMS = MAX_ITEMS
        self.items = items


    def inventry(self):
        """
        Function to display the items in the items list if they exist.
        :return:
        """
        if len(self.items) > 0 :
            for item in self.items :
                print(item)
        else :
            print('There are no items in the items list')

    def take(self,new_item):
        """

        :param new_item:
        :return:
        """

        if len(self.items) < self.MAX_ITEMS :
            self.items.append(new_item)
        else :
            print('The items for the player is full, cannot add anymore items')

    def drop(self,item):
        """

        :param item:
        :return:
        """

        if len(self.items) >0 :
            if item in self.items :
                self.items.remove(item)
            else :
                print('Player doesnt have the item : {}'.format(item))
        else :
            print('Players dosnt have the item : {}'.format(item))


if __name__=='__main__':
    player1 = Player(name='sagar',MAX_ITEMS=10)

    for i in range(1,9):
        player1.take(i)



    player1.drop(5)
    player1.inventry()

    print(player1.name)
    print(player1.MAX_ITEMS)
    print(player1.items)