function reference_click_function() {
	clear_prev_reference($(this).parents("article"));
	clear_focus();
	set_focus($(this));
	request_partial(this.href);
	return false;
}

function edit_click_function() {
	$(this).next(".content").toggle();
	$(this).nextAll(".edit-content").toggle();
	return false;
}

function reference_binding() {
	$(".reference").click(reference_click_function);
}

function edit_binding() {
	$(".edit").click(edit_click_function);
	$(".edit-submit").click(save_content);
}

function clear_prev_reference(element) {
	element.nextAll("article").remove();
}

function clear_focus() {
	$(".focus").toggleClass("focus");
}

function set_focus(element) {
	element.toggleClass("focus");
}

function update_width() {
	var n_articles = $("article").length;
	var width = 600;
	if (n_articles > 1) {
		width += 400 * (n_articles - 1);
	}
	$("#content").width(width);
}

function request_partial(address) {
	$.get(address, function (data) {
		var new_article = $("<article></article>").append(data);
		new_article.find(".reference").click(reference_click_function);
		new_article.find(".edit").click(edit_click_function);
		new_article.find(".edit-submit").click(save_content);
		$("#content").append(new_article);
		update_width();
	});
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

$(document).ready(function () {
	reference_binding();
	edit_binding();
});
