(function() {
  tinymce.PluginManager.requireLangPack('latex');
  tinymce.create('tinymce.plugins.LatexPlugin',{
    init: function(ed,url) {
      ed.addCommand('LatexPlugin',function() {
        ed.windowManager.open( {
          file:url+'/dialog.htm',
          width:750+parseInt(ed.getLang('latex.delta_width',0)),
          height:530+parseInt(ed.getLang('latex.delta_height',0)),
          inline:1
        },{
          plugin_url:url
        })
      });
      ed.addButton('latex', {
        title:'Insert latex code',
        cmd:'LatexPlugin',
        image:url+'/img/latex.gif'
      });
      ed.onNodeChange.add(function(ed,cm,n) {
        cm.setActive('latex',n.nodeName=='IMG')
      })
    },
    getInfo:function() {
      return {
        longname:'Latex plugin',
        author:'Eric Wohnlich',
        authorurl:'http://www.imsweb.com',
        infourl:'https://git.imsweb.com/plone/collective.tinymceplugins.latex',
        version:"1.0"
      }
    }
  });
  tinymce.PluginManager.add('latex',tinymce.plugins.LatexPlugin)
})();