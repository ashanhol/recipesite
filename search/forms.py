from django import forms

# Create the form class.

SEARCHTYPE = (
    ('NAME', 'Search By Recipe Name'),
    ('INGR', 'Search By Recipe Ingredient'),

)

class searchForm(forms.Form):
    search_box = forms.CharField(max_length=100)
    search_box.widget = forms.TextInput(attrs={'class': 'form-control', 'size' : 100, 'placeholder' : 'Search', 'id': 'search'})
    
    Search_By = forms.CharField(max_length=20)
    Search_By.widget= forms.Select(choices = SEARCHTYPE, attrs={'class' : 'form-control', 'id' : 'searchtype'})
    
    vegetarian = forms.BooleanField()
    vegetarian.widget = forms.CheckboxInput(attrs={'id': 'vegetarian'})
    
    vegan = forms.BooleanField()
    vegan.widget = forms.CheckboxInput(attrs={'id': 'vegan'})
    
    gluten_free = forms.BooleanField()
    gluten_free.widget = forms.CheckboxInput(attrs={'id': 'gluten-free'})
    
    soy_free = forms.BooleanField()
    soy_free.widget = forms.CheckboxInput(attrs={'id': 'soy-free'})
    
    dairy_free = forms.BooleanField()
    dairy_free.widget = forms.CheckboxInput(attrs={'id': 'dairy-free'})
    
   


