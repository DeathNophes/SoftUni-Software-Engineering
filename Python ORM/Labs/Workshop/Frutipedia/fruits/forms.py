from django import forms

from Frutipedia.fruits.models import Category, Fruit


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryAddForm(CategoryBaseForm):
    pass


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitAddForm(BaseFruitForm):
    pass


class EditFruitForm(BaseFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True