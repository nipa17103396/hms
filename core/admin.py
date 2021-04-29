from django.contrib import admin

# Register your models here.
from core.models import User, Doctor, Patient, Appointment, Prescription, Feedback, Notification, Medicine,CustomUser


admin.site.register(CustomUser)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email',)
    list_filter = ('name','email')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','designation','email',)
    list_filter = ('name','email')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','age','gender','address','phone')
    list_filter = ('name','age')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date','name','age','phone','email','p_doctor','gender')
    # list_filter = ('pname','date')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('pname','date','bp','weight','medicine','additional_instruction','history')
    list_filter = ('pname','date')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('pname','feedback',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('name','date','description',)
    list_filter = ('name','date')

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name','generic_name',)
    list_filter = ('name','generic_name')
