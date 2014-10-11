from django import forms

from addrecipe.models import Recipe, Ingredient, Instruction, UNITS


# Create the form class.

#class AddRecipeForm(ModelForm):
#    class Meta:
#        model = Recipe
#        fields = ['recipe_name']

#class AddIngredientForm(ModelForm):
#    class Meta:
#        model = Ingredient
#        fields = ['recipe', 'ingredient_text', 'amount', 'unit']


#class AddRecipeForm(forms.Form):
#    recipe_name = forms.CharField(max_length=100)

#class AddIngredientForm(forms.Form):
#    recipe = forms.ModelChoiceField(queryset=Recipe.objects.all())
#    ingredient_text = forms.CharField(max_length=100)
#    amount =  forms.FloatField(0.0) #default = 0.0
#    unit = forms.CharField(max_length=10, widget=forms.Select(choices= UNITS))

class AddRecipeForm(forms.ModelForm):
    recipe_name = forms.CharField(max_length=100)
    class Meta:
        model = Recipe
        fields = ['recipe_name']

class AddIngredientForm(forms.ModelForm):
    #recipe = forms.ModelChoiceField(queryset=Recipe.objects.all())
    ingredient_text = forms.CharField(max_length=100)
    amount =  forms.FloatField(999.9) 
    unit = forms.CharField(max_length=10, widget=forms.Select(choices= UNITS))
    
    
    class Meta:
        model = Ingredient
        fields = ['ingredient_text', 'amount', 'unit']
        exclude = ['recipe']


class AddInstructionForm(forms.ModelForm):
    #recipe = forms.ModelChoiceField(queryset=Recipe.objects.all())
    instruction_text = forms.CharField(max_length=200)
    
    class Meta:
        model = Instruction
        fields = ['instruction_text']
        exclude = ['recipe']
