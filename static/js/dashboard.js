var filter_obj = {
  object: "",
};
const ajax_method = {
  url: url_path,
  type: "GET",
  data: filter_obj,
  beforeSend: function () {
    $("#filter_data_post").hide();
    $(".ajaxLoader").show();
  },
  success: function (res) {
    // console.log(res);
    $("#filter_data_post").show();
    $("#filter_data_post").html(res.data);
    $(".ajaxLoader").hide();
  },
};

$(document).ready(function () {
  $(".ajaxLoader").hide();
  for (let index = 0; index < nav_fields.length; index++) {
    $("#" + nav_fields[index]).on("click", function () {
      filter_obj.object = nav_fields[index];
      // console.log(filter_obj)
      $.ajax(ajax_method);
    });
  }
  $("#all_data").on("click", function () {
    filter_obj.object = "ALL";
    $.ajax(ajax_method);
  });

  for (let index = 0; index < posts.length; index++) {
    let element = posts[index];
    if (saved_post_list.includes(element)) {
      // saved
      $("#savepost-btn-" + element).hide();
      $("#remove-saved-btn-" + element).show();
    } else {
      // not saved
      $("#savepost-btn-" + element).show();
      $("#remove-saved-btn-" + element).hide();
    }
    $("#savepost-btn-" + element).click(function () {
      $("#savepost-btn-" + element).hide();
      $("#remove-saved-btn-" + element).show();
    });
    $("#remove-saved-btn-" + element).click(function () {
      $("#savepost-btn-" + element).show();
      $("#remove-saved-btn-" + element).hide();
    });
  }
});

let savePost = (p_id) => {
  const save_post_details = {
    post_id: p_id,
  };

  const url = "/save_post/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ save_post_details: save_post_details }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log();
    });
};
let removeSavedPost = (p_id) => {
  const save_post_details = {
    post_id: p_id,
  };

  const url = "/remove_saved_post/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ save_post_details: save_post_details }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log();
    });
};
