/**
 * ajax_caller.js: an array of feature (independent variables) names, and the
 *                 generalized count of features that can be expected within an
 *                 observation, is inserted to respective DOM elements.
 */

// AJAX Process
function ajaxCaller(callbackDone, callbackFail, args) {
  // set the contentType
  if (args.contentType === null) {
    args.contentType = 'application/x-www-form-urlencoded; charset=UTF-8';
  }

  // process the data
  if (args.processData === null) {
    args.processData = true;
  }

  // ajax logic
  fetch(args.endpoint, {
    method: 'post',
    body: args.data,
    headers: {
      'Accept': 'text/javascript'
    }
  }).then(function(response) {
    if (response.ok) {
      // asynchronous callback
      response.json().then(function(data) { callbackDone(data); });
    } else {
      // throw custom error
      var error = {
        'statusText': response.statusText,
        'status': response.status
	  }
      throw error;
    }
  }).catch(function(e) {
    // asynchronous callback
    callbackFail(e.statusText, e.status);
  });
}
