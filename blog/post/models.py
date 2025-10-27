from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class PostModel(models.Model):

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    title = models.CharField(_("Title"), max_length=1024)
    description = models.TextField(_("Short description"))
    content = models.TextField(_("Content"))
    image = models.ImageField(
        _("Image"),
        upload_to="post_images",
        max_length=None,
        null=True,
    )
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("PostModel_detail", kwargs={"pk": self.pk})
