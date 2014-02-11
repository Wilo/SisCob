#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

#Mantenimiento de Aseguradora v
class Aseguradora(models.Model):
    #Id= models.AutoField(db_column="ASE_Id", primary_key=True, unique=True, null=False)
    Descripcion= models.CharField(db_column="ASE_Desc", max_length=45, verbose_name="Descripción")
    Usuario= models.CharField(max_length=30, db_column="ASE_Usua")
    Fecha= models.DateTimeField(db_column="ASE_Fech", default=datetime.today(), verbose_name="Fecha de Creación")

    def __unicode__(self):
        return self.Descripcion

    class Meta:
        ordering = ('Descripcion',)
        db_table = 'SISCBR_MAseguradora'

#Mantenimiento de Bombero v
class Bombero(models.Model):
    #Id= models.AutoField(db_column="PER_Id", primary_key=True, unique=True, null=False)
    Ruc = models.CharField(db_column="BOM_Ruc", max_length=15, primary_key=True, null=False, unique=True)
    Nombre = models.CharField(db_column="BOM_Nombre", max_length=45)
    Logotipo = models.CharField(db_column="BOM_Logotipo", max_length=45)
    Direccion = models.CharField(db_column="BOM_Direccion", max_length= 45, verbose_name="Dirección")
    Telefono = models.CharField(db_column="BOM_Telefono", max_length= 45, verbose_name="Teléfono")
    Fax = models.CharField(db_column="BOM_Fax", max_length=20)
    Mail = models.EmailField(db_column="BOM_Mail", max_length=45, verbose_name="Email")
    Web = models.URLField(db_column="BOM_Web")
    Slogan = models.CharField(db_column= "BOM_Slogan", max_length=45)
    RUC_Comandante = models.CharField(db_column="BOM_Ruc_Comandante", max_length=15, null=False, unique=True,
                                            verbose_name="Ruc Comandante")
    Comandante = models.CharField(db_column="BOM_Comandante", max_length=45)
    Usuario = models.CharField(max_length=30, db_column= "BOM_Usua")
    Fecha = models.DateTimeField(db_column= "BOM_Fech", default=datetime.today(), verbose_name="Fecha de Creación")
    Cost_Titulo= models.DecimalField(db_column="BOM_Cost_Titulo", max_digits=10, decimal_places=2,
                                     verbose_name="Costo Título")
    Tasa_Predio = models.DecimalField(db_column="BOM_Tasa_Predio", max_digits=10, decimal_places=2,
                                     verbose_name="Tasa Predio")
    Tasa_Certificado = models.DecimalField(db_column="BOM_Tasa_Certificado", max_digits=10, decimal_places=2,
                                     verbose_name="Tasa Certificado")

    def __unicode__(self):
        return str(self.Nombre)

    class Meta:
        ordering = ('Nombre',)
        db_table = 'SISCBR_Bombero'

#Mantenimiento de Ciudadela
class Ciudadela(models.Model):
    #Id= models.AutoField(db_column="CIU_Id", primary_key=True, unique=True, null=False)
    Descripcion = models.CharField(db_column="CIU_Desc", max_length=45, verbose_name="Descripción")
    Usuario = models.CharField(max_length=30, db_column="CIU_Usua")
    Fecha= models.DateTimeField(db_column="CIU_Fech", default=datetime.today(), verbose_name="Fecha de Creación")

    def __unicode__(self):
        return self.Descripcion

    class Meta:
        ordering= ('Descripcion',)
        db_table= 'SISCBR_MCiudadela'

#Mantenimiento de Cliente
class Cliente(models.Model):
    #Id= models.AutoField(db_column="CLI_Id", primary_key=True, unique=True, null=False)
    Ciudadela= models.ForeignKey(Ciudadela, db_column="CIU_Id")
    Cedula= models.CharField(db_column="CLI_Cedu", max_length=13, verbose_name="Cédula")
    Apellido= models.CharField(db_column="CLI_Apel", max_length=45)
    Nombre= models.CharField(db_column="CLI_Nomb", max_length=45)
    Direccion= models.CharField(db_column="CLI_Dire", max_length=45)
    Telefono= models.CharField(db_column="CLI_Fono", max_length=20, verbose_name="Teléfono")
    Email= models.EmailField(db_column="CLI_Mail", max_length=45)
    Usuario= models.CharField(max_length=30, db_column="CLI_Usua")
    Fecha= models.DateTimeField(db_column="CLI_Fech", default=datetime.today(), verbose_name="Fecha de Creación")

    def __unicode__(self):
        return '%s %s'%(self.Nombre, self.Apellido)

    class Meta:
        ordering = ('Apellido',)
        db_table = 'SISCBR_MCliente'

