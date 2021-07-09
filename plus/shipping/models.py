from oscar.apps.shipping.methods import *  # noqa isort:skip
from oscar.apps.shipping import repository
from oscar.core import prices


class Free(Base):
    code = 'standard'
    name = 'Standard shipping (free)'
    description = 'Доставка в течении 3-х рабочих дней'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('25000'), incl_tax=D('0.00'))


class Express(FixedPrice):
    code = 'express'
    name = 'Экспресс доставка'
    description = 'Доставка в 24 часа'
    charge_excl_tax = D('25000')


class Repository(repository.Repository):
    methods = (
        Free(),
        Express()
    )


from oscar.apps.shipping.models import *  # noqa isort:skip
