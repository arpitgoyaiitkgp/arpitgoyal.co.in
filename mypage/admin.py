from django.contrib import admin
from mypage.models import TestScores, Honors, Projects, VolunteerServices, Certifications, Languages, Skills, Experience, Education
# Register your models here.

class TestScoresAdmin(admin.ModelAdmin):

    pass


class HonorsAdmin(admin.ModelAdmin):

    pass


class ProjectsAdmin(admin.ModelAdmin):

    pass


class VolunteerServicesAdmin(admin.ModelAdmin):

    pass


class CertificationsAdmin(admin.ModelAdmin):

    pass


class LanguagesAdmin(admin.ModelAdmin):

    pass


class SkillsAdmin(admin.ModelAdmin):

    pass


class ExperienceAdmin(admin.ModelAdmin):

    pass


class EducationAdmin(admin.ModelAdmin):

    pass


admin.site.register(TestScores, TestScoresAdmin)
admin.site.register(Honors, HonorsAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(VolunteerServices, VolunteerServicesAdmin)
admin.site.register(Certifications, CertificationsAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
