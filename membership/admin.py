from django.contrib import admin

from .models import MembershipPlan, Customer

admin.site.register(MembershipPlan)
admin.site.register(Customer)
