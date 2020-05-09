$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })


$(document).ready(function() {
	$(".clickable-row").click(function() {
			if(2500 <= $(this).data("follower-count") && $(this).data("follower-count") <= 7499) {
					$(".choose-tokens").css("display", "block");
          $(".token-add-plist-id").val($(this).data("playlist-id"))
			}
       else if(8000 <= $(this).data("follower-count")) {
          $(".choose-tokens").css("display", "block");
          $(".value-3-tokens").css('display', 'block')
          $(".token-add-plist-id").val($(this).data("playlist-id"))
       }
  });

  var existingSongsTable = $('#existingSongs').DataTable( {
      dom: 'Bfrtip',
      select: {
        style: 'single'
      },
      paging: false,
      searching: false,
      buttons: [{text: "", className: 'existingSongsBtn'}]
  } );

  var table = $('#similarPlaylists').DataTable( {
      dom: 'Bfrtip',
      select: {
        style: 'single'
      },
      paging: false,
      searching: false,
      buttons: [
          {
              text: 'Add song to playlist',
              action: function () {
                  console.log(table.rows( { selected: true } ).data()[0][0]);
                  regex = new RegExp(/<([^\s]+).*?id="([^"]*?)".*?>(.+?)<\/\1>/gi);
									matches = existingSongsTable.rows({ selected: true}).data()[0][1].match(regex);
									results = [];
									for (i in matches) {
									    parts = regex.exec(matches[i]);
									    results.push(parts[2])
									}

                  if (confirm("Are you sure you want to add your song to this playlist?")) {
                    route = '/song_to_plist?plist_id=' + table.rows( { selected: true } ).data()[0][0] +
                            '&song_id=' + results[0]
                    fetch(route, {
						          method: 'POST'
						        }).then(function(result) {
						          return result.json()
						        }).then(redirectAfterPlistAdd);
                  } else {
                    alert("Addition cancelled");
                  }

              }
          }
      ]
  } );

  function redirectAfterPlistAdd(responseJson) {
    if (responseJson.error) {
			alert("Error adding song to playlist, please try again");
    }
    else {
      window.location.href = "/artist_profile"
    }
  }

});

