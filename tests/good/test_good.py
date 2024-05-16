from src.models.Good import Good

class TestGood:

    def test_create_good(self):
        unit_good = Good()
        assert unit_good.get_idItem == 0
        assert unit_good.get_name == ""
        assert unit_good.get_price == 0.0
        assert unit_good.get_stock == 0
        assert unit_good.get_imgSource == ""
    
    def test_create_good_notempty(self):
        unit_good = Good(123, "Pisang", 10, 132000.0, "")
        assert unit_good.get_idItem == 123
        assert unit_good.get_name == "Pisang"
        assert unit_good.get_price == 132000.0
        assert unit_good.get_stock == 10
        assert unit_good.get_imgSource == ""