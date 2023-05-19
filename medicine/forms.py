from django import forms
from .models import MedicineModel

class MedicineForm(forms.ModelForm):

    class Meta:
        model = MedicineModel
        fields = '__all__'

        