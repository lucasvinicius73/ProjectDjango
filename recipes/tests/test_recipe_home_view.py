from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):
    def tearDown(self) -> None: #Executado Depois da função
        return super().tearDown()
    
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

                    #Testes Home
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'Nenhuma Receita encontrada',
            response.content.decode('utf-8')
        )
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Recipe Title', content)
        self.assertIn('5 Porções',content)

        self.assertEqual(len(response_context_recipes),1 )
    
    def test_recipe_home_template_dont_load_recipeS_not_published(self):
        """Test recipe is_published False dont show"""
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        

        self.assertIn(
            'Nenhuma Receita encontrada',
            response.content.decode('utf-8')
        )
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