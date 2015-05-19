function edit_click_function() {
	toggle_edit(this);
	return false;
}

function toggle_edit(sender) {
	var article = $(sender).closest("article");
	article.find(".content").toggle();
	article.find(".edit-content").toggle();
	article.find(".remove-logic").toggle();
	article.find(".add-reference").toggle();
}

function save_content() {
	var textarea = $(this).prev(".edit-pad");
	var id = textarea.attr("data-id");
	var content = textarea.val();
	var that = this;
	$.post("/edit/" + id + '/', { content: content }, function (data) {
		toggle_edit(that);
	})
	.fail(function (error) {
		console.log(error);
	});
}

function edit_binding() {
	$(".edit").click(edit_click_function);
	$(".edit-submit").click(save_content);
}

$(document).ready(function () {
	edit_binding();
});