#Local
class Local(models.Model):
    #Id= models.AutoField(db_column="LOC_Id", primary_key=True, unique=True, null=False)
    Cliente= models.ForeignKey(Cliente, db_column="CLI_Id")
    Aseguradora= models.ForeignKey(Aseguradora, db_column="ASE_Id")
    Ciudadela= models.ForeignKey(Ciudadela, db_column="CIU_Id")
    Descripcion= models.CharField(db_column="LOC_Desc", max_length=45, verbose_name="Descripción")
    Ruc= models.CharField(db_column="LOC_Ruc", max_length=13)
    Direccion= models.CharField(db_column="LOC_Direc", max_length=45, verbose_name="Dirección")
    Catastro= models.CharField(db_column="LOC_Cata", max_length=20)
    Telefono= models.CharField(db_column="LOC_Fono", max_length=20, verbose_name="Teléfono")
    Avaluo= models.DecimalField(db_column="LOC_Avaluo", max_digits=18, decimal_places=2, default=0.0)
    Poliza= models.CharField(db_column="LOC_NPol", max_length=20, verbose_name="N° de Póliza")
    Estado = models.BooleanField(db_column="LOC_Est", default=True)
    Usuario= models.CharField(max_length=30, db_column="LOC_Usua")
    Fecha= models.DateTimeField(db_column="LOC_Fech", default=datetime.today(), verbose_name="Fecha de Creación")

    def __unicode__(self):
        return self.Descripcion

    class Meta:
        ordering = ('Direccion',)
        db_table = 'SISCBR_DLocal'

#Mantenimiento de Vehículo
class Vehiculo(models.Model):
    #Id= models.AutoField(db_column="VEH_Id", primary_key=True, unique=True, null=False)
    Cliente = models.ForeignKey(Cliente, db_column="CLI_Id")
    Modelo = models.CharField(db_column="VEH_Modelo", max_length=20)
    Marca = models.CharField(db_column="VEH_Marca", max_length=20)
    Color = models.CharField(db_column="VEH_Color", max_length=20)
    Anio = models.IntegerField(db_column="VEH_Anio", verbose_name="Año")
    Chofer = models.CharField(db_column="VEH_Chofer", max_length=45)
    Ruta = models.CharField(db_column="VEH_Ruta", max_length=45)
    Avaluo = models.DecimalField(db_column="VEH_Avaluo", max_digits=18, decimal_places=2, default=0.0)
    Capacidad = models.DecimalField(db_column="VEH_Capa", max_digits=10, decimal_places=2, default=0.0)
    Tipo = models.CharField(db_column="VEH_Tipo", max_length=45)
    Estado = models.BooleanField(db_column="VEH_Estado", default=True)
    Usuario = models.CharField(max_length=30, db_column="VEH_Usua")
    Fecha = models.DateTimeField(db_column="VEH_Fech", default=datetime.today(), verbose_name="Fecha de Creación")

    def __unicode__(self):
        return self.Modelo

    class Meta:
        ordering = ('Anio',)
        db_table = 'SISCBR_MVehiculo'

#Tipo de Cobros
class Tipo_Cobro(models.Model):
    #Id= models.AutoField(db_column="TCO_Id", primary_key=True, unique=True, null=False)
    Descripcion = models.CharField(db_column="TCO_Desc", max_length=45, verbose_name="Descripción")
    Titulo = models.CharField(db_column="TCO_Titulo", max_length=90, verbose_name="Título")
    Subtitulo = models.CharField(db_column="TCO_Subtitulo", max_length=90, verbose_name="Subtítulo")
    Nombres = models.CharField(db_column="TCO_Nombres", max_length=90)
    Cargos = models.CharField(db_column="TCO_Cargos", max_length=90)
    Usuario = models.CharField(max_length=30, db_column="TCO_Usua")
    Fecha = models.DateTimeField(db_column="TCO_Fech", default=datetime.today(), verbose_name="Fecha de Creación")

    def __unicode__(self):
        return self.Descripcion

    class Meta:
        ordering = ('Descripcion',)
        db_table = 'SISCBR_MTipoCobros'

