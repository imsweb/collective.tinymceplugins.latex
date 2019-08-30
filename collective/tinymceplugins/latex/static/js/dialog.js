var LatexDialog = {

    init: function () {
        var code = top.tinymce.activeEditor.selection.getNode().alt,
            size = top.tinymce.activeEditor.selection.getNode().getAttribute('data-latex_size'),
            pad_inches = top.tinymce.activeEditor.selection.getNode().getAttribute('data-pad_inches'),
            alignment = top.tinymce.activeEditor.selection.getNode().getAttribute('data-alignment');
        // also check class for alignment
        if (!alignment) {
            $.each(top.tinymce.activeEditor.selection.getNode().getAttribute('class').split(' '), function(idx, val) {
                if (val.startsWith('image-')) {
                    alignment = val.substring(6);
                }
            })
        }

        if (code) {
            document.forms[0].latex_code.innerHTML = code;
        }
        if (size) {
            document.forms[0].latex_size.value = size;
        }
        if (pad_inches) {
            document.forms[0].pad_inches.value = pad_inches;
        }
        if (alignment) {
            document.forms[0].alignment.value = alignment;
        }
    },

    close: function () {
        top.tinymce.activeEditor.windowManager.close();
    },

    insert: function () {

        var latexCode = document.forms[0].latex_code.value,
            latexSize = document.forms[0].latex_size.value,
            pad_inches = document.forms[0].pad_inches.value,
            alignment = document.forms[0].alignment.value;
        if (alignment) {
            alignment = ' image-' + alignment;
        }
        if (latexCode) {
            var img = '<img class="latex' + alignment + '" src="' + LatexDialog.getSrc(latexCode, latexSize, pad_inches) + '" alt="' + latexCode + '" data-latex_size="' + latexSize + '" data-pad_inches="' + pad_inches + ' data-alignment="' + alignment + '"/>';

            top.tinymce.activeEditor.selection.setContent(img);
        }
        top.tinymce.activeEditor.windowManager.close();
    },

    preview: function () {
        var latexCode = document.forms[0].latex_code.value,
            latexSize = document.forms[0].latex_size.value,
            pad_inches = document.forms[0].pad_inches.value,
            error_text = $('#error_text'),
            preview_img = $('#previewImg'),
            loading = $('.loading_text');
        error_text.html('');
        preview_img.attr('src', '../++plone++static/select2-spinner.gif');
        loading.show();

        var latex_src = LatexDialog.getSrc(latexCode, latexSize, pad_inches);
        // check if it created a valid image
        $.get(latex_src).success(function (data) {
            if (typeof(data) === "string" && data.startsWith('error')) {
                data = 'There was an error rendering this image: ' + data.slice(7);
                error_text.html(data);
                error_text.show();
                preview_img.attr('src','');
            }
        });

        if (document.forms[0].latex_code.value !== '') {
            preview_img.attr('src', latex_src);
        }
        loading.hide();

    },

    getSrc: function (code, size, pad_inches) {

        return '@@latex?f=' + encodeURIComponent(code) + '&s=' + size + '&p=' + pad_inches;

    }
};