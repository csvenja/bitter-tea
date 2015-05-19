function edit_click_function() {
	toggle_edit(this);
	return false;
}

function toggle_edit(sender) {
	var article = $(sender).closest("article");
	article.find(".content").toggle();
	article.find(".edit-content").toggle();
	article.find(".remove-reference").toggle();
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

function add_reference() {
	var article = $(this).closest("article");
	var from_id = article.find(".current-id").val()
	var to_id = article.find(".add-reference-select").val()
	var logic = article.find(".add-reference-logic").val()
	console.log(from_id)
	console.log(to_id)
	console.log(logic)

	var that = this;
	$.post("/add_link/", {
		from_id: from_id,
		to_id: to_id,
		logic: logic
	}, function (data) {
		toggle_edit(that);

		// FIXME: could be more 优雅
		location.reload();
	})
	.fail(function (error) {
		console.log(error);
	});
}

function remove_reference() {
	var article = $(this).closest("article");
	var from_id = article.find(".current-id").val()
	var li = $(this).closest("li");
	var to_id = $(this).attr("data-to-id")

	var that = this;
	$.post("/remove_link/", {
		from_id: from_id,
		to_id: to_id
	}, function (data) {
		toggle_edit(that);

		// FIXME: could be more 优雅
		location.reload();
	})
	.fail(function (error) {
		console.log(error);
	});
}

function edit_binding() {
	$(".edit").click(edit_click_function);
	$(".edit-submit").click(save_content);
	$(".add-reference-button").click(add_reference);
	$(".remove-reference").click(remove_reference);
}

$(document).ready(function () {
	edit_binding();
});
