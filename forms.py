from datetime import date
from wtforms.form import Form
from wtforms.fields import BooleanField, FieldList, FormField, HiddenField, IntegerField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms.widgets import CheckboxInput, TextInput, TextArea, Select, SubmitInput
from wtforms.widgets.html5 import DateInput, NumberInput


class BaseForm(Form):
    class Meta:
        locales = ['ru_RU', 'ru']


class CustomCheckboxInput(CheckboxInput):
    """Custom checkbox input with Bootstrap validation from WTForms CheckboxInput"""

    def __init__(self, error_class=u"is-invalid"):
        super(CustomCheckboxInput, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        c = kwargs.pop(
            "class", "") or kwargs.pop("class_", "")
        kwargs["class"] = u"form-check-input %s" % c

        if field.errors:
            kwargs["class"] += self.error_class
            kwargs["aria-describedby"] = u"%sValidationFeedback" % field.id

        return super(CustomCheckboxInput, self).__call__(field, **kwargs)

class CustomNumberInput(NumberInput):
    """Custom number input with Bootstrap validation from WTForms NumberInput"""

    def __init__(self, error_class=u"is-invalid", step=None, min=None, max=None):
        super(CustomNumberInput, self).__init__(step, min, max)
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        c = kwargs.pop(
            "class", "") or kwargs.pop("class_", "")
        kwargs["class"] = u"form-control form-control-sm %s" % c

        if field.errors:
            kwargs["class"] += self.error_class
            kwargs["aria-describedby"] = u"%sValidationFeedback" % field.id

        return super(CustomNumberInput, self).__call__(field, **kwargs)

class CustomTextInput(TextInput):
    """Custom input with Bootstrap validation from WTForms TextInput"""

    def __init__(self, error_class=u"is-invalid"):
        super(CustomTextInput, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        c = kwargs.pop(
            "class", "") or kwargs.pop("class_", "")
        kwargs["class"] = u"form-control form-control-sm %s" % c

        if field.errors:
            kwargs["class"] += self.error_class
            kwargs["aria-describedby"] = u"%sValidationFeedback" % field.id

        return super(CustomTextInput, self).__call__(field, **kwargs)

class CustomSelect(Select):
    """Custom select with Bootstrap validation from WTForms Select"""

    def __init__(self, error_class=u"is-invalid"):
        super(CustomSelect, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        c = kwargs.pop(
            "class", "") or kwargs.pop("class_", "")
        kwargs["class"] = u"form-control form-control-sm custom-select custom-select-sm %s" % c

        if field.errors:
            kwargs["class"] += self.error_class
            kwargs["aria-describedby"] = u"%sValidationFeedback" % field.id

        return super(CustomSelect, self).__call__(field, **kwargs)

class CustomSubmitInput(SubmitInput):
    """Custom submit input with Bootstrap validation from WTForms SubmitInput"""

    def __init__(self, error_class=u"is-invalid"):
        super(CustomSubmitInput, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        c = kwargs.pop(
            "class", "") or kwargs.pop("class_", "")
        if c:
            kwargs["class"] = c
        else:
            kwargs["class"] = u"btn btn-primary"

        return super(CustomSubmitInput, self).__call__(field, **kwargs)
