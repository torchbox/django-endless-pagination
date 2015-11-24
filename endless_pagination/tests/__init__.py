"""Test model definitions."""


def make_model_instances(number):
    """Make a ``number`` of test model instances and return a queryset."""
    from endless_pagination.models import TestModel
    for _ in range(number):
        TestModel.objects.create()
    return TestModel.objects.all()