#Cobro de Predios
class Cobro_Predios(models.Model):
    Anio=models.IntegerField(verbose_name="Año", db_column="COB_Anio", max_length=11, primary_key=True, null=False,
                             unique=True)
    Enero= models.DecimalField(db_column="COB_Ener", max_digits=10, decimal_places=2, default=0.0)
    Febrero= models.DecimalField(db_column="COB_Febr", max_digits=10, decimal_places=2, default=0.0)
    Marzo= models.DecimalField(db_column="COB_Marz", max_digits=10, decimal_places=2, default=0.0)
    Abril= models.DecimalField(db_column="COB_Abri", max_digits=10, decimal_places=2, default=0.0)
    Mayo= models.DecimalField(db_column="COB_Mayo", max_digits=10, decimal_places=2, default=0.0)
    Junio= models.DecimalField(db_column="COB_Juni", max_digits=10, decimal_places=2, default=0.0)
    Julio= models.DecimalField(db_column="COB_Juli", max_digits=10, decimal_places=2, default=0.0)
    Agosto= models.DecimalField(db_column="COB_Agos", max_digits=10, decimal_places=2, default=0.0)
    Septiembre= models.DecimalField(db_column="COB_Sept", max_digits=10, decimal_places=2, default=0.0)
    Octubre= models.DecimalField(db_column="COB_Octu", max_digits=10, decimal_places=2, default=0.0)
    Noviembre= models.DecimalField(db_column="COB_Novi", max_digits=10, decimal_places=2, default=0.0)
    Diciembre= models.DecimalField(db_column="COB_Dici", max_digits=10, decimal_places=2, default=0.0)
    Usuario= models.CharField(max_length=30,db_column="COB_Usua")
    Fecha= models.DateTimeField(db_column="COB_Fech", default=datetime.today(), verbose_name="Fecha de Creación")

    def __unicode__(self):
        return self.Anio

    class Meta:
        ordering= ('Anio',)
        db_table= 'SISCBR_VCobPredios'

#Predios
class Predio(models.Model):
    #Id= models.AutoField(db_column="PDI_Id", primary_key=True, unique=True, null=False)
    Cliente=  models.ForeignKey(Cliente,db_column="CLI_Id")
    Ciudadela= models.ForeignKey(Ciudadela, db_column="CIU_Id")
    Catastro= models.CharField(db_column="PDI_Cata", max_length=20)
    Direccion= models.CharField(db_column="PDI_Direc", max_length=100, verbose_name="Dirección")
    Avaluo= models.DecimalField(db_column="PDI_Avaluo", max_digits=10, decimal_places=2, default=0.0)
    Observacion= models.CharField(db_column="PDI_Obs", max_length=45, verbose_name="Observación")
    Estado= models.BooleanField(db_column="PDI_Est", default=True)
    Usuario= models.CharField(max_length=30, db_column="PDI_Usua")
    Fecha= models.DateTimeField(db_column="PDI_Fech", default=datetime.today(), verbose_name="Fecha de Creación")

    def __unicode__(self):
        return self.Direccion

    class Meta:
        ordering= ('Direccion',)
        db_table= 'SISCBR_MPredio'

#Tipo de Costo Vario
class Tipo_Costo_Vario(models.Model):
    #Id= models.AutoField(db_column="TIC_Id", primary_key=True, unique=True, null=False)
    Descripcion= models.CharField(db_column="TIC_Descripcion", max_length= 45, verbose_name= "Descripción")
    Valor= models.DecimalField(db_column="TIC_Valo", max_digits=10, decimal_places=2, default=0.0)
    Usuario= models.CharField(max_length=30,db_column= "TIC_Usua")
    Fecha= models.DateTimeField(db_column= "TIC_Fech", default= datetime.today(), verbose_name= "Fecha de Creación")

    def __unicode__(self):
        return self.Descripcion

    class Meta:
        ordering= ('Descripcion',)
        db_table= 'SISCBR_MTipoCostoVario'

#Costo Vario
class Trans_Costo_Vario(models.Model):
    #Id= models.AutoField(db_column="ASE_Id", primary_key=True, unique=True, null=False)
    Ciente = models.ForeignKey(Cliente, db_column="CLI_Id")
    Tipo_Costo = models.ForeignKey(Tipo_Costo_Vario, db_column="TIC_Id", verbose_name="Tipo Costo Vario")
    Tipo_Cobro= models.ForeignKey(Tipo_Cobro, db_column="TCO_Id", verbose_name="Tipo de Cobro")
    Valor= models.DecimalField(db_column="COS_Valo", max_digits=10, decimal_places=2, default=0.0)
    Titulo= models.DecimalField(db_column="COS_Titu", max_digits=10, decimal_places=2, default=0.0,
                                verbose_name="Título")
    Observacion= models.CharField(db_column="COS_Obs", max_length=90, verbose_name="Observación")
    Estado= models.CharField(db_column="COS_Est", max_length=45)
    Usuario= models.CharField(max_length=30,db_column= "COS_Usua")
    Fecha= models.DateTimeField(db_column= "COS_Fech", default= datetime.today(), verbose_name= "Fecha de Creación")

    class Meta:
        ordering= ('Fecha',)
        db_table= 'SISCBR_TCostoVario'

