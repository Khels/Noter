from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


class Note(models.Model):
    class Meta:
        ordering = ['-date_created']

    text = models.TextField(
        _('content'),
        help_text="Write everything down here so as not to forget it later!",
    )
    date_created = models.DateTimeField(
        _('date of creation'),
        auto_now_add=True,
        db_index=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
    )
    image = models.ImageField(
        _('image'),
        upload_to='notes/',
        blank=True,
        null=True,
        help_text='Attach here any image you want if need be'
    )

    def __repr__(self):
        return ('<Note %s, %s, %s>' %
                self.text[:15], self.created, self.author)

    def __str__(self):
        return self.text[:15]
