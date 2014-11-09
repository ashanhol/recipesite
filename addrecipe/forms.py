from django import forms

from addrecipe.models import Recipe, Ingredient, Instruction, UNITS


# Create the form class.


class AddRecipeForm(forms.ModelForm):
    recipe_name = forms.CharField(max_length=100, label = 'Recipe Name')
    recipe_name.widget = forms.TextInput(attrs={'class': 'form-control', 'size' : 100, 'placeholder' : 'Recipe Name'})
    vegetarian = forms.CheckboxInput()
    vegetarian.widget = forms.CheckboxInput(attrs={'class': 'form-control'})
    vegan = forms.CheckboxInput()
    vegan.widget = forms.CheckboxInput(attrs={'class': 'form-control'})
    gluten_free = forms.CheckboxInput()
    gluten_free.widget = forms.CheckboxInput(attrs={'class': 'form-control'})
    soy_free = forms.CheckboxInput()
    soy_free.widget = forms.CheckboxInput(attrs={'class': 'form-control'})
    dairy_free = forms.CheckboxInput()
    dairy_free.widget = forms.CheckboxInput(attrs={'class': 'form-control'})

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'vegetarian', 'vegan', 'gluten_free', 'soy_free', 'dairy_free']

class AddIngredientForm(forms.ModelForm):
    ingredient_text = forms.CharField(max_length=100)
    ingredient_text.widget = forms.TextInput(attrs={'class': 'form-control', 'size' : 100, 'placeholder' : 'Enter Ingredient'})
    amount =  forms.FloatField(999.9)
    amount.widget = forms.TextInput(attrs={'class': 'form-control', 'size' : 999.9})
    unit = forms.CharField(max_length=10)
    unit.widget= forms.Select(choices = UNITS, attrs={'class' : 'form-control'})

    class Meta:
        model = Ingredient
        fields = ['ingredient_text', 'amount', 'unit']
        exclude = ['recipe']
        

class AddInstructionForm(forms.ModelForm):
    instruction_text = forms.CharField(max_length=200)
    instruction_text.widget = forms.TextInput(attrs={'class': 'form-control', 'size' : 200, 'placeholder' : 'Enter Instruction'})

    class Meta:
        model = Instruction
        fields = ['instruction_text']
        exclude = ['recipe']
