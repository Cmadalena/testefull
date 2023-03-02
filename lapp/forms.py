from django.forms import ModelForm
from lapp.models import Funcionario


# Create the form class.
class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'apelido', 'sexo', 'tipodoc',
                  'nrdoc', 'dataadmissao', 'cargo', 'formacaoacademica',
                  'nivelacademico', 'nuit', 'estadocivil', 'localnasc',
                  'telefone', 'telefone1', 'email', 'observacao']