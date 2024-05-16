import os

from controller import *
from models import *
from data import connection

class TestController:

    def test_good_controller(self):
        unit_good_1 = Good(idItem=1, name="Test 1", stock=10, price=10000, imgSource="dummyImage")
        unit_good_2 = Good(idItem=2, name="Test 2", stock=10, price=10000, imgSource="dummyImage")
        unit_good_3 = Good(idItem=3, name="Berto 3", stock=10, price=10000, imgSource="dummyImage")
        unit_good_4 = Good(idItem=4, name="Test 4", stock=0, price=10000, imgSource="dummyImage")
        unit_good_5 = Good(idItem=5, name="Berto 5", stock=10, price=10000, imgSource="dummyImage")

        GoodController.addItem(unit_good_1)
        GoodController.addItem(unit_good_2)

        assert GoodController.getAll() == [(1, "Test 1", 10, 10000, "dummyImage"), (2, "Test 2", 10, 10000, "dummyImage")]

        GoodController.addItem(unit_good_3)
        GoodController.addItem(unit_good_4)
        GoodController.addItem(unit_good_5)
        assert GoodController.getAllGoods() == [unit_good_1, unit_good_2, unit_good_3, unit_good_4, unit_good_5]

        assert GoodController.getSome("Berto") == [(3, "Berto 3", 10, 10000, "dummyImage"), (5, "Berto 5", 10, 10000, "dummyImage")]
        assert GoodController.getSomeGoods("Test") == [unit_good_1, unit_good_2, unit_good_4]

        assert GoodController.isItemExist(1) == True
        assert GoodController.isItemExist(2) == True
        assert GoodController.isItemExist(3) == True
        assert GoodController.isItemExist(4) == True
        assert GoodController.isItemExist(5) == True
        assert GoodController.isItemExist(6) == False

        assert GoodController.getItem(1) == unit_good_1

        assert GoodController.sellOneGood(2) == True
        assert GoodController.getItem(2).get_stock == 9
        
        GoodController.cancelOneGood(2)
        assert GoodController.getItem(2).get_stock == 10

        assert GoodController.sellOneGood(4) == False

        unit_good_6 = Good(idItem=3, name="Test 6", stock=10, price=10000, imgSource="dummyImage")
        GoodController.setEditedGood(unit_good_6)
        assert GoodController.getItem(3) == unit_good_6

        GoodController.deleteItem(5)
        assert GoodController.isItemExist(5) == False
    
    def test_coupon_controller(self):
        unit_free_coupon_1 = FreeCoupon(1, "BERTOOO1", 1, 2, 2, 1)
        unit_free_coupon_2 = FreeCoupon(2, "BERTOOO2", 3, 4, 1, 1)

        CouponController.addFreeCoupon(unit_free_coupon_1)
        CouponController.addFreeCoupon(unit_free_coupon_2)

        unit_discount_coupon_1 = DiscountCoupon(3, "SUTHAAA1", 12000, 50, 4000)
        unit_discount_coupon_2 = DiscountCoupon(4, "SUTHAAA2", 40000, 80, 10000)

        CouponController.addDiscountCoupon(unit_discount_coupon_1)
        CouponController.addDiscountCoupon(unit_discount_coupon_2)

        assert CouponController.isDiscountCouponExist("SUTHAAA1")
        assert CouponController.isFreeCouponExist("BERTOOO2")

        assert CouponController.getFreeCoupon("BERTOOO1") == unit_free_coupon_1
        assert CouponController.getDiscountCoupon("SUTHAAA2") == unit_discount_coupon_2

        assert CouponController.getAllCoupon() == [(1, "BERTOOO1", "free_coupon"), (2, "BERTOOO2", "free_coupon"), (3, "SUTHAAA1", "discount_coupon"), (4, "SUTHAAA2", "discount_coupon")]

        assert CouponController.getAll() == [unit_free_coupon_1, unit_free_coupon_2, unit_discount_coupon_1, unit_discount_coupon_2]

        assert CouponController.getSome("SUTHA") == [(3, "SUTHAAA1", "discount_coupon"), (4, "SUTHAAA2", "discount_coupon")]

        assert CouponController.getSomeCoupon("BERTO") == [unit_free_coupon_1, unit_free_coupon_2]

        unit_discount_coupon_3 = DiscountCoupon(3, "SUTHAAA1", 0, 90, 3000)
        unit_free_coupon_3 = FreeCoupon(1, "BERTOOO1", 2, 4, 4, 1)

        CouponController.setEditedDiscountCoupon(unit_discount_coupon_3)
        assert CouponController.getDiscountCoupon("SUTHAAA1") == unit_discount_coupon_3

        CouponController.setEditedFreeCoupon(unit_free_coupon_3)
        assert CouponController.getFreeCoupon("BERTOOO1") == unit_free_coupon_3

        assert CouponController.deleteByCode("BERTOOO1") == True
        assert CouponController.deleteByCode("BERTOOO1") == False

        assert CouponController.deleteByID(4) == True
        assert CouponController.deleteByID(4) == False

    def test_transaction_controller(self):

        connection.close()
        os.remove("src/data/KasirkeunData.db")