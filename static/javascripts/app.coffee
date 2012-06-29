$ ->
    $prompt = $('#prompt')
    $history = $('#history')
    $content = $('#content')
    converter = new Showdown.converter
    answerDelay = 1000
    
    $history.data 'log', []
    
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
    .on 'keydown', (e) ->
        key = e.keyCode || e.which
        switch key
            when 38
                index = $history.data('logIndex') - 1
            when 40
                index = $history.data('logIndex') + 1
            else
                $history.data 'logIndex', $history.data('log').length
                return
        if $history.data('log')[index]
            $history.data 'logIndex', index
            $prompt.val $history.data('log')[index]
        else if key == 40
            $history.data 'logIndex', $history.data('log').length
            $prompt.val("")
    
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
        if data.type == 'question'
            log = $history.data 'log'
            log.push data.text
            $history.data 'log', log
            $history.data 'logIndex', log.length
        $entryContainer = $('<li>')
        $entry = $('<div class="entry">')
        $entryContainer.addClass data.type
        $entryContainer.addClass data.slug
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
        , complete: ->
            $history.trigger 'didscroll', latestEntry: $entry
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
            if data.text
                $history.trigger 'message', type: 'answer', slug: data.slug, html: converter.makeHtml(data.text)
            if data.page
                $content.trigger 'showwebpage', url: data.page
            else if data.url
                $content.trigger 'showwebpage', url: data.url
            if data.javascript
                eval "msg = (function(m) { #{data.javascript} })(data.matches);"
                if msg
                    $history.trigger 'message', type: 'answer', slug: data.slug, html: converter.makeHtml(msg)
            if location.pathname != "/#{data.slug}"
                history.pushState question: msg, "", "/#{data.slug}"
    
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
    
    $(window).on 'popstate', (e) ->
        $history.trigger 'question', 'welcome'
        if location.pathname != "/"
            if 'state' of e.originalEvent and e.originalEvent.state? and 'question' of e.originalEvent.state
                question = e.originalEvent.state.question
            else
                question = location.pathname.substr(1)
            $history.one 'message', ->
                $prompt.trigger 'enterquestion', text: question
    
    if not Modernizr.history
        $(window).trigger 'popstate'
    
    $history.on 'didscroll', (e, data) ->
        $welcome = $('li.welcome:first:not(.pinned)', this)
        if $welcome.length and $welcome.position().top < 0
            $welcome.addClass 'pinned'
            $welcome.css top: '-50px'
            $welcome.animate top: 0, 500, 'linear'