#Permiso
class Permiso(models.Model):
    #Id= models.AutoField(db_column="PER_Id", primary_key=True, unique=True, null=False)
    Local = models.ForeignKey(Local, db_column="LOC_Id")
    Tipo_Cobro = models.ForeignKey(Tipo_Cobro, db_column="TCO_Id")
    Anio = models.IntegerField(db_column="PER_Anio", verbose_name="Año")
    Fecha_Emision = models.DateTimeField(db_column="PER_Femi", default=datetime.today(), verbose_name="Fecha Emisión")
    Avaluo = models.DecimalField(db_column="PER_Avaluo", max_digits=18, decimal_places=2, verbose_name="Avaluo")
    Tasa = models.DecimalField(db_column="PER_Tasa", max_digits=10, decimal_places=2)
    Valor_Tasa = models.DecimalField(db_column="PER_Vtasa", max_digits=10, decimal_places=2, verbose_name="Valor Tasa")
    Titu = models.DecimalField(db_column="PER_Titu", max_digits=10, decimal_places=2, verbose_name="Título")
    Esado = models.BooleanField(db_column="PER_Esta", default=True)
    Usuario = models.CharField(max_length=30,db_column= "PER_Usua")
    Fecha = models.DateTimeField(db_column="PER_Fech", default=datetime.today(), verbose_name="Fecha de Creación")

    def __unicode__(self):
        return self.Anio

    class Meta:
        ordering = ('Fecha',)
        db_table = 'SISCBR_TPermiso'

#Transacción Predio
class Trans_Predio(models.Model):
    Predio = models.ForeignKey(Predio, db_column="PDI_Id")
    Anio = models.ForeignKey(Cobro_Predios, db_column="COB_Id", verbose_name="Año")
    Tipo_Cobro = models.ForeignKey(Tipo_Cobro, db_column="TCO_Id", verbose_name="Tipo Cobro")
    Metros = models.DecimalField(db_column="PRE_Metros", max_digits=10, decimal_places=2)
    Avaluo = models.DecimalField(db_column="PRE_Aval", max_digits=18, decimal_places=2)
    Titulo = models.DecimalField(db_column="PRE_Titu", max_digits=10, decimal_places=2, verbose_name="Título")
    Tasa = models.DecimalField(db_column="PRE_Tasa", max_digits=10, decimal_places=2)
    Valor_Tasa = models.DecimalField(db_column="PRE_Vtas", max_digits=10, decimal_places=2, verbose_name="Valor Tasa")
    Recargos = models.DecimalField(db_column="PRE_Reca", max_digits=10, decimal_places=2)
    Fecha_Emision = models.DecimalField(db_column="PRE_Femi", max_digits=10, decimal_places=2,
                                        verbose_name="Fecha Emisión")
    Estado = models.BooleanField(db_column="PRE_Est", default=True)
    Usuario = models.CharField(max_length=30,db_column="PRE_Usua")
    Fecha = models.DateTimeField(db_column="PRE_Fech", default=datetime.today(), verbose_name="Fecha de Creación")
    Tipo_Pago = models.IntegerField(verbose_name="Tipo Pago")

    def __unicode__(self):
        return self.Titulo

    class Meta:
        ordering = ('Fecha',)
        db_table = 'SISCBR_TPredio'

#Combustible
class Combustible(models.Model):
    Vehiculo = models.ForeignKey(Vehiculo, db_column="VEH_Id", verbose_name="Vehículo")
    Tipo_Cobro = models.ForeignKey(Tipo_Cobro, db_column="TCO_Id", verbose_name="Tipo de Cobro")
    Avaluo = models.DecimalField(db_column="COM_Aval", max_digits=10, decimal_places=2, verbose_name="Avalúo")
    Titulo = models.DecimalField(db_column="COM_Titu", max_digits=10, decimal_places=2, verbose_name="Título")
    Tasa = models.DecimalField(db_column="COM_Tasa", max_digits=10, decimal_places=2)
    Valor_Tasa = models.DecimalField(db_column="COM_Vtas", max_digits=10, decimal_places=2, verbose_name="Valor Tasa")
    Fecha_Emision = models.DateTimeField(db_column="COM_Femi", default=datetime.today(), verbose_name="Fecha Emisión")
    Estado = models.BooleanField(db_column="COM_Est", default=True)
    Usuario = models.CharField(max_length=30,db_column="COM_Usua")
    Fecha = models.DateTimeField(db_column="COM_Fech", default=datetime.today(), verbose_name = "Fecha de Creación")

    def __unicode__(self):
        return self.Fecha

    class Meta:
        db_table = 'SISCBR_TCombustible'

