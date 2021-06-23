from arches.app.datatypes.base import BaseDataType
from arches.app.models import models
from arches.app.models.system_settings import settings

html_widget = models.Widget.objects.get(name="htmlembed-widget")

details = {
    "datatype": "html-datatype",
    "iconclass": "fa fa-file-code-o",
    "modulename": "datatypes.py",
    "classname": "HTMLDataType",
    "defaultwidget": html_widget,
    "defaultconfig": None,
    "configcomponent": None,
    "configname": None,
    "isgeometric": False,
    "issearchable": False,
}


class HTMLDataType(BaseDataType):

    def validate(self, value, row_number=None, source=None, node=None, nodeid=None, strict=False):
        errors = []
        # try:
        #     value.upper()
        # except Exception:
        #     errors.append(
        #         {
        #             "type": "ERROR",
        #             "message": "datatype: {0} value: {1} {2} {3} - {4}. {5}".format(
        #                 self.datatype_model.datatype, value, row_number, source, "this is not a string", "This data was not imported."
        #             ),
        #         }
        #     )
        return errors


