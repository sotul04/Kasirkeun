from src.models.Good import Good

class TestGood:

    def test_create_good(self):
        unit_good = Good()
        assert unit_good.get_idItem == 0
        assert unit_good.get_name == ""
        assert unit_good.get_price == 0.0
        assert unit_good.get_stock == 0
        assert unit_good.get_imgSource == ""