$ ->
    $prompt = $('#prompt')
    $history = $('#history')
    $content = $('#content')
    converter = new Showdown.converter
    
    $prompt.on 'keypress', (e, data) ->
        key = e.keyCode || e.which
        msg = $prompt.val().toLowerCase().trim()
        if data || (key == 13 && msg.length)
            $history.trigger 'message', type: 'question', text: msg
            $history.trigger 'question', msg
    .on 'webkitspeechchange', (e) ->
        $prompt.trigger 'keypress', $prompt.val()
    .on 'blur', (e) ->
        window.setTimeout ->
            $prompt[0].focus()
        , 1
    
    $prompt.on 'enterquestion', (e, data) ->
        $prompt.val('')
        i = 0
        for char in data.text
            do ->
                theChar = char
                theI = i
                setTimeout ->
                    $prompt.val $prompt.val() + theChar
                    if theI == data.text.length-1
                        setTimeout ->
                            evt = $.Event('keypress')
                            evt.which = 13
                            evt.keyCode = 13
                            $prompt.trigger(evt)
                        , 400
                , ++i*100 + Math.random() * 100
    
    $history.on 'message', (e, data) ->
        $entry = $('<li>')
        $entry.addClass data.type
        if 'html' of data
            $entry.html data.html
        else
            $entry.text data.text
        $history.append $entry
        $prompt.val ''
        $history.scrollTop(99999999)
    
    $history.on 'question', (e, msg) ->
        $.ajax
            url: '/'
            data: 
                question: msg
            type: 'GET'
            dataType: 'json'
        .success (data) ->
            if data.text
                $history.trigger 'message', type: 'answer', html: converter.makeHtml(data.text)
            if data.page
                $content.trigger 'showwebpage', url: data.page
            else if data.url
                $content.trigger 'showwebpage', url: data.url
            if data.javascript
                eval "msg = (function(m) { #{data.javascript} })(data.matches);"
                if msg
                    $history.trigger 'message', type: 'answer', html: converter.makeHtml(msg)
    
    $content.on 'updatecontent', (e, data) ->
        $content.html data.content
    
    $content.on 'showwebpage', (e, data) ->
        $iframe = $('<iframe border="0" frameborder="0">')
        $iframe.attr('src', data.url)
        $content.trigger 'updatecontent', content: $iframe
    
    $content.on 'showtext', (e, data) ->
        $div = $('<div>')
        $div.html data.text
        $content.trigger 'updatecontent', content: $div
    
    $(window).on 'hashchange', (e) ->
        question = location.hash.substr(location.hash.indexOf('#')+1).replace(/\-/g, ' ')
        $prompt.trigger 'enterquestion', text: question
    
    if location.hash.length && location.hash != '#'
        $(window).trigger 'hashchange'
