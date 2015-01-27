from django.contrib import admin
from app.models import UOM, ProductCategory, Product


from import_export import resources, fields, widgets

class ProductCategoryResource (resources.ModelResource):
    class Meta:
        model = ProductCategory
        exclude = ('show_it', 'created_date', 'last_modify_time')
        import_id_fields = ['code']

class UOMResource (resources.ModelResource):
    class Meta:
        model = UOM
        exclude = ('created_date', 'last_modify_time')

class ProductForeignKeyWidgetUOM (widgets.ForeignKeyWidget):
    def clean(self, value):
        # for import usage, return uom object for uom code
        t1 = super(widgets.ForeignKeyWidget, self).clean(value)
        return self.model.objects.get(name=t1) if t1 else None

    def render(self, value):
        return value.name

class ProductForeignKeyWidgetCategory (widgets.ForeignKeyWidget):
    def clean(self, value):
        # return product_category  object for product category code
        t1 = super(widgets.ForeignKeyWidget, self).clean(value)
        return self.model.objects.get(code=t1) if t1 else None
    def render(self, value):
        return value.name

class ProductResource (resources.ModelResource):
    uom = fields.Field(column_name='uom', attribute='uom', widget=ProductForeignKeyWidgetUOM(UOM, 'name'))
    category = fields.Field(column_name='category', attribute='category', widget=ProductForeignKeyWidgetCategory(ProductCategory, 'code'))

    class Meta:
        model = Product
        exclude = ('sales_intro', 'sales_intro_indo', 'sales_intro_viet', 'sort_order', 'created_date', 'last_modify_time')
        import_id_fields = ['code']


# ModelAdmins
from import_export.admin import ImportExportModelAdmin, ImportExportModelAdmin

class UOMAdmin(ImportExportModelAdmin):
    resource_class = UOMResource
    pass

class ProductCategoryAdmin(ImportExportModelAdmin):
    resource_class = ProductCategoryResource
    pass

class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    pass

admin.site.register(UOM, UOMAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)