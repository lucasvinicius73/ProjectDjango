from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError

class RecipeModelTest(RecipeTestBase):
    
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_recipe_title_raises_error_if_title_has_more_than_65_char(self):
       self.recipe.title = 'A' * 75
       
       with self.assertRaises(ValidationError):
        self.recipe.full_clean() #Validação Ocorre aqui