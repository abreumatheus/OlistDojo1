from src.models.sport import Sport
import pytest

class TestSportModel:

    @pytest.fixture
    def create_instance(self):
        sport = Sport('Esporte1', 'Esporte legal')
        return sport

    def test_sport_instance(self, create_instance):
        assert isinstance(create_instance, Sport)

    def test_sport_name_empty(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.name = ''

    def test_sport_name_len(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.name = 'um nome bem grandão'*100

    def test_sport_name_no_str(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.name = 100


    def test_sport_description_len(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.description = 'descrição'*500


    def test_sport_description_no_string(self,create_instance):
        with pytest.raises(TypeError):
            create_instance.description = 10
