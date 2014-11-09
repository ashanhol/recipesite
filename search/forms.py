from django import forms

# Create the form class.

class searchForm(forms.ModelForm):
    search_box = forms.CharField(max_length=100)
    search_box.widget = forms.TextInput(attrs={'class': 'form-control', 'size' : 100, 'placeholder' : 'Search', 'id': 'search'})
    vegetarian = forms.CheckboxInput()
    vegetarian.widget = forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'vegetarian'})
    vegan = forms.CheckboxInput()
    vegan.widget = forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'vegan'})
    gluten_free = forms.CheckboxInput()
    gluten_free.widget = forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'gluten-free'})
    soy_free = forms.CheckboxInput()
    soy_free.widget = forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'soy-free'})
    dairy_free = forms.CheckboxInput()
    dairy_free.widget = forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'dairy-free'})
