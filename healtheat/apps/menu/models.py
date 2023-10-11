from healtheat.apps.base import models as base_models
from healtheat.apps.base.models import models


class DailyMenuModel(base_models.TimeStampedModel):

    class Day(models.IntegerChoices):
        MON = 1, 'Понедельник'
        TUE = 2, 'Вторник'
        WED = 3, 'Среда'
        THU = 4, 'Четверг'
        FRI = 5, 'Пятница'
        SAT = 6, 'Суббота'
        SUN = 7, 'Воскресенье'

    day = models.PositiveSmallIntegerField(verbose_name='День недели', unique=True, choices=Day.choices)
    breakfast = base_models.BlankCharField(verbose_name='Завтрак')
    elevenses = base_models.BlankCharField(verbose_name='Второй завтрак')
    lunch = base_models.BlankCharField(verbose_name='Обед')
    afternoon_tea = base_models.BlankCharField(verbose_name='Полдник')
    dinner = base_models.BlankCharField(verbose_name='Ужин')

    class Meta:
        ordering = ['day']
        verbose_name = 'Ежедневное меню'
        verbose_name_plural = verbose_name

    def __str__(self):
        return list(filter(lambda x: (x[0] == self.day), DailyMenu.Day.choices))[0][1]
