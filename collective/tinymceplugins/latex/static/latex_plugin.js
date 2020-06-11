(function () {
    tinymce.PluginManager.requireLangPack('latex');
    tinymce.create('tinymce.plugins.LatexPlugin', {
        init: function (ed, url) {
            ed.addCommand('LatexPlugin', function () {
                ed.windowManager.open({
                    url: url + '/@@dialog.html',
                    title: 'LaTeX Editor',
                    width: 750,
                    height: 530,
                    inline: 1
                }, {
                    plugin_url: url
                })
            });
            ed.addButton('latex', {
                title: 'Insert latex code',
                cmd: 'LatexPlugin',
                image: url + '/latex.gif',
                stateSelector: 'img[src*="@@latex"]'
            });
        },
        getInfo: function () {
            return {
                longname: 'Latex plugin',
                author: 'Eric Wohnlich',
                authorurl: 'http://www.imsweb.com',
                infourl: 'https://github.com/imsweb/collective.tinymceplugins.latex',
                version: "1.0"
            }
        }
    });
    tinymce.PluginManager.add('latex', tinymce.plugins.LatexPlugin)
})();