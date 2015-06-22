from django.db import models


class TestScores(models.Model):
    test_name = models.CharField(max_length = 100)
    score = models.CharField(max_length = 50)
    test_month = models.IntegerField()
    test_year = models.IntegerField()
    description = models.TextField()


class Honors(models.Model):
    honors_name = models.CharField(max_length = 100)
    honor_month = models.IntegerField()
    honor_year = models.IntegerField()
    description = models.TextField()


class Projects(models.Model):
    project_title = models.CharField(max_length = 100)
    start_year = models.IntegerField()
    start_month = models.IntegerField()
    end_year = models.IntegerField()
    end_month = models.IntegerField()
    description = models.TextField()


class VolunteerServices(models.Model):
    volunteer_experience_name = models.CharField(max_length = 50)
    volunteer_start_month = models.IntegerField()
    volunteer_start_year = models.IntegerField()
    volunteer_end_month = models.IntegerField()
    volunteer_end_year = models.IntegerField()
    description = models.TextField


class Certifications(models.Model):
    certification_name = models.CharField(max_length = 100)
    certification_duration_in_year = models.IntegerField()
    certification_duration_in_month = models.IntegerField()
    description = models.TextField()


class Languages(models.Model):
    language_name = models.CharField(max_length = 50)


class Skills(models.Model):
    skill_name = models.CharField(max_length = 50)
    skill_upvote = models.IntegerField()


class Experience(models.Model):
    company_name = models.CharField(max_length = 100)
    company_logo_url = models.URLField()
    job_title = models.CharField(max_length = 100)
    start_year = models.IntegerField()
    start_month = models.IntegerField()
    end_year = models.IntegerField()
    end_month = models.IntegerField()
    is_current = models.BooleanField()
    description = models.TextField()
    projects = models.ForeignKey('Projects')


class Education(models.Model):
    institute_name = models.CharField(max_length = 100)
    qualifications = models.CharField(max_length = 100)
    start_year = models.IntegerField()
    start_month = models.IntegerField()
    end_year = models.IntegerField()
    end_month = models.IntegerField()
    projects = models.ForeignKey('Projects')
