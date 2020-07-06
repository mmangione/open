from django.db.models import DecimalField, ForeignKey, CASCADE

from open.core.betterself.models.supplement import Supplement
from open.core.betterself.models.user_supplement_stack import UserSupplementStack
from open.utilities.models import BaseModelWithUserGeneratedContent


class UserSupplementStackComposition(BaseModelWithUserGeneratedContent):
    supplement = ForeignKey(Supplement, on_delete=CASCADE)
    stack = ForeignKey(
        UserSupplementStack, related_name="compositions", on_delete=CASCADE
    )
    # by default, don't allow this to be blank, it doesn't make sense for a supplement stack
    quantity = DecimalField(
        max_digits=10, decimal_places=4, null=False, blank=False, default=1
    )

    class Meta:
        unique_together = ("user", "supplement", "stack")

    def __str__(self):
        return "{}-{}".format(self.stack, self.supplement)

    @property
    def description(self):
        return "{quantity} {supplement}".format(
            quantity=self.quantity, supplement=self.supplement
        )
