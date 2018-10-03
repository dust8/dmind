import hashlib
import json

import pkg_resources
from IPython.core.magic import (Magics, cell_magic, line_cell_magic,
                                line_magic, magics_class)

STRING_KITY = pkg_resources.resource_string(__name__,
                                            "./static/kity.min.js").decode()
STRING_KITYMINDER_JS = pkg_resources.resource_string(
    __name__, "./static/kityminder.core.min.js").decode()
STRING_KITYMINDER_CSS = pkg_resources.resource_string(
    __name__, "./static/kityminder.core.css").decode()
STRING_RENDER = pkg_resources.resource_string(__name__,
                                              './static/render.js').decode()

DATATYPE = ['json', 'text', 'markdown']
TEMPLATE = {
    'default': '思维导图',
    'tianpan': '天盘图',
    'structure': '组织结构图',
    'filetree': '目录组织图',
    'right': '逻辑结构图',
    'fish-bone': '鱼骨头图'
}
THEME = {
    'classic': '脑图经典',
    'classic-compact': '紧凑经典',
    'snow': '温柔冷光',
    'snow-compact': '紧凑冷光',
    'fish': '鱼骨图',
    'wire': '线框',
    'fresh-red': '清新红',
    'fresh-soil': '泥土黄',
    'fresh-green': '文艺绿',
    'fresh-blue': '天空蓝',
    'fresh-purple': '浪漫紫',
    'fresh-pink': '脑残粉',
    'fresh-red-compat': '紧凑红',
    'fresh-soil-compat': '紧凑黄',
    'fresh-green-compat': '紧凑绿',
    'fresh-blue-compat': '紧凑蓝',
    'fresh-purple-compat': '紧凑紫',
    'fresh-pink-compat': '紧凑粉',
    'tianpan': '经典天盘',
    'tianpan-compact': '紧凑天盘'
}


class Warner:
    def __init__(self, message):
        self.message = message

    def _repr_html_(self):
        return self.message


class Header:
    def _repr_html_(self):
        html = '<script>%s</script>' % (STRING_KITY)
        html += '<script>%s</script>' % (STRING_KITYMINDER_JS)
        html += '<style type="text/css">%s</style>' % (STRING_KITYMINDER_CSS)
        html += '<script>%s</script>' % (STRING_RENDER)
        html += 'imported assert.'
        return html


class Section:
    def __init__(self, datatype, text, template, theme):
        self.datatype = datatype
        self.text = text
        self.template = template
        self.theme = theme
        self.selector_id = 'd_' + hashlib.md5(text.encode()).hexdigest()

    def __str__(self):
        return self.text

    def _repr_html_(self):
        html = '<script id="%s" type="application/kityminder" minder-data-type="%s">%s</script>' % (
            self.selector_id, self.datatype, self.text)
        html += '<script>renderMind("#%s","%s","%s")</script>' % (
            self.selector_id, self.template, self.theme)
        return html


@magics_class
class MindMagics(Magics):
    @line_magic
    def dmindheader(self, line):
        return Header()

    @cell_magic
    def dmind(self, line, cell):
        args = line.strip().split()
        cell = cell.strip()

        while len(args) < 3:
            args.append(None)

        datatype, template, theme = args
        if datatype and datatype not in DATATYPE:
            return Warner('datatype not found.<pre>%s</pre>' % (json.dumps(
                DATATYPE, ensure_ascii=False, indent=4)))

        if template and template not in TEMPLATE:
            return Warner('template not found.<pre>%s</pre>' % (json.dumps(
                TEMPLATE, ensure_ascii=False, indent=4)))

        if theme and theme not in THEME:
            return Warner('theme not found.<pre>%s</pre>' % (json.dumps(
                THEME, ensure_ascii=False, indent=4)))

        return Section(datatype or 'markdown', cell, template or 'default',
                       theme or 'classic-compact')
