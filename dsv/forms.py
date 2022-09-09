from django.forms import ModelForm
from .models import Processo, Equipamento

class ProcessoForm(ModelForm):
    class Meta:
        model = Processo
        fields = ['num_processo', 'tipo_processo', 'data_processo', 'logradouro','cruzamento', 'bairro', 'status']


class EquipamentoForm(ModelForm):
    class Meta:
        model = Equipamento
        fields = ['processo', 'categoria', 'data', 'codigo_placa', 'codigo_parada', 'codigo_semaforo', 'tipo_camera',
                    'fiscalizacao', 'respons', 'quant_bastao', 'largura', 'comprim', 'material', 'nomeclatura_placa',
                    'nomeclatura_placa', 'diametro', 'area', 'suporte', 'nomeclatura', 'tipo_parada', 'tipo_equipamento', 
                    'quant_abrigo', 'rede', 'coord_inicio_eixo_x', 'coord_incio_eixo_y', 'coord_final_eixo_x', 'coord_final_eixo_y', 
          ]


   
    # nomeclatura_placa = models.CharField(max_length=200)
    # diametro = models.FloatField()
    # area = models.FloatField()
    # suporte = models.CharField(max_length=20,choices=SUPORTE,default=POSTE_ENERGISA)
    # nomeclatura = models.CharField(max_length=20)
    # tipo_parada = models.CharField(max_length=20,choices=TIPO_PARADA,default='ABRIGO')
    # tipo_equipamento = models.CharField(max_length=200, choices=EQUIPAMENTO)
    # quant_abrigo = models.IntegerField()            
    # rede = models.CharField(max_length=20)    
    # coord_inicio_eixo_x = models.DecimalField(max_digits=9, decimal_places=7)
    # coord_incio_eixo_y = models.DecimalField(max_digits=9, decimal_places=7)
    # coord_final_eixo_x = models.DecimalField(max_digits=9, decimal_places=7)
    # coord_final_eixo_y = models.DecimalField(max_digits=9, decimal_places=7)