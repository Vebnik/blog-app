from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class CommentModel(models.Model):

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    author = models.CharField(_("Author"), max_length=128)
    content = models.TextField(_("Content"))
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    post = models.ForeignKey("post.PostModel", verbose_name=_("Post"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post} ({self.author})"

    def get_absolute_url(self):
        return reverse("CommentModel_detail", kwargs={"pk": self.pk})
