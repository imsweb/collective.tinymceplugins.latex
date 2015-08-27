/*
 * TinyMCELatexPlugin - A plugin to write formulae in TinyMCE through Google APIs .
 * v1.0 - by Diego Caponera - http://www.diegocaponera.com/
 * MIT Licensed.
 */

tinyMCEPopup.requireLangPack();

var LatexDialog = {

	init : function() {
		if (code = tinyMCE.activeEditor.selection.getNode().alt){

			document.forms[0].latex_code.innerHTML = code;

		}
	},

	insert : function() {

		var latexCode = document.forms[0].latex_code.value;

		var img = '<img class="latex" src="' + LatexDialog.getSrc(latexCode) + '" alt="'+ latexCode +'"/>';

		tinyMCEPopup.editor.execCommand('mceInsertContent', false, img);
		tinyMCEPopup.close();
	},

	preview : function() {

		var latexCode = document.forms[0].latex_code.value

		if (document.forms[0].latex_code.value != ''){

			document.getElementById('previewImg').src = LatexDialog.getSrc(latexCode);

		}

	},

	getSrc : function(code){

		return '@@latex?f=' + encodeURIComponent(code);

	}
};

tinyMCEPopup.onInit.add(LatexDialog.init, LatexDialog);
