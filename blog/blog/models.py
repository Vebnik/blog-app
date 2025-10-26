from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class PostModel(models.Model):

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    name = models.CharField(_("Name"), max_length=1024)
    short_description = models.TextField(_("Short description"))
    content = models.TextField(_("Content"))
    image = models.ImageField(
        _("Image"),
        upload_to="post_images",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PostModel_detail", kwargs={"pk": self.pk})


class CommentModel(models.Model):

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    author = models.CharField(_("Author"), max_length=128)
    content = models.TextField(_("Content"))
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    post = models.ForeignKey(PostModel, verbose_name=_("Post"), on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.post} - {self.author}"

    def get_absolute_url(self):
        return reverse("CommentModel_detail", kwargs={"pk": self.pk})
