from django.db import models


class Menu(models.Model):
    """
    Model Main Menu
    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-id",)
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'


class MenuItem(models.Model):
    """
    Model Menu Item
    """
    title = models.CharField(max_length=255)

    menu = models.ForeignKey(Menu, blank=True, related_name='items', 
        on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True,
        related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("-id",)
        verbose_name = 'Подкаталог'
        verbose_name_plural = 'Подкаталоги'