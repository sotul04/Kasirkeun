from models import Triple, Transaction, Good

class TestTransaction:
    def test_create_triple(self) : 
        unit_triple = Triple()
        assert unit_triple.get_first == None 
        assert unit_triple.get_second == None 
        assert unit_triple.get_third == None

    def test_create_triple_notempty(self) : 
        unit_good = Good()
        unit_triple = Triple(unit_good, 12, 4.0)
        
        assert unit_triple.get_first == unit_good
        assert unit_triple.get_second == 12 
        assert unit_triple.get_third == 4.0


    def test_create_triple_sets(self) : 
        unit_good = Good()
        unit_triple = Triple()

        unit_triple.set_first = unit_good 
        unit_triple.set_second = 6
        unit_triple.set_third = 2.5
        assert unit_triple.get_first == unit_good
        assert unit_triple.get_second == 6 
        assert unit_triple.get_third == 2.5

    def test_create_transaction(self) : 
        unit_transaction = Transaction()
        assert unit_transaction.get_idTransaction == 0 
        assert unit_transaction.get_couponFree == None 
        assert unit_transaction.get_couponDiscount == None 
        assert unit_transaction.get_items == []
        assert unit_transaction.get_totalPrice == 0.0
        assert unit_transaction.get_datetime == ""
        assert unit_transaction.get_discount == 0.0

    def test_create_transaction_notempty(self) : 
        unit_good1 = Good()
        unit_triple1 = Triple(unit_good1, 2, 12.5) 
        unit_good2 = Good()
        unit_triple2 = Triple(unit_good2, 4, 7.5) 
        unit_transaction = Transaction(1, 1, 1, [unit_triple1, unit_triple2], 55.0, "2012-12-12", 12)

        assert unit_transaction.get_idTransaction == 1
        assert unit_transaction.get_couponFree == 1 
        assert unit_transaction.get_couponDiscount == 1 
        assert unit_transaction.get_items == [unit_triple1, unit_triple2]
        assert unit_transaction.get_totalPrice == 55.0
        assert unit_transaction.get_datetime == "2012-12-12"
        assert unit_transaction.get_discount == 12

    def test_set_transaction(self) : 
        unit_good1 = Good()
        unit_triple1 = Triple(unit_good1, 2, 12.5) 

        unit_good2 = Good()
        unit_triple2 = Triple(unit_good2, 4, 7.5) 

        unit_transaction = Transaction()
        unit_transaction.set_idTransaction = 1 
        unit_transaction.set_couponFree = 1 
        unit_transaction.set_couponDiscount = 1 
        unit_transaction.set_items = [unit_triple1, unit_triple2]
        unit_transaction.set_totalPrice = 55.0
        unit_transaction.set_datetime = "2012-12-12"
        unit_transaction.set_discount = 12
        assert unit_transaction.get_idTransaction == 1
        assert unit_transaction.get_couponFree == 1 
        assert unit_transaction.get_couponDiscount == 1 
        assert unit_transaction.get_items == [unit_triple1, unit_triple2]
        assert unit_transaction.get_totalPrice == 55
        assert unit_transaction.get_datetime == "2012-12-12"
        assert unit_transaction.get_discount == 12

    def test_method_transaction(self) : 
        unit_good1 = Good(idItem= 1)
        unit_good2 = Good(idItem= 2)
        unit_good3 = Good(idItem= 3)
        unit_good4 = Good(idItem= 4)

        unit_triple1 = Triple(unit_good1, 2, 12.5) 
        unit_triple2 = Triple(unit_good2, 4, 7.5) 
        unit_triple3 = Triple(unit_good3, 2, 12) 
        unit_transaction = Transaction(1, 1, 1, [unit_triple1, unit_triple2], 55.0, "2012-12-12", 12)
 

        assert unit_transaction.getItem(0) == unit_triple1
        assert unit_transaction.getItemGood(0) == unit_triple1.first
        assert unit_transaction.getItemQuantity(0) == unit_triple1.second
        assert unit_transaction.getItemPrices(0) == unit_triple1.third
        assert unit_transaction.getItem(1) == unit_triple2

        unit_transaction.setItem(1, unit_triple1) 
        assert unit_transaction.getItem(1) == unit_triple1

        unit_transaction.addItem(unit_triple3) 
        assert unit_transaction.getItem(2) == unit_triple3
        assert unit_transaction.getItemPosition(unit_good3) == 2

        unit_transaction.add(unit_good4, 2, 2.0)
        assert unit_transaction.getItemGood(3) == unit_good4 
        assert unit_transaction.getItemQuantity(3) == 2
        assert unit_transaction.getItemPrices(3) == 2.0

        assert unit_transaction.cancelOneItem(unit_good4) == True 
        assert unit_transaction.getItemGood(3) == unit_good4
        assert unit_transaction.getItemQuantity(3) == 1
        assert unit_transaction.getItemPrices(3)  == 2.0

        assert unit_transaction.cancelOneItem(unit_good4) == True 
        assert len(unit_transaction.get_items) == 3

        assert unit_transaction.cancelOneItem(unit_good4) == False

