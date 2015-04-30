function click_function() {
	clear_prev_reference($(this).parents("article"));
	clear_focus();
	set_focus($(this));
	request_partial(this.href);
	return false;
}

function reference_binding() {
	$(".reference").click(click_function);
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

function request_partial(address) {
	$.get(address, function (data) {
		var new_article = $("<article></article>").append(data);
		new_article.click(click_function);
		$("#content").append(new_article);
	});
}

$(document).ready(function () {
	reference_binding();
});
