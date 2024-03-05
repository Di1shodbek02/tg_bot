from django.contrib import admin

from main.models import Position, Employee


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
