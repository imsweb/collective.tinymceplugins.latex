tinyMCEPopup.requireLangPack();

var LatexDialog = {

	init : function() {
		if (code = tinyMCE.activeEditor.selection.getNode().alt){
			document.forms[0].latex_code.innerHTML = code;
		}
		if (size = tinyMCE.activeEditor.selection.getNode().attributes['latex_size']){
		  document.forms[0].latex_size.value = size;
		}

	},

	insert : function() {

		var latexCode = document.forms[0].latex_code.value
		    latexSize = document.forms[0].latex_size.value;

		var img = '<img class="latex" src="' + LatexDialog.getSrc(latexCode,latexSize) + '" alt="'+ latexCode +'" latex_size="' + latexSize + '"/>';

		tinyMCEPopup.editor.execCommand('mceInsertContent', false, img);
		tinyMCEPopup.close();
	},

	preview : function() {
		var latexCode = document.forms[0].latex_code.value
		    latexSize = document.forms[0].latex_size.value;

    latex_src = LatexDialog.getSrc(latexCode,latexSize);
    // check if it created a valid image
    $.get(latex_src).success(function(data) {
      if (data.startsWith('error')) {
        data = 'There was an error rendering this image: ' + data.slice(7);
        document.getElementById('error_text').innerHTML = data;
      }
    });

		if (document.forms[0].latex_code.value != ''){
			document.getElementById('previewImg').src = latex_src;
		}

	},

	getSrc : function(code,size){

		return '@@latex?f=' + encodeURIComponent(code) + '&s=' + size;

	}
};

tinyMCEPopup.onInit.add(LatexDialog.init, LatexDialog);
