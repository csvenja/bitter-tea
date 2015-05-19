function edit_click_function() {
	$(this).next(".content").toggle();
	$(this).nextAll(".edit-content").toggle();
	$(".remove-logic").toggle();
	$(".add-reference").toggle();
	return false;
}

function save_content() {
	var textarea = $(this).prev(".edit-pad");
	var id = textarea.attr("data-id");
	var content = textarea.val();
	var edit = $(this).parent();
	$.post("/edit/" + id + '/', { content: content }, function (data) {
		edit.prev(".content").toggle();
		edit.toggle();
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
