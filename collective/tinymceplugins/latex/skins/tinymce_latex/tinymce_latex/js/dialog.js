tinyMCEPopup.requireLangPack();

var LatexDialog = {

	init : function() {
		if (code = tinyMCE.activeEditor.selection.getNode().alt){
			document.forms[0].latex_code.innerHTML = code;
		}
		if (size = tinyMCE.activeEditor.selection.getNode().latex_size){
		  document.forms[0].latex_size.value = size;
		}

	},

	insert : function() {

		var latexCode = document.forms[0].latex_code.value
		    latexSize = document.forms[0].latex_size.value;

		var img = '<img class="latex" src="' + LatexDialog.getSrc(latexCode) + '" alt="'+ latexCode +'" latex_size="' + latexSize + '"/>';

		tinyMCEPopup.editor.execCommand('mceInsertContent', false, img);
		tinyMCEPopup.close();
	},

	preview : function() {

		var latexCode = document.forms[0].latex_code.value
		    latexSize = document.forms[0].latex_size.value;

		if (document.forms[0].latex_code.value != ''){

			document.getElementById('previewImg').src = LatexDialog.getSrc(latexCode,latexSize);

		}

	},

	getSrc : function(code,size){

		return '@@latex?f=' + encodeURIComponent(code) + '&s=' + size;

	}
};

tinyMCEPopup.onInit.add(LatexDialog.init, LatexDialog);
