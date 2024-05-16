from src.models.Coupon import Coupon
from src.models.Coupon import FreeCoupon
from src.models.Coupon import DiscountCoupon

class TestCoupon:

    def test_create_coupon(self):
        unit_coupon = Coupon()
        assert unit_coupon.get_idCoupon == 0
        assert unit_coupon.get_code == ""

    def test_create_defined_coupon(self):
        unit_coupon = Coupon(5,"HESOYAM")
        assert unit_coupon.get_idCoupon == 5
        assert unit_coupon.get_code == "HESOYAM"

    def test_create_set_coupon(self):
        unit_coupon = Coupon()
        unit_coupon.set_idCoupon = 2222
        unit_coupon.set_code = "MUKACHINNO"
        assert unit_coupon.get_idCoupon == 2222
        assert unit_coupon.get_code == "MUKACHINNO"

    def test_create_free_coupon(self):
        unit_coupon = FreeCoupon()
        assert unit_coupon.get_idCoupon == 0
        assert unit_coupon.get_code == ""
        assert unit_coupon.get_idItem == 0
        assert unit_coupon.get_nItem == 0
        assert unit_coupon.get_idFree == 0
        assert unit_coupon.get_nFree == 0

    def test_create_defined_free_coupon(self):
        unit_coupon = FreeCoupon(69,"BERTO",132,34,6,234)
        assert unit_coupon.get_idCoupon == 69
        assert unit_coupon.get_code == "BERTO"
        assert unit_coupon.get_idItem == 132
        assert unit_coupon.get_nItem == 34
        assert unit_coupon.get_idFree == 6
        assert unit_coupon.get_nFree == 234

    def test_create_set_free_coupon(self):
        unit_coupon = FreeCoupon()
        unit_coupon.set_idCoupon = 2232
        unit_coupon.set_code = "FANUMTAXRIZZMAXXING"
        unit_coupon.set_idFree = 1
        unit_coupon.set_nFree = 2
        unit_coupon.set_idItem = 2
        unit_coupon.set_nItem = 1
        assert unit_coupon.get_idCoupon == 2232
        assert unit_coupon.get_code == "FANUMTAXRIZZMAXXING"
        assert unit_coupon.get_idFree == 1
        assert unit_coupon.get_nFree == 2
        assert unit_coupon.get_idItem == 2
        assert unit_coupon.get_nItem == 1

    def test_create_discount_coupon(self):
        unit_coupon = DiscountCoupon()
        assert unit_coupon.get_idCoupon == 0
        assert unit_coupon.get_code == ""
        assert unit_coupon.get_maxDiscount == 0
        assert unit_coupon.get_minBuy == 0
        assert unit_coupon.get_percentage == 0

    def test_create_defined_discount_coupon(self):
        unit_coupon = DiscountCoupon(2024,"OSKENAPASUSAH",125000,20,25000)
        assert unit_coupon.get_idCoupon == 2024
        assert unit_coupon.get_code == "OSKENAPASUSAH"
        assert unit_coupon.get_maxDiscount == 25000
        assert unit_coupon.get_minBuy == 125000
        assert unit_coupon.get_percentage == 20

    def test_create_set_discount_coupon(self):
        unit_coupon = DiscountCoupon()
        unit_coupon.set_idCoupon = 13
        unit_coupon.set_code = "SUTALOVESPYTHON"
        unit_coupon.set_maxDiscount = 20000
        unit_coupon.set_percentage = 20
        unit_coupon.set_minBuy = 40000
        assert unit_coupon.get_idCoupon == 13
        assert unit_coupon.get_code == "SUTALOVESPYTHON"
        assert unit_coupon.get_maxDiscount == 20000
        assert unit_coupon.get_minBuy == 40000
        assert unit_coupon.get_percentage == 20
        