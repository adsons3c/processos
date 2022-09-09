from django.db import models
 
class Processo(models.Model):
 
 
    A_INICIAR = 'A INICIAR'
    EM_ANDAMENTO = 'EM ANDAMENTO'
    FINALIZADO = 'FINALIZADO'
    STATUS_PROCESSO = [(A_INICIAR,'A INICIAR'),
                       (EM_ANDAMENTO,'EM ANDAMENTO'),
                       (FINALIZADO,'FINALIZADO'),]
   
    num_processo = models.CharField(max_length=20)
    tipo_processo = models.CharField(max_length=50)
    data_processo = models.DateTimeField(auto_now=False)
    logradouro = models.CharField(max_length=200)
    cruzamento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=30)
    status = models.CharField(max_length=15, choices=STATUS_PROCESSO,default=A_INICIAR)
   
 
    def __str__(self):
        return self.num_processo


class Equipamento(models.Model):

    INSTALACAO = 'INSTALAÇÃO'
    MANUTENCAO = 'MANUTENÇÃO'
    REMOCAO = 'REMOÇÃO'
    CATEGORIA = [(INSTALACAO,'INSTALAÇÃO'),
                (MANUTENCAO,'MANUTENÇÃO'),
                (REMOCAO,'REMOÇÃO'),]    
 
 
    SEMOB = 'SEMOB'
    TERCEIRIZADA = 'TERCEIRIZADA'
    RESPONSAVEL = [(SEMOB,'SEMOB'),
                    (TERCEIRIZADA,'TERCEIRIZADA')]                  
 
   
    ACRÍLICA = 'ACRÍLICO'
    TERMOPLASTICA = 'TERMOPLASTICO'
    MATERIAL = [(ACRÍLICA, 'ACRÍLICO'),
                (TERMOPLASTICA, 'TERMOPLASTICO')]
 
 
    POSTE_PRÓPRIO = 'POSTE TUBO'
    POSTE_ENERGISA = 'POSTE ENERGISA'
    SUPORTE = [(POSTE_PRÓPRIO, 'POSTE TUBO'),
               (POSTE_ENERGISA, 'POSTE ENERGISA')]            
 
 
    ABRIGO = 'ABRIGO'
    PLACA = 'PLACA'
    TIPO_PARADA = [(ABRIGO, 'ABRIGO'),
                   (PLACA, 'PLACA')]
   
   
    DOME = 'DOME'
    TIPO_CAMERA = [(DOME,'DOME'),]
 
    SIM = 'SIM'
    NAO = 'NÃO'
    FISCALIZACAO = [(SIM,'SIM'),
                    (NAO, 'NÃO'),]
 
 
    CAMERA = 'CAMERA'
    CANALIZACAO = 'CANALIZAÇÃO'
    FAIXA_PEDESTRE = 'FAIXA DE PEDESTRE'
    EIXO = 'EIXO'
    ESTACIONAMENTO = 'ESTACIONAMENTO'
    ILHA = 'ILHA'
    LOMBADA_FISICA = 'LOMBADA FÍSICA'
    PARADA_ONIBUS = 'PARADAS DE ÔNIBUS'
    REDUTOR_VELOCIDADE = 'REDUTOR DE VELOCIDADE'
    SINALIZACAO_VERTICAL = 'SINALIZAÇÃO VERTICAL'
    SEMAFORO = 'SEMÁFORO'
    ZEBRADO = 'ZEBRADO'
    EQUIPAMENTO = [(CAMERA, 'CAMERA'),
                    (CANALIZACAO, 'CANALIZAÇÃO'),
                    (FAIXA_PEDESTRE, 'FAIXA DE PEDESTRE'),
                    (EIXO, 'EIXO'),
                    (ESTACIONAMENTO, 'ESTACIONAMENTO'),
                    (ILHA, 'ILHA'),
                    (LOMBADA_FISICA, 'LOMBADA FÍSICA'),
                    (PARADA_ONIBUS, 'PARADAS DE ÔNIBUS'),
                    (REDUTOR_VELOCIDADE, 'REDUTOR DE VELOCIDADE'),
                    (SINALIZACAO_VERTICAL, 'SINALIZAÇÃO VERTICAL'),
                    (SEMAFORO, 'SEMÁFORO'),
                    (ZEBRADO, 'ZEBRADO')]
 
    processo = models.ForeignKey(Processo, null=True, blank=True, on_delete=models.CASCADE)       
    categoria = models.CharField(max_length=20, choices=CATEGORIA,default=INSTALACAO)      
    data = models.DateTimeField(auto_now=False)          
    codigo_placa = models.CharField(max_length=20)
    codigo_parada = models.CharField(max_length=20)
    codigo_semaforo = models.IntegerField()
    tipo_camera = models.CharField(max_length=10, choices=TIPO_CAMERA,default=DOME)
    fiscalizacao = models.CharField(max_length=10,choices=FISCALIZACAO)
    respons = models.CharField(max_length=20,choices=RESPONSAVEL,default=SEMOB)
    quant_bastao = models.DecimalField(max_digits=5, decimal_places=3)
    largura = models.DecimalField(max_digits=5, decimal_places=3)
    comprim = models.DecimalField(max_digits=5, decimal_places=3)
    material = models.CharField(max_length=30,choices=MATERIAL,default=ACRÍLICA)
    nomeclatura_placa = models.CharField(max_length=200)
    diametro = models.FloatField()
    area = models.FloatField()
    suporte = models.CharField(max_length=20,choices=SUPORTE,default=POSTE_ENERGISA)
    nomeclatura = models.CharField(max_length=20)
    tipo_parada = models.CharField(max_length=20,choices=TIPO_PARADA,default='ABRIGO')
    tipo_equipamento = models.CharField(max_length=200, choices=EQUIPAMENTO)
    quant_abrigo = models.IntegerField()            
    rede = models.CharField(max_length=20)    
    coord_inicio_eixo_x = models.DecimalField(max_digits=9, decimal_places=7)
    coord_incio_eixo_y = models.DecimalField(max_digits=9, decimal_places=7)
    coord_final_eixo_x = models.DecimalField(max_digits=9, decimal_places=7)
    coord_final_eixo_y = models.DecimalField(max_digits=9, decimal_places=7)

    def __str__(self):
        return self.tipo_equipamento

