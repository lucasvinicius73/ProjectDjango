from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):
    def tearDown(self) -> None: #Executado Depois da função
        return super().tearDown()


    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id':1})
            )
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
    

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        self.make_recipe(title= needed_title)
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        autor1 = {
            "first_name" : "vini",
            "last_name" : 'name',
            "username" : 'vinizin',
            "password" : '123456',
            "email" : 'vini@email.com',
        }
        autor2 = {
            "first_name" : "zezin",
            "last_name" : 'silva',
            "username" : 'zezin23',
            "password" : '123456',
            "email" : 'zezin23@email.com',
        }
        """Test recipe is_published in category False dont show"""
        recipe1 = self.make_recipe(title="Test 1", is_published=True, author_data= autor1, slug="slug1")
        recipe2 = self.make_recipe(title="Test 2", is_published=True, author_data= autor2,slug="slug2")
        recipe3 = self.make_recipe(is_published=False, slug="slug3")

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe3.category.id})
        )
        self.assertEqual(response.status_code, 404)
