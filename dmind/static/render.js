function renderMind(target, template, theme) {
    var protocols = { json: 'json', text: 'text', markdown: 'markdown' };
    var km = new kityminder.Minder();
    if (typeof target == 'string') {
        target = document.querySelector(target);
    }
    if (!target) return;
    var protocol = target.getAttribute('minder-data-type');
    if (protocol in protocols) {
        var data = target.textContent;
        target.textContent = null;
        km.renderTo(target);
        km.importData(protocol, data);
    }
    km.disable();
    km.execCommand('hand');
    km.execCommand('Zoom', 70);
    setTimeout(function () {
        km.useTemplate(template || 'default');
        km.useTheme(theme || 'classic');
    },
        0
    )
}
