# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Aseguradora'
        db.create_table('SISCBR_MAseguradora', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Descripcion', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='ASE_Desc')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='ASE_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='ASE_Fech')),
        ))
        db.send_create_signal(u'main', ['Aseguradora'])

        # Adding model 'Bombero'
        db.create_table('SISCBR_Bombero', (
            ('Ruc', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15, primary_key=True, db_column='BOM_Ruc')),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='BOM_Nombre')),
            ('Logotipo', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='BOM_Logotipo')),
            ('Direccion', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='BOM_Direccion')),
            ('Telefono', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='BOM_Telefono')),
            ('Fax', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='BOM_Fax')),
            ('Mail', self.gf('django.db.models.fields.EmailField')(max_length=45, db_column='BOM_Mail')),
            ('Web', self.gf('django.db.models.fields.URLField')(max_length=200, db_column='BOM_Web')),
            ('Slogan', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='BOM_Slogan')),
            ('RUC_Comandante', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15, db_column='BOM_Ruc_Comandante')),
            ('Comandante', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='BOM_Comandante')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='BOM_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='BOM_Fech')),
            ('Cost_Titulo', self.gf('django.db.models.fields.DecimalField')(db_column='BOM_Cost_Titulo', decimal_places=2, max_digits=10)),
            ('Tasa_Predio', self.gf('django.db.models.fields.DecimalField')(db_column='BOM_Tasa_Predio', decimal_places=2, max_digits=10)),
            ('Tasa_Certificado', self.gf('django.db.models.fields.DecimalField')(db_column='BOM_Tasa_Certificado', decimal_places=2, max_digits=10)),
        ))
        db.send_create_signal(u'main', ['Bombero'])

        # Adding model 'Ciudadela'
        db.create_table('SISCBR_MCiudadela', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Descripcion', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='CIU_Desc')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='CIU_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='CIU_Fech')),
        ))
        db.send_create_signal(u'main', ['Ciudadela'])

        # Adding model 'Cliente'
        db.create_table('SISCBR_MCliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Ciudadela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Ciudadela'], db_column='CIU_Id')),
            ('Cedula', self.gf('django.db.models.fields.CharField')(max_length=13, db_column='CLI_Cedu')),
            ('Apellido', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='CLI_Apel')),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='CLI_Nomb')),
            ('Direccion', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='CLI_Dire')),
            ('Telefono', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='CLI_Fono')),
            ('Email', self.gf('django.db.models.fields.EmailField')(max_length=45, db_column='CLI_Mail')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='CLI_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='CLI_Fech')),
        ))
        db.send_create_signal(u'main', ['Cliente'])

        # Adding model 'Local'
        db.create_table('SISCBR_DLocal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Cliente'], db_column='CLI_Id')),
            ('Aseguradora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Aseguradora'], db_column='ASE_Id')),
            ('Ciudadela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Ciudadela'], db_column='CIU_Id')),
            ('Descripcion', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='LOC_Desc')),
            ('Ruc', self.gf('django.db.models.fields.CharField')(max_length=13, db_column='LOC_Ruc')),
            ('Direccion', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='LOC_Direc')),
            ('Catastro', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='LOC_Cata')),
            ('Telefono', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='LOC_Fono')),
            ('Avaluo', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='LOC_Avaluo', decimal_places=2, max_digits=18)),
            ('Poliza', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='LOC_NPol')),
            ('Estado', self.gf('django.db.models.fields.BooleanField')(default=True, db_column='LOC_Est')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='LOC_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='LOC_Fech')),
        ))
        db.send_create_signal(u'main', ['Local'])

        # Adding model 'Vehiculo'
        db.create_table('SISCBR_MVehiculo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Cliente'], db_column='CLI_Id')),
            ('Modelo', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='VEH_Modelo')),
            ('Marca', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='VEH_Marca')),
            ('Color', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='VEH_Color')),
            ('Anio', self.gf('django.db.models.fields.IntegerField')(db_column='VEH_Anio')),
            ('Chofer', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='VEH_Chofer')),
            ('Ruta', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='VEH_Ruta')),
            ('Avaluo', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='VEH_Avaluo', decimal_places=2, max_digits=18)),
            ('Capacidad', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='VEH_Capa', decimal_places=2, max_digits=10)),
            ('Tipo', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='VEH_Tipo')),
            ('Estado', self.gf('django.db.models.fields.BooleanField')(default=True, db_column='VEH_Estado')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='VEH_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='VEH_Fech')),
        ))
        db.send_create_signal(u'main', ['Vehiculo'])

        # Adding model 'Tipo_Cobro'
        db.create_table('SISCBR_MTipoCobros', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Descripcion', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='TCO_Desc')),
            ('Titulo', self.gf('django.db.models.fields.CharField')(max_length=90, db_column='TCO_Titulo')),
            ('Subtitulo', self.gf('django.db.models.fields.CharField')(max_length=90, db_column='TCO_Subtitulo')),
            ('Nombres', self.gf('django.db.models.fields.CharField')(max_length=90, db_column='TCO_Nombres')),
            ('Cargos', self.gf('django.db.models.fields.CharField')(max_length=90, db_column='TCO_Cargos')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='TCO_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='TCO_Fech')),
        ))
        db.send_create_signal(u'main', ['Tipo_Cobro'])

        # Adding model 'Cobro_Predios'
        db.create_table('SISCBR_VCobPredios', (
            ('Anio', self.gf('django.db.models.fields.IntegerField')(unique=True, max_length=11, primary_key=True, db_column='COB_Anio')),
            ('Enero', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Ener', decimal_places=2, max_digits=10)),
            ('Febrero', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Febr', decimal_places=2, max_digits=10)),
            ('Marzo', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Marz', decimal_places=2, max_digits=10)),
            ('Abril', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Abri', decimal_places=2, max_digits=10)),
            ('Mayo', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Mayo', decimal_places=2, max_digits=10)),
            ('Junio', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Juni', decimal_places=2, max_digits=10)),
            ('Julio', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Juli', decimal_places=2, max_digits=10)),
            ('Agosto', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Agos', decimal_places=2, max_digits=10)),
            ('Septiembre', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Sept', decimal_places=2, max_digits=10)),
            ('Octubre', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Octu', decimal_places=2, max_digits=10)),
            ('Noviembre', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Novi', decimal_places=2, max_digits=10)),
            ('Diciembre', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COB_Dici', decimal_places=2, max_digits=10)),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='COB_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='COB_Fech')),
        ))
        db.send_create_signal(u'main', ['Cobro_Predios'])

        # Adding model 'Predio'
        db.create_table('SISCBR_MPredio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Cliente'], db_column='CLI_Id')),
            ('Ciudadela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Ciudadela'], db_column='CIU_Id')),
            ('Catastro', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='PDI_Cata')),
            ('Direccion', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='PDI_Direc')),
            ('Avaluo', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='PDI_Avaluo', decimal_places=2, max_digits=10)),
            ('Observacion', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='PDI_Obs')),
            ('Estado', self.gf('django.db.models.fields.BooleanField')(default=True, db_column='PDI_Est')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='PDI_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='PDI_Fech')),
        ))
        db.send_create_signal(u'main', ['Predio'])

        # Adding model 'Tipo_Costo_Vario'
        db.create_table('SISCBR_MTipoCostoVario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Descripcion', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='TIC_Descripcion')),
            ('Valor', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='TIC_Valo', decimal_places=2, max_digits=10)),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='TIC_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='TIC_Fech')),
        ))
        db.send_create_signal(u'main', ['Tipo_Costo_Vario'])

        # Adding model 'Trans_Costo_Vario'
        db.create_table('SISCBR_TCostoVario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Ciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Cliente'], db_column='CLI_Id')),
            ('Tipo_Costo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Tipo_Costo_Vario'], db_column='TIC_Id')),
            ('Tipo_Cobro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Tipo_Cobro'], db_column='TCO_Id')),
            ('Valor', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COS_Valo', decimal_places=2, max_digits=10)),
            ('Titulo', self.gf('django.db.models.fields.DecimalField')(default=0.0, db_column='COS_Titu', decimal_places=2, max_digits=10)),
            ('Observacion', self.gf('django.db.models.fields.CharField')(max_length=90, db_column='COS_Obs')),
            ('Estado', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='COS_Est')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='COS_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='COS_Fech')),
        ))
        db.send_create_signal(u'main', ['Trans_Costo_Vario'])

        # Adding model 'Permiso'
        db.create_table('SISCBR_TPermiso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Local', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Local'], db_column='LOC_Id')),
            ('Tipo_Cobro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Tipo_Cobro'], db_column='TCO_Id')),
            ('Anio', self.gf('django.db.models.fields.IntegerField')(db_column='PER_Anio')),
            ('Fecha_Emision', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='PER_Femi')),
            ('Avaluo', self.gf('django.db.models.fields.DecimalField')(db_column='PER_Avaluo', decimal_places=2, max_digits=18)),
            ('Tasa', self.gf('django.db.models.fields.DecimalField')(db_column='PER_Tasa', decimal_places=2, max_digits=10)),
            ('Valor_Tasa', self.gf('django.db.models.fields.DecimalField')(db_column='PER_Vtasa', decimal_places=2, max_digits=10)),
            ('Titu', self.gf('django.db.models.fields.DecimalField')(db_column='PER_Titu', decimal_places=2, max_digits=10)),
            ('Esado', self.gf('django.db.models.fields.BooleanField')(default=True, db_column='PER_Esta')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='PER_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='PER_Fech')),
        ))
        db.send_create_signal(u'main', ['Permiso'])

        # Adding model 'Trans_Predio'
        db.create_table('SISCBR_TPredio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Predio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Predio'], db_column='PDI_Id')),
            ('Anio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Cobro_Predios'], db_column='COB_Id')),
            ('Tipo_Cobro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Tipo_Cobro'], db_column='TCO_Id')),
            ('Metros', self.gf('django.db.models.fields.DecimalField')(db_column='PRE_Metros', decimal_places=2, max_digits=10)),
            ('Avaluo', self.gf('django.db.models.fields.DecimalField')(db_column='PRE_Aval', decimal_places=2, max_digits=18)),
            ('Titulo', self.gf('django.db.models.fields.DecimalField')(db_column='PRE_Titu', decimal_places=2, max_digits=10)),
            ('Tasa', self.gf('django.db.models.fields.DecimalField')(db_column='PRE_Tasa', decimal_places=2, max_digits=10)),
            ('Valor_Tasa', self.gf('django.db.models.fields.DecimalField')(db_column='PRE_Vtas', decimal_places=2, max_digits=10)),
            ('Recargos', self.gf('django.db.models.fields.DecimalField')(db_column='PRE_Reca', decimal_places=2, max_digits=10)),
            ('Fecha_Emision', self.gf('django.db.models.fields.DecimalField')(db_column='PRE_Femi', decimal_places=2, max_digits=10)),
            ('Estado', self.gf('django.db.models.fields.BooleanField')(default=True, db_column='PRE_Est')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='PRE_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='PRE_Fech')),
            ('Tipo_Pago', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'main', ['Trans_Predio'])

        # Adding model 'Combustible'
        db.create_table('SISCBR_TCombustible', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Vehiculo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Vehiculo'], db_column='VEH_Id')),
            ('Tipo_Cobro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Tipo_Cobro'], db_column='TCO_Id')),
            ('Avaluo', self.gf('django.db.models.fields.DecimalField')(db_column='COM_Aval', decimal_places=2, max_digits=10)),
            ('Titulo', self.gf('django.db.models.fields.DecimalField')(db_column='COM_Titu', decimal_places=2, max_digits=10)),
            ('Tasa', self.gf('django.db.models.fields.DecimalField')(db_column='COM_Tasa', decimal_places=2, max_digits=10)),
            ('Valor_Tasa', self.gf('django.db.models.fields.DecimalField')(db_column='COM_Vtas', decimal_places=2, max_digits=10)),
            ('Fecha_Emision', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='COM_Femi')),
            ('Estado', self.gf('django.db.models.fields.BooleanField')(default=True, db_column='COM_Est')),
            ('Usuario', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='COM_Usua')),
            ('Fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 10, 0, 0), db_column='COM_Fech')),
        ))
        db.send_create_signal(u'main', ['Combustible'])


    def backwards(self, orm):
        # Deleting model 'Aseguradora'
        db.delete_table('SISCBR_MAseguradora')

        # Deleting model 'Bombero'
        db.delete_table('SISCBR_Bombero')

        # Deleting model 'Ciudadela'
        db.delete_table('SISCBR_MCiudadela')

        # Deleting model 'Cliente'
        db.delete_table('SISCBR_MCliente')

        # Deleting model 'Local'
        db.delete_table('SISCBR_DLocal')

        # Deleting model 'Vehiculo'
        db.delete_table('SISCBR_MVehiculo')

        # Deleting model 'Tipo_Cobro'
        db.delete_table('SISCBR_MTipoCobros')

        # Deleting model 'Cobro_Predios'
        db.delete_table('SISCBR_VCobPredios')

        # Deleting model 'Predio'
        db.delete_table('SISCBR_MPredio')

        # Deleting model 'Tipo_Costo_Vario'
        db.delete_table('SISCBR_MTipoCostoVario')

        # Deleting model 'Trans_Costo_Vario'
        db.delete_table('SISCBR_TCostoVario')

        # Deleting model 'Permiso'
        db.delete_table('SISCBR_TPermiso')

        # Deleting model 'Trans_Predio'
        db.delete_table('SISCBR_TPredio')

        # Deleting model 'Combustible'
        db.delete_table('SISCBR_TCombustible')


    models = {
        u'main.aseguradora': {
            'Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'ASE_Desc'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'ASE_Fech'"}),
            'Meta': {'ordering': "('Descripcion',)", 'object_name': 'Aseguradora', 'db_table': "'SISCBR_MAseguradora'"},
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'ASE_Usua'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.bombero': {
            'Comandante': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'BOM_Comandante'"}),
            'Cost_Titulo': ('django.db.models.fields.DecimalField', [], {'db_column': "'BOM_Cost_Titulo'", 'decimal_places': '2', 'max_digits': '10'}),
            'Direccion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'BOM_Direccion'"}),
            'Fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'BOM_Fax'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'BOM_Fech'"}),
            'Logotipo': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'BOM_Logotipo'"}),
            'Mail': ('django.db.models.fields.EmailField', [], {'max_length': '45', 'db_column': "'BOM_Mail'"}),
            'Meta': {'ordering': "('Nombre',)", 'object_name': 'Bombero', 'db_table': "'SISCBR_Bombero'"},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'BOM_Nombre'"}),
            'RUC_Comandante': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15', 'db_column': "'BOM_Ruc_Comandante'"}),
            'Ruc': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15', 'primary_key': 'True', 'db_column': "'BOM_Ruc'"}),
            'Slogan': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'BOM_Slogan'"}),
            'Tasa_Certificado': ('django.db.models.fields.DecimalField', [], {'db_column': "'BOM_Tasa_Certificado'", 'decimal_places': '2', 'max_digits': '10'}),
            'Tasa_Predio': ('django.db.models.fields.DecimalField', [], {'db_column': "'BOM_Tasa_Predio'", 'decimal_places': '2', 'max_digits': '10'}),
            'Telefono': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'BOM_Telefono'"}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'BOM_Usua'"}),
            'Web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'db_column': "'BOM_Web'"})
        },
        u'main.ciudadela': {
            'Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'CIU_Desc'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'CIU_Fech'"}),
            'Meta': {'ordering': "('Descripcion',)", 'object_name': 'Ciudadela', 'db_table': "'SISCBR_MCiudadela'"},
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'CIU_Usua'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.cliente': {
            'Apellido': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'CLI_Apel'"}),
            'Cedula': ('django.db.models.fields.CharField', [], {'max_length': '13', 'db_column': "'CLI_Cedu'"}),
            'Ciudadela': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Ciudadela']", 'db_column': "'CIU_Id'"}),
            'Direccion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'CLI_Dire'"}),
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '45', 'db_column': "'CLI_Mail'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'CLI_Fech'"}),
            'Meta': {'ordering': "('Apellido',)", 'object_name': 'Cliente', 'db_table': "'SISCBR_MCliente'"},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'CLI_Nomb'"}),
            'Telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'CLI_Fono'"}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'CLI_Usua'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.cobro_predios': {
            'Abril': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Abri'", 'decimal_places': '2', 'max_digits': '10'}),
            'Agosto': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Agos'", 'decimal_places': '2', 'max_digits': '10'}),
            'Anio': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '11', 'primary_key': 'True', 'db_column': "'COB_Anio'"}),
            'Diciembre': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Dici'", 'decimal_places': '2', 'max_digits': '10'}),
            'Enero': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Ener'", 'decimal_places': '2', 'max_digits': '10'}),
            'Febrero': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Febr'", 'decimal_places': '2', 'max_digits': '10'}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'COB_Fech'"}),
            'Julio': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Juli'", 'decimal_places': '2', 'max_digits': '10'}),
            'Junio': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Juni'", 'decimal_places': '2', 'max_digits': '10'}),
            'Marzo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Marz'", 'decimal_places': '2', 'max_digits': '10'}),
            'Mayo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Mayo'", 'decimal_places': '2', 'max_digits': '10'}),
            'Meta': {'ordering': "('Anio',)", 'object_name': 'Cobro_Predios', 'db_table': "'SISCBR_VCobPredios'"},
            'Noviembre': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Novi'", 'decimal_places': '2', 'max_digits': '10'}),
            'Octubre': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Octu'", 'decimal_places': '2', 'max_digits': '10'}),
            'Septiembre': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COB_Sept'", 'decimal_places': '2', 'max_digits': '10'}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'COB_Usua'"})
        },
        u'main.combustible': {
            'Avaluo': ('django.db.models.fields.DecimalField', [], {'db_column': "'COM_Aval'", 'decimal_places': '2', 'max_digits': '10'}),
            'Estado': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'COM_Est'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'COM_Fech'"}),
            'Fecha_Emision': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'COM_Femi'"}),
            'Meta': {'object_name': 'Combustible', 'db_table': "'SISCBR_TCombustible'"},
            'Tasa': ('django.db.models.fields.DecimalField', [], {'db_column': "'COM_Tasa'", 'decimal_places': '2', 'max_digits': '10'}),
            'Tipo_Cobro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Tipo_Cobro']", 'db_column': "'TCO_Id'"}),
            'Titulo': ('django.db.models.fields.DecimalField', [], {'db_column': "'COM_Titu'", 'decimal_places': '2', 'max_digits': '10'}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'COM_Usua'"}),
            'Valor_Tasa': ('django.db.models.fields.DecimalField', [], {'db_column': "'COM_Vtas'", 'decimal_places': '2', 'max_digits': '10'}),
            'Vehiculo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Vehiculo']", 'db_column': "'VEH_Id'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.local': {
            'Aseguradora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Aseguradora']", 'db_column': "'ASE_Id'"}),
            'Avaluo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'LOC_Avaluo'", 'decimal_places': '2', 'max_digits': '18'}),
            'Catastro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'LOC_Cata'"}),
            'Ciudadela': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Ciudadela']", 'db_column': "'CIU_Id'"}),
            'Cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Cliente']", 'db_column': "'CLI_Id'"}),
            'Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'LOC_Desc'"}),
            'Direccion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'LOC_Direc'"}),
            'Estado': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'LOC_Est'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'LOC_Fech'"}),
            'Meta': {'ordering': "('Direccion',)", 'object_name': 'Local', 'db_table': "'SISCBR_DLocal'"},
            'Poliza': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'LOC_NPol'"}),
            'Ruc': ('django.db.models.fields.CharField', [], {'max_length': '13', 'db_column': "'LOC_Ruc'"}),
            'Telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'LOC_Fono'"}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'LOC_Usua'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.permiso': {
            'Anio': ('django.db.models.fields.IntegerField', [], {'db_column': "'PER_Anio'"}),
            'Avaluo': ('django.db.models.fields.DecimalField', [], {'db_column': "'PER_Avaluo'", 'decimal_places': '2', 'max_digits': '18'}),
            'Esado': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'PER_Esta'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'PER_Fech'"}),
            'Fecha_Emision': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'PER_Femi'"}),
            'Local': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Local']", 'db_column': "'LOC_Id'"}),
            'Meta': {'ordering': "('Fecha',)", 'object_name': 'Permiso', 'db_table': "'SISCBR_TPermiso'"},
            'Tasa': ('django.db.models.fields.DecimalField', [], {'db_column': "'PER_Tasa'", 'decimal_places': '2', 'max_digits': '10'}),
            'Tipo_Cobro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Tipo_Cobro']", 'db_column': "'TCO_Id'"}),
            'Titu': ('django.db.models.fields.DecimalField', [], {'db_column': "'PER_Titu'", 'decimal_places': '2', 'max_digits': '10'}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'PER_Usua'"}),
            'Valor_Tasa': ('django.db.models.fields.DecimalField', [], {'db_column': "'PER_Vtasa'", 'decimal_places': '2', 'max_digits': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.predio': {
            'Avaluo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'PDI_Avaluo'", 'decimal_places': '2', 'max_digits': '10'}),
            'Catastro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'PDI_Cata'"}),
            'Ciudadela': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Ciudadela']", 'db_column': "'CIU_Id'"}),
            'Cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Cliente']", 'db_column': "'CLI_Id'"}),
            'Direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'PDI_Direc'"}),
            'Estado': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'PDI_Est'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'PDI_Fech'"}),
            'Meta': {'ordering': "('Direccion',)", 'object_name': 'Predio', 'db_table': "'SISCBR_MPredio'"},
            'Observacion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'PDI_Obs'"}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'PDI_Usua'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.tipo_cobro': {
            'Cargos': ('django.db.models.fields.CharField', [], {'max_length': '90', 'db_column': "'TCO_Cargos'"}),
            'Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'TCO_Desc'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'TCO_Fech'"}),
            'Meta': {'ordering': "('Descripcion',)", 'object_name': 'Tipo_Cobro', 'db_table': "'SISCBR_MTipoCobros'"},
            'Nombres': ('django.db.models.fields.CharField', [], {'max_length': '90', 'db_column': "'TCO_Nombres'"}),
            'Subtitulo': ('django.db.models.fields.CharField', [], {'max_length': '90', 'db_column': "'TCO_Subtitulo'"}),
            'Titulo': ('django.db.models.fields.CharField', [], {'max_length': '90', 'db_column': "'TCO_Titulo'"}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'TCO_Usua'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.tipo_costo_vario': {
            'Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'TIC_Descripcion'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'TIC_Fech'"}),
            'Meta': {'ordering': "('Descripcion',)", 'object_name': 'Tipo_Costo_Vario', 'db_table': "'SISCBR_MTipoCostoVario'"},
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'TIC_Usua'"}),
            'Valor': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'TIC_Valo'", 'decimal_places': '2', 'max_digits': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.trans_costo_vario': {
            'Ciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Cliente']", 'db_column': "'CLI_Id'"}),
            'Estado': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'COS_Est'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'COS_Fech'"}),
            'Meta': {'ordering': "('Fecha',)", 'object_name': 'Trans_Costo_Vario', 'db_table': "'SISCBR_TCostoVario'"},
            'Observacion': ('django.db.models.fields.CharField', [], {'max_length': '90', 'db_column': "'COS_Obs'"}),
            'Tipo_Cobro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Tipo_Cobro']", 'db_column': "'TCO_Id'"}),
            'Tipo_Costo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Tipo_Costo_Vario']", 'db_column': "'TIC_Id'"}),
            'Titulo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COS_Titu'", 'decimal_places': '2', 'max_digits': '10'}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'COS_Usua'"}),
            'Valor': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'COS_Valo'", 'decimal_places': '2', 'max_digits': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.trans_predio': {
            'Anio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Cobro_Predios']", 'db_column': "'COB_Id'"}),
            'Avaluo': ('django.db.models.fields.DecimalField', [], {'db_column': "'PRE_Aval'", 'decimal_places': '2', 'max_digits': '18'}),
            'Estado': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'PRE_Est'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'PRE_Fech'"}),
            'Fecha_Emision': ('django.db.models.fields.DecimalField', [], {'db_column': "'PRE_Femi'", 'decimal_places': '2', 'max_digits': '10'}),
            'Meta': {'ordering': "('Fecha',)", 'object_name': 'Trans_Predio', 'db_table': "'SISCBR_TPredio'"},
            'Metros': ('django.db.models.fields.DecimalField', [], {'db_column': "'PRE_Metros'", 'decimal_places': '2', 'max_digits': '10'}),
            'Predio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Predio']", 'db_column': "'PDI_Id'"}),
            'Recargos': ('django.db.models.fields.DecimalField', [], {'db_column': "'PRE_Reca'", 'decimal_places': '2', 'max_digits': '10'}),
            'Tasa': ('django.db.models.fields.DecimalField', [], {'db_column': "'PRE_Tasa'", 'decimal_places': '2', 'max_digits': '10'}),
            'Tipo_Cobro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Tipo_Cobro']", 'db_column': "'TCO_Id'"}),
            'Tipo_Pago': ('django.db.models.fields.IntegerField', [], {}),
            'Titulo': ('django.db.models.fields.DecimalField', [], {'db_column': "'PRE_Titu'", 'decimal_places': '2', 'max_digits': '10'}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'PRE_Usua'"}),
            'Valor_Tasa': ('django.db.models.fields.DecimalField', [], {'db_column': "'PRE_Vtas'", 'decimal_places': '2', 'max_digits': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.vehiculo': {
            'Anio': ('django.db.models.fields.IntegerField', [], {'db_column': "'VEH_Anio'"}),
            'Avaluo': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'VEH_Avaluo'", 'decimal_places': '2', 'max_digits': '18'}),
            'Capacidad': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'db_column': "'VEH_Capa'", 'decimal_places': '2', 'max_digits': '10'}),
            'Chofer': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'VEH_Chofer'"}),
            'Cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Cliente']", 'db_column': "'CLI_Id'"}),
            'Color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'VEH_Color'"}),
            'Estado': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'VEH_Estado'"}),
            'Fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 10, 0, 0)', 'db_column': "'VEH_Fech'"}),
            'Marca': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'VEH_Marca'"}),
            'Meta': {'ordering': "('Anio',)", 'object_name': 'Vehiculo', 'db_table': "'SISCBR_MVehiculo'"},
            'Modelo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'VEH_Modelo'"}),
            'Ruta': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'VEH_Ruta'"}),
            'Tipo': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'VEH_Tipo'"}),
            'Usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'VEH_Usua'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['main']