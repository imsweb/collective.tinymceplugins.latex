var LatexDialog = {

    init: function () {
        var code = top.tinymce.activeEditor.selection.getNode().alt,
            size = top.tinymce.activeEditor.selection.getNode().attributes['data-latex_size'];
        if (code) {
            document.forms[0].latex_code.innerHTML = code;
        }
        if (size) {
            document.forms[0].latex_size.value = size;
        }

    },

    close: function () {
        top.tinymce.activeEditor.windowManager.close();
    },

    insert: function () {

        var latexCode = document.forms[0].latex_code.value,
            latexSize = document.forms[0].latex_size.value;

        var img = '<img class="latex" src="' + LatexDialog.getSrc(latexCode, latexSize) + '" alt="' + latexCode + '" data-latex_size="' + latexSize + '"/>';

        top.tinymce.activeEditor.selection.setContent(img);
        top.tinymce.activeEditor.windowManager.close();
    },

    preview: function () {
        var latexCode = document.forms[0].latex_code.value,
            latexSize = document.forms[0].latex_size.value,
            error_text = $('#error_text'),
            preview_img = $('#previewImg');
        error_text.html('');
        preview_img.attr('src', '../++plone++static/select2-spinner.gif');

        var latex_src = LatexDialog.getSrc(latexCode, latexSize);
        // check if it created a valid image
        $.get(latex_src).success(function (data) {
            if (typeof(data) == "string" && data.startsWith('error')) {
                data = 'There was an error rendering this image: ' + data.slice(7);
                error_text.html(data);
                preview_img.attr('src','');
            }
        });

        if (document.forms[0].latex_code.value != '') {
            preview_img.attr('src', latex_src);
        }

    },

    getSrc: function (code, size) {

        return '@@latex?f=' + encodeURIComponent(code) + '&s=' + size;

    }
};