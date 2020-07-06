from open.utilities.fields import DEFAULT_MODELS_CHAR_FIELD
from open.utilities.models import BaseModelWithUserGeneratedContent


class UserSupplementStack(BaseModelWithUserGeneratedContent):
    # name = CharField(max_length=300, blank=False, default="")
    name = DEFAULT_MODELS_CHAR_FIELD

    class Meta:
        unique_together = ("user", "name")
        ordering = ["user", "name"]
        verbose_name = "Supplements Stack"
        verbose_name_plural = "Supplements Stacks"

    def __str__(self):
        return "{} Stack".format(self.name)

    @property
    def description(self):
        compositions = self.compositions.all()
        descriptions = [composition.description for composition in compositions]

        if descriptions:
            return ", ".join(descriptions)
        else:
            return ""
