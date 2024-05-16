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
    
    def test_create_good_sets(self):
        unit_good = Good()
        unit_good.set_idItem = 10
        unit_good.set_name = "Jagung"
        unit_good.set_price = 50000.0
        unit_good.set_stock = 10
        unit_good.set_imgSource = "ini_gambar_dummy"
        assert unit_good.get_idItem == 10
        assert unit_good.get_name == "Jagung"
        assert unit_good.get_price == 50000.0
        assert unit_good.get_stock == 10
        assert unit_good.get_imgSource == "ini_gambar_dummy"