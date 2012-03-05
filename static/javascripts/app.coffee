$ ->
    $prompt = $('#prompt')
    $history = $('#history')
    $content = $('#content')
    converter = new Showdown.converter
    answerDelay = 1000
    
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
        $entryContainer = $('<li>')
        $entry = $('<div class="entry">')
        $entryContainer.addClass data.type
        if 'html' of data
            $entry.html data.html
        else
            $entry.text data.text
        $entry.hide()
        $entryContainer.append $entry
        $history.append $entryContainer
        entryHeight = $entry.outerHeight()
        duration = 200
        
        $entryContainer.animate (height: entryHeight), (duration: duration, easing: "linear", step: (now, fx) ->
            $history.scrollTop(99999999)
        )
        $entry.css opacity: 0
        $entry.show()
        $entry.animate opacity: 1, duration, "linear", ->
            $history.scrollTop(99999999)
        
        $prompt.val ''
    
    $history.on 'question', (e, msg) ->
        $.ajax
            url: '/'
            data: 
                question: msg
            type: 'GET'
            dataType: 'json'
        .success (data) ->
            window.setTimeout ->
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
            , answerDelay
    
    $history.on 'clear', ->
        $history.html('')
        $content.html('')
        $history.trigger 'question', 'welcome'
    
    $(document).on 'click', '#history a:not([href*="/"])', (e) ->
        e.preventDefault()
        slug = $(this).attr('href')
        if Modernizr.history
            history.pushState null, "", "/#{slug}"
        else
            location.hash = '#{slug}'
        $prompt.trigger 'enterquestion', text: slug
        return false
    
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
    
    $(window).on 'popstate', (e,x,y) ->
        if location.pathname != "/"
            slug = location.pathname.substr(1)
            $prompt.trigger 'enterquestion', text: slug
        else
            $history.trigger 'question', 'welcome'
    
    if not Modernizr.history
        $(window).trigger 'popstate'
