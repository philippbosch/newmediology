(function() {

  $(function() {
    var $content, $history, $prompt, converter;
    $prompt = $('#prompt');
    $history = $('#history');
    $content = $('#content');
    converter = new Showdown.converter;
    $prompt.on('keypress', function(e, data) {
      var key, msg;
      key = e.keyCode || e.which;
      msg = $prompt.val().toLowerCase().trim();
      if (data || (key === 13 && msg.length)) {
        $history.trigger('message', {
          type: 'question',
          text: msg
        });
        return $history.trigger('question', msg);
      }
    }).on('webkitspeechchange', function(e) {
      return $prompt.trigger('keypress', $prompt.val());
    }).on('blur', function(e) {
      return window.setTimeout(function() {
        return $prompt[0].focus();
      }, 1);
    });
    $prompt.on('enterquestion', function(e, data) {
      var char, i, _i, _len, _ref, _results;
      $prompt.val('');
      i = 0;
      _ref = data.text;
      _results = [];
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        char = _ref[_i];
        _results.push((function() {
          var theChar, theI;
          theChar = char;
          theI = i;
          return setTimeout(function() {
            $prompt.val($prompt.val() + theChar);
            if (theI === data.text.length - 1) {
              return setTimeout(function() {
                var evt;
                evt = $.Event('keypress');
                evt.which = 13;
                evt.keyCode = 13;
                return $prompt.trigger(evt);
              }, 400);
            }
          }, ++i * 100 + Math.random() * 100);
        })());
      }
      return _results;
    });
    $history.on('message', function(e, data) {
      var $entry;
      $entry = $('<li>');
      $entry.addClass(data.type);
      if ('html' in data) {
        $entry.html(data.html);
      } else {
        $entry.text(data.text);
      }
      $history.append($entry);
      $prompt.val('');
      return $history.scrollTop(99999999);
    });
    $history.on('question', function(e, msg) {
      return $.ajax({
        url: '/',
        data: {
          question: msg
        },
        type: 'GET',
        dataType: 'json'
      }).success(function(data) {
        if (data.text) {
          $history.trigger('message', {
            type: 'answer',
            html: converter.makeHtml(data.text)
          });
        }
        if (data.page) {
          $content.trigger('showwebpage', {
            url: data.page
          });
        } else if (data.url) {
          $content.trigger('showwebpage', {
            url: data.url
          });
        }
        if (data.javascript) {
          eval("msg = (function(m) { console.log(m); " + data.javascript + " })(data.matches);");
          if (msg) {
            return $history.trigger('message', {
              type: 'answer',
              html: converter.makeHtml(msg)
            });
          }
        }
      });
    });
    $content.on('updatecontent', function(e, data) {
      return $content.html(data.content);
    });
    $content.on('showwebpage', function(e, data) {
      var $iframe;
      $iframe = $('<iframe border="0" frameborder="0">');
      $iframe.attr('src', data.url);
      return $content.trigger('updatecontent', {
        content: $iframe
      });
    });
    $content.on('showtext', function(e, data) {
      var $div;
      $div = $('<div>');
      $div.html(data.text);
      return $content.trigger('updatecontent', {
        content: $div
      });
    });
    $(window).on('hashchange', function(e) {
      var question;
      question = location.hash.substr(location.hash.indexOf('#') + 1).replace(/\-/g, ' ');
      return $prompt.trigger('enterquestion', {
        text: question
      });
    });
    if (location.hash.length && location.hash !== '#') {
      return $(window).trigger('hashchange');
    }
  });

}).call(this);