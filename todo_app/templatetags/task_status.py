from django import template

register = template.Library()


@register.filter
def transform_task_status(status):
    if status:
        return "Undo"
    return "Complete"


@register.filter
def display_task_status(status):
    if status:
        return "Done"
    return "Not done"
